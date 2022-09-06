import UTPM_Run_Model
from IPython.display import Markdown, display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def printmd(string):
    display(Markdown(string))

#Only runs model if results have not been run before
try:
    policy_results=pd.read_csv('fig1.csv',index_col=0)
    print('Model already run')
    print(policy_results)
except:
    print('Running model')
    policy_results={}
    policy_results['base']=UTPM_Run_Model.Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
    policy_results['base_ren']=UTPM_Run_Model.Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2020,rate=28)
    policy_results['p3030']=UTPM_Run_Model.Run_Model(phase_out_date=2030,phase_out_hybrid=2030,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
    policy_results['p2525']=UTPM_Run_Model.Run_Model(phase_out_date=2025,phase_out_hybrid=2025,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
    policy_results['third_rf']=UTPM_Run_Model.Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0.33,manufacture=0,elec=2050,rate=28)
    policy_results['lw_20']=UTPM_Run_Model.Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1120,\
                fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
    policy_results['lw_40']=UTPM_Run_Model.Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=840,\
                fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
    policy_results['base_eu']=UTPM_Run_Model.Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=1,elec=2050,rate=28)
    policy_results['mts1']=UTPM_Run_Model.Run_Model(phase_out_date=2030,phase_out_hybrid=2030,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                fleet_size_projection=-12,miles_driven_projection=-12,retrofit_percentage=0,manufacture=0,elec=2050,rate=19)
    policy_results['mts2']=UTPM_Run_Model.Run_Model(phase_out_date=2030,phase_out_hybrid=2030,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                fleet_size_projection=-27,miles_driven_projection=-27,retrofit_percentage=0,manufacture=0,elec=2050,rate=8)               
    policy_results['d4343']=UTPM_Run_Model.Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                fleet_size_projection=-42.99,miles_driven_projection=-42.99,retrofit_percentage=0,manufacture=0,elec=2050,rate=5)
    policy_results['d6666']=UTPM_Run_Model.Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                fleet_size_projection=-66,miles_driven_projection=-66,retrofit_percentage=0,manufacture=0,elec=2050,rate=5)
    policy_results['d8181']=UTPM_Run_Model.Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                fleet_size_projection=-81,miles_driven_projection=-81,retrofit_percentage=0,manufacture=0,elec=2050,rate=5)
    policy_results['extreme1']=UTPM_Run_Model.Run_Model(phase_out_date=2025,phase_out_hybrid=2025,scrap_age_pre2020=15,scrap_age_post2020=10,mass=840,\
                fleet_size_projection=-76,miles_driven_projection=-76,retrofit_percentage=0.2,manufacture=1,elec=2020,rate=3)
    policy_results['extreme2']=UTPM_Run_Model.Run_Model(phase_out_date=2025,phase_out_hybrid=2025,scrap_age_pre2020=15,scrap_age_post2020=10,mass=840,\
                fleet_size_projection=-88,miles_driven_projection=-88,retrofit_percentage=0.2,manufacture=1,elec=2020,rate=5)
    df = pd.DataFrame(policy_results) 
    df.to_csv('fig1.csv', index=True)
"""
    with pd.ExcelWriter('fig1.xlsx') as writer:  
        for key1 in policy_results.keys():
            for key2 in policy_results[key1].keys()
                policy_results[key1][key2].to_excel(writer, sheet_name=key1+key2)
"""


#results_by_category gives a list of emissions and energy demand results for each policy outcome by results category for the plot
results_fig1={}
results_categories=['electric_emiss','tailpipe_emiss','wtt_emiss','ev_prod_emiss','ice_prod_emiss','conv_prod_emiss',
                    'elec_demand','foss_demand','ev_prod_energy','ice_prod_energy','conv_prod_energy']

#ISSUE IS IN THE SAVING AND READING OF THE CSV FILE
#policy_reuslts['base']['electric_emiss'] is read as a string rather than a list of floats

for i in results_categories:
    results_fig1[i]=[]
    for j in policy_results:
        results_fig1[i].append(policy_results[j][i][-1])
    #append with 0 for carbon budget bar
    results_fig1[i].append(0)
    results_fig1[i]=np.array(results_fig1[i])

    print('this is results fig 1')
    print(results_fig1)

