import UTPM_Run_Model
from IPython.display import Markdown, display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def printmd(string):
    display(Markdown(string))

#Only runs model if results have not been run before
try:
    policy_results=pd.read_excel('fig1_no_cb.xlsx', None)
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
                fleet_size_projection=-81,miles_driven_projection=-81,retrofit_percentage=0.2,manufacture=1,elec=2020,rate=5)
    #policy_results['extreme2']=UTPM_Run_Model.Run_Model(phase_out_date=2025,phase_out_hybrid=2025,scrap_age_pre2020=15,scrap_age_post2020=10,mass=840,\
    #            fleet_size_projection=-88,miles_driven_projection=-88,retrofit_percentage=0.2,manufacture=1,elec=2020,rate=5)
    #df = pd.DataFrame(policy_results) 
    #df.to_csv('fig1.csv', index=True)

    with pd.ExcelWriter('fig1_no_cb.xlsx') as writer:  
        for policy_type in policy_results.keys():
            df=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in policy_results[policy_type].items() ]))
            df.to_excel(writer,sheet_name=policy_type)

#results_by_category gives a list of emissions and energy demand results for each policy outcome by results category for the plot
results_fig1={}
#results_categories=['cum_electric','cum_tailpipe','cum_wtt_emiss','cum_ev_prod','cum_ice_prod','cum_conv_prod',
#                    'cum_elec','cum_foss','cum_ev_en','cum_ice_en','cum_conv_en']
results_categories=['cum_electric','cum_tailpipe','cum_ev_prod','cum_ice_prod','cum_wtt_emiss','cum_conv_prod',
                    'cum_elec','cum_foss','cum_wtt_en','cum_ev_en','cum_ice_en','cum_conv_en']


#ISSUE IS IN THE SAVING AND READING OF THE CSV FILE
#policy_reuslts['base']['cum_electric'] is read as a string rather than a list of floats

for i in results_categories:
    results_fig1[i]=[]
    for j in policy_results:
        if type(policy_results[j][i])==pd.Series:
            results_fig1[i].append(policy_results[j][i].dropna().tolist()[-1])
        else:
            results_fig1[i].append(policy_results[j][i][-1])
    results_fig1[i]=np.array(results_fig1[i])
    if i in ['cum_elec','cum_foss','cum_wtt_en','cum_ev_en','cum_ice_en','cum_conv_en']:
        results_fig1[i]=results_fig1[i]/10**12

    print('this is results fig 1')
    print(results_fig1)

labels_fig1=["Baseline","BEVs Powered by 100%\nRenewable Energy","Fossil Fuel Phase-Out: 2030", "2025","Retrofitting: 33%",
   "Light-weighting: 20%","40%", "Regulated EV Manufacture",
   "Local Transport Strategy","Local Net-Zero 2030 Target","Car Travel Activity (CTA): -43%","-66%","-81%",
   "Combined Policies"]

#calculates percentage change from base case
if type(policy_results['base']['cum_electric'])==pd.Series:
    base_case_emissions=policy_results['base']['cum_electric'].dropna().tolist()[-1]+policy_results['base']['cum_tailpipe'].dropna().tolist()[-1]+policy_results['base']['cum_wtt_emiss'].dropna().tolist()[-1]+policy_results['base']['cum_ev_prod'].dropna().tolist()[-1]+policy_results['base']['cum_ice_prod'].dropna().tolist()[-1]+policy_results['base']['cum_conv_prod'].dropna().tolist()[-1]
    base_case_energy=(policy_results['base']['cum_elec'].dropna().tolist()[-1]+policy_results['base']['cum_foss'].dropna().tolist()[-1]+policy_results['base']['cum_wtt_en'].dropna().tolist()[-1]+policy_results['base']['cum_ev_en'].dropna().tolist()[-1]+policy_results['base']['cum_ice_en'].dropna().tolist()[-1]+policy_results['base']['cum_conv_en'].dropna().tolist()[-1])/10**12
