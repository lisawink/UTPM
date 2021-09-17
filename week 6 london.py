# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:01:45 2021

@author: User
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns



year=[2014,2015,2016,2017,2018,2019]
future=[2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,
        2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,
        2042,2043,2044,2045,2046,2047,2048,2049,2050,2051,2052,2053,2054,2055,2056,2057,
        2058,2059,2060,2061,2062,2063,2064,2065,2066,2067,2068,2069,2070,2071,2072,2073,
        2074,2075,2076,2077,2078,2079,2080,2081,2082,2083,2084,2085,2086,2087,2088,2089,
        2090,2091,2092,2093,2094,2095,2096,2097,2098,2099,2100]

# number of vehicle type in UK yearly from 2014 to 2019
# p=petrol, d=diesel, h=hybrid, ph=plug-in hybrid, b=battery electric, r=range-extended,
# f=fuel cell, g=gas, o=other, t=total
# data sourced from DfT's VEH0203

no_car_p=[19053.40,18929.20,18825.00,18759.90,18912.70,19236.70]
no_car_d=[11208.80,11927.80,12574.30,12901.60,12951.50,12852.30]
no_car_h=[184.20,224.10,271.60,336.90,417.50,521.90]
no_car_ph=[7.90,24.10,49.70,79.40,116.90,146.50]
no_car_b=[12.40,21.00,29.70,42.00,56.30,90.90]
no_car_r=[2.20,3.80,5.60,7.80,9.70,9.90]
no_car_f=[0,0,0,0.10,0.10,0.20]
no_car_g=[43.90,40.30,36.00,31.80,28.20,25.60]
no_car_o=[0.40,0.40,0.40,0.40,0.40,0.30]
no_car_t=[30513.30,31170.70,31792.30,32159.90,32493.30,32884.30]

#number of cars in GB and london from 1994-2019 veh0204
no_car_gb=[21199.2,21394.1,22237.5,22831.7,23293.3,23974.9,24405.5,25125.9,25781.9,26240.4,27028.1,27520.4,27609.2,28000.3,28160.7,28246.5,28420.9,28467.3,28722.5,29140.9,29611.5,30250.3,30850.4,31200.2,31517.6,31888.4]
no_car_lon=[2266.2,2260.8,2336.8,2340.8,2371.2,2402.8,2415.9,2461.7,2473.7,2480.0,2523.1,2561.9,2560.1,2578.9,2594.7,2556.7,2557.4,2542.7,2535.5,2549.3,2588.4,2635.9,2668.2,2665.9,2661.2,2661.0]

#2019 number of cars in uk or lon
uk_car_2019=32884.30
lon_car_2019=2661

# percentage of fuel types in GB yearly from 1989 to 2019 
# 1994 to 2019 from DfT's VEH0203, I have assumed 100% petrol pre 1994
per_car_p=[100]*5+[92.6,91.1,90.2,89.3,88.4,87.7,87.0,86.1,84.7,83.1,81.3,79.5,77.7,75.9,74.2,72.5,70.7,68.7,66.7,64.8,62.9,61.2,59.7,58.8,58.7,59.0]
per_car_d=[0]*5+[7.4,8.8,9.8,10.7,11.6,12.2,12.9,13.8,15.2,16.8,18.5,20.3,22.0,23.8,25.4,27.1,28.9,30.8,32.7,34.5,36.2,37.8,39.1,39.6,39.3,38.5]
per_car_h=[0]*5+[0.0,0.0,0.0,0.0,0.0,0.0,0,0,0,0,0,0,0.1,0.1,0.2,0.2,0.3,0.4,0.4,0.5,0.6,0.7,0.9,1.1,1.3,1.6]
per_car_ph=[0]*26+[0.1,0.2,0.3,0.4,0.5]
per_car_b=[0]*26+[0.1,0.1,0.1,0.2,0.3]
per_car_r=[0]*31
per_car_f=[0]*31
per_car_g=[0]*9+[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.1,0.1,0.1,0.1,0.1,0.1]
per_car_o=[0]*31
per_car_t=[100]*31

# adoption rate of fuel type in GB yearly from 2001/2015 to 2019 [VEH0253]
# number of newly registered vehicles of fuel type / total new registrations in that year
# data sourced from DfT's VEH0253

adop_car_p=[82.1,76.2,72.3,67.3,63.2,61.5,59.3,56.0,57.8,53.1,48.5,48.1,49.0,48.1,49.0,49.3,53.5,62.3,65.6]
adop_car_d=[17.8,23.7,27.5,32.6,36.6,38.1,40.0,43.2,41.4,45.7,50.3,50.5,49.5,49.8,48.2,47.4,41.8,31.4,26.3]
adop_car_h=[0]*3+[0.1,0.2,0.4,0.7,0.7,0.7,1.1,1.2,1.2,1.3,1.5,1.7,1.9,2.8,3.7,4.9]
adop_car_ph=[0]*13+[0.3,0.7,1.0,1.3,1.8,1.5]
adop_car_b=[0]*10+[0.1,0.1,0.1,0.3,0.4,0.4,0.5,0.7,1.6]
#adop_car_b=[0.4,0.4,0.5,0.7,1.6]
adop_car_r=[]
adop_car_f=[]
adop_car_g=[]
adop_car_o=[]
adop_car_t=[]

#2019 ages of cars in % of cars at given age starting from 0 to 30+ (i.e. 2019 to <1989)
car_per_age=[6.701865813,6.865554769,7.316778939,7.803457088,7.685096727,7.201434605,6.537954259,5.55890771,5.143852754,5.264539452,5.021894934,
     4.926460392,5.162837486,4.390143996,3.717893513,3.07826344,2.417367913,1.756067938,1.103872606,0.678520949,0.452388859,0.305495142,
     0.21615469,0.146699095,0.111399597,0.07995604,0.063239866,0.052973575,0.060591188,0.05324118,0.087805982]
car_age=list(car_per_age[-i]/100 for i in range(0,31))

#average fuel consumption in litres per 100km for new cars registered from 1997 to 2019 (ENV0103)
fuel_car_p=[8.3,8.3,8.1,8.0,7.9,7.8,7.7,7.6,7.5,7.4,7.2,7.0,6.5,6.3,6.1,5.8,5.6,5.5,5.4,5.4,5.5,5.6,5.7]
fuel_car_d=[7.0,6.9,6.6,6.3,6.2,6.1,6.2,6.2,6.2,6.3,6.2,5.9,5.7,5.5,5.2,5.0,4.9,4.7,4.6,4.5,4.6,4.9,5.1]

