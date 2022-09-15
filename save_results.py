import pandas as pd
from UTPM_Run_Model import Run_Model

results=pd.DataFrame()

phaseout=[2025,2030,2040]
elec_decarb=[2020,2050,2060]
scrap=[20,18,16,14,12,10]
modal=[20,0,-20,-40,-60,-80,-90]
retro=[0,0.2,0.33]
weights=[1400,1120,840]
china=[0,1]
all_cases=[]
policies=[]
file_list=[]
total=[]
total1=[]
#q=0
rate=[3,8,19,28]
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
                                
                                data = {'Phase-Out:':i,'Net-zero:':p,'Retro-fitting:':n,'Light-weighting:':l,'Modal shift:':m,'Scrap age:':k,'Regulated EV manufacture:':o,'Modal shift rate (years):':j,
                                        'Cumulative Electric Emissions':case['cum_electric'],'Cumulative Tailpipe Emissions':case['cum_tailpipe'],'Cumulative WTT Emissions':case['cum_wtt_emiss'],
                                        'Cumulative EV Production Emissions':case['cum_ev_prod'],'Cumulative ICE Production Emissions':case['cum_ice_prod'],'Cumulative Conversion Production Emissions':case['cum_conv_prod'],
                                        'Cumulative Electric Energy':case['cum_elec'],'Cumulative Tailpipe Energy':case['cum_foss'],'Cumulative WTT Energy':case['cum_wtt_en'],
                                        'Cumulative EV Production Energy':case['cum_ev_en'],'Cumulative ICE Production Energy':case['cum_ice_en'],'Cumulative Conversion Production Energy':case['cum_conv_en']}
                                df=pd.DataFrame(data)
                                results=results.append(df,ignore_index=True)

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
results.to_csv('figure_6.csv',index=False)
with pd.ExcelWriter('fig6.xlsx') as writer:
    df.to_excel(writer)
print(df)