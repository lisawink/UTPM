"""Module containing method for creating Figure 3"""

from UTPM_Run_Model import Run_Model
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Polygon

#Only runs model if results have not been run before
try:
    policy_results=pd.read_excel('fig3.xlsx', None)
    print('Model already run')
    print(policy_results)
except:
    print('Running model')
    policy_results={}
    policy_results['base']=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                                     fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
    policy_results['base_ren']=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                                         fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2020,rate=28)
    policy_results['third_rf']=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                                         fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0.33,manufacture=0,elec=2050,rate=28)
    policy_results['lw_40']=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=840,\
                                      fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
    policy_results['d4343_8']=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                                        fleet_size_projection=-42.99,miles_driven_projection=-42.99,retrofit_percentage=0,manufacture=0,elec=2050,rate=8)
    policy_results['d6666_8']=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                                        fleet_size_projection=-66,miles_driven_projection=-66,retrofit_percentage=0,manufacture=0,elec=2050,rate=8)
    policy_results['d8181_8']=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                                        fleet_size_projection=-81,miles_driven_projection=-81,retrofit_percentage=0,manufacture=0,elec=2050,rate=8)
    policy_results['d4343_18']=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                                         fleet_size_projection=-42.99,miles_driven_projection=-42.99,retrofit_percentage=0,manufacture=0,elec=2050,rate=18)
    policy_results['d6666_18']=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                                         fleet_size_projection=-66,miles_driven_projection=-66,retrofit_percentage=0,manufacture=0,elec=2050,rate=18)
    policy_results['d8181_18']=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                                         fleet_size_projection=-81,miles_driven_projection=-81,retrofit_percentage=0,manufacture=0,elec=2050,rate=18)
    policy_results['p2525']=Run_Model(phase_out_date=2025,phase_out_hybrid=2025,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
                                      fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
    policy_results['early']=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=15,scrap_age_post2020=10,mass=1400,\
                                      fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
    
    with pd.ExcelWriter('fig3.xlsx') as writer:  
        for policy_type in policy_results.keys():
            df=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in policy_results[policy_type].items() ]))
            df.to_excel(writer,sheet_name=policy_type)

print(policy_results['base']['electric_emiss'].dropna())
print(policy_results['base']['tailpipe_emiss'].dropna())
print((policy_results['base']['electric_emiss'].dropna()+policy_results['base']['tailpipe_emiss'].dropna()))

emiss_base=policy_results['base']['electric_emiss']+policy_results['base']['tailpipe_emiss']
emiss_p25=policy_results['p2525']['electric_emiss']+policy_results['p2525']['tailpipe_emiss']
emiss_lw40=policy_results['lw_40']['electric_emiss']+policy_results['lw_40']['tailpipe_emiss']
emiss_rf=policy_results['third_rf']['electric_emiss']+policy_results['third_rf']['tailpipe_emiss']
emiss_d43_8=policy_results['d4343_8']['electric_emiss']+policy_results['d4343_8']['tailpipe_emiss']
emiss_d66_8=policy_results['d6666_8']['electric_emiss']+policy_results['d6666_8']['tailpipe_emiss']
emiss_d81_8=policy_results['d8181_8']['electric_emiss']+policy_results['d8181_8']['tailpipe_emiss']
emiss_early=policy_results['early']['electric_emiss']+policy_results['early']['tailpipe_emiss']
emiss_ren=policy_results['base_ren']['electric_emiss']+policy_results['base_ren']['tailpipe_emiss']
emiss_d43_18=policy_results['d4343_18']['electric_emiss']+policy_results['d4343_18']['tailpipe_emiss']
emiss_d66_18=policy_results['d6666_18']['electric_emiss']+policy_results['d6666_18']['tailpipe_emiss']
emiss_d81_18=policy_results['d8181_18']['electric_emiss']+policy_results['d8181_18']['tailpipe_emiss']