#kgC02 per litre of petrol and diesel from DEFRA 2020 conversion factors
petrol=2.30176
diesel=2.65242

#electricity emission factors kgco2/kwh (grid including losses) from 1989 to 2020 [source 2019 ghg conversion factors]
elec_emissions=[0.760,0.741,0.715,0.671,0.602,0.593,0.562,0.532,0.489,0.498,0.463,0.487,0.511,0.495,0.519,0.515,0.500,0.520,0.530,0.521,0.488,0.493,0.480,0.533,0.496,0.446,0.381,0.305,0.275,0.281,0.254,0.231]

#km driven per year by cars & taxis in GB and london from 1994 to 2019 (billion km) TRA0201/0206
km_gb=[345.0,351.1,359.9,365.8,370.6,377.4,376.0,381.2,390.6,390.0,394.2,392.7,397.4,397.9,395.0,394.0,389.2,393.2,395.1,396.9,408.0,415.4,424.7,432.9,438.3,447.8]
km_lon=[25.9,25.8,26,26.1,26.2,26.8,26.5,26.3,26.3,25.7,25.4,25.1,24.8,24.4,23.9,23.9,24.7,24.5,24.6,24.7,25.4,25.6,25.7,26.3,27.3,28.1]

#hybrid emission factors

#UK historic car&taxi road transport emissions (1990-2018) from ENV0202
hist_emissions_uk=[72.3,72.0,73.6,74.5,73.9,73.2,75.9,76.6,75.8,77.2,77.0,76.8,78.3,77.0,77.4,77.4,76.9,77.1,74.8,72.5,70.3,69.5,69.2,68.1,68.3,68.8,69.8,69.7,68.5]


