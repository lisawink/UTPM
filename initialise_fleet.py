"""Function to initialise the fleet"""

import LondonData as regional_data
from sub_models import Adoption_Rate
from sub_models import Vehicle

def initialise_fleet(p,ph,m,fs,md,c,e):
    """
    Generate a model car fleet for the year 2019 based on 2019 data.
    """
    
    car_fleet_size=regional_data.cars_2019
    
    #find adoption rates of fuel types
    adoption_diesel=Adoption_Rate(p,ph).adoption_diesel()
    adoption_bev=Adoption_Rate(p,ph).adoption_bev()
    adoption_plugin=Adoption_Rate(p,ph).adoption_plugin()
    adoption_petrol=Adoption_Rate(p,ph).adoption_petrol()+Adoption_Rate(p,ph).adoption_hybrid()
    
    car_list=[]
    
    #to avoid small number of cars aged 20-30+ skewing model results from scrapping, remove these from list
    #cut first 10 years of car age and distribute proportionally on all other years
    new_car_age=list(regional_data.car_age[i]/sum(regional_data.car_age[10:]) for i in range(10,31))
    
    #for every year of manufacture i.e. 1999 to 2019 (21 years)
    for i in range(0,len(new_car_age)):
        dcount=0
        bcount=0
        pcount=0
        hcount=0
        
        #make diesel cars (fuel type 0)
        # % of cars that age * 2019 car fleet size * adoption of diesel cars that year /100 
        for j in range(0,int(new_car_age[i]*car_fleet_size*adoption_diesel[i]/100)):
            c=Vehicle(fuel_type=0,age=(1999+i),mass=m,manufacture=c,elec=e)
            car_list.append(c)
            dcount=dcount+1
            
        #make petrol fuel type 1
        for j in range(0,int(new_car_age[i]*car_fleet_size*adoption_petrol[i]/100)):
            c=Vehicle(fuel_type=1,age=(1999+i),mass=m,manufacture=c,elec=e)
            car_list.append(c)
            pcount=pcount+1    
        
        #make plug-in hybrid fuel type 2
        for j in range(0,int(new_car_age[i]*car_fleet_size*adoption_plugin[i]/100)):
            c=Vehicle(fuel_type=2,age=(1999+i),mass=m,manufacture=c,elec=e)
            car_list.append(c)
            hcount=hcount+1
        
        #make bev fuel type 4
        for j in range(0,int(new_car_age[i]*car_fleet_size*adoption_bev[i]/100)):
            c=Vehicle(fuel_type=4,age=(1999+i),mass=m,manufacture=c,elec=e)
            car_list.append(c)
            bcount=bcount+1
               
        #print('year:',1989+i,'petrol cars:', pcount,'diesel cars:', dcount,'bev cars:',bcount,'phev cars:',hcount)
        
    #print('all cars=',len(car_list))
    #print('petrol&hybrid=',sum(p.fuel_type == 1 for p in car_list))
    #print('diesel=',sum(p.fuel_type == 0 for p in car_list))
    #print('bev=',sum(p.fuel_type == 4 for p in car_list))
    #print('plug-in hybrid=',sum(p.fuel_type == 2 for p in car_list))
    
    return car_list