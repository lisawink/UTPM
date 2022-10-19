"""Data classes and sub-models required to run the UTPM"""

import numpy as np
import scipy as sp
import LondonData as regional_data

class Mathematics:
    """
    Creates straight and polynomial fit functions
    """
    def poly_fit(years,data,power):
        """
        Generate polynomial fit of given data.
        Inputs: x values (usually years), data, power (1 for linear, 2 for quadratic)
        """
        coeff = np.polyfit(years,data,power,cov=False)
        function=sp.poly1d(coeff)
        return(function)
    
    def straight_fit(x1,y1,x2,y2,f):
        """
        Straight fit between two points
        """
        m = (y2 - y1) / (x2 - x1)
        c = (y2 - (m * x2))
        return [i*m+c for i in f]

class Vehicle:
    """
    Creates vehicle object with emission properties
    """
    def __init__(self, fuel_type, age, mass, manufacture, elec):
        self.fuel_type = fuel_type
        self.age = age 
        self.m=mass
        self.c=manufacture
        self.e=elec
       
    def emissions(self,y):
        """
        Specifies the CO2 emissions intensity of every fuel type (g/km)
        """
        emissions_value=0
        phev_electric_emissions=0
        phev_tailpipe_emissions=0

        #kgC02 per litre of petrol and diesel (average biofuel blend, 2022 DEFRA)
        #petrol=2.14805
        #diesel=2.52058
        
        #kgC02eq per litre of petrol and diesel (average biofuel blend, 2022 DEFRA)
        petrol=2.16
        diesel=2.56
        
        #if diesel
        if self.fuel_type==0:
            #[diesel]=kgCO2/l, [fuel consumption]=l/100km, so *10 gives [emissions]=g/km
            emissions_value=diesel*10*np.array(Fuel_Consumption(self.m).diesel()[self.age-1989])
        #if petrol
        if self.fuel_type==1:
            #[petrol]=kgCO2/l, [fuel consumption]=l/100km, so *10 gives [emissions]=g/km
            emissions_value=petrol*10*np.array(Fuel_Consumption(self.m).petrol()[self.age-1989])
        #if hybrid
        if self.fuel_type==2:
            #real-world PHEV utility factor of 39% as found by the ICCT
            phev_electric_emissions=0.39*np.array(Fuel_Consumption(self.m).bev()[self.age-1989])*10*np.array(Electricity(self.e).lca_emissions()[y-2010])
            phev_tailpipe_emissions=0.61*petrol*10*np.array(Fuel_Consumption(self.m).petrol()[self.age-1989])
        #if retrofitted ICEV (same emissions as BEV)
        if self.fuel_type==3:
            emissions_value=np.array(Fuel_Consumption(self.m).bev()[self.age-1989])*10*np.array(Electricity(self.e).lca_emissions()[y-2010])
        #if BEV
        if self.fuel_type==4:
            emissions_value=np.array(Fuel_Consumption(self.m).bev()[self.age-1989])*10*np.array(Electricity(self.e).lca_emissions()[y-2010])

        return emissions_value,phev_electric_emissions,phev_tailpipe_emissions

    def wtt_emissions(self,y):
        """
        Specifies well-to-tank emissions for petrol and diesel
        """
        #kgC02e per litre of petrol and diesel
        petrol=0.61328
        diesel=0.60986

        #if diesel
        if self.fuel_type==0:
            #[diesel]=kgCO2/l, [fuel consumption]=l/100km, so *10 gives [emissions]=g/km
            emissions_value=diesel*10*np.array(Fuel_Consumption(self.m).diesel()[self.age-1989])
        #if petrol
        if self.fuel_type==1:
            #[petrol]=kgCO2/l, [fuel consumption]=l/100km, so *10 gives [emissions]=g/km
            emissions_value=petrol*10*np.array(Fuel_Consumption(self.m).petrol()[self.age-1989])
        #if hybrid
        if self.fuel_type==2:
            #real-world PHEV utility factor of 39% as found by the ICCT
            emissions_value=0.61*petrol*10*np.array(Fuel_Consumption(self.m).petrol()[self.age-1989])

        return emissions_value
    
    def prod_emissions(self,y):
        """
        Specifies the production emissions of each type of vehicle (kgco2)
        Consists of emissions from manufacturing + end-of-life emissions + emissions change with mass + emissions of road construction
        22% of car production gets decarbonised with electrical grid
        """
        emissions_value=0
        #if diesel
        if self.fuel_type==0:
            emissions_value=3303+((self.m-1400)/1400)*0.73*4235+(15334/3.6)*Electricity(self.e).lca_emissions()[y-2010]+3447
        #if petrol
        if self.fuel_type==1:
            emissions_value=3303+((self.m-1400)/1400)*0.73*4235+(15334/3.6)*Electricity(self.e).lca_emissions()[y-2010]+3447
        #if hybrid
        if self.fuel_type==2:
            #Non-regulated manufacturing
            if self.c==0:
                emissions_value=15000+((self.m-1400)/1400)*0.67*15000+3447
            #Regulated manufacturing
            elif self.c==1:
                emissions_value=4320+((self.m-1400)/1400)*0.67*5538+(18766/3.6)*Electricity(self.e).lca_emissions()[y-2010]+3447
        #if retrofit
        if self.fuel_type==3:
            #Non-regulated manufacturing
            if self.c==0:
                emissions_value=8043+3447
            #Regulated manufacturing
            elif self.c==1:
                emissions_value=3385+(10636/3.6)*Electricity(self.e).lca_emissions()[y-2010]+3447
        #if BEV
        if self.fuel_type==4:
            #Non-regulated manufacturing
            if self.c==0:
                emissions_value=15000+((self.m-1400)/1400)*0.67*15000+3447
            #Regulated manufacturing
            elif self.c==1:
                emissions_value=6784+((self.m-1400)/1400)*0.67*8698+(21318/3.6)*Electricity(self.e).lca_emissions()[y-2010]+3447   
                
        return emissions_value
    
    def prod_energy(self):
        """
        Specifies the production energy of each type of vehicle
        """
        #in MJ per car
        #manufacturing + endoflife energy + energy change with mass + energy of road construction
        energy_value=0
        #if diesel
        if self.fuel_type==0:
            #Non-regulated manufacturing
            if self.c==0:
                energy_value=75700+((self.m-1400)/1400)*0.8*75700+87362
            #Regulated manufacturing
            if self.c==1:
                energy_value=69700+((self.m-1400)/1400)*0.8*69700+87362
        #if petrol
        if self.fuel_type==1:
            #Non-regulated manufacturing
            if self.c==0:
                energy_value=75700+((self.m-1400)/1400)*0.8*75700+87362
            #Regulated manufacturing
            if self.c==1:
                energy_value=69700+((self.m-1400)/1400)*0.8*69700+87362
        #if hybrid
        if self.fuel_type==2:
            #Non-regulated manufacturing
            if self.c==0:
                energy_value=90300+((self.m-1400)/1400)*0.75*90300+87362
            #Regulated manufacturing
            if self.c==1:
                energy_value=85300+((self.m-1400)/1400)*0.75*85300+87362
        #if retrofit
        if self.fuel_type==3:
            energy_value=50000+87362
        #if BEV
        if self.fuel_type==4:
            #Non-regulated manufacturing
            if self.c==0:
                energy_value=100000+((self.m-1400)/1400)*0.75*100000+87362
            #Regulated manufacturing
            if self.c==1:
                energy_value=96900+((self.m-1400)/1400)*0.75*96900+87362
        return energy_value
    
