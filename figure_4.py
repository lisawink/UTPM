import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import matplotlib.cm as mpl_cm
import matplotlib.pylab as pl

ResultsDF=pd.read_csv('all_policies_results_sorted.csv')

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

fig, ax = plt.subplots(figsize=(11,8))
plt.grid()
mask= ResultsDF['Regulated EV manufacture'] == 0
cmap=plt.cm.get_cmap('viridis', 6)
im=ax.scatter(ResultsDF[mask].Energy/1e12,ResultsDF[mask].Emissions, marker='_', c=ResultsDF[mask]['Modal Shift'],cmap=cmap ,s=30, vmax=30,vmin=-90)
ax.scatter(ResultsDF[~mask].Energy/1e12,ResultsDF[~mask].Emissions, marker='|', c=ResultsDF[mask]['Modal Shift'],cmap=cmap,s=30, vmax=30,vmin=-90 )
plt.legend(['No Regulated EV Manufacture','Regulated EV Manufacture','test3'])
fig.colorbar(im, ax=ax,label='Car Travel Activity (%)')
plt.plot(1,66,'ro')
plt.text(1,66,'CCC Balanced Pathway')
plt.savefig('EnergyEmissionsPlot.png')
plt.xlabel('Cumulative Energy Demand up to 2050 (EJ)')
plt.ylabel('Cumulative Emissions up to 2050 (MtCO$_{2eq}$)')
plt.xlim(0.5,3)
plt.grid(b=True)
#plt.axhline(y=21.7, ls='--', c='red')
plt.savefig('Fig4.png', bbox_inches="tight")
plt.savefig('Fig4.pdf', bbox_inches="tight")
plt.show()
#plt.scatter(ResultsDF.Energy,ResultsDF.Emissions,c=ResultsDF['Modal Shift'],s=2)