labels_fig1=["Baseline","BEVs Powered by 100%\nRenewable Energy","Fossil Fuel Phase-Out: 2030", "2025","Retrofitting: 33%",
   "Light-weighting: 20%","40%", "Regulated EV Manufacture",
   "Local Transport Strategy","Local Net-Zero 2030 Target","Car Travel Activity (CTA): -43%","-66%","-81%",
   "Combined Policies with CTA:\n-76% by 2025","-88% by 2027","Use-Phase Carbon Budget if\nHistorical Share Continues"]

"""
    results=['total_cars','bev_cars','petrol_cars','diesel_cars','plugin_cars','conv_cars','ages','demand_difference','electric_emiss',
            'tailpipe_emiss','wtt_emiss','mod_shift_emiss','elec_demand','foss_demand','mod_shift_energy','ev_prod_emiss',
            'ice_prod_emiss','conv_prod_emiss','ev_prod_energy','ice_prod_energy','conv_prod_energy','km_driven']

"""

"""
electric=[base['electric_emiss'][-1],base_ren['electric_emiss'][-1],p3030['electric_emiss'][-1],p2525['electric_emiss'][-1],third_rf['electric_emiss'][-1],lw_20['electric_emiss'][-1],lw_40['electric_emiss'][-1],base_eu['electric_emiss'][-1],mts1['electric_emiss'][-1],mts2['electric_emiss'][-1],d4343['electric_emiss'][-1],d6666['electric_emiss'][-1],d8181['electric_emiss'][-1],extreme1['electric_emiss'][-1],extreme2['electric_emiss'][-1],0]
elec=((np.array(electric)))

tailpipe=[base[7][-1],base_ren[7][-1],p3030[7][-1],p2525[7][-1],third_rf[7][-1],lw_20[7][-1],lw_40[7][-1],base_eu[7][-1],mts1[7][-1],mts2[7][-1],d4343[7][-1],d6666[7][-1],d8181[7][-1],extreme1[7][-1],extreme2[7][-1],0]
tail=((np.array(tailpipe)))

ev_prod=[base[8][-1],base_ren[8][-1],p3030[8][-1],p2525[8][-1],third_rf[8][-1],lw_20[8][-1],lw_40[8][-1],base_eu[8][-1],mts1[8][-1],mts2[8][-1],d4343[8][-1],d6666[8][-1],d8181[8][-1],extreme1[8][-1],extreme2[8][-1],0]
ev=((np.array(ev_prod)))

ice_prod=[base[9][-1],base_ren[9][-1],p3030[9][-1],p2525[9][-1],third_rf[9][-1],lw_20[9][-1],lw_40[9][-1],base_eu[9][-1],mts1[9][-1],mts2[9][-1],d4343[9][-1],d6666[9][-1],d8181[9][-1],extreme1[9][-1],extreme2[9][-1],0]
ice=((np.array(ice_prod)))

converted=[base[10][-1],base_ren[10][-1],p3030[10][-1],p2525[10][-1],third_rf[10][-1],lw_20[10][-1],lw_40[10][-1],base_eu[10][-1],mts1[10][-1],mts2[10][-1],d4343[10][-1],d6666[10][-1],d8181[10][-1],extreme1[10][-1],extreme2[10][-1],0]
conv=((np.array(converted)))
"""

carbon_budg=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,21.7]
cb=((np.array(carbon_budg)))

"""
electric1=[base[18][-1],base_ren[18][-1],p3030[18][-1],p2525[18][-1],third_rf[18][-1],lw_20[18][-1],lw_40[18][-1],base_eu[18][-1],mts1[18][-1],mts2[18][-1],d4343[18][-1],d6666[18][-1],d8181[18][-1],extreme1[18][-1],extreme2[18][-1],0]
elec1=((np.array(electric1))/10**12)

tailpipe1=[base[19][-1],base_ren[19][-1],p3030[19][-1],p2525[19][-1],third_rf[19][-1],lw_20[19][-1],lw_40[19][-1],base_eu[19][-1],mts1[19][-1],mts2[19][-1],d4343[19][-1],d6666[19][-1],d8181[19][-1],extreme1[19][-1],extreme2[19][-1],0]
tail1=((np.array(tailpipe1))/10**12)

ev_prod1=[base[20][-1],base_ren[20][-1],p3030[20][-1],p2525[20][-1],third_rf[20][-1],lw_20[20][-1],lw_40[20][-1],base_eu[20][-1],mts1[20][-1],mts2[20][-1],d4343[20][-1],d6666[20][-1],d8181[20][-1],extreme1[20][-1],extreme2[20][-1],0]
ev1=((np.array(ev_prod1))/10**12)

ice_prod1=[base[21][-1],base_ren[21][-1],p3030[21][-1],p2525[21][-1],third_rf[21][-1],lw_20[21][-1],lw_40[21][-1],base_eu[21][-1],mts1[21][-1],mts2[21][-1],d4343[21][-1],d6666[21][-1],d8181[21][-1],extreme1[21][-1],extreme2[21][-1],0]
ice1=((np.array(ice_prod1))/10**12)

converted1=[base[22][-1],base_ren[22][-1],p3030[22][-1],p2525[22][-1],third_rf[22][-1],lw_20[22][-1],lw_40[22][-1],base_eu[22][-1],mts1[22][-1],mts2[22][-1],d4343[22][-1],d6666[22][-1],d8181[22][-1],extreme1[22][-1],extreme2[22][-1],0]
conv1=((np.array(converted1))/10**12)
"""