class ModalShift:
    """
    Finds emissions and energy intensity of non-car modes
    """
    #non car modal share for london
    modal_walk=[0.39]*31
    modal_cycle=[0.04]*31
    modal_bus=[0.22]*31
    modal_rail=[0.35]*31
    modal_ferry=[0]*31
    
    def co2intensity(elec):
        """
        CO2 intensity of non-car modes
        Can adjust modal shares and emissions intensities (e.g. due to changing occupancies) to find lower emissions
        """
        
        #kgco2-eq per passenger kilometer transport (pkt)
        #values based on sustainability paper sustainability-650843-SI
        co2walk=[0.00025]*31
        co2cycle=[0.0094]*31
        #at bus occupancy of 20
        #keeping emissions from manufacture and infrastructure relatively fixed 
        #emissions from energy use per km is straight line between 2020 co2 value and 2050 100% electricity value
        co2bus=np.array([0.023]*31)+Mathematics.straight_fit(2019,0.088,2050, \
                                                             0.319*Electricity(elec).lca_emissions()[-1],range(2020,2051))
        #use electricity values for 2020 and 2050
        co2rail=np.array([0.013]*31)+Mathematics.straight_fit(2019,0.15*Electricity(elec).lca_emissions()[10],2050, \
                                                             0.15*Electricity(elec).lca_emissions()[-1],range(2020,2051))
        
        avg=np.array(ModalShift.modal_walk)*np.array(co2walk)+np.array(ModalShift.modal_cycle)*np.array(co2cycle) \
            +np.array(ModalShift.modal_bus)*np.array(co2bus)+np.array(ModalShift.modal_rail)*np.array(co2rail)
        return avg
    
    def energy():
        """
        Energy intensity of non-car modes
        """
        
        #MJ per passenger kilometer transport (pkt)
        #values based on sustainability paper [sustainability-650843-SI]
        walk=[0.007]*31
        cycle=[0.1524]*31
        #at bus occupancy of 20
        bus=[1.42]*31
        #at train occupancy of 146/200
        rail=[0.751]*31
        
        avg=np.array(ModalShift.modal_walk)*np.array(walk)+np.array(ModalShift.modal_cycle)*np.array(cycle) \
            +np.array(ModalShift.modal_bus)*np.array(bus)+np.array(ModalShift.modal_rail)*np.array(rail)
        return avg
        