energy_base=(policy_results['base']['elec_demand']+policy_results['base']['foss_demand'])/10**9
energy_p25=(policy_results['p2525']['elec_demand']+policy_results['p2525']['foss_demand'])/10**9
energy_lw40=(policy_results['lw_40']['elec_demand']+policy_results['lw_40']['foss_demand'])/10**9
energy_rf=(policy_results['third_rf']['elec_demand']+policy_results['third_rf']['foss_demand'])/10**9
energy_d43_8=(policy_results['d4343_8']['elec_demand']+policy_results['d4343_8']['foss_demand'])/10**9
energy_d66_8=(policy_results['d6666_8']['elec_demand']+policy_results['d6666_8']['foss_demand'])/10**9
energy_d81_8=(policy_results['d8181_8']['elec_demand']+policy_results['d8181_8']['foss_demand'])/10**9
energy_early=(policy_results['early']['elec_demand']+policy_results['early']['foss_demand'])/10**9
energy_ren=(policy_results['base_ren']['elec_demand']+policy_results['base_ren']['foss_demand'])/10**9
energy_d43_18=(policy_results['d4343_18']['elec_demand']+policy_results['d4343_18']['foss_demand'])/10**9
energy_d66_18=(policy_results['d6666_18']['elec_demand']+policy_results['d6666_18']['foss_demand'])/10**9
energy_d81_18=(policy_results['d8181_18']['elec_demand']+policy_results['d8181_18']['foss_demand'])/10**9

print(emiss_base.dropna())

#make figure
fig, axs = plt.subplots(1,2,figsize=(14,9),sharey=False,sharex=False, gridspec_kw={'width_ratios': [1, 1]})
# horizontal space between axes
fig.subplots_adjust(wspace=0.15)

def gradient_fill(x, y, fill_color=None, ax=None, **kwargs):
    """
    Plot a line with a linear alpha gradient filled beneath it.

    Parameters
    ----------
    x, y : array-like
        The data values of the line.
    fill_color : a matplotlib color specifier (string, tuple) or None
        The color for the fill. If None, the color of the line will be used.
    ax : a matplotlib Axes instance
        The axes to plot on. If None, the current pyplot axes will be used.
    Additional arguments are passed on to matplotlib's ``plot`` function.

    Returns
    -------
    line : a Line2D instance
        The line plotted.
    im : an AxesImage instance
        The transparent gradient clipped to just the area beneath the curve.
    """
    if ax is None:
        ax = plt.gca()

    line, = axs[0].plot(x, y, **kwargs,color='None',alpha=0.3)
    if fill_color is None:
        fill_color = 'limegreen'

    zorder = line.get_zorder()
    alpha = line.get_alpha()
    alpha = 1.0 if alpha is None else alpha

    z = np.empty((100, 1, 4), dtype=float)
    rgb = mcolors.colorConverter.to_rgb(fill_color)
    z[:,:,:3] = rgb
    z[:,:,-1] = np.linspace(0, alpha, 100)[:,None]

    xmin, xmax, ymin, ymax = x.min(), x.max(), y.min(), y.max()
    im = axs[0].imshow(z[:], aspect='auto', extent=[xmin, xmax,ymin,ymax],
                   origin='upper', zorder=zorder)

    xy = np.column_stack([x, y])
    xy = np.vstack([[xmin, ymin], xy, [xmax, ymin], [xmin, ymin]])
    clip_path = Polygon(xy, facecolor='none', edgecolor='none', closed=True)
    axs[0].add_patch(clip_path)
    im.set_clip_path(clip_path)

    axs[0].autoscale(True)
    return line, im

