"""Module containing main method for the UTPM"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.cm as mpl_cm
import matplotlib.pylab as pl
import seaborn as sns

import sub_models
import evolve_fleet

print("This is my file to test Python's execution methods.")
print("The variable __name__ tells me which context this file is running in.")
print("The value of __name__ is:", repr(__name__))
print("File has changed")

def Run_Model(phase_out_date,phase_out_hybrid,scrap_age_pre2020,scrap_age_post2020,mass,\
                fleet_size_projection,miles_driven_projection,retrofit_percentage,manufacture,elec,rate):
    
    #Run evolve fleet function with parameters given
    results_dict=evolve_fleet.evolve_fleet(phase_out_date,phase_out_hybrid,scrap_age_pre2020,scrap_age_post2020,mass,\
                fleet_size_projection,miles_driven_projection,retrofit_percentage,manufacture,elec,rate)
    #print(results_dict)

    #Print policy choices
    print('Policies: Phase-Out:',phase_out_date,'Hybrid Phase-Out:',phase_out_hybrid,'Scrap Age:',scrap_age_post2020,\
          'Light-weighting:',mass,'Modal shift:',fleet_size_projection,'Retro-fitting:',retrofit_percentage,\
          'Regulated manufacture:',manufacture,'Electricity decarb:',elec,'Modal Shift Rate:',rate)


    if __name__ == '__main__':

        #Make emission graphs for the model run
        import matplotlib.cm as mpl_cm
        import matplotlib.pylab as pl
        SMALL_SIZE = 15
        MEDIUM_SIZE = 17
        BIGGER_SIZE = 18
        plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
        plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
        plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
        plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
        plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
        
        fig, axs = plt.subplots(1, 3,figsize=(16,6))
        # horizontal space between axes
        fig.subplots_adjust(wspace=0.5)

        axs[0].set_ylabel("Number of Cars in\n London (thousands)")
        axs[0].set_xlabel("Year")
        axs[0].plot(range(2020,2051),results_dict['total_cars'],label='Total cars')
        axs[0].plot(range(2020,2051),results_dict['bev_cars'],label='BEV cars')
        axs[0].plot(range(2020,2051),results_dict['petrol_cars'],label='Petrol cars')
        axs[0].plot(range(2020,2051),results_dict['diesel_cars'],label='Diesel cars')
        axs[0].plot(range(2020,2051),results_dict['conv_cars'],label='Retrofitted cars')
        axs[0].plot(range(2020,2051),results_dict['plugin_cars'],label='PHEV cars')
        axs[0].legend(bbox_to_anchor=(0.8,-0.2))
        axs[0].set_xlim(2020,2050)
        axs[0].grid()

        axs[1].stackplot(range(2020,2051),np.array(results_dict['electric_emiss']),np.array(results_dict['tailpipe_emiss']),np.array(results_dict['ev_prod_emiss']),np.array(results_dict['ice_prod_emiss']),np.array(results_dict['conv_prod_emiss']),np.array(results_dict['mod_shift_emiss']), labels=['Electricity Emissions','Tailpipe Emissions','EV Embedded Emissions','ICE Embedded Emissions','Retrofit Embedded Emissions','Replacement Mode Emissions'],colors=['black','blue','red','orange','purple','skyblue'],alpha=0.8,linestyle='None')
        axs[1].set_ylabel('Emissions (MtCO2)')
        axs[1].set_xlabel('Year')
        #axs[1].legend(bbox_to_anchor=(1.7, 0.7))
        axs[1].set_xlim(2020,2050)
        axs[1].grid()

        axs[2].stackplot(range(2020,2051),np.cumsum(np.array(results_dict['electric_emiss'])),np.cumsum(np.array(results_dict['tailpipe_emiss'])),np.cumsum(np.array(results_dict['ev_prod_emiss'])),np.cumsum(np.array(results_dict['ice_prod_emiss'])),np.cumsum(np.array(results_dict['conv_prod_emiss'])),np.cumsum(np.array(results_dict['mod_shift_emiss'])), labels=['Electricity Emissions','Tailpipe Emissions','EV Embedded Emissions','ICE Embedded Emissions','Retrofit Embedded Emissions','Replacement Mode Emissions'],colors=['black','blue','red','orange','purple','skyblue'],alpha=0.8,linestyle='None')
        axs[2].set_ylabel('Cumulative Emissions (MtCO2)')
        axs[2].set_xlabel('Year')
        axs[2].legend(bbox_to_anchor=(0.3,-0.2))
        axs[2].set_xlim(2020,2050)
        axs[2].grid()
        plt.savefig('UTPM_result.png', bbox_inches="tight")

        plt.show()

        #Make energy demand graphs
        plt.figure()
        plt.stackplot(range(2020,2051),np.array(results_dict['elec_demand']),np.array(results_dict['foss_demand']),np.array(results_dict['ev_prod_energy']),np.array(results_dict['ice_prod_energy']),np.array(results_dict['conv_prod_energy']),np.array(results_dict['mod_shift_energy']), labels=['Electricity','Fossil Fuel Energy','EV Embedded Energy','ICE Embedded Energy','Retrofit Embedded Energy','Replacement Mode Energy'],colors=['black','blue','red','orange','purple','skyblue'],alpha=0.8,linestyle='None')
        plt.ylabel('Energy Demand (MJ)')
        plt.xlabel('Year')
        plt.legend(bbox_to_anchor=(1.9, 0.7))
        plt.xlim(2020,2050)
        plt.grid()
        plt.show()

        plt.figure()
        plt.stackplot(range(2020,2051),np.cumsum(np.array(results_dict['elec_demand'])),np.cumsum(np.array(results_dict['foss_demand'])),np.cumsum(np.array(results_dict['ev_prod_energy'])),np.cumsum(np.array(results_dict['ice_prod_energy'])),np.cumsum(np.array(results_dict['conv_prod_energy'])),np.cumsum(np.array(results_dict['mod_shift_energy'])), labels=['Electricity','Fossil Fuel Energy','EV Embedded Energy','ICE Embedded Energy','Retrofit Embedded Energy','Replacement Mode Energy'],colors=['black','blue','red','orange','purple','skyblue'],alpha=0.8,linestyle='None')
        plt.ylabel('Cumulative\nEnergy Demand (MJ)')
        plt.xlabel('Year')
        plt.legend(bbox_to_anchor=(1.9, 0.7))
        plt.xlim(2020,2050)
        plt.grid()
        plt.show()

    results_dict['cum_electric']=np.append(0,np.cumsum(np.array(results_dict['electric_emiss'])))
    results_dict['cum_tailpipe']=np.append(0,np.cumsum(np.array(results_dict['tailpipe_emiss'])))
    results_dict['cum_ev_prod']=np.append(0,np.cumsum(np.array(results_dict['ev_prod_emiss'])))
    results_dict['cum_ice_prod']=np.append(0,np.cumsum(np.array(results_dict['ice_prod_emiss'])))
    results_dict['cum_wtt_emiss']=np.append(0,np.cumsum(np.array(results_dict['wtt_emiss'])))
    results_dict['cum_conv_prod']=np.append(0,np.cumsum(np.array(results_dict['conv_prod_emiss'])))
    results_dict['cum_mod_shift_emiss']=np.append(0,np.cumsum(np.array(results_dict['mod_shift_emiss'])))

    results_dict['cum_elec']=np.append(0,np.cumsum(np.array(results_dict['elec_demand'])))
    results_dict['cum_foss']=np.append(0,np.cumsum(np.array(results_dict['foss_demand'])))
    results_dict['cum_wtt_en']=np.append(0,np.cumsum(np.array(results_dict['wtt_energy'])))
    results_dict['cum_ev_en']=np.append(0,np.cumsum(np.array(results_dict['ev_prod_energy'])))
    results_dict['cum_ice_en']=np.append(0,np.cumsum(np.array(results_dict['ice_prod_energy'])))
    results_dict['cum_conv_en']=np.append(0,np.cumsum(np.array(results_dict['conv_prod_energy'])))
    results_dict['cum_mod_en']=np.append(0,np.cumsum(np.array(results_dict['mod_shift_energy'])))

    #ages list too long for csv output so set to 0
    results_dict['ages']=0
    
    return results_dict

#run main method for UTPM
if __name__ == '__main__':
    #Run base case
    #base=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
    extreme1=Run_Model(phase_out_date=2025,phase_out_hybrid=2025,scrap_age_pre2020=15,scrap_age_post2020=10,mass=840,fleet_size_projection=-70,miles_driven_projection=-70,retrofit_percentage=0.2,manufacture=1,elec=2020,rate=3)
    extreme2=Run_Model(phase_out_date=2025,phase_out_hybrid=2025,scrap_age_pre2020=15,scrap_age_post2020=10,mass=840,fleet_size_projection=-82,miles_driven_projection=-82,retrofit_percentage=0.2,manufacture=1,elec=2020,rate=5)
    print(extreme1['cum_tailpipe'])
    print(extreme2['cum_tailpipe'])