class Adoption_Rate:
    """
    Calculates adoption rates (percentage of new cars sold of a specific fuel type) from 1989 to 2050
    Takes hisotrical data and estimates furture rates
    """
    def __init__(self,phase_out_date,phase_out_hybrid):
        self.p=phase_out_date
        self.ph=phase_out_hybrid
        
    def adoption_bev(self):
        """
        Adoption of Battery-Electric Cars is the difference between 100% and all other fuel types
        """
        adoption_bev=[]
        adoption_diesel=Adoption_Rate(self.p,self.ph).adoption_diesel()
        adoption_petrol=Adoption_Rate(self.p,self.ph).adoption_petrol()
        adoption_hybrid=Adoption_Rate(self.p,self.ph).adoption_hybrid()
        adoption_plugin=Adoption_Rate(self.p,self.ph).adoption_plugin()
        
        for i in range(0,62):
            adoption_bev.append(100-adoption_diesel[i]-adoption_petrol[i]-adoption_hybrid[i]-adoption_plugin[i])
        return(adoption_bev)
    
        
    def adoption_diesel(self):
        """
        Creates list of adoption rates of diesel cars from 1989 to 2050 in percentage
        Assumes linear decrease from historical data
        """
        diesel_increase=Mathematics.poly_fit([2001,2002,2003],regional_data.adop_car_d[0:3],1)
        diesel_decrease=Mathematics.poly_fit([2017,2018,2019,2020],regional_data.adop_car_d[16:],1)
        
        adoption_diesel=np.append(np.append(np.append([0]*9,diesel_increase(range(1998,2004))),regional_data.adop_car_d[3:-4]),np.append(diesel_decrease(range(2017,2023)),[0]*28))
        return(adoption_diesel)

    def adoption_plugin(self):
        """
        Plug-in hybrid phase-out date can only take values 2025,2030,2035,2040
        Consists of a gaussian that peaks and drop back to zero at the phase-out date
        """
        
        x=np.linspace(2020,self.ph-1,self.ph-2021)
        
        def gaussian(x, mu, sig):
            return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
        
        if self.ph==2025:
            adoption_plugin=np.append(np.append(np.append([0]*12,regional_data.adop_car_ph),10*gaussian(x,2020+(self.ph-2020)/2,5)),[0]*(2050-self.ph+1))
        elif self.ph==2030:
            adoption_plugin=np.append(np.append(np.append([0]*12,regional_data.adop_car_ph),15*gaussian(x,2020+(self.ph-2020)/2,4)),[0]*(2050-self.ph+1))
        elif self.ph==2035:
            adoption_plugin=np.append(np.append(np.append([0]*12,regional_data.adop_car_ph),20*gaussian(x,2020+(self.ph-2020)/2,6)),[0]*(2050-self.ph+1))
        elif self.ph==2040:
            adoption_plugin=np.append(np.append(np.append([0]*12,regional_data.adop_car_ph),25*gaussian(x,2020+(self.ph-2020)/2,7)),[0]*(2050-self.ph+1))
        else:
            adoption_plugin=np.append(np.append(np.append([0]*12,regional_data.adop_car_ph),15*gaussian(x,2020+(self.ph-2020)/2,5)),[0]*(2050-self.ph+1))
        return(adoption_plugin)
    
    def adoption_hybrid(self):
        """
        Hybrid phase-out date can only take values 2025,2030,2035,2040
        Consists of a gaussian that peaks and drop back to zero at the phase-out date
        """
              
        x=np.linspace(2020,self.p,self.p-2021)
        
        def gaussian(x, mu, sig):
            return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
        
        if self.p==2025:
            adoption_hybrid=np.append(np.append(np.append([0]*12,np.array(regional_data.adop_car_h)),15*gaussian(x,2020+(self.p-2020)/2,6)),[0]*(2050-self.p+1))
        elif self.p==2030:
            adoption_hybrid=np.append(np.append(np.append([0]*12,np.array(regional_data.adop_car_h)),20*gaussian(x,2020+(self.p-2020)/2,6)),[0]*(2050-self.p+1))
        elif self.p==2035:
            adoption_hybrid=np.append(np.append(np.append([0]*12,np.array(regional_data.adop_car_h)),25*gaussian(x,2020+(self.p-2020)/2,7)),[0]*(2050-self.p+1))
        elif self.p==2040:
            adoption_hybrid=np.append(np.append(np.append([0]*12,np.array(regional_data.adop_car_h)),30*gaussian(x,2020+(self.p-2020)/2,9)),[0]*(2050-self.p+1))
        else:
            adoption_hybrid=np.append(np.append(np.append([0]*12,np.array(regional_data.adop_car_h)),20*gaussian(x,2020+(self.p-2020)/2,6)),[0]*(2050-self.p+1))    
        return(adoption_hybrid)
    
    def adoption_petrol(self):
        """
        Assumes 100% adoption rate, until historical data, then linear decrease from 2020 to 0 at phase-out date
        """
        decline=Mathematics.straight_fit(2020,regional_data.adop_car_p[-1],self.p,0,range(2021,self.p))
        diesel_increase=[100]*3-np.array(Mathematics.poly_fit([2001,2002,2003],regional_data.adop_car_d[0:3],1)(range(1998,2001)))
        adoption_petrol=np.append(np.append(np.append(np.append([100]*9,diesel_increase),regional_data.adop_car_p),decline),[0]*(2050-self.p+1))
        return(adoption_petrol)

