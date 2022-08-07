#from UTPM_final import Run_Model
from IPython.display import Markdown, display

def printmd(string):
    display(Markdown(string))

base=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
base_ren=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2020,rate=28)
base_eu=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=1,elec=2050,rate=28)
third_rf=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0.33,manufacture=0,elec=2050,rate=28)
lw_20=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1120,\
               fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
lw_40=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=840,\
               fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
d4343=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=-42.99,miles_driven_projection=-42.99,retrofit_percentage=0,manufacture=0,elec=2050,rate=5)
d6666=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=-66,miles_driven_projection=-66,retrofit_percentage=0,manufacture=0,elec=2050,rate=5)
d8181=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=-81,miles_driven_projection=-81,retrofit_percentage=0,manufacture=0,elec=2050,rate=5)
p2525=Run_Model(phase_out_date=2025,phase_out_hybrid=2025,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
p3030=Run_Model(phase_out_date=2030,phase_out_hybrid=2030,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
opt=Run_Model(phase_out_date=2025,phase_out_hybrid=2025,scrap_age_pre2020=15,scrap_age_post2020=10,mass=840,\
               fleet_size_projection=-81,miles_driven_projection=-81,retrofit_percentage=0.33,manufacture=1,elec=2020,rate=5)
mts=Run_Model(phase_out_date=2030,phase_out_hybrid=2030,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=-43,miles_driven_projection=-43,retrofit_percentage=0,manufacture=0,elec=2050,rate=8)

x=["Baseline","BEVs Powered by 100%\nRenewable Energy","Fossil Fuel Phase-Out: 2030", "2025","Retrofitting: 33%",
   "Light-weighting: 20%","40%", "Regulated EV Manufacture",
   "Local Transport Policies","Modal Shift: -43%","-66%","-81%","Combined","Carbon Budget if Historical\nShare Continues"]

electric=[base[6][-1],base_ren[6][-1],p3030[6][-1],p2525[6][-1],third_rf[6][-1],lw_20[6][-1],lw_40[6][-1],base_eu[6][-1],mts[6][-1],d4343[6][-1],d6666[6][-1],d8181[6][-1],opt[6][-1],0]
elec=((np.array(electric)))

tailpipe=[base[7][-1],base_ren[7][-1],p3030[7][-1],p2525[7][-1],third_rf[7][-1],lw_20[7][-1],lw_40[7][-1],base_eu[7][-1],mts[7][-1],d4343[7][-1],d6666[7][-1],d8181[7][-1],opt[7][-1],0]
tail=((np.array(tailpipe)))

ev_prod=[base[8][-1],base_ren[8][-1],p3030[8][-1],p2525[8][-1],third_rf[8][-1],lw_20[8][-1],lw_40[8][-1],base_eu[8][-1],mts[8][-1],d4343[8][-1],d6666[8][-1],d8181[8][-1],opt[8][-1],0]
ev=((np.array(ev_prod)))

ice_prod=[base[9][-1],base_ren[9][-1],p3030[9][-1],p2525[9][-1],third_rf[9][-1],lw_20[9][-1],lw_40[9][-1],base_eu[9][-1],mts[9][-1],d4343[9][-1],d6666[9][-1],d8181[9][-1],opt[9][-1],0]
ice=((np.array(ice_prod)))

converted=[base[10][-1],base_ren[10][-1],p3030[10][-1],p2525[10][-1],third_rf[10][-1],lw_20[10][-1],lw_40[10][-1],base_eu[10][-1],mts[10][-1],d4343[10][-1],d6666[10][-1],d8181[10][-1],opt[10][-1],0]
conv=((np.array(converted)))

carbon_budg=[0,0,0,0,0,0,0,0,0,0,0,0,0,21.7]
cb=((np.array(carbon_budg)))

electric1=[base[18][-1],base_ren[18][-1],p3030[18][-1],p2525[18][-1],third_rf[18][-1],lw_20[18][-1],lw_40[18][-1],base_eu[18][-1],mts[18][-1],d4343[18][-1],d6666[18][-1],d8181[18][-1],opt[18][-1],0]
elec1=((np.array(electric1))/10**12)

tailpipe1=[base[19][-1],base_ren[19][-1],p3030[19][-1],p2525[19][-1],third_rf[19][-1],lw_20[19][-1],lw_40[19][-1],base_eu[19][-1],mts[19][-1],d4343[19][-1],d6666[19][-1],d8181[19][-1],opt[19][-1],0]
tail1=((np.array(tailpipe1))/10**12)

ev_prod1=[base[20][-1],base_ren[20][-1],p3030[20][-1],p2525[20][-1],third_rf[20][-1],lw_20[20][-1],lw_40[20][-1],base_eu[20][-1],mts[20][-1],d4343[20][-1],d6666[20][-1],d8181[20][-1],opt[20][-1],0]
ev1=((np.array(ev_prod1))/10**12)

ice_prod1=[base[21][-1],base_ren[21][-1],p3030[21][-1],p2525[21][-1],third_rf[21][-1],lw_20[21][-1],lw_40[21][-1],base_eu[21][-1],mts[21][-1],d4343[21][-1],d6666[21][-1],d8181[21][-1],opt[21][-1],0]
ice1=((np.array(ice_prod1))/10**12)

converted1=[base[22][-1],base_ren[22][-1],p3030[22][-1],p2525[22][-1],third_rf[22][-1],lw_20[22][-1],lw_40[22][-1],base_eu[22][-1],mts[22][-1],d4343[22][-1],d6666[22][-1],d8181[22][-1],opt[22][-1],0]
conv1=((np.array(converted1))/10**12)


per=((elec+tail+ev+ice+conv-(base[6][-1]+base[7][-1]+base[8][-1]+base[9][-1]+base[10][-1]))/(base[6][-1]+base[7][-1]+base[8][-1]+base[9][-1]+base[10][-1]))*100
per1=((elec1+tail1+ev1+ice1+conv1-(base[18][-1]+base[19][-1]+base[20][-1]+base[21][-1]+base[22][-1]+base[23][-1])/10**12)/((base[18][-1]+base[19][-1]+base[20][-1]+base[21][-1]+base[22][-1]+base[23][-1])/10**12))*100


fig, axs = plt.subplots(1,2,figsize=(14,9),sharey=True,sharex=False, gridspec_kw={'width_ratios': [5, 2]})

# horizontal space between axes
fig.subplots_adjust(wspace=0.05)

pos = [0,1.6,3.2,4,5.6,7.2,8,9.6,11.2,12.8,13.6,14.4,16,17.6]
width = [1,1,0.75,0.75,1,0.75,0.75,1,1,0.75,0.75,0.75,1,1]
error=np.random.rand(8)

axs[0].grid(axis='x')
axs[0].barh(pos,elec,width,color=['black'], align='center',label='Electricity')
axs[0].barh(pos,tail,width,elec,color=['tab:blue'], align='center',label='Tailpipe')
axs[0].barh(pos,ev,width,elec+tail,color=['tab:red'], align='center',label='EV Embedded')
axs[0].barh(pos,ice,width,elec+tail+ev,color=['tab:orange'], align='center',label='ICEV Embedded')
axs[0].barh(pos,conv,width,elec+tail+ev+ice,color=['tab:purple'], align='center',label='Retrofit Embedded')
axs[0].barh(pos,cb,width,elec+tail+ev+ice+conv,color=['tab:green'], align='center')

axs[0].legend(bbox_to_anchor=(0.63,0.32), prop={'size': 14})
axs[0].set_xlim(0,160)
axs[0].set_ylim(-1,19)

axs[0].set_xlabel('Cumulative Emissions up to 2050 (MtCO$_{2eq}$)')
axs[0].invert_yaxis()
axs[0].set_yticks(pos)
axs[0].set_yticklabels(x)
axs[0].invert_yaxis()
axs[0].plot([(base[6][-1]+base[7][-1]+base[8][-1]+base[9][-1]+base[10][-1]), (base[6][-1]+base[7][-1]+base[8][-1]+base[9][-1]+base[10][-1])], [-2,24], "k--")
axs[0].plot([21.7,21.7], [-2,24], "k--",color='black')
axs[0].text(-0.03, 1, 'a', transform=axs[0].transAxes,fontsize='medium', va='bottom',weight="bold")


axs[1].barh(pos,elec1,width,color=['black'], align='center',label='Electricity')
axs[1].barh(pos,tail1,width,elec1,color=['tab:blue'], align='center',label='Tailpipe')
axs[1].barh(pos,ev1,width,elec1+tail1,color=['tab:red'], align='center',label='EV Embedded')
axs[1].barh(pos,ice1,width,elec1+tail1+ev1,color=['tab:orange'], align='center',label='ICEV Embedded')
axs[1].barh(pos,conv1,width,elec1+tail1+ev1+ice1,color=['tab:purple'], align='center',label='Retrofit Embedded')
axs[1].grid(axis='x')
axs[1].set_xlabel('Cumulative Energy\nDemand up to 2050 (EJ)')
axs[1].set_yticks(pos)
axs[1].set_yticklabels(x)
axs[1].plot([(base[18][-1]+base[19][-1]+base[20][-1]+base[21][-1]+base[22][-1]+base[23][-1])/10**12, (base[18][-1]+base[19][-1]+base[20][-1]+base[21][-1]+base[22][-1]+base[23][-1])/10**12], [-2,24], "k--")
axs[1].text(-0.08, 1, 'b', transform=axs[1].transAxes,fontsize='medium', va='bottom',weight="bold")

for i, v in enumerate(elec+tail+ev+ice+conv):
    if i<13:
        axs[0].text(v-21,pos[i]+0.25, '{:.1f}%'.format(per[i]))
        #plt.text(130,pos[i]+0.1, '{:.1f}%'.format(per[i]))
        #v+1

for i, v in enumerate(elec1+tail1+ev1+ice1+conv1):
    if i<13:
        axs[1].text(v-0.5,pos[i]+0.25, '{:.1f}%'.format(per1[i]))
        #plt.text(130,pos[i]+0.1, '{:.1f}%'.format(per[i]))
        #v+1 
        
plt.gca().invert_yaxis()
plt.show()