class Make_Graphs:
    def __init__(self,location,phase_out_date,phase_out_hybrid,fleet_size_projection,grandfather1,grandfather2):
        self.l=location
        self.p=phase_out_date
        self.ph=phase_out_hybrid
        self.f=fleet_size_projection
        self.g1=grandfather1
        self.g2=grandfather2
        
        SMALL_SIZE = 13
        MEDIUM_SIZE = 14
        BIGGER_SIZE = 18
        
        plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
        plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
        plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
        plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
        plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
        
    def adoption_rate(self):
        """
        Make_Graphs(2030,1,0.05).adoption_rate()
        """
        plt.figure()
        plt.ylabel("Adoption Rate of BEV Cars in the UK (%)")
        plt.xlabel("Year")
        plt.plot(range(2015,2044),Mathematics.poly_fit(range(2015,2020),adop_car_b[-5:],2)(range(2015,2044)),color='red',label="Quadratic fit")
        #plt.plot(phase_out(future,per_car_adop,2035)[0],phase_out(future,per_car_adop,2035)[1],color='black',marker='o')
        plt.plot(range(1989,2051),Adoption_Rate(self.p,self.ph,self.f).adoption_bev(),color='black',label='Exponential fit')
        plt.plot(range(2001,2020),adop_car_b,label="Historic data", marker='x', linestyle="None")
        #plt.plot(2035,100,marker='o')
        #plt.plot(future,fleetsize,marker='x')
        plt.yticks(np.arange(0, 140, 20))
        plt.ylim(0,110)
        #plt.xlim(1990,2050)
        plt.legend()
        plt.savefig('adoption_bev.png', bbox_inches='tight')
        plt.show()
        
        plt.figure()
        plt.ylabel("Adoption Rate of Diesel Cars in the UK (%)")
        plt.xlabel("Year")
        plt.plot(range(1989,2051),Adoption_Rate(self.p,self.ph,self.f).adoption_diesel(),color='red',label='Linear fit')
        plt.plot(range(1989,1998),[0]*9, color='black')
        plt.plot(range(2023,2051),[0]*28, color='black')
        plt.plot(range(2004,2017),adop_car_d[3:-3],color='black')
        plt.plot(range(2001,2020),adop_car_d,label="Historic data", marker='x', linestyle="None")
        plt.legend()
        #plt.annotate('Euro 5', xy=(2009, 45),  xycoords='data',xytext=(2005, 50), textcoords='data',arrowprops=dict(facecolor='black', shrink=0.05),horizontalalignment='right', verticalalignment='top')
        plt.savefig('adoption_diesel.png', bbox_inches='tight')
        plt.show()
        
        plt.figure()
        plt.ylabel("Adoption Rate of Hybrid Cars in the UK (%)")
        plt.xlabel("Year")
        #plt.plot(range(2,2049),Vehicle_Fleet_Sizes(self.p,self.f,self.a).adoption_petrol(),color='black')
        plt.plot(range(1989,2051),Adoption_Rate(self.p,self.ph,self.f).adoption_hybrid(),label="Quadratic fit",color='red')
        plt.plot(range(2035,2051),[0]*16, color='black',label='2035 Phase-Out')
        plt.plot([2034,2035],[5.5,0],color='black')
        plt.plot(range(2001,2020),np.array(adop_car_h)+np.array(adop_car_ph),label="Historic data", marker='x',linestyle="None")
        #plt.plot(2035,1,marker='o')
        plt.legend()
        plt.savefig('adoption_hybrid.png', bbox_inches='tight')
        plt.show()
        """
        plt.figure()
        plt.ylabel("Adoption Rate of Plug-in Hybrid Cars in the UK (%)")
        plt.xlabel("Year")
        #plt.plot(range(2,2049),Vehicle_Fleet_Sizes(self.p,self.ph,self.f).adoption_petrol(),color='black')
        plt.plot(range(1989,2051),Vehicle_Fleet_Sizes(self.p,self.ph,self.f).adoption_plugin(),label="Quadratic fit",color='red')
        #plt.plot(range(2035,2051),[0]*16, color='black',label='2035 Phase-Out')
        #plt.plot([2034,2035],[5.5,0],color='black')
        plt.plot(range(2001,2020),np.array(adop_car_ph),label="Historic data", marker='x',linestyle="None")
        #plt.plot(2035,1,marker='o')
        plt.legend()
        plt.savefig('adoption_plugin.png', bbox_inches='tight')
        plt.show()
        """
        plt.figure()
        plt.ylabel("Adoption Rate of Petrol Cars in the UK (%)")
        plt.xlabel("Year")
        plt.plot(range(1989,2051),Adoption_Rate(self.p,self.ph,self.f).adoption_petrol(),color='black',label='100%-Diesel-Hybrid-BEV')
        plt.plot(range(2001,2020),adop_car_p,label="Historic data", marker='x',linestyle="None")
        #plt.plot(2035,0,marker='o')
        plt.legend()
        plt.savefig('adoption_petrol.png', bbox_inches='tight')
        plt.show()
        return()
    
    def fuel_consumption(self):
        """
        e.g. Make_Graphs(2030,1,0.05).fuel_consumption()
        """
        
        fig, ax1 = plt.subplots()
        ax1.set_ylabel("Average New Car Fuel Consumption \n (litres per 100km)")
        ax1.set_xlabel("Year")
        #plt.plot([1989,1997],petrol*10*np.array([fuel_car_p[0],fuel_car_p[0]]),label='Extrapolated data',color='black')
        #plt.plot([1989,1997],diesel*10*np.array([fuel_car_d[0],fuel_car_d[0]]),color='black')
        ax1.plot(range(1989,2051),Fuel_Consumption().petrol()[0],label='Petrol Medium Car',color='black',linestyle='dashed')
        ax1.plot(range(1989,2051),Fuel_Consumption().diesel()[0],label='Diesel Medium Car',color='blue',linestyle='dashed')
        ax1.plot(range(1989,2051),Fuel_Consumption().petrol()[1],label='Petrol SUV',color='black')
        ax1.plot(range(1989,2051),Fuel_Consumption().diesel()[1],label='Diesel SUV',color='blue')
        #plt.plot(range(1989,2051),Fuel_Consumption(self.p,self.f,self.a).hybrid(),label='Hybrid cars',color='orange')
        #ax1.plot(range(1999,2020),Fuel_Consumption().petrol()[0][10:31],label='Petrol cars',color='black')
        #ax1.plot(range(1999,2020),Fuel_Consumption().diesel()[0][10:31],label='Diesel cars',color='blue')
        ax1.plot(range(1997,2020),fuel_car_p,marker='x',linestyle="None",color='black',label='Historic data')
        ax1.plot(range(1997,2020),fuel_car_d,marker='x',linestyle="None",color='blue')
        ax1.plot(range(1989,2051),Fuel_Consumption().hybrid()[0],label='PHEV (Official Figures)',color='darkorange',linestyle='dashed')
        ax1.plot(range(1989,2051),Fuel_Consumption().hybrid()[1],label='PHEV (Real World Figures)',color='darkorange')
        #plt.plot([2019,2050],petrol*10*np.array([fuel_car_p[-1],fuel_car_p[-1]]),color='black')
        #plt.plot([2019,2050],diesel*10*np.array([fuel_car_d[-1],fuel_car_d[-1]]),color='black')
        ax1.grid()
        
        ax2=ax1.twinx()
        ax2.set_ylabel('Average New Electric Car Power \n Consumption (kWh per 100km)',color='green')
        ax2.plot(range(1989,2051),Fuel_Consumption().bev(),label='Battery-Electric Car',color='green')
        ax2.tick_params(axis='y', labelcolor='green')
        ax2.axis(ymin=5,ymax=20)
        
        fig.legend(bbox_to_anchor=(1.5, 0.85))
        fig.tight_layout()  # otherwise the right y-label is slightly clipped
        fig.savefig('fuel_consumption.png', bbox_inches='tight')
        plt.show()
        
        
        plt.figure()
        plt.ylabel("Average New Car Emissions \n (gCO2 per km)")
        plt.xlabel("Year")
        #plt.plot([1989,1997],petrol*10*np.array([fuel_car_p[0],fuel_car_p[0]]),label='Extrapolated data',color='black')
        #plt.plot([1989,1997],diesel*10*np.array([fuel_car_d[0],fuel_car_d[0]]),color='black')
        plt.plot(range(1989,2051),petrol*10*np.array(Fuel_Consumption().petrol())[0],label='Petrol Medium Car',color='black',linestyle='dashed')
        plt.plot(range(1989,2051),diesel*10*np.array(Fuel_Consumption().diesel())[0],label='Diesel Medium Car',color='blue',linestyle='dashed')
        plt.plot(range(1989,2051),petrol*10*np.array(Fuel_Consumption().petrol())[1],label='Petrol SUV',color='black')
        plt.plot(range(1989,2051),diesel*10*np.array(Fuel_Consumption().diesel())[1],label='Diesel SUV',color='blue')
        #plt.plot(range(1999,2020),petrol*10*np.array(Fuel_Consumption().petrol()[0][10:31]),label='Petrol cars',color='black')
        #plt.plot(range(1999,2020),diesel*10*np.array(Fuel_Consumption().diesel()[0][10:31]),label='Diesel cars',color='blue')
        #plt.plot(range(1989,2051),0.67*0.5*10*(diesel+petrol)*np.array(Fuel_Consumption().hybrid()),label='Hybrid cars',color='orange')
        plt.plot(range(1997,2020),petrol*10*np.array(fuel_car_p),marker='x',linestyle="None",color='black',label='Historic data')
        plt.plot(range(1997,2020),diesel*10*np.array(fuel_car_d),marker='x',linestyle="None",color='blue')
        plt.plot(range(1989,2051),petrol*10*np.array(Fuel_Consumption().hybrid())[0],label='PHEV (Official Figures)',color='darkorange',linestyle='dashed')
        plt.plot(range(1989,2051),petrol*10*np.array(Fuel_Consumption().hybrid())[1],label='PHEV (Real World Figures)',color='darkorange')
        plt.plot(range(1989,2051),10*np.array(Fuel_Consumption().bev())*np.array(Fuel_Consumption().electricity()),label='Battery-Electric cars',color='green')
        plt.plot(range(1989,2020),10*np.array(Fuel_Consumption().bev()[:31])*np.array(Fuel_Consumption().electricity()[:31]),marker='x',linestyle="None",color='green')
        #plt.plot([2019,2050],petrol*10*np.array([fuel_car_p[-1],fuel_car_p[-1]]),color='black')
        #plt.plot([2019,2050],diesel*10*np.array([fuel_car_d[-1],fuel_car_d[-1]]),color='black')
        plt.grid()
        plt.legend(bbox_to_anchor=(1, 0.85))
        plt.savefig('fuel_consumption_emissions.png', bbox_inches='tight')
        plt.show()
        
        plt.figure()
        plt.ylabel("Emissions from the UK \n Electrical Grid (kgCO2 per kWh)")
        plt.xlabel("Year")
        plt.plot(range(1989,2051),Fuel_Consumption().electricity(),color='red',label='Linear fit')
        plt.plot(range(1989,2021), elec_emissions,marker='x',linestyle="None",color='blue',label='Historic data')
        plt.grid()
        plt.legend()
        plt.savefig('electricity_emissions.png', bbox_inches='tight')
        plt.show()
        
    def km_driven(self):
        
        plt.figure()
        plt.ylabel("Annual Distance Driven by \n Cars in Great Britain (billion km)")
        plt.xlabel("Year")
        plt.plot(range(1994,2051),Distance_Driven().GB(),color='black')
        plt.plot(range(1994,2020),Distance_Driven().GB()[:26],marker='x',linestyle="None",color='black',label='Historic data')
        plt.grid()
        plt.legend()
        plt.savefig('km_gb.png', bbox_inches='tight')
        plt.show()
        
        plt.figure()
        plt.ylabel("Annual Kilometres Driven by \n Cars in London (billion km)")
        plt.xlabel("Year")
        plt.plot(range(1994,2020),km_lon)
        plt.grid()
        plt.show()
        
        plt.figure()
        plt.ylabel("Annual Kilometres Driven by the \n Average Car in Great Britain (km)")
        plt.xlabel("Year")
        plt.plot(range(1994,2051),[1000000000*i for i in Distance_Driven().GB_avg()])
        plt.grid()
        plt.show()
        
        plt.figure()
        plt.ylabel("Annual kilometres driven by the \n average car in London (km)")
        plt.xlabel("Year")
        plt.plot(range(1994,2051),[1000000000*i for i in Distance_Driven().London_avg()])
        plt.grid()
        plt.show()
        
        plt.figure()
        plt.ylabel("Relationship Between Annual \n Distance Driven and Car Age")
        plt.xlabel("Age")
        plt.plot(range(0,31),Distance_Driven().age_distribution(),color='black')
        plt.yticks([])
        plt.savefig('km_age.png', bbox_inches='tight')
        plt.show()
        
    def num_of_evs(self):
        """
        e.g. Make_Graphs(2030,1,0.05).num_of_evs()
        """
        print('Initialising model...')
        total,bev,petrol,diesel,hybrid,emissions,ages,driven_emissions,km_driven,elec_demand=evolve_fleet(2019,self.l,self.p,self.ph,self.f,self.g1,self.g2)
        
        plt.figure()
        plt.ylabel("Number of Cars in the UK (thousands)")
        plt.xlabel("Year")
        plt.plot(range(2014,2051),np.append(no_car_t,total),label='Total cars')
        plt.plot(range(2014,2051),np.append(no_car_b,bev),label='BEV cars')
        plt.plot(range(2014,2051),np.append(no_car_p,petrol),label='Petrol cars')
        plt.plot(range(2014,2051),np.append(no_car_d,diesel),label='Diesel cars')
        plt.plot(range(2014,2051),np.append(np.array(no_car_h)+np.array(no_car_ph),hybrid),label='Hybrid cars')
        plt.annotate('Phase-out date: {:d}'.format(self.p), xy=(0.01, 0.81), xycoords='axes fraction')
        plt.legend(loc='lower right')
        #plt.yticks(np.arange(0, 4000, 500))
        plt.xlim(2010,2051)
        plt.show()
        
        plt.figure()
        plt.ylabel("Average Carbon Intensity (g/km)")
        plt.xlabel("Year")
        plt.plot(range(2020,2051),emissions,label='Total cars')
        #plt.legend(loc='lower right')
        #plt.yticks(np.arange(0, 4000, 500))
        plt.xlim(2010,2051)
        plt.show()
        
        fig, ax1 = plt.subplots()
        #color = 'tab:red'
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Number of Cars in the UK (thousands)')
        ax1.plot(range(2014,2051),np.append(no_car_t,total),label='Total cars')
        ax1.plot(range(2014,2051),np.append(no_car_b,bev),label='BEV cars')
        ax1.plot(range(2014,2051),np.append(no_car_p,petrol),label='Petrol cars')
        ax1.plot(range(2014,2051),np.append(no_car_d,diesel),label='Diesel cars')
        ax1.plot(range(2014,2051),np.append(np.array(no_car_h)+np.array(no_car_ph),hybrid),label='Hybrid cars')
        ax1.annotate('Phase-out date: {:d} \nPre-2020 Scrap Age: {:d} \nPost-2020 Scrap Age: {:d}'.format(self.p,self.g1,self.g2), xy=(0.01, 1.1), xycoords='axes fraction')
        #ax1.legend(loc='lower right')
        ax1.grid()

        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
        #color = 'tab:blue'
        ax2.set_ylabel('Average Carbon Intensity (g/km)')  # we already handled the x-label with ax1
        ax2.plot(range(2020,2051),emissions,label='Average Carbon Intensity',color='black')
        ax2.axis(ymin=-3,ymax=140)

        fig.legend(bbox_to_anchor=(1.5, 0.7))
        fig.tight_layout()  # otherwise the right y-label is slightly clipped
        fig.savefig('number_of_cars.png', bbox_inches='tight')
        plt.show()
        
        plt.figure(figsize=(16,9))
        plt.ylabel("Distribution of Ages in Car Fleet (Years)")
        plt.xlabel("Year")
        ax = sns.violinplot(data=ages)
        ax.set_xticklabels(range(2020,2051))
        plt.xticks(rotation=90)
        plt.savefig('seaborn.png', bbox_inches='tight')
        plt.show()
        
        plt.figure()
        plt.ylabel("Total Car Fleet Emissions (Million tonnes of CO2)")
        plt.xlabel("Year")
        plt.plot(range(2020,2051),np.array(driven_emissions)/10**12)
        plt.grid()
        plt.savefig('total_driven_emissions.png', bbox_inches='tight')
        plt.show()
        
        print(np.array(driven_emissions)/10**12)
        
        plt.figure()
        plt.ylabel("Cumulative Total Car Fleet Emissions \n (Million tonnes of CO2)")
        plt.xlabel("Year")
        plt.plot(range(2020,2051),np.cumsum(np.array(driven_emissions)/10**12))
        plt.grid()
        plt.savefig('cum_total_driven_emissions.png', bbox_inches='tight')
        #plt.ylim(0,900)
        plt.show()
        
        plt.figure()
        plt.ylabel("Electricity Demand \n (kWh)")
        plt.xlabel("Year")
        plt.plot(range(2020,2051),np.array(elec_demand))
        plt.grid()
        plt.savefig('elec_demand.png', bbox_inches='tight')
        #plt.ylim(0,900)
        plt.show()
        