class Fuel_Consumption:
    """
    Calculates fuel consumption of petrol, diesel and hybrid cars, and the emissions intensity of the electrical grid
    1989 to 2050
    """
    
    def __init__(self,mass):
        """
        Initialises class with mass parameter
        """
        self.m=mass
        
    def petrol(self):
        #takes average fuel consumption of petrol cars every year and calculates increase/decrease due to lightweighting policies
        pre_1997=Mathematics.poly_fit([1997,1998,1999],regional_data.fuel_car_p[0:3],1)
        post_2020=np.append(Mathematics.straight_fit(2020,regional_data.fuel_car_p[-1],2025,regional_data.fuel_car_p[-1]+(self.m-1400)*0.0032,range(2020,2026)),
                            [regional_data.fuel_car_p[-1]+(self.m-1400)*0.0032]*25)
        return np.append(pre_1997(range(1989,2000)),np.append(regional_data.fuel_car_p[3:],post_2020))
        
    def diesel(self):
        #takes average fuel consumption of diesel cars every year and calculates increase/decrease due to lightweighting policies
        pre_1997=Mathematics.poly_fit([1997,1998,1999],regional_data.fuel_car_d[0:3],1)
        post_2020=np.append(Mathematics.straight_fit(2020,regional_data.fuel_car_d[-1],2025,regional_data.fuel_car_d[-1]+(self.m-1400)*0.0028,range(2020,2026)),
                            [regional_data.fuel_car_d[-1]+(self.m-1400)*0.0028]*25)
        return np.append(pre_1997(range(1989,2000)),np.append(regional_data.fuel_car_d[3:],post_2020))
    
    def bev(self):
        #takes average fuel consumption of BEVs every year and calculates increase/decrease due to lightweighting policies
        bev=np.append([18]*31,np.append(Mathematics.straight_fit(2020,18,2025,18+(self.m-1400)*0.01,range(2020,2026)),[18+(self.m-1400)*0.01]*25))
        return(bev)
    