else:
    base_case_emissions=policy_results['base']['cum_electric'][-1]+policy_results['base']['cum_tailpipe'][-1]+policy_results['base']['cum_wtt_emiss'][-1]+policy_results['base']['cum_ev_prod'][-1]+policy_results['base']['cum_ice_prod'][-1]+policy_results['base']['cum_conv_prod'][-1]
    base_case_energy=(policy_results['base']['cum_elec'][-1]+policy_results['base']['cum_foss'][-1]+policy_results['base']['cum_wtt_en'][-1]+policy_results['base']['cum_ev_en'][-1]+policy_results['base']['cum_ice_en'][-1]+policy_results['base']['cum_conv_en'][-1])/10**12

per_change_emiss=((results_fig1['cum_electric']+results_fig1['cum_tailpipe']+results_fig1['cum_wtt_emiss']+results_fig1['cum_ev_prod']+results_fig1['cum_ice_prod']+results_fig1['cum_conv_prod']-base_case_emissions)/base_case_emissions)*100

per_change_energy=((results_fig1['cum_elec']+results_fig1['cum_foss']+results_fig1['cum_wtt_en']+results_fig1['cum_ev_en']+
        results_fig1['cum_ice_en']+results_fig1['cum_conv_en']-
        base_case_energy)/base_case_energy)*100

SMALL_SIZE = 15
MEDIUM_SIZE = 17
BIGGER_SIZE = 18
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)

fig, axs = plt.subplots(1,2,figsize=(14,9),sharey=True,sharex=False, gridspec_kw={'width_ratios': [5, 2]})

# horizontal space between axes
fig.subplots_adjust(wspace=0.1)

pos = [0,1.6,3.2,4,5.6,7.2,8,9.6,11.2,12,13.6,14.4,15.2,16.8]
width = [1,1,0.75,0.75,1,0.75,0.75,1,0.75,0.75,0.75,0.75,0.75,1]
error=np.random.rand(8)

axs[0].grid(axis='x')
axs[0].barh(pos,results_fig1['cum_tailpipe'],width,color=['black'], align='center',label='Tailpipe')
axs[0].barh(pos,results_fig1['cum_electric'],width,results_fig1['cum_tailpipe'],color=['tab:blue'], align='center',label='Electricity')
axs[0].barh(pos,results_fig1['cum_wtt_emiss'],width,results_fig1['cum_electric']+results_fig1['cum_tailpipe'],color=['tab:grey'], align='center',label='WTT Fuels')
axs[0].barh(pos,results_fig1['cum_ev_prod'],width,results_fig1['cum_electric']+results_fig1['cum_tailpipe']+results_fig1['cum_wtt_emiss'],color=['tab:red'], align='center',label='EV Embedded',alpha=1)
axs[0].barh(pos,results_fig1['cum_ice_prod'],width,results_fig1['cum_electric']+results_fig1['cum_tailpipe']+results_fig1['cum_wtt_emiss']+results_fig1['cum_ev_prod'],color=['tab:orange'], align='center',label='ICEV Embedded')
axs[0].barh(pos,results_fig1['cum_conv_prod'],width,results_fig1['cum_electric']+results_fig1['cum_tailpipe']+results_fig1['cum_wtt_emiss']+results_fig1['cum_ev_prod']+results_fig1['cum_ice_prod'],color=['tab:purple'], align='center',label='Retrofit Embedded')
#axs[0].barh(pos,cb,width,results_fig1['cum_electric']+results_fig1['cum_tailpipe']+results_fig1['cum_wtt_emiss']+results_fig1['cum_ev_prod']+results_fig1['cum_ice_prod']+results_fig1['cum_conv_prod'],color=['tab:green'], align='center')

axs[0].legend(bbox_to_anchor=(0.57,0.3), prop={'size': 14})
axs[0].set_xlim(0,170)
axs[0].set_ylim(-1,18)

axs[0].set_xlabel('Cumulative Emissions up to 2050 (MtCO$_{2eq}$)')
axs[0].invert_yaxis()