class Vehicle:
    def __init__(self, body_type, fuel_type, age):
        self.body_type = body_type
        self.fuel_type = fuel_type
        self.age = age 
        #self.y=y
        #self.emissions = emissions
    
    """
    @property
    def emissions(self):
        if self.fuel_type==1:
            emissions_value=500+5*(self.y-self.age)
        if self.fuel_type==2:
            emissions_value=1000+5*(self.y-self.age)
        return emissions_value
    """
    
    def emissions(self,y):
        emissions_value=0
        #if BEV
        if self.fuel_type==0:
            emissions_value==(Fuel_Consumption().bev()[self.age-1989]/100)*Fuel_Consumption().electricity()[self.age-1989]
        #if petrol
        if self.fuel_type==1:
            emissions_value=petrol*10*np.array(Fuel_Consumption().petrol()[0][self.age-1989])
        #if diesel
        if self.fuel_type==2:
            emissions_value=diesel*10*np.array(Fuel_Consumption().diesel()[0][self.age-1989])
        #if hybrid
        if self.fuel_type==3:
            emissions_value=petrol*10*np.array(Fuel_Consumption().hybrid()[1][self.age-1989])
        return emissions_value
    
    def prod_emissions(self):
        emissions_value=0
        #if BEV
        if self.fuel_type==0:
            emissions_value==8.8
        #if petrol
        if self.fuel_type==1:
            emissions_value=5.6
        #if diesel
        if self.fuel_type==2:
            emissions_value=5.6
        #if hybrid
        if self.fuel_type==3:
            emissions_value=6.7
        return emissions_value
        