class Electricity:
    """
    Calculates life cycle electricity generation emissions, average efficiency of electric grid, percentage of renewables in grid,
    
    """
    
    #assumptions for energy mix values, in percentage of total electricity generation
    #each element in array represents a different time-step
    #default (2050 net-zero case) is each element 1 decade apart starting from 2010
    coal=np.array([28,2,0,0,0])
    gas=np.array([47,35,21,10,0])
    wind=np.array([3,25,42,47,51])
    nuclear=np.array([15,17,18,19,20])
    solar=np.array([0,4,10,15,20])
    bioenergy=np.array([3,7,7,7,7])
    hydro=np.array([1,2,2,2,2])
    other=np.array([3,8,0,0,0])
    storage=(wind+solar)*0.15
    
    def __init__(self,elec):
        """
        Initialises class with net-zero electricity generation date
        """
        self.e=elec   
        
    def lca_emissions(self):
        #calculates the life cycle electricity generation emissions every year from 2010 to 2051
        #sum of electricity generation and transmission infrastructure emissions
        
        avg_lca=(np.array(Electricity.coal)*980+np.array(Electricity.gas)*450+np.array(Electricity.wind)*10+np.array(Electricity.nuclear)*12\
        +np.array(Electricity.solar)*45+np.array(Electricity.bioenergy)*29+np.array(Electricity.hydro)*31+np.array(Electricity.other)*500)/100\
        +Electricity.storage/100*43
        
        division=int((self.e-2020)/3)
        
        #lcaemissions in gco2/kwh
        if self.e<2050:
            projection1=Mathematics.straight_fit(2010,avg_lca[0],2020,avg_lca[1],range(2010,2020))
            projection2=Mathematics.straight_fit(2020,avg_lca[1],2020+division,avg_lca[2],range(2020,2020+division))
            projection3=Mathematics.straight_fit(2020+division,avg_lca[2],2020+division*2,avg_lca[3],range(2020+division,2020+division*2))
            projection4=Mathematics.straight_fit(2020+division*2,avg_lca[3],2020+division*3,avg_lca[4],range(2020+division*2,2020+division*3))
            projection5=Mathematics.straight_fit(2020+division*3,avg_lca[4],2050,avg_lca[4],range(2020+division*3,2051))
            lcaemissions=(np.append(np.append(np.append(np.append(projection1,projection2),projection3),projection4),projection5))+0.011
        #the case for 100% renewable electricity generation for electric vehicles
        elif self.e==2020:
            lcaemissions=np.array([avg_lca[4]]*41)+0.011
        else:
            projection1=Mathematics.straight_fit(2010,avg_lca[0],2020,avg_lca[1],range(2010,2020))
            projection2=Mathematics.straight_fit(2020,avg_lca[1],2020+division,avg_lca[2],range(2020,2020+division))
            projection3=Mathematics.straight_fit(2020+division,avg_lca[2],2020+division*2,avg_lca[3],range(2020+division,2020+division*2))
            projection4=Mathematics.straight_fit(2020+division*2,avg_lca[3],2020+division*3,avg_lca[4],range(2020+division*2,2051))
            lcaemissions=(np.append(np.append(np.append(projection1,projection2),projection3),projection4))+0.011
   
        return lcaemissions/1000

    def avg_efficiency(self):
        #calculates average efficiency of electrical grid from 2010 to 2051
        
        avg_efficiency=(np.array(Electricity.coal)*32.1+np.array(Electricity.gas)*48.3+np.array(Electricity.wind)*97.3+np.array(Electricity.nuclear)*40.3\
        +np.array(Electricity.solar)*97.3+np.array(Electricity.bioenergy)*34.7+np.array(Electricity.hydro)*99.6+np.array(Electricity.other)*64.2)/100
        
        division=int((self.e-2020)/3)
        
        #avg efficiency in %
        if self.e<2050:
            projection1=Mathematics.straight_fit(2010,avg_efficiency[0],2020,avg_efficiency[1],range(2010,2020))
            projection2=Mathematics.straight_fit(2020,avg_efficiency[1],2020+division,avg_efficiency[2],range(2020,2020+division))
            projection3=Mathematics.straight_fit(2020+division,avg_efficiency[2],2020+division*2,avg_efficiency[3],range(2020+division,2020+division*2))
            projection4=Mathematics.straight_fit(2020+division*2,avg_efficiency[3],2020+division*3,avg_efficiency[4],range(2020+division*2,2020+division*3))
            projection5=Mathematics.straight_fit(2020+division*3,avg_efficiency[4],2050,avg_efficiency[4],range(2020+division*3,2051))
            avgefficiency=(np.append(np.append(np.append(np.append(projection1,projection2),projection3),projection4),projection5))
        elif self.e==2020:
            avgefficiency=np.array([avg_efficiency[4]]*41)
        else:
            projection1=Mathematics.straight_fit(2010,avg_efficiency[0],2020,avg_efficiency[1],range(2010,2020))
            projection2=Mathematics.straight_fit(2020,avg_efficiency[1],2020+division,avg_efficiency[2],range(2020,2020+division))
            projection3=Mathematics.straight_fit(2020+division,avg_efficiency[2],2020+division*2,avg_efficiency[3],range(2020+division,2020+division*2))
            projection4=Mathematics.straight_fit(2020+division*2,avg_efficiency[3],2020+division*3,avg_efficiency[4],range(2020+division*2,2051))
            avgefficiency=(np.append(np.append(np.append(projection1,projection2),projection3),projection4))
   
        return avgefficiency/100
        
    def ren_percentage(self):
        #calculates percentage of renewables (wind and solar) in grid
        
        renewables=Electricity.wind+Electricity.solar
        
        division=int((self.e-2020)/3)
        
        if self.e<2050:
            projection1=Mathematics.straight_fit(2010,renewables[0],2020,renewables[1],range(2010,2020))
            projection2=Mathematics.straight_fit(2020,renewables[1],2020+division,renewables[2],range(2020,2020+division))
            projection3=Mathematics.straight_fit(2020+division,renewables[2],2020+division*2,renewables[3],range(2020+division,2020+division*2))
            projection4=Mathematics.straight_fit(2020+division*2,renewables[3],2020+division*3,renewables[4],range(2020+division*2,2020+division*3))
            projection5=Mathematics.straight_fit(2020+division*3,renewables[4],2050,renewables[4],range(2020+division*3,2051))
            ren_perc=(np.append(np.append(np.append(np.append(projection1,projection2),projection3),projection4),projection5))
        elif self.e==2020:
            ren_perc=np.array([renewables[4]]*41)
        else:
            projection1=Mathematics.straight_fit(2010,renewables[0],2020,renewables[1],range(2010,2020))
            projection2=Mathematics.straight_fit(2020,renewables[1],2020+division,renewables[2],range(2020,2020+division))
            projection3=Mathematics.straight_fit(2020+division,renewables[2],2020+division*2,renewables[3],range(2020+division,2020+division*2))
            projection4=Mathematics.straight_fit(2020+division*2,renewables[3],2020+division*3,renewables[4],range(2020+division*2,2051))
            ren_perc=(np.append(np.append(np.append(projection1,projection2),projection3),projection4))
        
        return ren_perc/100
        
    def avg_eroi(self):
        #calculates average EROI of electricity generation sources to find embedded energy
        
        avg_eroi=(np.array(Electricity.coal)*46+np.array(Electricity.gas)*20+np.array(Electricity.wind)*20+np.array(Electricity.nuclear)*14\
        +np.array(Electricity.solar)*10+np.array(Electricity.bioenergy)*5+np.array(Electricity.hydro)*84+np.array(Electricity.other)*34)/100
        
        division=int((self.e-2020)/3)
        
        #avg efficiency in %
        if self.e<2050:
            projection1=Mathematics.straight_fit(2010,avg_eroi[0],2020,avg_eroi[1],range(2010,2020))
            projection2=Mathematics.straight_fit(2020,avg_eroi[1],2020+division,avg_eroi[2],range(2020,2020+division))
            projection3=Mathematics.straight_fit(2020+division,avg_eroi[2],2020+division*2,avg_eroi[3],range(2020+division,2020+division*2))
            projection4=Mathematics.straight_fit(2020+division*2,avg_eroi[3],2020+division*3,avg_eroi[4],range(2020+division*2,2020+division*3))
            projection5=Mathematics.straight_fit(2020+division*3,avg_eroi[4],2050,avg_eroi[4],range(2020+division*3,2051))
            avgeroi=(np.append(np.append(np.append(np.append(projection1,projection2),projection3),projection4),projection5))
        elif self.e==2020:
            avgeroi=np.array([avg_eroi[4]]*41)+0.011
        else:
            projection1=Mathematics.straight_fit(2010,avg_eroi[0],2020,avg_eroi[1],range(2010,2020))
            projection2=Mathematics.straight_fit(2020,avg_eroi[1],2020+division,avg_eroi[2],range(2020,2020+division))
            projection3=Mathematics.straight_fit(2020+division,avg_eroi[2],2020+division*2,avg_eroi[3],range(2020+division,2020+division*2))
            projection4=Mathematics.straight_fit(2020+division*2,avg_eroi[3],2020+division*3,avg_eroi[4],range(2020+division*2,2051))
            avgeroi=(np.append(np.append(np.append(projection1,projection2),projection3),projection4))
   
        return avgeroi

        
class Distance_Driven:
    """
    Calculates distance driven by average car by dividing total km driven by whole fleet with number of fleet from data
    """
    def __init__(self,miles_driven,rate):
        """
        Initialises class with distance driven parameter
        """
        self.md=miles_driven
        self.r=rate
    
    def Lon(self):
        end=2022+self.r 
        km=regional_data.km_2019

        #rate of modal shift determined by the number of years the modal shift happens over r (starting from 2022)
        preprojection=Mathematics.straight_fit(2020,km,2022,km,range(2020,2022))
        projection=Mathematics.straight_fit(2022,km,end,km*(1+self.md/100),range(2022,end+1))
        postprojection=Mathematics.straight_fit(end,km*(1+self.md/100),2052,km*(1+self.md/100),range(end+1,2052))
        return np.append(np.append(preprojection,projection),postprojection)