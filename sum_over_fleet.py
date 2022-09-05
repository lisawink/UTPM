"""
Module containing function that sums over fleet to calculate yearly emissions and energy demand
"""

from sub_models1 import Fuel_Consumption

def sum_over_fleet(car_list,dist,mass,year):
    """
    Loops over entire car fleet to sum yearly emissions and energy demand
    Electricity demand in kwh
    Fossil fuel energy demand in MJ 
    """

    #yearly results saved in dictionary
    yearly_results={}
    yearly_results_type=['electric_emiss','tailpipe_emiss','wtt_emiss','elec_demand','foss_demand','ev_prod_emiss',
                        'ice_prod_emiss','conv_prod_emiss','ev_prod_energy','ice_prod_energy','conv_prod_energy','km_driven']
    
    for i in yearly_results_type:
        yearly_results[i]=[]

    """
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
    """
    
    
    #for every car in list
    for j in range(0,len(car_list)):
        yearly_results['km_driven'].append(dist)
        
        #add emissions from that car to yearly list (emissions=carbon intensity*distance driven)
        
        if car_list[j].fuel_type==0:
            #diesel
            #MJ of fossil fuel energy (l/km fuel consumption*energy density of fuel*km driven)
            yearly_results['foss_demand'].append(Fuel_Consumption(mass).diesel()[car_list[j].age-1989]/100*36.9*dist)
            #emissions in gCO2e
            yearly_results['tailpipe_emiss'].append(car_list[j].emissions(2020+year)[0]*dist)
            yearly_results['wtt_emiss'].append(car_list[j].wtt_emissions(2020+year)*dist)
            
        if car_list[j].fuel_type==1:
            #petrol
            yearly_results['foss_demand'].append(Fuel_Consumption(mass).petrol()[car_list[j].age-1989]/100*33.7*dist)
            yearly_results['tailpipe_emiss'].append(car_list[j].emissions(2020+year)[0]*dist)
            yearly_results['wtt_emiss'].append(car_list[j].wtt_emissions(2020+year)*dist)
        
        if car_list[j].fuel_type==2:
            #phev
            #utility factor of 39% as found by the ICCT
            #combination of BEV and petrol energy consumption/emissions
            yearly_results['elec_demand'].append(0.39*(Fuel_Consumption(mass).bev()[year+30]/100*dist+Fuel_Consumption(mass).bev()[year+30]/100*dist*1.36/3.6))
            yearly_results['electric_emiss'].append(car_list[j].emissions(2020+year)[1]*dist+0.39*Fuel_Consumption(mass).bev()[year+30]/100*dist*94.06)
            yearly_results['foss_demand'].append(0.61*Fuel_Consumption(mass).petrol()[car_list[j].age-1989]/100*33.7*dist)
            yearly_results['tailpipe_emiss'].append(car_list[j].emissions(2020+year)[2]*dist)
            yearly_results['wtt_emiss'].append(car_list[j].wtt_emissions(2020+year)*dist)
        
        if car_list[j].fuel_type==3:
            #retroffited ICEV, now acts as BEV
            yearly_results['elec_demand'].append(Fuel_Consumption(mass).bev()[year+30]/100*dist+Fuel_Consumption(mass).bev()[year+30]/100*dist*1.36/3.6)
            yearly_results['electric_emiss'].append(car_list[j].emissions(2020+year)[0]*dist+Fuel_Consumption(mass).bev()[year+30]/100*dist*94.06)

        if car_list[j].fuel_type==4:
            #BEV
            #energy consumption of EV driving + energy demand for EV charging point infrastructure (in kwh)
            yearly_results['elec_demand'].append(Fuel_Consumption(mass).bev()[year+30]/100*dist+Fuel_Consumption(mass).bev()[year+30]/100*dist*1.36/3.6)
            #emissions in gCO2e
            #emissions from driving EVs + emissions from EV charging infrastructure
            yearly_results['electric_emiss'].append(car_list[j].emissions(2020+year)[0]*dist+Fuel_Consumption(mass).bev()[year+30]/100*dist*94.06)
        
        #for cars made in this year, add the embedded emissions from manufacture+end-of-life
        if car_list[j].age==(2020+year):
            if car_list[j].fuel_type==0:
                yearly_results['ice_prod_emiss'].append(car_list[j].prod_emissions(2020+year)*1000)
                yearly_results['ice_prod_energy'].append(car_list[j].prod_energy()*1000)
            if car_list[j].fuel_type==1:
                yearly_results['ice_prod_emiss'].append(car_list[j].prod_emissions(2020+year)*1000)
                yearly_results['ice_prod_energy'].append(car_list[j].prod_energy()*1000)
            if car_list[j].fuel_type==2:
                yearly_results['ev_prod_emiss'].append(car_list[j].prod_emissions(2020+year)*1000)
                yearly_results['ev_prod_energy'].append(car_list[j].prod_energy()*1000)
            if car_list[j].fuel_type==3:
                yearly_results['conv_prod_emiss'].append(car_list[j].prod_emissions(2020+year)*1000)
                yearly_results['conv_prod_energy'].append(car_list[j].prod_energy()*1000)
            if car_list[j].fuel_type==4:
                yearly_results['ev_prod_emiss'].append(car_list[j].prod_emissions(2020+year)*1000)
                yearly_results['ev_prod_energy'].append(car_list[j].prod_energy()*1000)

    for i in yearly_results:
        yearly_results[i]=sum(yearly_results[i])
        print(yearly_results[i])
    print(yearly_results)

    yearly_results['electric_emiss']=yearly_results['electric_emiss']/10**12
    yearly_results['tailpipe_emiss']=yearly_results['tailpipe_emiss']/10**12
    yearly_results['wtt_emiss']=yearly_results['wtt_emiss']/10**12
    yearly_results['ev_prod_emiss']=yearly_results['ev_prod_emiss']/10**9
    yearly_results['ice_prod_emiss']=yearly_results['ice_prod_emiss']/10**9
    yearly_results['conv_prod_emiss']=yearly_results['conv_prod_emiss']/10**9
    
    #print('Year is',year,yearly_results)   
    return(yearly_results)