gradient_fill(np.array([2020,2030,2050]),np.array([4,2.2,0]))
"""
axs[0].set_ylabel("Use-phase Emissions (MtCO$_{2eq}$)")
axs[0].set_xlabel("Year")
axs[0].grid()
axs[0].plot(range(2020,2051),emiss_base.dropna(),label='Baseline',linewidth=2,color='black')
axs[0].plot(range(2020,2051),emiss_rf.dropna(),label='33% Retro-fitting',linewidth=2,color='turquoise')
axs[0].plot(range(2020,2051),emiss_ren.dropna(),label="BEVs Powered by 100% Renewable Energy",linewidth=2,color='grey',ls='dashdot')
axs[0].plot(range(2020,2051),emiss_p25.dropna(),label='2025 Phase-Out',linewidth=2, color='purple')
axs[0].plot(range(2020,2051),emiss_early.dropna(),label="Early Scrapping",linewidth=2,color='red',ls='-')
axs[0].plot(range(2020,2051),emiss_lw40.dropna(),label='Lightweighting to 800kg',linewidth=2,color='limegreen',ls='dashdot',)
axs[0].plot(range(2020,2051),emiss_d43_8.dropna(),label='43% Modal Shift by 2030',linewidth=2,color='blue',ls='-')
axs[0].plot(range(2020,2051),emiss_d43_18.dropna(),label='43% Modal Shift by 2040',linewidth=2,color='blue',ls='--')
axs[0].plot(range(2020,2051),emiss_d66_8.dropna(),label='66% Modal Shift by 2030',linewidth=2,color='tab:orange',ls='-')
axs[0].plot(range(2020,2051),emiss_d66_18.dropna(),label='66% Modal Shift by 2040',linewidth=2,color='tab:orange',ls='--')
axs[0].plot(range(2020,2051),emiss_d81_8.dropna(),label='81% Modal Shift by 2030',linewidth=2,color='fuchsia')
axs[0].plot(range(2020,2051),emiss_d81_18.dropna(),label='81% Modal Shift by 2040',linewidth=2,color='fuchsia',ls='--')
axs[0].plot([2020,2030,2050],[3.7,3.7*0.3,0],label='70% Reduction by 2030',linewidth=2,color='black',ls='--')
axs[0].annotate("45% Reduction\nby 2030", xy=(2030, 2.2), xytext=(2040, 2.1),arrowprops=dict(arrowstyle="->"))
axs[0].text(-0.15, 1, 'a', transform=axs[0].transAxes,fontsize='medium', va='bottom',weight="bold")
axs[0].set_xlim(2020,2050)
axs[0].set_ylim(0,)

axs[1].set_ylabel("Use-phase Energy Demand (PJ)")
axs[1].set_xlabel("Year")
axs[1].grid()
axs[1].plot(range(2020,2051),energy_base.dropna(),label='Baseline',linewidth=2,color='black')
axs[1].plot(range(2020,2051),energy_rf.dropna(),label='33% Retrofitting',linewidth=2,color='turquoise')
axs[1].plot(range(2020,2051),energy_ren.dropna(),label="BEVs Powered by 100%\nRenewable Energy",linewidth=2,color='grey',ls='dashdot')
axs[1].plot(range(2020,2051),energy_p25.dropna(),label='2025 ICEV Phase-Out',linewidth=2, color='purple')
axs[1].plot(range(2020,2051),energy_early.dropna(),label="Premature Scrapping",linewidth=2,color='red',ls='-')
axs[1].plot(range(2020,2051),energy_lw40.dropna(),label='40% Light-weighting',linewidth=2,color='limegreen',ls='dashdot',)
axs[1].plot(range(2020,2051),energy_d43_8.dropna(),label='43% Modal Shift by 2030',linewidth=2,color='blue',ls='-')
axs[1].plot(range(2020,2051),energy_d43_18.dropna(),label='43% Modal Shift by 2040',linewidth=2,color='blue',ls='--')
axs[1].plot(range(2020,2051),energy_d66_8.dropna(),label='66% Modal Shift by 2030',linewidth=2,color='tab:orange',ls='-')
axs[1].plot(range(2020,2051),energy_d66_18.dropna(),label='66% Modal Shift by 2040',linewidth=2,color='tab:orange',ls='--')
axs[1].plot(range(2020,2051),energy_d81_8.dropna(),label='81% Modal Shift by 2030',linewidth=2,color='fuchsia',ls='-')
axs[1].plot(range(2020,2051),energy_d81_18.dropna(),label='81% Modal Shift by 2040',linewidth=2,color='fuchsia',ls='--')
axs[1].set_xlim(2020,2050)
axs[1].set_ylim(0,)
axs[1].text(-0.13, 1, 'b', transform=axs[1].transAxes,fontsize='medium', va='bottom',weight="bold")
"""
axs[0].set_ylabel("Use-phase Emissions (MtCO$_{2eq}$)")
axs[0].set_xlabel("Year")
axs[0].grid()
axs[0].plot(range(2020,2051),emiss_base.dropna(),label='Baseline',linewidth=2,color=sns.color_palette("Paired")[0])
axs[0].plot(range(2020,2051),emiss_rf.dropna(),label='33% Retro-fitting',linewidth=2,color=sns.color_palette("Paired")[1])
axs[0].plot(range(2020,2051),emiss_ren.dropna(),label="BEVs Powered by 100% Renewable Energy",linewidth=2,color=sns.color_palette("Paired")[2])
axs[0].plot(range(2020,2051),emiss_p25.dropna(),label='2025 Phase-Out',linewidth=2, color=sns.color_palette("Paired")[3])
axs[0].plot(range(2020,2051),emiss_early.dropna(),label="Early Scrapping",linewidth=2,color=sns.color_palette("Paired")[4])
axs[0].plot(range(2020,2051),emiss_lw40.dropna(),label='Lightweighting to 800kg',linewidth=2,color=sns.color_palette("Paired")[5])
axs[0].plot(range(2020,2051),emiss_d43_8.dropna(),label='43% Modal Shift by 2030',linewidth=2,color=sns.color_palette("Paired")[6])
axs[0].plot(range(2020,2051),emiss_d43_18.dropna(),label='43% Modal Shift by 2040',linewidth=2,color=sns.color_palette("Paired")[7])
axs[0].plot(range(2020,2051),emiss_d66_8.dropna(),label='66% Modal Shift by 2030',linewidth=2,color=sns.color_palette("Paired")[8])
axs[0].plot(range(2020,2051),emiss_d66_18.dropna(),label='66% Modal Shift by 2040',linewidth=2,color=sns.color_palette("Paired")[9])
axs[0].plot(range(2020,2051),emiss_d81_8.dropna(),label='81% Modal Shift by 2030',linewidth=2,color=sns.color_palette("Paired")[10])
axs[0].plot(range(2020,2051),emiss_d81_18.dropna(),label='81% Modal Shift by 2040',linewidth=2,color=sns.color_palette("Paired")[11])
axs[0].plot([2020,2030,2050],[3.7,3.7*0.3,0],label='70% Reduction by 2030',linewidth=2,color='black',ls='--')
axs[0].annotate("45% Reduction\nby 2030", xy=(2030, 2.2), xytext=(2040, 2.1),arrowprops=dict(arrowstyle="->"))
axs[0].text(-0.15, 1, 'a', transform=axs[0].transAxes,fontsize='medium', va='bottom',weight="bold")
axs[0].set_xlim(2020,2050)
axs[0].set_ylim(0,)

