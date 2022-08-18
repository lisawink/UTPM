from UTPM_final import Run_Model
import matplotlib.pyplot as plt
import numpy as np

base=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
base_ren=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2020,rate=28)
third_rf=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0.33,manufacture=0,elec=2050,rate=28)
lw_40=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=840,\
               fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
d4343_8=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=-42.99,miles_driven_projection=-42.99,retrofit_percentage=0,manufacture=0,elec=2050,rate=8)
d6666_8=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=-66,miles_driven_projection=-66,retrofit_percentage=0,manufacture=0,elec=2050,rate=8)
d8181_8=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=-81,miles_driven_projection=-81,retrofit_percentage=0,manufacture=0,elec=2050,rate=8)
d4343_18=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=-42.99,miles_driven_projection=-42.99,retrofit_percentage=0,manufacture=0,elec=2050,rate=18)
d6666_18=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=-66,miles_driven_projection=-66,retrofit_percentage=0,manufacture=0,elec=2050,rate=18)
d8181_18=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=-81,miles_driven_projection=-81,retrofit_percentage=0,manufacture=0,elec=2050,rate=18)
p2525=Run_Model(phase_out_date=2025,phase_out_hybrid=2025,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
               fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
early=Run_Model(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=15,scrap_age_post2020=10,mass=1400,\
               fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)

emiss1=base[0]+base[1]
emiss2=lw_40[0]+lw_40[1]
emiss3=p2525[0]+p2525[1]
emiss4=third_rf[0]+third_rf[1]
emiss5=d4343_8[0]+d4343_8[1]
emiss6=d6666_8[0]+d6666_8[1]
emiss7=d8181_8[0]+d8181_8[1]
emiss8=early[0]+early[1]
emiss9=base_ren[0]+base_ren[1]
emiss10=d4343_18[0]+d4343_18[1]
emiss11=d6666_18[0]+d6666_18[1]
emiss12=d8181_18[0]+d8181_18[1]

energy1=(base[12]+base[13])/10**9
energy2=(lw_40[12]+lw_40[13])/10**9
energy3=(p2525[12]+p2525[13])/10**9
energy4=(third_rf[12]+third_rf[13])/10**9
energy5=(d4343_8[12]+d4343_8[13])/10**9
energy6=(d6666_8[12]+d6666_8[13])/10**9
energy7=(d8181_8[12]+d8181_8[13])/10**9
energy8=(early[12]+early[13])/10**9
energy9=(base_ren[12]+base_ren[13])/10**9
energy10=(d4343_18[12]+d4343_18[13])/10**9
energy11=(d6666_18[12]+d6666_18[13])/10**9
energy12=(d8181_18[12]+d8181_18[13])/10**9

fig, axs = plt.subplots(1,2,figsize=(14,9),sharey=False,sharex=False, gridspec_kw={'width_ratios': [1, 1]})

# horizontal space between axes
fig.subplots_adjust(wspace=0.15)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Polygon

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

axs[0].set_ylabel("Use-phase Emissions (MtCO$_{2eq}$)")
axs[0].set_xlabel("Year")
axs[0].grid()
axs[0].plot(range(2020,2051),emiss1,label='Baseline',linewidth=2,color='black')
axs[0].plot(range(2020,2051),emiss4,label='33% Retro-fitting',linewidth=2,color='turquoise')
axs[0].plot(range(2020,2051),emiss9,label="BEVs Powered by 100% Renewable Energy",linewidth=2,color='grey',ls='dashdot')
axs[0].plot(range(2020,2051),emiss3,label='2025 Phase-Out',linewidth=2, color='purple')
axs[0].plot(range(2020,2051),emiss8,label="Early Scrapping",linewidth=2,color='red',ls='-')
axs[0].plot(range(2020,2051),emiss2,label='Lightweighting to 800kg',linewidth=2,color='limegreen',ls='dashdot',)
axs[0].plot(range(2020,2051),emiss5,label='43% Modal Shift by 2030',linewidth=2,color='blue',ls='-')
axs[0].plot(range(2020,2051),emiss10,label='43% Modal Shift by 2040',linewidth=2,color='blue',ls='--')
axs[0].plot(range(2020,2051),emiss6,label='66% Modal Shift by 2030',linewidth=2,color='tab:orange',ls='-')
axs[0].plot(range(2020,2051),emiss11,label='66% Modal Shift by 2040',linewidth=2,color='tab:orange',ls='--')
axs[0].plot(range(2020,2051),emiss7,label='81% Modal Shift by 2030',linewidth=2,color='fuchsia')
axs[0].plot(range(2020,2051),emiss12,label='81% Modal Shift by 2040',linewidth=2,color='fuchsia',ls='--')
axs[0].annotate("45% Reduction\nby 2030", xy=(2030, 2.2), xytext=(2040, 2.1),arrowprops=dict(arrowstyle="->"))
axs[0].text(-0.15, 1, 'a', transform=axs[0].transAxes,fontsize='medium', va='bottom',weight="bold")
axs[0].set_xlim(2020,2050)
axs[0].set_ylim(0,)

axs[1].set_ylabel("Use-phase Energy Demand (PJ)")
axs[1].set_xlabel("Year")
axs[1].grid()
axs[1].plot(range(2020,2051),energy1,label='Baseline',linewidth=2,color='black')
axs[1].plot(range(2020,2051),energy4,label='33% Retrofitting',linewidth=2,color='turquoise')
axs[1].plot(range(2020,2051),energy9,label="BEVs Powered by 100%\nRenewable Energy",linewidth=2,color='grey',ls='dashdot')
axs[1].plot(range(2020,2051),energy3,label='2025 ICEV Phase-Out',linewidth=2, color='purple')
axs[1].plot(range(2020,2051),energy8,label="Premature Scrapping",linewidth=2,color='red',ls='-')
axs[1].plot(range(2020,2051),energy2,label='40% Light-weighting',linewidth=2,color='limegreen',ls='dashdot',)
axs[1].plot(range(2020,2051),energy5,label='43% Modal Shift by 2030',linewidth=2,color='blue',ls='-')
axs[1].plot(range(2020,2051),energy10,label='43% Modal Shift by 2040',linewidth=2,color='blue',ls='--')
axs[1].plot(range(2020,2051),energy6,label='66% Modal Shift by 2030',linewidth=2,color='tab:orange',ls='-')
axs[1].plot(range(2020,2051),energy11,label='66% Modal Shift by 2040',linewidth=2,color='tab:orange',ls='--')
axs[1].plot(range(2020,2051),energy7,label='81% Modal Shift by 2030',linewidth=2,color='fuchsia',ls='-')
axs[1].plot(range(2020,2051),energy12,label='81% Modal Shift by 2040',linewidth=2,color='fuchsia',ls='--')
axs[1].set_xlim(2020,2050)
axs[1].set_ylim(0,)
axs[1].text(-0.13, 1, 'b', transform=axs[1].transAxes,fontsize='medium', va='bottom',weight="bold")

plt.legend(bbox_to_anchor=(1,0.8))
plt.show()