class Mathematics:
    
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
        
class Adoption_Rate:
    
    def __init__(self,phase_out_date,phase_out_hybrid,fleet_size_projection):
        """
        Initialises class with data file
        """
        self.p=phase_out_date
        self.ph=phase_out_hybrid
        self.f=fleet_size_projection
        
    """
    def adoption_bev(self):
        
        #Creates list of adoption rates of BEVs from 1989 to 2100 in percentage
        #Generate exponential fit of adoption rate between 2019 and the phase out date,
        #then generate a straight 100% line until 2100. e.g. Vehicle_Fleet_Sizes(uk_data,2030).adoption_rate()
        #Inputs: future years, historic adoption rate and phase out year.
        
        
        # Two given datapoints to which the exponential function with power ps should fit
        #x = [2019,self.p] #Fit exponential until phase-out year
        #y = [adop_car_b[-1],100] #Fit exponential from last known adoption rate
        
        x = [2019,self.p] #Fit exponential until phase-out year
        y = [adop_car_b[-1],100] #Fit exponential from last known adoption rate
        
        def exp(x, adj1,adj2):
            return ((x+adj1) ** pw) * adj2
        
        pw = 3
        A = np.exp(np.log(y[0]/y[1])/pw)
        a = (x[0] - x[1]*A)/(A-1)
        b = y[0]/(x[0]+a)**pw
        
        #Exponential only important until it has reached 100% at phase-out date
        #exp_to_phaseout=future[6:future.index(self.p)+1]
        #exponential=exp(exp_to_phaseout,a,b)
        
        exponential=exp(range(2010,self.p+1),a,b)
        print(exponential)
        
        #Append exponential graph with a straight line at 100% adoption rate from phase-out to 2050
        #return(np.append([0]*26,np.append(np.append(adop_car_b,exponential),[100]*(2050-self.p))))
        return(np.append(np.append([0]*21,exponential),[100]*(2050-self.p)))
    """
    
        
    def adoption_bev(self):
        
        adoption_bev=[]
        adoption_diesel=Adoption_Rate(self.p,self.ph,self.f).adoption_diesel()
        adoption_petrol=Adoption_Rate(self.p,self.ph,self.f).adoption_petrol()
        adoption_hybrid=Adoption_Rate(self.p,self.ph,self.f).adoption_hybrid()
        #adoption_plugin=Vehicle_Fleet_Sizes(self.p,self.f,self.a).adoption_plugin()
        
        for i in range(0,62):
            adoption_bev.append(100-adoption_diesel[i]-adoption_petrol[i]-adoption_hybrid[i])
        
        return(adoption_bev)
    
        
    def adoption_diesel(self):
        """
        Creates list of adoption rates of diesel cars from 1989 to 2100 in percentage
        Vehicle_Fleet_Sizes(ldn_data, 2030, 1, 0.05).adoption_diesel()
        """
        diesel_increase=Mathematics.poly_fit([2001,2002,2003],adop_car_d[0:3],1)
        diesel_decrease=Mathematics.poly_fit([2017,2018,2019],adop_car_d[16:],1)
        
        #adoption_diesel=[0]*9+diesel_increase(range(1997,2002))+self.d.adop_car_d+diesel_decrease(range(2019,2022))+[0]*79
        
       # d2=diesel_increase(range(1997,2002))
        #print(d2)
        
        #adoption_diesel=[0]*9+self.d.adop_car_d
        #print(adoption_diesel)
        
        adoption_diesel=np.append(np.append(np.append([0]*9,diesel_increase(range(1998,2004))),adop_car_d[3:-3]),np.append(diesel_decrease(range(2017,2023)),[0]*28))
        return(adoption_diesel)
    """ 
    def adoption_hybrid(self):
        
        x=np.linspace(2019,2029,11)
        
        def gaussian(x, mu, sig):
            return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

        adoption_hybrid=np.append(np.append(np.append([0]*12,adop_car_h[:-1]),15*gaussian(x,2025,5)),[0]*21)
        
        return(adoption_hybrid)
    
    def adoption_plugin(self):
        
        x=np.linspace(2019,2034,16)
        
        def gaussian(x, mu, sig):
            return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

        adoption_plugin=np.append(np.append(np.append([0]*12,adop_car_ph[:-1]),10*gaussian(x,2030,7)),[0]*16)
        
        return(adoption_plugin)
    """
    
    def adoption_hybrid(self):
        
        x=np.linspace(2020,self.ph-1,self.ph-2020)
        
        def gaussian(x, mu, sig):
            return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
        if self.ph==2030:
            adoption_hybrid=np.append(np.append(np.append([0]*12,np.array(adop_car_ph)+np.array(adop_car_h)),10*gaussian(x,2020+(self.ph-2020)/2,6)),[0]*(2050-self.ph+1))
        elif self.ph==2035:
            adoption_hybrid=np.append(np.append(np.append([0]*12,np.array(adop_car_ph)+np.array(adop_car_h)),10*gaussian(x,2020+(self.ph-2020)/2,9)),[0]*(2050-self.ph+1))
        elif self.ph==2040:
            adoption_hybrid=np.append(np.append(np.append([0]*12,np.array(adop_car_ph)+np.array(adop_car_h)),10*gaussian(x,2020+(self.ph-2020)/2,12)),[0]*(2050-self.ph+1))
        else:
            adoption_hybrid=np.append(np.append(np.append([0]*12,np.array(adop_car_ph)+np.array(adop_car_h)),10*gaussian(x,2020+(self.ph-2020)/2,6)),[0]*(2050-self.ph+1))
        return(adoption_hybrid)
    
    def adoption_petrol(self):
        
        x=np.linspace(2020,self.p-1,self.p-2020)
        
        def gaussian(x, mu, sig):
            return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
        
        if self.p==2025:
            adoption_petrol=np.append(np.append(np.append([100]*12,adop_car_p),80*gaussian(x,2020+(self.p-2020)/4,3)),[0]*(2050-self.p+1))
        elif self.p==2030:
            adoption_petrol=np.append(np.append(np.append([100]*12,adop_car_p),80*gaussian(x,2020+(self.p-2020)/4,5)),[0]*(2050-self.p+1))
        elif self.p==2035:
            adoption_petrol=np.append(np.append(np.append(np.append(np.append([100]*12,adop_car_p),80*gaussian(np.linspace(2020,2021,2),2021,3)),[80]*3),80*gaussian(np.linspace(2025,2034,10),2025,5)),[0]*(2050-self.p+1))
        elif self.p==2040:
            adoption_petrol=np.append(np.append(np.append(np.append(np.append([100]*12,adop_car_p),80*gaussian(np.linspace(2020,2021,2),2021,3)),[80]*8),80*gaussian(np.linspace(2030,2039,10),2030,5)),[0]*(2050-self.p+1))
        else:
            adoption_petrol=np.append(np.append(np.append([100]*12,adop_car_p),80*gaussian(x,2020+(self.p-2020)/4,9)),[0]*(2050-self.p+1))
        return(adoption_petrol)
    """
    def adoption_petrol(self):
        
        adoption_petrol=[]
        adoption_diesel=Vehicle_Fleet_Sizes(self.p,self.f,self.a).adoption_diesel()
        adoption_bev=Vehicle_Fleet_Sizes(self.p,self.f,self.a).adoption_rate()
        adoption_hybrid=Vehicle_Fleet_Sizes(self.p,self.f,self.a).adoption_hybrid()
        adoption_plugin=Vehicle_Fleet_Sizes(self.p,self.f,self.a).adoption_plugin()
        
        for i in range(0,60):
            adoption_petrol.append(100-adoption_diesel[i]-adoption_bev[i]-adoption_hybrid[i]-adoption_plugin[i])
        return(adoption_petrol)
    """
    
