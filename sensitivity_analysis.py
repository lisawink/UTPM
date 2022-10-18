import pandas as pd
from UTPM_Run_Model import Run_Model

results=pd.DataFrame()

phaseout=[2025]
elec_decarb=[2020]
scrap=[10]
modal=[-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-86,-88,-90]
retro=[0.2]
weights=[840]
china=[1]
all_cases=[]
policies=[]
file_list=[]
total=[]
total1=[]
#q=0
rate=[3,5,7,9,11,13,15,17,19,21,23,25,27]
count=0
existing_df=pd.DataFrame()
for i in phaseout:
    for j in rate:
        for p in elec_decarb:
            for n in retro:
                for l in weights:
                    for m in modal:
                        for k in scrap:
                            for o in china:
                                
                                #q=q+1
                                #policy=('Phase-Out:',i,'Net-zero:',p,'Retro-fitting:',n,'Light-weighting:',l,'Modal shift:',m,'Scrap age:',k,'Regulated EV manufacture:',o,'Modal shift rate (years):',j)
                                #policies.append(policy)
                                case=Run_Model(phase_out_date=i,phase_out_hybrid=i,scrap_age_pre2020=k+5,scrap_age_post2020=k,mass=l,\
                                   fleet_size_projection=m,miles_driven_projection=m,retrofit_percentage=n,manufacture=o,elec=p,rate=j)
                                #all_cases.append(case)
                                
                                data = {'Count':count,'Phase-Out:':i,'Net-zero:':p,'Retro-fitting:':n,'Light-weighting:':l,'Modal shift:':m,'Scrap age:':k,'Regulated EV manufacture:':o,'Modal shift rate (years):':j,
                                        'Cumulative Electric Emissions':case['cum_electric'][-1],'Cumulative Tailpipe Emissions':case['cum_tailpipe'][-1],'Cumulative WTT Emissions':case['cum_wtt_emiss'][-1],
                                        'Cumulative EV Production Emissions':case['cum_ev_prod'][-1],'Cumulative ICE Production Emissions':case['cum_ice_prod'][-1],'Cumulative Conversion Production Emissions':case['cum_conv_prod'][-1],
                                        'Cumulative Electric Energy':case['cum_elec'][-1],'Cumulative Tailpipe Energy':case['cum_foss'][-1],'Cumulative WTT Energy':case['cum_wtt_en'][-1],
                                        'Cumulative EV Production Energy':case['cum_ev_en'][-1],'Cumulative ICE Production Energy':case['cum_ice_en'][-1],'Cumulative Conversion Production Energy':case['cum_conv_en'][-1]}
                                df=pd.DataFrame(data,index=[count])
                                existing_df=pd.concat([existing_df,df])
                                print(existing_df)
                                existing_df.to_csv('sens_an2.csv')
                                #results=results.append(df,ignore_index=True)

                                #add cumulative emissions and energy results of use phase and embedded 
                                #total_em=case[6][-1]+case[7][-1]+case[8][-1]+case[9][-1]+case[10][-1]
                                #total_en=case[18][-1]+case[19][-1]+case[20][-1]+case[21][-1]+case[22][-1]
                                #total.append(total_em)
                                #total1.append(total_en)
                                
                                #np.savetxt('policy_data.txt',policies,fmt='%s')
                                #np.savetxt('emissions_data.txt',total,fmt='%s')
                                #np.savetxt('energy_data.txt',total1,fmt='%s')
                                                           
#list_dict = {'Policies':policies, 'Emissions':total, 'Energy':total1} 
#df = pd.DataFrame(list_dict) 
#df.to_csv('all_policies_results.csv', index=False)
#results.to_csv('sensitivity_analysis.csv',index=False)
with pd.ExcelWriter('sens2.xlsx') as writer:
    existing_df.to_excel(writer)
print(existing_df)