import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import matplotlib.cm as mpl_cm
import matplotlib.pylab as pl

ResultsDF = pd.read_csv('sens_an.csv')

ResultsDF['Emissions'] = ResultsDF['Cumulative Electric Emissions'] + \
                         ResultsDF['Cumulative Tailpipe Emissions'] + \
                         ResultsDF['Cumulative WTT Emissions'] + \
                         ResultsDF['Cumulative EV Production Emissions'] + \
                         ResultsDF['Cumulative EV Production Emissions'] + \
                         ResultsDF['Cumulative ICE Production Emissions'] + \
                         ResultsDF['Cumulative Conversion Production Emissions']

ResultsDF['Energy'] = ResultsDF['Cumulative Electric Energy'] + \
                      ResultsDF['Cumulative WTT Energy'] + \
                      ResultsDF['Cumulative Tailpipe Energy'] + \
                      ResultsDF['Cumulative EV Production Energy'] + \
                      ResultsDF['Cumulative EV Production Energy'] + \
                      ResultsDF['Cumulative ICE Production Energy'] + \
                      ResultsDF['Cumulative Conversion Production Energy']

ResultsDF['Emissions'] = ResultsDF['Cumulative Tailpipe Emissions']

ResultsDF['Energy'] = ResultsDF['Cumulative Tailpipe Energy']

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

mask= ResultsDF['Regulated EV manufacture:'] == 0
print((ResultsDF[mask].Energy/1e12))
print((ResultsDF[mask].Emissions))
print((ResultsDF[mask]['Modal shift:']))
color=ResultsDF[mask]['Modal shift:']
color2=ResultsDF[~mask]['Modal shift:']
print(color)

fig, ax = plt.subplots(figsize=(11,8))
plt.grid()
mask= ResultsDF['Regulated EV manufacture:'] == 0
cmap=plt.cm.get_cmap('viridis', 6)
im=ax.scatter(ResultsDF[mask]['Energy']/1e12,ResultsDF[mask]['Emissions'], marker='_', c=color,cmap=cmap ,s=30, vmax=-50,vmin=-90)
im2=ax.scatter(ResultsDF[~mask]['Energy']/1e12,ResultsDF[~mask]['Emissions'], marker='|', c=color2,cmap=cmap,s=30, vmax=-50,vmin=-90 )
#im=ax.scatter(ResultsDF[mask]['Energy']/1e12,ResultsDF[mask]['Emissions'], marker='_')
#ax.scatter(ResultsDF[~mask]['Energy']/1e12,ResultsDF[~mask]['Emissions'], marker='|' )
plt.legend(['No Regulated EV Manufacture','Regulated EV Manufacture','test3'])
fig.colorbar(im, ax=ax,label='Car Travel Activity (%)')
#plt.plot([0,4.5],[63.25,63.25],linewidth=1,color='black',ls='--')
#plt.text(3,66,'CCC Balanced Pathway',fontsize='small')
#plt.plot([0,4.5],[46.42,46.42],linewidth=1,color='black',ls='--')
#plt.text(3,48,'CCC ~50% 1.5°C ',fontsize='small')
#plt.plot([0,4.5],[72.05,72.05],linewidth=1,color='black',ls='--')
#plt.text(3,74,'CCC >66% 2°C',fontsize='small')
#plt.plot([0,4.5],[21.7,21.7],linewidth=1,color='black',ls='--')
#plt.text(3,23,'Tyndall',fontsize='small')
plt.xlabel('Cumulative Energy Demand up to 2050 (EJ)')
plt.ylabel('Cumulative Emissions up to 2050 (MtCO$_{2eq}$)')
plt.xlim(0,4.3)
plt.grid(b=True)
#plt.axhline(y=21.7, ls='--', c='red')
#plt.savefig('Fig4.png', bbox_inches="tight")
#plt.savefig('Fig4.pdf', bbox_inches="tight")
plt.show()
#plt.scatter(ResultsDF.Energy,ResultsDF.Emissions,c=ResultsDF['Modal Shift'],s=2)

ResultsDF['Emissions'] = ResultsDF['Cumulative Tailpipe Emissions']

ResultsDF['Energy'] = ResultsDF['Cumulative Tailpipe Energy']

fig, ax = plt.subplots(figsize=(11,8))
plt.grid()
mask= ResultsDF['Regulated EV manufacture:'] == 0
cmap=plt.cm.get_cmap('viridis', 6)
im=ax.scatter(ResultsDF[mask]['Energy']/1e12,ResultsDF[mask]['Emissions'], marker='o', c=color,cmap=cmap ,s=30, vmax=30,vmin=-90)
#im2=ax.scatter(ResultsDF[~mask]['Energy']/1e12,ResultsDF[~mask]['Emissions'], marker='|', c=color2,cmap=cmap,s=30, vmax=30,vmin=-90 )
#im=ax.scatter(ResultsDF[mask]['Energy']/1e12,ResultsDF[mask]['Emissions'], marker='_')
#ax.scatter(ResultsDF[~mask]['Energy']/1e12,ResultsDF[~mask]['Emissions'], marker='|' )
#plt.legend(['No Regulated EV Manufacture','Regulated EV Manufacture','test3'])
fig.colorbar(im, ax=ax,label='Car Travel Activity (%)')
plt.plot([0,2],[63.25,63.25],linewidth=1,color='black',ls='--')
plt.text(1.35,64,'CCC Balanced Pathway',fontsize='small')
plt.plot([0,2],[46.42,46.42],linewidth=1,color='black',ls='--')
plt.text(1.5,47,'CCC ~50% 1.5°C ',fontsize='small')
plt.plot([0,2],[72.05,72.05],linewidth=1,color='black',ls='--')
plt.text(1.55,73,'CCC >66% 2°C',fontsize='small')
plt.plot([0,2],[32,32],linewidth=1,color='black',ls='--')
plt.text(1.05,32.5,'Element Energy Accelerated Green',fontsize='small')
plt.plot([0,2],[27.5,27.5],linewidth=1,color='black',ls='--')
plt.text(1.15,28,'Element Energy No Constraints',fontsize='small')
plt.plot([0,2],[21.7,21.7],linewidth=1,color='black',ls='--')
plt.text(1.75,22,'Tyndall',fontsize='small')
#plt.savefig('EnergyEmissionsPlot.png')
plt.xlabel('Cumulative Energy Demand up to 2050 (EJ)')
plt.ylabel('Cumulative Emissions up to 2050 (MtCO$_{2eq}$)')
plt.xlim(0,2)
plt.grid(b=True)
#plt.axhline(y=21.7, ls='--', c='red')
plt.savefig('Fig4_tailpipe.png', bbox_inches="tight")
plt.savefig('Fig4_tailpipe.pdf', bbox_inches="tight")
plt.show()
#plt.scatter(ResultsDF.Energy,ResultsDF.Emissions,c=ResultsDF['Modal Shift'],s=2)