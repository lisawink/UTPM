"""Data required to run the UTPM for London"""
"""Data sourced primarily from the Department for Transport (DfT): https://www.gov.uk/government/organisations/department-for-transport/about/statistics"""

#2019 number of cars in London (thousands) [DfT VEH0204]
cars_2019=2661

# adoption rate of fuel type in GB yearly from 2001/2015 to 2020 [DfT VEH0253]
# number of newly registered vehicles of fuel type / total new registrations in that year
adop_car_p=[82.1,76.2,72.3,67.3,63.2,61.5,59.3,56.0,57.8,53.1,48.5,48.1,49.0,48.1,49.0,49.3,53.5,62.3,65.6,62.5]
adop_car_d=[17.8,23.7,27.5,32.6,36.6,38.1,40.0,43.2,41.4,45.7,50.3,50.5,49.5,49.8,48.2,47.4,41.8,31.4,26.3,18.9]
adop_car_h=[0]*3+[0.1,0.2,0.4,0.7,0.7,0.7,1.1,1.2,1.2,1.3,1.5,1.7,1.9,2.8,3.7,4.9,9.4]
adop_car_ph=[0]*13+[0.3,0.7,1.0,1.3,1.8,1.5,3.3]
adop_car_b=[0]*10+[0.1,0.1,0.1,0.3,0.4,0.4,0.5,0.7,1.6,5.8]

#2019 ages of cars in % of cars at given age starting from 0 to 30+ (i.e. 2019 to <1989)
car_per_age=[6.701865813,6.865554769,7.316778939,7.803457088,7.685096727,7.201434605,6.537954259,5.55890771,5.143852754,5.264539452,5.021894934,
     4.926460392,5.162837486,4.390143996,3.717893513,3.07826344,2.417367913,1.756067938,1.103872606,0.678520949,0.452388859,0.305495142,
     0.21615469,0.146699095,0.111399597,0.07995604,0.063239866,0.052973575,0.060591188,0.05324118,0.087805982]
#swap order of cars (oldest first) and put in decimal form
car_age=list(car_per_age[-i]/100 for i in range(0,31))

#average fuel consumption in litres per 100km for new cars registered from 1997 to 2019 [DfT ENV0103]
fuel_car_p=[8.3,8.3,8.1,8.0,7.9,7.8,7.7,7.6,7.5,7.4,7.2,7.0,6.5,6.3,6.1,5.8,5.6,5.5,5.4,5.4,5.5,5.6,5.7]
fuel_car_d=[7.0,6.9,6.6,6.3,6.2,6.1,6.2,6.2,6.2,6.3,6.2,5.9,5.7,5.5,5.2,5.0,4.9,4.7,4.6,4.5,4.6,4.9,5.1]

#km driven per year by cars & taxis in London in 2019 (billion km) [DfT TRA0206]
km_2019=28.1