#calculates percentage change from base case
base_case_emissions=policy_results['base']['electric_emiss'][-1]+policy_results['base']['tailpipe_emiss'][-1]+policy_results['base']['wtt_emiss'][-1]+policy_results['base']['ev_prod_emiss'][-1]+policy_results['base']['ice_prod_emiss'][-1]+policy_results['base']['conv_prod_emiss'][-1]

per_change_emiss=((results_fig1['electric_emiss']+results_fig1['tailpipe_emiss']+results_fig1['wtt_emiss']+results_fig1['ev_prod_emiss']+results_fig1['ice_prod_emiss']+results_fig1['conv_prod_emiss']-base_case_emissions)/base_case_emissions)*100

base_case_energy=(policy_results['base']['elec_demand'][-1]+policy_results['base']['foss_demand'][-1]+policy_results['base']['ev_prod_energy'][-1]+policy_results['base']['ice_prod_energy'][-1]+policy_results['base']['conv_prod_energy'][-1])/10**12

per_change_energy=((results_fig1['elec_demand']+results_fig1['foss_demand']+results_fig1['ev_prod_energy']+
        results_fig1['ice_prod_energy']+results_fig1['conv_prod_energy']-
        base_case_energy)/base_case_energy)*100

fig, axs = plt.subplots(1,2,figsize=(14,9),sharey=True,sharex=False, gridspec_kw={'width_ratios': [5, 2]})

# horizontal space between axes
fig.subplots_adjust(wspace=0.1)

pos = [0,1.6,3.2,4,5.6,7.2,8,9.6,11.2,12,13.6,14.4,15.2,16.8,18,19.7]
width = [1,1,0.75,0.75,1,0.75,0.75,1,0.75,0.75,0.75,0.75,0.75,1,1,1]
error=np.random.rand(8)

axs[0].grid(axis='x')
axs[0].barh(pos,results_fig1['tailpipe_emiss'],width,color=['black'], align='center',label='Tailpipe')
axs[0].barh(pos,results_fig1['electric_emiss'],width,results_fig1['tailpipe_emiss'],color=['tab:blue'], align='center',label='Electricity')
axs[0].barh(pos,results_fig1['wtt_emiss'],width,results_fig1['electric_emiss']+results_fig1['tailpipe_emiss'],color=['tab:blue'], align='center',label='Electricity')
axs[0].barh(pos,results_fig1['ev_prod_emiss'],width,results_fig1['electric_emiss']+results_fig1['tailpipe_emiss']+results_fig1['wtt_emiss'],color=['tab:red'], align='center',label='EV Embedded',alpha=1)
axs[0].barh(pos,results_fig1['ice_prod_emiss'],width,results_fig1['electric_emiss']+results_fig1['tailpipe_emiss']+results_fig1['wtt_emiss']+results_fig1['ev_prod_emiss'],color=['tab:orange'], align='center',label='ICEV Embedded')
axs[0].barh(pos,results_fig1['conv_prod_emiss'],width,results_fig1['electric_emiss']+results_fig1['tailpipe_emiss']+results_fig1['wtt_emiss']+results_fig1['ev_prod_emiss']+results_fig1['ice_prod_emiss'],color=['tab:purple'], align='center',label='Retrofit Embedded')
axs[0].barh(pos,cb,width,results_fig1['electric_emiss']+results_fig1['tailpipe_emiss']+results_fig1['wtt_emiss']+results_fig1['ev_prod_emiss']+results_fig1['ice_prod_emiss']+results_fig1['conv_prod_emiss'],color=['tab:green'], align='center')

