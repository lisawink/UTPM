"""Module containing method for creating Figure 4"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import matplotlib.cm as mpl_cm
import matplotlib.pylab as pl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib.colors
from matplotlib.lines import Line2D

ResultsDF = pd.read_csv('figure_4.csv')

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

ResultsDF['Tailpipe Emissions'] = ResultsDF['Cumulative Tailpipe Emissions']

ResultsDF['Emissions'] = ResultsDF['Cumulative Electric Emissions'] + \
                         ResultsDF['Cumulative Tailpipe Emissions'] + \
                         ResultsDF['Cumulative WTT Emissions'] + \
                         ResultsDF['Cumulative EV Production Emissions'] + \
                         ResultsDF['Cumulative EV Production Emissions'] + \
                         ResultsDF['Cumulative ICE Production Emissions'] + \
                         ResultsDF['Cumulative Conversion Production Emissions']

ResultsDF['Energy'] = ResultsDF['Cumulative Tailpipe Energy']

def create_bins(lower_bound, width, quantity):
    bins=[]
    for low in range(lower_bound,
                     lower_bound + quantity*width + 1, width):
        bins.append((low, low+width))
    return bins

def find_bin(value, bins):
    """ bins is a list of tuples, like [(0,20), (20, 40), (40, 60)],
        binning returns the smallest index i of bins so that
        bin[i][0] <= value < bin[i][1]
    """
    
    for i in range(0, len(bins)):
        if bins[i][0] <= value < bins[i][1]:
            return i
    return -1

#create bins for tailpipe emissions
bins_tail = create_bins(lower_bound=15,
                   width=10,
                   quantity=8)

#create bins for total emissions
bins_tot = create_bins(lower_bound=35,
                   width=30,
                   quantity=9)

#find bins for each line of tailpipe emissions
bin_array=[]
for i in ResultsDF['Tailpipe Emissions']:
    bin_array.append(bins_tail[find_bin(i,bins_tail)]) 
ResultsDF['Tailpipe Bin Array']=bin_array

#find bins for each line of total emissions
bin_array=[]
for i in ResultsDF['Emissions']:
    bin_array.append(bins_tot[find_bin(i,bins_tot)]) 
ResultsDF['Total Bin Array']=bin_array

#code for bubble plot with tailpipe and total emissions
count=[]
avg_cta=[]
tail_emiss=[]
tot_emiss=[]
for i in bins_tail:
    for j in bins_tot:
        results_bin=ResultsDF[(ResultsDF['Tailpipe Bin Array'] == i) & (ResultsDF['Total Bin Array'] == j)]
        tail_emiss.append(results_bin['Tailpipe Emissions'].sum(axis=0)/len(results_bin))
        tot_emiss.append(results_bin['Emissions'].sum(axis=0)/len(results_bin))
        count.append(len(results_bin))
        avg_cta.append(results_bin['Modal shift:'].sum(axis=0)/len(results_bin))

df = pd.DataFrame({
    'X': tot_emiss,
    'Y': tail_emiss,
    'bubble_colors': avg_cta,
    'bubble_size':count})
df=df.dropna()
print(df)
print(len(df['X']))
print(len(df['Y']))
print(len(df['bubble_colors']))

norm = plt.Normalize(df['bubble_colors'].min(), df['bubble_colors'].max())

fig, ax = plt.subplots(figsize=(11,8))
minsize = min(df['bubble_size'])**1.2
maxsize = max(df['bubble_size'])**1.2
im=sns.scatterplot(x='X',y= 'Y', size='bubble_size', sizes=(minsize,maxsize),data=df,alpha=0.9,hue='bubble_colors',palette=cmap)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm,label='Car Travel Activity (%)')
h, l = plt.gca().get_legend_handles_labels()
legend_handles=[Line2D([0], [0], marker='o', color='w', label='Scatter',markerfacecolor=(0.2,0.2,0.2,1), markersize=9)]+h[7:]
legend_labels=['20','100','180','260','340','420']
plt.legend(legend_handles,legend_labels,labelspacing=1.2, title="Possible Policy Combinations",bbox_to_anchor=(1.15,1.17),ncol=6)
plt.plot([0,350],[63.25,63.25],linewidth=1,color='black',ls='--')
plt.text(305,64,'CCC Balanced\nPathway',fontsize='small',horizontalalignment='center')
plt.plot([0,350],[46.42,46.42],linewidth=1,color='black',ls='--')
plt.text(305,47,'CCC Global Avg.\n~50% 1.5°C ',fontsize='small',horizontalalignment='center')
plt.plot([0,350],[72.05,72.05],linewidth=1,color='black',ls='--')
plt.text(305,73,'CCC Global Avg.\n>66% 2°C',fontsize='small',horizontalalignment='center')
plt.plot([0,350],[32,32],linewidth=1,color='black',ls='--')
plt.text(305,32.5,'Element Energy\nAccelerated Green',fontsize='small',horizontalalignment='center')
#plt.plot([0,300],[27.5,27.5],linewidth=1,color='black',ls='--')
#plt.text(1.15,28,'Element Energy No Constraints',fontsize='small')
plt.plot([0,350],[21.7,21.7],linewidth=1,color='black',ls='--')
plt.text(305,22,'Tyndall',fontsize='small',horizontalalignment='center')
plt.annotate("Global\nEqual\nShare",xy=(21,18),xytext=(21,80),arrowprops=dict(arrowstyle='<->',lw=3),horizontalalignment='center')
plt.annotate("Fair Share",xy=(2,15))
plt.xlabel('Cumulative Total Emissions up to 2050 (MtCO$_{2eq}$)')
plt.ylabel('Cumulative Tailpipe Emissions up to 2050 (MtCO$_{2}$)')
plt.xlim(0,350)
plt.ylim(10,100)
plt.grid(b=True)
plt.savefig('Fig4_bubble_v2.png', bbox_inches="tight")
plt.savefig('Fig4_bubble_v2.pdf', bbox_inches="tight")
plt.show()