class Fuel_Consumption:
    """
    Fuel_Consumption(2030,1,0.05).petrol()
    """
        
    def petrol(self):
        
        pre_1997=Mathematics.poly_fit([1997,1998,1999],fuel_car_p[0:3],1)
        post_2020_typ=Mathematics.straight_fit(2020,fuel_car_p[-1],2050,4.5,range(2020,2051))
        post_2020_suv=Mathematics.straight_fit(2020,fuel_car_p[-1],2050,8.7,range(2020,2051))
        fuel_petrol_typ=np.append(pre_1997(range(1989,2000)),np.append(fuel_car_p[3:],post_2020_typ))
        fuel_petrol_suv=np.append(pre_1997(range(1989,2000)),np.append(fuel_car_p[3:],post_2020_suv))
        return fuel_petrol_typ,fuel_petrol_suv
        
    def diesel(self):
        
        pre_1997=Mathematics.poly_fit([1997,1998,1999],fuel_car_d[0:3],1)
        post_2020_typ=Mathematics.straight_fit(2020,fuel_car_d[-1],2050,3.3,range(2020,2051))
        post_2020_suv=Mathematics.straight_fit(2020,fuel_car_d[-1],2050,6.5,range(2020,2051))
        fuel_diesel_typ=np.append(pre_1997(range(1989,2000)),np.append(fuel_car_d[3:],post_2020_typ))
        fuel_diesel_suv=np.append(pre_1997(range(1989,2000)),np.append(fuel_car_d[3:],post_2020_suv))
        return fuel_diesel_typ,fuel_diesel_suv
    
    def hybrid(self):
        
        #hybrid=(0.5*(np.array(Fuel_Consumption().petrol())+np.array(Fuel_Consumption().diesel())))
        official=[1.66]*62
        realworld=[4.4]*62
        return official,realworld
    
    def bev(self):
        
        #bev=Mathematics.straight_fit(2020,15,2050,10,range(2020,2051))
        return([15]*62)
    
    def electricity(self):
        
        projection=Mathematics.straight_fit(2020,elec_emissions[-1],2050,0.029,range(2021,2051))
        return np.append(elec_emissions,projection)
        
class Distance_Driven:
    """
    Calculates distance driven by average car by dividing total km driven by whole fleet from data with number of fleet in data
    """
    
    def GB(self):
        projection=Mathematics.straight_fit(2020,km_gb[-1],2050,km_gb[-1],range(2020,2052))
        return np.append(km_gb,projection)
    
    def UK(self):
        #plus 20 for ireland
        projection=Mathematics.straight_fit(2020,km_gb[-1]+20,2050,km_gb[-1]+20,range(2020,2052))
        return np.append(np.array(km_gb)+20,projection)
    
    def Lon(self):
        projection=Mathematics.straight_fit(2020,km_lon[-1],2050,km_lon[-1],range(2020,2052))
        return np.append(np.array(km_lon),projection)
    
    def GB_avg(self):
        avg_km=np.array(km_gb)/np.array(no_car_gb)
        projection=Mathematics.straight_fit(2020,avg_km[-1],2050,avg_km[-1],range(2020,2052))
        return np.append(avg_km,projection)
    
    def London_avg(self):
        avg_km=np.array(km_lon)/np.array(no_car_lon)
        projection=Mathematics.straight_fit(2020,avg_km[-1],2050,avg_km[-1],range(2020,2052))
        return np.append(avg_km,projection)
    
    def age_distribution(self):
        x=np.array(range(0,31))
        y=(x**2-60*x+900)/900
        area_under=np.trapz(y,x)
        return y/area_under
    