axs[1].set_ylabel("Use-phase Energy Demand (PJ)")
axs[1].set_xlabel("Year")
axs[1].grid()
axs[1].plot(range(2020,2051),energy_base.dropna(),label='Baseline',linewidth=2,color='black')
axs[1].plot(range(2020,2051),energy_rf.dropna(),label='33% Retrofitting',linewidth=2,color='turquoise')
axs[1].plot(range(2020,2051),energy_ren.dropna(),label="BEVs Powered by 100%\nRenewable Energy",linewidth=2,color='grey',ls='dashdot')
axs[1].plot(range(2020,2051),energy_p25.dropna(),label='2025 ICEV Phase-Out',linewidth=2, color='purple')
axs[1].plot(range(2020,2051),energy_early.dropna(),label="Premature Scrapping",linewidth=2,color='red',ls='-')
axs[1].plot(range(2020,2051),energy_lw40.dropna(),label='40% Light-weighting',linewidth=2,color='limegreen',ls='dashdot',)
axs[1].plot(range(2020,2051),energy_d43_8.dropna(),label='43% Modal Shift by 2030',linewidth=2,color='blue',ls='-')
axs[1].plot(range(2020,2051),energy_d43_18.dropna(),label='43% Modal Shift by 2040',linewidth=2,color='blue',ls='--')
axs[1].plot(range(2020,2051),energy_d66_8.dropna(),label='66% Modal Shift by 2030',linewidth=2,color='tab:orange',ls='-')
axs[1].plot(range(2020,2051),energy_d66_18.dropna(),label='66% Modal Shift by 2040',linewidth=2,color='tab:orange',ls='--')
axs[1].plot(range(2020,2051),energy_d81_8.dropna(),label='81% Modal Shift by 2030',linewidth=2,color='fuchsia',ls='-')
axs[1].plot(range(2020,2051),energy_d81_18.dropna(),label='81% Modal Shift by 2040',linewidth=2,color='fuchsia',ls='--')
axs[1].set_xlim(2020,2050)
axs[1].set_ylim(0,)
axs[1].text(-0.13, 1, 'b', transform=axs[1].transAxes,fontsize='medium', va='bottom',weight="bold")

plt.legend(bbox_to_anchor=(1,0.8))
plt.savefig('Fig3.png', bbox_inches="tight")
plt.savefig('Fig3.pdf', bbox_inches="tight")
plt.show()