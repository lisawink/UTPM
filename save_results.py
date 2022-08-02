import pandas as pd
from UTPM import Run_Model

phaseout=[2025,2030,2040]
elec_decarb=[2020,2050,2060]
binary=[0]
scrap=[20,18,16,14,12,10]
modal=[20,0,-20,-40,-60,-80]
retro=[0,0.2,0.5]
weights=[1400,1120,840]
china=[0,1]
all_cases=[]
policies=[]
file_list=[]
total=[]
total1=[]
q=0
r=8
for i in phaseout:
    for j in binary:
        for p in elec_decarb:
            for n in retro:
                for l in weights:
                    for m in modal:
                        for k in scrap:
                            for o in china:
                                
                                q=q+1
                                policy=('Phase-Out:',i,'Net-zero:',p,'Retro-fitting:',n,'Light-weighting:',l,'Modal shift:',m,'Scrap age:',k,'Regulated EV manufacture:',o,'Modal shift rate (years):',r)
                                policies.append(policy)
                                case=Run_Model(phase_out_date=i,phase_out_hybrid=i+j,scrap_age_pre2020=k+5,scrap_age_post2020=k,mass=l,\
                                   fleet_size_projection=m,miles_driven_projection=m,retrofit_percentage=n,manufacture=o,elec=p,rate=r)
                                all_cases.append(case)
                                
                                #add cumulative emissions and energy results of use phase and embedded 
                                total_em=case[6][-1]+case[7][-1]+case[8][-1]+case[9][-1]+case[10][-1]
                                total_en=case[18][-1]+case[19][-1]+case[20][-1]+case[21][-1]+case[22][-1]
                                total.append(total_em)
                                total1.append(total_en)
                                
                                #np.savetxt('policy_data.txt',policies,fmt='%s')
                                #np.savetxt('emissions_data.txt',total,fmt='%s')
                                #np.savetxt('energy_data.txt',total1,fmt='%s')
                                                           
list_dict = {'Policies':policies, 'Emissions':total, 'Energy':total1} 
df = pd.DataFrame(list_dict) 
df.to_csv('all_policies_results.csv', index=False)