def initialise_fleet(year,l,p,ph,f):
    """
    Generate a vehicle fleet based on base data. Evolve it through time based on projections.
    e.g. initialise_fleet(2019,2030,1,0.05)
    """
    
    #if model in uk (0) or london (1)
    if l==0:
        car_fleet_size=uk_car_2019
    elif l==1:
        car_fleet_size=lon_car_2019
    adoption_diesel=Adoption_Rate(p,ph,f).adoption_diesel()
    adoption_bev=Adoption_Rate(p,ph,f).adoption_bev()
    adoption_hybrid=Adoption_Rate(p,ph,f).adoption_hybrid()
    adoption_petrol=Adoption_Rate(p,ph,f).adoption_petrol()
    
    car_list=[]
    
    print('the following number of cars were made every year in the 2019 fleet')
    
    #for every year of manufacture i.e. 1989 to 2019 (31 years)
    for i in range(0,len(car_age)):
        
        dcount=0
        bcount=0
        pcount=0
        hcount=0
        
        #make diesel cars (fuel type 2)
        # % of cars that age * 2019 car fleet size * adoption of diesel cars that year /100 from adoption percentage
        for j in range(0,int(car_age[i]*car_fleet_size*adoption_diesel[i]/100)):
            c=Vehicle(body_type=0,fuel_type=2,age=(1989+i))
            car_list.append(c)
            dcount=dcount+1
        
        #make bev fuel type 0
        for j in range(0,int(car_age[i]*car_fleet_size*adoption_bev[i]/100)):
            c=Vehicle(body_type=0,fuel_type=0,age=(1989+i))
            car_list.append(c)
            bcount=bcount+1
            
        #make hybrid fuel type 3
        for j in range(0,int(car_age[i]*car_fleet_size*adoption_hybrid[i]/100)):
            c=Vehicle(body_type=0,fuel_type=3,age=(1989+i))
            car_list.append(c)
            hcount=hcount+1
        
        #make petrol fuel type 1
        for j in range(0,int(car_age[i]*car_fleet_size*adoption_petrol[i]/100)):
            c=Vehicle(body_type=0,fuel_type=1,age=(1989+i))
            car_list.append(c)
            pcount=pcount+1
            
        print('year:',1989+i,'petrol cars:', pcount,'diesel cars:', dcount,'bev cars:',bcount,'hybrid cars:',hcount)
        
    print('all cars=',len(car_list))
    print('petrol=',sum(p.fuel_type == 1 for p in car_list))
    print('diesel=',sum(p.fuel_type == 2 for p in car_list))
    print('bev=',sum(p.fuel_type == 0 for p in car_list))
    print('hybrid=',sum(p.fuel_type == 3 for p in car_list))
    
    return car_list