axs[0].legend(bbox_to_anchor=(0.9,0.28), prop={'size': 14})
axs[0].set_xlim(0,160)
axs[0].set_ylim(-1,21)

axs[0].set_xlabel('Cumulative Emissions up to 2050 (MtCO$_{2eq}$)')
axs[0].invert_yaxis()
axs[0].set_yticks(pos)
axs[0].set_yticklabels(labels_fig1)
axs[0].invert_yaxis()
axs[0].plot([base_case_emissions, base_case_emissions], [-2,24], "k--")
#axs[0].plot([21.7,21.7], [-2,24], "k--",color='black')
axs[0].text(-0.03, 1, 'a', transform=axs[0].transAxes,fontsize='medium', va='bottom',weight="bold")

from scipy.interpolate import make_interp_spline

x_new = np.linspace(0, 16.8, 300)
a_BSpline = make_interp_spline(pos[0:16],np.array(tail)[0:16])
y_new = a_BSpline(x_new)

axs[0].plot([63.08470628110841]+list(y_new)+[21.80],[-1]+list(x_new)+[21.7],color='tab:green', alpha=1)

axs[0].set_yticks(pos)
axs[0].set_yticklabels(labels_fig1)

axs[1].barh(pos,results_fig1['foss_demand'],width,color=['black'], align='center',label='Tailpipe')
axs[1].barh(pos,results_fig1['elec_demand'],width,results_fig1['foss_demand'],color=['tab:blue'], align='center',label='Electricity')
axs[1].barh(pos,results_fig1['ev_prod_energy'],width,results_fig1['elec_demand']+results_fig1['foss_demand'],color=['tab:red'], align='center',label='EV Embedded')
axs[1].barh(pos,results_fig1['ice_prod_energy'],width,results_fig1['elec_demand']+results_fig1['foss_demand']+results_fig1['ev_prod_energy'],color=['tab:orange'], align='center',label='ICEV Embedded')
axs[1].barh(pos,results_fig1['conv_prod_energy'],width,results_fig1['elec_demand']+results_fig1['foss_demand']+results_fig1['ev_prod_energy']+results_fig1['ice_prod_energy'],color=['tab:purple'], align='center',label='Retrofit Embedded')
axs[1].grid(axis='x')
axs[1].set_xlabel('Cumulative Energy\nDemand up to 2050 (EJ)')
axs[1].set_yticks(pos)
axs[1].set_yticklabels(labels_fig1)
axs[1].plot([base_case_energy, base_case_energy], [-2,24], "k--")
axs[1].text(-0.08, 1, 'b', transform=axs[1].transAxes,fontsize='medium', va='bottom',weight="bold")
axs[1].set_xticks(np.arange(0,3,0.5))

"""
for i, v in enumerate(elec+tail+ev+ice+conv):
    if i<15:
        axs[0].text(v-21,pos[i]+0.25, '{:.1f}%'.format(per[i]))
        #plt.text(130,pos[i]+0.1, '{:.1f}%'.format(per[i]))
        #v+1
"""
for i, v in enumerate(results_fig1['electric_emiss']+results_fig1['tailpipe_emiss']+results_fig1['wtt_emiss']+results_fig1['ev_prod_emiss']+results_fig1['ice_prod_emiss']+results_fig1['conv_prod_emiss']):
    if i<15:
        axs[0].text(v-21,pos[i]+0.25, '{:.1f}%'.format(per[i]),color='white')
        #plt.text(130,pos[i]+0.1, '{:.1f}%'.format(per[i]))
        #v+1

for i, v in enumerate(results_fig1['elec_demand']+results_fig1['foss_demand']+results_fig1['ev_prod_energy']+results_fig1['ice_prod_energy']+results_fig1['conv_prod_energy']):
    if i<15:
        axs[1].text(v-0.55,pos[i]+0.25, '{:.1f}%'.format(per1[i]),color='white')
        #plt.text(130,pos[i]+0.1, '{:.1f}%'.format(per[i]))
        #v+1 
        
plt.gca().invert_yaxis()
plt.savefig('Fig1.pdf', bbox_inches="tight")
plt.savefig('Fig1.png', bbox_inches="tight")
plt.show()