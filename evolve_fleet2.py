import numpy as np
import initialise_fleet1
import sum_over_fleet
from LondonData import cars_2019
from sub_models1 import Mathematics, Adoption_Rate, Vehicle, Distance_Driven, Fuel_Consumption, Electricity, ModalShift

def evolve_fleet(p,ph,g1,g2,m,fs,md,rf,c,e,r):
    """
    Take 2019 model car fleet and evolve fleet year-on-year, based on policy parameters
    """
    
    #create car list from vehicle initialisation class sorted by year of manufacture in ascending order (oldest cars first)
    car_list=initialise_fleet1.initialise_fleet(p,ph,m,fs,md,c,e) 
    
    results=['total_cars','bev_cars','petrol_cars','diesel_cars','plugin_cars','conv_cars','ages','demand_difference','electric_emiss',
            'tailpipe_emiss','wtt_emiss','mod_shift_emiss','elec_demand','foss_demand','wtt_energy','mod_shift_energy','ev_prod_emiss',
            'ice_prod_emiss','conv_prod_emiss','ev_prod_energy','ice_prod_energy','conv_prod_energy','km_driven']

    results_dict={}

    for i in results:
        results_dict[i]=[]

    """
    total_cars=[]
    bev_cars=[]
    petrol_cars=[]
    diesel_cars=[]
    plugin_cars=[]
    conv_cars=[]
    ages=[]
    demand_difference=[]
    electric_emiss=[]
    tailpipe_emiss=[]
    wtt_emiss=[]
    ev_prod_emissions=[]
    ice_prod_emissions=[]
    conv_prod_emissions=[]
    elec_demand=[]
    foss_demand=[]
    ev_prod_energy=[]
    ice_prod_energy=[]
    conv_prod_energy=[]
    km_driven=[]
    """
    
    #find future fleet size using user input for % increase from fleet size in 2019 to 2041 levels
    fleetsize=np.append(Mathematics.straight_fit(2019,cars_2019,2041,cars_2019*(1+fs/100),range(2020,2041)),[cars_2019*(1+fs/100)]*11)
 
    #for evolution of fleet from 2020 to 2050
    for i in range(0,31):

        #find age distribution of cars 
        age_list=[(2020+i-x.age) for x in car_list]
        results_dict['ages'].append(age_list)
        
        before_removal=len(car_list)
        
        #count number of ICE cars removed
        ice_count=0
        
        #remove cars based on a grandfathering policy
        #EVs have default lifetime of 20 years, whereas ICEVs have variable lifetimes set by g1 (cars made prior to 2020) 
        #and g2 (cars made post 2020)
        #save non-scrapped cars in new car list                
        car_list2=[]
        for j in range(0,len(car_list)):
            #for BEV cars, lifetime is 20 years
            if car_list[j].fuel_type==4:
                if car_list[j].age>=2020+i-20:
                    car_list2.append(car_list[j])
            #for retrofitted cars, lifetime is 10 years longer than normal ICE scrapping age (post-2020)
            elif car_list[j].fuel_type==3:
                if car_list[j].age>=2020+i-g2-10:
                        car_list2.append(car_list[j])
            #for petrol, diesel and plug-in hybrid, lifetime is set by scrap ages g1 and g2
            else: 
                if car_list[j].age<2020:
                    #for cars made prior to 2020, allow a longer age set by g1
                    if car_list[j].age>=2020+i-g1:
                        car_list2.append(car_list[j])
                    else:
                        if car_list[j].fuel_type==0:
                            ice_count=ice_count+1
                        if car_list[j].fuel_type==1:
                            ice_count=ice_count+1    
                else:
                    #for cars made post 2020, make scrap policy happen earlier set by g2
                    if car_list[j].age>=2020+i-g2:
                        car_list2.append(car_list[j])
                    else:
                        if car_list[j].fuel_type==0:
                            ice_count=ice_count+1
                        if car_list[j].fuel_type==1:
                            ice_count=ice_count+1                   
                    
        car_list=car_list2
        after_removal=len(car_list)
        
        #find number of new cars needed to satisfy total fleet size
        #fleet size in year n+1 - number of cars in list after cars have been scrapped
        new_cars=fleetsize[i+1]-after_removal
        
        #making new cars
        if new_cars>0:
            #X% of old fossil fuel cars are retrofitted, depending on retrofit input
            #if there are more new cars than ICEV cars removed, retrofit X% of ICEV cars 
            if new_cars-ice_count>=0:
                new_conv=int(rf*ice_count)
            #if there are less new cars than ICEV cars removed, retrofit X% of the number of new cars
            if new_cars-ice_count<0:
                new_conv=int(rf*new_cars)
            
            #calculate how many new cars of each type based on adoption rates
            rest_of_cars=new_cars-new_conv
            new_BEV=int(Adoption_Rate(p,ph).adoption_bev()[i+30]/100*rest_of_cars)
            new_diesel=int(Adoption_Rate(p,ph).adoption_diesel()[i+30]/100*rest_of_cars)
            new_plugin=int(Adoption_Rate(p,ph).adoption_plugin()[i+30]/100*rest_of_cars)
            new_petrol=int((Adoption_Rate(p,ph).adoption_petrol()[i+30]/100+Adoption_Rate(p,ph).adoption_hybrid()[i+30]/100)*rest_of_cars)
            
            #make cars based on adoption rate* new cars
            for j in range(0,new_BEV):
                car=Vehicle(fuel_type=4,age=2020+i,mass=m,manufacture=c,elec=e)
                car_list.append(car)
            for j in range(0,new_petrol):
                car=Vehicle(fuel_type=1,age=2020+i,mass=m,manufacture=c,elec=e)
                car_list.append(car)
            for j in range(0,new_diesel):
                car=Vehicle(fuel_type=0,age=2020+i,mass=m,manufacture=c,elec=e)
                car_list.append(car)
            for j in range(0,new_plugin):
                car=Vehicle(fuel_type=2,age=2020+i,mass=m,manufacture=c,elec=e)
                car_list.append(car)
            for j in range(0,new_conv):
                car=Vehicle(fuel_type=3,age=2020+i,mass=m,manufacture=c,elec=e)
                car_list.append(car)
            
            
        count=0    
        #if more cars need to be removed due to a modal shift, then remove oldest diesel, then petrol, then plug-in hybrid cars
        if new_cars<0:
            car_list.sort(key=lambda x: x.age, reverse=False)
            car_list.sort(key=lambda x: x.fuel_type, reverse=False)
            del car_list[0:-int(new_cars)]
            
        #print('fleetsize[i+1]',fleetsize[i+1],'fleetsize[i]',fleetsize[i])
        
        #print('year=',2020+i,'new cars=',new_cars, 'new bevs=', new_BEV, 'new petrol=',new_petrol, 'new diesel', new_diesel, 'new plugin', new_plugin)
            
        #find number of cars for plotting
        results_dict['total_cars'].append(len(car_list))
        results_dict['bev_cars'].append(sum(p.fuel_type == 4 for p in car_list))
        results_dict['petrol_cars'].append(sum(p.fuel_type==1 for p in car_list))
        results_dict['diesel_cars'].append(sum(p.fuel_type==0 for p in car_list))
        results_dict['plugin_cars'].append(sum(p.fuel_type==2 for p in car_list))
        results_dict['conv_cars'].append(sum(p.fuel_type==3 for p in car_list))
        
        #find difference in distance driven in baseline (business-as-usual case) and modally shifted case
        #in order to calculate modal shift emissions
        demand_diff=Distance_Driven(20,28).Lon()[i]*1000000000-Distance_Driven(md,r).Lon()[i]*1000000000
        if demand_diff>0:
            results_dict['demand_difference'].append(demand_diff)
        if demand_diff<=0:
            results_dict['demand_difference'].append(0)
        
        #dist=distance driven by each cars in that year
        dist=Distance_Driven(md,r).Lon()[i]*1000000000/len(car_list)
        
        """
        Now in sum_over_fleet
        
        #create lists
        electric_emissions=[]
        tailpipe_emissions=[]
        wtt_emissions=[]
        ice_production_emissions=[]
        ev_production_emissions=[]
        ice_production_energy=[]
        ev_production_energy=[]
        conv_production_emissions=[]
        conv_production_energy=[]
        elec_demand_yearly=[]
        foss_demand_yearly=[]
        kilometres=[]
        
        #for every car in list
        for j in range(0,len(car_list)):
            kilometres.append(dist)
            
            #add emissions from that car to yearly list (emissions=carbon intensity*distance driven)
            
            if car_list[j].fuel_type==0:
                #diesel
                #MJ of fossil fuel energy (l/km fuel consumption*energy density of fuel*km driven)
                foss_demand_yearly.append(Fuel_Consumption(m).diesel()[car_list[j].age-1989]/100*36.9*dist)
                #emissions in gCO2e
                tailpipe_emissions.append(car_list[j].emissions(2020+i)[0]*dist)
                wtt_emissions.append(car_list[j].emissions(2020+i)*dist)
                
            if car_list[j].fuel_type==1:
                #petrol
                foss_demand_yearly.append(Fuel_Consumption(m).petrol()[car_list[j].age-1989]/100*33.7*dist)
                tailpipe_emissions.append(car_list[j].emissions(2020+i)[0]*dist)
                wtt_emissions.append(car_list[j].emissions(2020+i)*dist)
            
            if car_list[j].fuel_type==2:
                #phev
                #utility factor of 39% as found by the ICCT
                #combination of BEV and petrol energy consumption/emissions
                elec_demand_yearly.append(0.39*(Fuel_Consumption(m).bev()[i+30]/100*dist+Fuel_Consumption(m).bev()[i+30]/100*dist*1.36/3.6))
                electric_emissions.append(car_list[j].emissions(2020+i)[1]*dist+0.39*Fuel_Consumption(m).bev()[i+30]/100*dist*94.06)
                foss_demand_yearly.append(0.61*Fuel_Consumption(m).petrol()[car_list[j].age-1989]/100*33.7*dist)
                tailpipe_emissions.append(car_list[j].emissions(2020+i)[2]*dist)
                wtt_emissions.append(car_list[j].emissions(2020+i)*dist)
            
            if car_list[j].fuel_type==3:
                #retroffited ICEV, now acts as BEV
                elec_demand_yearly.append(Fuel_Consumption(m).bev()[i+30]/100*dist+Fuel_Consumption(m).bev()[i+30]/100*dist*1.36/3.6)
                electric_emissions.append(car_list[j].emissions(2020+i)[0]*dist+Fuel_Consumption(m).bev()[i+30]/100*dist*94.06)

            if car_list[j].fuel_type==4:
                #BEV
                #energy consumption of EV driving + energy demand for EV charging point infrastructure (in kwh)
                elec_demand_yearly.append(Fuel_Consumption(m).bev()[i+30]/100*dist+Fuel_Consumption(m).bev()[i+30]/100*dist*1.36/3.6)
                #emissions in gCO2e
                #emissions from driving EVs + emissions from EV charging infrastructure
                electric_emissions.append(car_list[j].emissions(2020+i)[0]*dist+Fuel_Consumption(m).bev()[i+30]/100*dist*94.06)
            
            #for cars made in this year, add the embedded emissions from manufacture+end-of-life
            if car_list[j].age==(2020+i):
                if car_list[j].fuel_type==0:
                    ice_production_emissions.append(car_list[j].prod_emissions(2020+i)*1000)
                    ice_production_energy.append(car_list[j].prod_energy()*1000)
                if car_list[j].fuel_type==1:
                    ice_production_emissions.append(car_list[j].prod_emissions(2020+i)*1000)
                    ice_production_energy.append(car_list[j].prod_energy()*1000)
                if car_list[j].fuel_type==2:
                    ev_production_emissions.append(car_list[j].prod_emissions(2020+i)*1000)
                    ev_production_energy.append(car_list[j].prod_energy()*1000)
                if car_list[j].fuel_type==3:
                    conv_production_emissions.append(car_list[j].prod_emissions(2020+i)*1000)
                    conv_production_energy.append(car_list[j].prod_energy()*1000)
                if car_list[j].fuel_type==4:
                    ev_production_emissions.append(car_list[j].prod_emissions(2020+i)*1000)
                    ev_production_energy.append(car_list[j].prod_energy()*1000)
                
        
        km_driven.append(sum(kilometres))
        electric_emiss.append(sum(electric_emissions))
        tailpipe_emiss.append(sum(tailpipe_emissions))
        wtt_emiss.append(sum(wtt_emissions))
        ev_prod_emissions.append(sum(ev_production_emissions))
        ice_prod_emissions.append(sum(ice_production_emissions))
        conv_prod_emissions.append(sum(conv_production_emissions))
        ev_prod_energy.append(sum(ev_production_energy))
        ice_prod_energy.append(sum(ice_production_energy))
        conv_prod_energy.append(sum(conv_production_energy))
        #electricity demand in kwh
        elec_demand.append(sum(elec_demand_yearly))
        #fossil fuel energy demand in MJ
        foss_demand.append(sum(foss_demand_yearly))
        """

        yearly_results=sum_over_fleet.sum_over_fleet(car_list,dist,m,i)

        for i in yearly_results:
            results_dict[i].append(yearly_results[i])
    
    avg_energy_efficiency=Electricity(e).avg_efficiency()
    avg_eroi=Electricity(e).avg_eroi()
    ren_perc=Electricity(e).ren_percentage()
    avg_renewable_efficiency=97.3/100
    storage_eroi=4
    
    #energy demand = electricity demand divided by the overall efficiency of the grid, plus embedded energy over EROI
    results_dict['elec_demand']=np.array(results_dict['elec_demand'])*3.6/np.array(avg_energy_efficiency)[10:]+\
    ((np.array(results_dict['elec_demand'])*3.6/np.array(avg_energy_efficiency)[10:]))/np.array(avg_eroi)[10:]+\
    (((np.array(results_dict['elec_demand'])*3.6*0.15*np.array(ren_perc)[10:]/100)/avg_renewable_efficiency))/storage_eroi
        
    #calculate emissions from modal shift
    co2intensity=ModalShift.co2intensity(e)
    mod_energy=ModalShift.energy()
    #average occupancy of car is 1.6, so calculate modal shift emissions for every passenger 
    results_dict['mod_shift_emiss']=np.array(results_dict['demand_difference'])*1.6*np.array(co2intensity)/1000000000
    results_dict['mod_shift_energy']=np.array(results_dict['demand_difference'])*1.6*np.array(mod_energy)    
  
    #print(results_dict)

    return(results_dict)

# example run
# evolve_fleet(2030,2035,20,15,1400,20,20,0,0,2050,28) 