def evolve_fleet(year,l,p,ph,f,g1,g2):
    """
    evolve_fleet(2019,2030,1,0.05)
    """
    
    #create car list from vehicle initialisation class sorted by year of 
    #manufacture in ascending order (oldest cars first)
    car_list=initialise_fleet(year,l,p,ph,f) 
    
    total_cars=[]
    bev_cars=[]
    petrol_cars=[]
    diesel_cars=[]
    hybrid_cars=[]
    avg_emissions=[]
    ages=[]
    driven_emissions=[]
    production_emissions=[]
    elec_demand=[]
    
    #new cars = fleet size from projection - cars currently in the object list (after removal)
    #slight discrepancy between vehicle fleet sizes list I have constructed and actual data (ie for fleet projection)

    #find future fleet size (either no growth, increase or reduction scenarios)
    if f==-1:
        fleetsize=Mathematics.straight_fit(2019,no_car_lon[-1],2051,no_car_lon[-1]/2,range(2020,2052))
        print(fleetsize)
    else:
        fleetsize=Mathematics.poly_fit(range(2014,2020),no_car_lon[-6:],f)(range(2020,2052))


    #find number of new cars needed every year to satisfy total fleet size
    #cars in year n+1 - cars in year n + cars removed

    #since number of cars rely on the year beforehand, need to create arrays with value 0 at index 0
    #then create loop for index 1 to 80 (i.e. 2020 to 2100), removing index 0 afterwards
    #new=[0]
    #for i in range(1,80):
    #    new.append(fleetsize[i+1]-fleetsize[i]+cars_removed)
    #new.pop(0)
    
    #for evolution of fleet from 2020 to 2050
    for i in range(0,31):
        #print('year=',2020+i)
        
        
        #delete cars older than 15 years of age and save into new list
        #car_list.remove(p.age < (2020+i-15) for p in car_list)
        #car_list.remove(p.age == 0 for p in car_list)
        before_removal=len(car_list)
        
        #car_list[:] =[car_list2 for car_list2 in car_list if car_list2.age>=2020+i-10]
        
        #[car_list2 for car_list2 in car_list]
        
        #if any([car_list2.age<2020 if car_list2.age>=2020+i-20, car_list2.age>=2020 if carlist2.age>=2020+i-15])]
        
        #remove cars based on a grandfathering policy
        car_list2=[]
        for j in range(0,len(car_list)):
            if car_list[j].age<2020:
                #for cars made prior to 2020, allow a longer age
                if car_list[j].age>=2020+i-g1:
                    car_list2.append(car_list[j])
            else:
                #for cars made post 2020, make scrap policy happen earlier
                if car_list[j].age>=2020+i-g2:
                    car_list2.append(car_list[j])
                    
        car_list=car_list2
        

        after_removal=len(car_list)
        
        #find how many cars removed
        cars_removed=before_removal-after_removal
    
        new_cars=fleetsize[i+1]-fleetsize[i]+cars_removed
        new_BEV=int(Adoption_Rate(p,ph,f).adoption_bev()[i+30]/100*new_cars)
        new_diesel=int(Adoption_Rate(p,ph,f).adoption_diesel()[i+30]/100*new_cars)
        new_hybrid=int(Adoption_Rate(p,ph,f).adoption_hybrid()[i+30]/100*new_cars)
        new_petrol=int(Adoption_Rate(p,ph,f).adoption_petrol()[i+30]/100*new_cars)
        
        print('fleetsize[i+1]',fleetsize[i+1],'fleetsize[i]',fleetsize[i],'cars removed',cars_removed)
        
        print('year=',2020+i,'new cars=',new_cars, 'new bevs=', new_BEV, 'new petrol=',new_petrol, 'new diesel', new_diesel, 'new hybrid', new_hybrid)
        
        #make BEVs based on adoption rate* new cars
        for j in range(0,new_BEV):
            c=Vehicle(body_type=0,fuel_type=0,age=2020+i)
            car_list.append(c)
        #make remaining new cars petrol
        for j in range(0,new_petrol):
            c=Vehicle(body_type=0,fuel_type=1,age=2020+i)
            car_list.append(c)
        for j in range(0,new_diesel):
            c=Vehicle(body_type=0,fuel_type=2,age=2020+i)
            car_list.append(c)
        for j in range(0,new_hybrid):
            c=Vehicle(body_type=0,fuel_type=3,age=2020+i)
            car_list.append(c)
        
        #find no of cars
        total_cars.append(len(car_list))
        print('length of car list',len(car_list))
        bev_cars.append(sum(p.fuel_type == 0 for p in car_list))
        #print(sum(p.fuel_type == 0 for p in car_list))
        petrol_cars.append(sum(p.fuel_type==1 for p in car_list))
        diesel_cars.append(sum(p.fuel_type==2 for p in car_list))
        hybrid_cars.append(sum(p.fuel_type==3 for p in car_list))
        
        #find carbon intensity
        total_emissions=sum(p.emissions(2020+i) for p in car_list)
        avg_emissions.append(total_emissions/len(car_list))
        print('total emissions',total_emissions,'average emissions',avg_emissions[i])
        
        
        #find age distribution for violin plot
        age_list=[(2020+i-x.age) for x in car_list]
        ages.append(age_list)
        #print('age_list=',age_list)
        #print('ages=',ages)
        
        
        #driving the fleet
        #find distribution of mileage of each age group (quadratic)
        km=Distance_Driven().age_distribution()
        
        #find number of cars in each age group * mileage distribution to find how much each age group contributes to total miles driven
        age0=sum(p.age==2020+i for p in car_list)*km[0]
        age1=sum(p.age==2020+i-1 for p in car_list)*km[1]
        age2=sum(p.age==2020+i-2 for p in car_list)*km[2]
        age3=sum(p.age==2020+i-3 for p in car_list)*km[3]
        age4=sum(p.age==2020+i-4 for p in car_list)*km[4]
        age5=sum(p.age==2020+i-5 for p in car_list)*km[5]
        age6=sum(p.age==2020+i-6 for p in car_list)*km[6]
        age7=sum(p.age==2020+i-7 for p in car_list)*km[7]
        age8=sum(p.age==2020+i-8 for p in car_list)*km[8]
        age9=sum(p.age==2020+i-9 for p in car_list)*km[9]
        age10=sum(p.age==2020+i-10 for p in car_list)*km[10]
        age11=sum(p.age==2020+i-11 for p in car_list)*km[11]
        age12=sum(p.age==2020+i-12 for p in car_list)*km[12]
        age13=sum(p.age==2020+i-13 for p in car_list)*km[13]
        age14=sum(p.age==2020+i-14 for p in car_list)*km[14]
        age15=sum(p.age==2020+i-15 for p in car_list)*km[15]
        age16=sum(p.age==2020+i-16 for p in car_list)*km[16]
        age17=sum(p.age==2020+i-17 for p in car_list)*km[17]
        age18=sum(p.age==2020+i-18 for p in car_list)*km[18]
        age19=sum(p.age==2020+i-19 for p in car_list)*km[19]
        age20=sum(p.age==2020+i-20 for p in car_list)*km[20]
        sum_age=age0+age1+age2+age3+age4+age5+age6+age7+age8+age9+age10+age11+age12+age13+age14+age15+age16+age17+age18+age19+age20
        
        #find km scale factor that matches total miles driven (go from billion km to km)
        if l==0:
            x=(Distance_Driven().UK()[i+27]*1000000000)/sum_age
        elif l==1:
            x=(Distance_Driven().Lon()[i+27]*1000000000)/sum_age
        
        #thus, find total km driven by each age group
        #unused variable ?
        km_driven=[age0*x,age1*x,age2*x,age3*x,age4*x,age5*x,age6*x,age7*x,age8*x,age9*x,age10*x,age11*x,age12*x,age13*x,age14*x,age15*x,age16*x,age17*x,age18*x,age19*x,age20*x]
        
        """
        plt.figure()
        plt.ylabel("Total Annual Distance driven \n by Car Age (billion km)")
        plt.xlabel("Age")
        plt.plot(range(0,21),np.array(km_driven)/10**9,color='black')
        plt.grid()
        plt.savefig('total_km_age.png', bbox_inches='tight')
        plt.show()
        
        plt.figure()
        plt.ylabel("Annual Distance driven \n by Car Age (billion km)")
        plt.xlabel("Age")
        plt.plot(range(0,31),np.array(km)*x,color='black')
        plt.grid()
        plt.savefig('mag_km_age.png', bbox_inches='tight')
        plt.show()
        """
        
        driving_emissions=[]
        elec_demand_yearly=[]
        #for every car in list
        for j in range(0,len(car_list)):
            #add emissions from that car to yearly list (emissions=carbon intensity*quadratic age distribution*km scale factor)
            driving_emissions.append(car_list[j].emissions(2020+i)*km[2020+i-car_list[j].age]*x)
            if car_list[j].fuel_type==0:
                #0.15kwh/km * km
                elec_demand_yearly.append(0.15*km[2020+i-car_list[j].age]*x)
        driven_emissions.append(sum(driving_emissions))
        elec_demand.append(sum(elec_demand_yearly))
        print('driven emissions=',driven_emissions)
        print('electricity demand=', elec_demand)
        
        """
        prod_emissions=[]
        for j in range(0,len(car_list)):
            prod_emissions.append(car_list[j].prod_emissions)
        production_emissions.append(sum(prod_emissions))
        print('production emissions=',)
        """
        
        
            
    
   # print(petrol_cars[-1])
   # print(total_cars[-1]-ev_cars[-1])
        
    return(total_cars,bev_cars,petrol_cars,diesel_cars,hybrid_cars,avg_emissions,ages,driven_emissions,km_driven,elec_demand)
        