axs[0].invert_yaxis()
axs[0].plot([base_case_emissions, base_case_emissions], [-2,24], "k--")
#axs[0].plot([21.7,21.7], [-2,24], "k--",color='black')
axs[0].text(-0.03, 1, 'a', transform=axs[0].transAxes,fontsize='medium', va='bottom',weight="bold")

from scipy.interpolate import make_interp_spline

x_new = np.linspace(0, 16.8, 300)
a_BSpline = make_interp_spline(pos[0:16],np.array(results_fig1['cum_tailpipe'])[0:16])
y_new = a_BSpline(x_new)

#axs[0].plot([63.08470628110841]+list(y_new)+[21.80],[-1]+list(x_new)+[21.7],color='tab:green', alpha=1)

axs[0].set_yticks(pos)
axs[0].set_yticklabels(labels_fig1)

axs[1].grid(axis='x')
axs[1].barh(pos,results_fig1['cum_foss'],width,color=['black'], align='center',label='Tailpipe')
axs[1].barh(pos,results_fig1['cum_wtt_en'],width,results_fig1['cum_foss'],color=['grey'], align='center',label='WTT Fuels')
axs[1].barh(pos,results_fig1['cum_elec'],width,results_fig1['cum_wtt_en']+results_fig1['cum_foss'],color=['tab:blue'], align='center',label='Electricity')
axs[1].barh(pos,results_fig1['cum_ev_en'],width,results_fig1['cum_wtt_en']+results_fig1['cum_elec']+results_fig1['cum_foss'],color=['tab:red'], align='center',label='EV Embedded')
axs[1].barh(pos,results_fig1['cum_ice_en'],width,results_fig1['cum_wtt_en']+results_fig1['cum_elec']+results_fig1['cum_foss']+results_fig1['cum_ev_en'],color=['tab:orange'], align='center',label='ICEV Embedded')
axs[1].barh(pos,results_fig1['cum_conv_en'],width,results_fig1['cum_wtt_en']+results_fig1['cum_elec']+results_fig1['cum_foss']+results_fig1['cum_ev_en']+results_fig1['cum_ice_en'],color=['tab:purple'], align='center',label='Retrofit Embedded')
axs[1].set_xlabel('Cumulative Energy\nDemand up to 2050 (EJ)')
axs[1].set_yticks(pos)
axs[1].set_yticklabels(labels_fig1)
axs[1].plot([base_case_energy, base_case_energy], [-2,24], "k--")
axs[1].text(-0.08, 1, 'b', transform=axs[1].transAxes,fontsize='medium', va='bottom',weight="bold")
axs[1].set_xticks(np.arange(0,2.9,0.5))

"""
for i, v in enumerate(elec+tail+ev+ice+conv):
    if i<15:
        axs[0].text(v-21,pos[i]+0.25, '{:.1f}%'.format(per[i]))
        #plt.text(130,pos[i]+0.1, '{:.1f}%'.format(per[i]))
        #v+1
"""
for i, v in enumerate(results_fig1['cum_electric']+results_fig1['cum_tailpipe']+results_fig1['cum_wtt_emiss']+results_fig1['cum_ev_prod']+results_fig1['cum_ice_prod']+results_fig1['cum_conv_prod']):
    if i<15:
        axs[0].text(v-21,pos[i]+0.25, '{:.1f}%'.format(per_change_emiss[i]),color='white')
        #plt.text(130,pos[i]+0.1, '{:.1f}%'.format(per[i]))
        #v+1

for i, v in enumerate(results_fig1['cum_elec']+results_fig1['cum_foss']+results_fig1['cum_wtt_en']+results_fig1['cum_ev_en']+results_fig1['cum_ice_en']+results_fig1['cum_conv_en']):
    if i<15:
        axs[1].text(v-0.55,pos[i]+0.25, '{:.1f}%'.format(per_change_energy[i]),color='white')
        #plt.text(130,pos[i]+0.1, '{:.1f}%'.format(per[i]))
        #v+1 
        
plt.gca().invert_yaxis()
plt.savefig('Fig1_no_cb.pdf', bbox_inches="tight")
plt.savefig('Fig1_no_cb.png', bbox_inches="tight")
plt.show()