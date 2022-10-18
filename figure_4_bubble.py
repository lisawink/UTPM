import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import matplotlib.cm as mpl_cm
import matplotlib.pylab as pl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib.colors

ResultsDF = pd.read_csv('figure_6_cont2.csv')

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
"""
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
im=ax.scatter(ResultsDF[mask]['Energy']/1e12,ResultsDF[mask]['Emissions'], marker='_', c=color,cmap=cmap ,s=30, vmax=30,vmin=-90)
im2=ax.scatter(ResultsDF[~mask]['Energy']/1e12,ResultsDF[~mask]['Emissions'], marker='|', c=color2,cmap=cmap,s=30, vmax=30,vmin=-90 )
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
plt.savefig('Fig4.png', bbox_inches="tight")
plt.savefig('Fig4.pdf', bbox_inches="tight")
plt.show()
#plt.scatter(ResultsDF.Energy,ResultsDF.Emissions,c=ResultsDF['Modal Shift'],s=2)

fig, ax = plt.subplots(figsize=(11,8))
plt.grid()
mask= ResultsDF['Regulated EV manufacture:'] == 0
cmap=plt.cm.get_cmap('viridis', 6)
im=ax.scatter(ResultsDF[mask]['Cumulative Tailpipe Emissions'],ResultsDF[mask]['Emissions'], marker='_', c=color,cmap=cmap ,s=30, vmax=30,vmin=-90)
im2=ax.scatter(ResultsDF[~mask]['Cumulative Tailpipe Emissions'],ResultsDF[~mask]['Emissions'], marker='|', c=color2,cmap=cmap,s=30, vmax=30,vmin=-90 )
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
plt.xlabel('Cumulative Tailpipe Emissions up to 2050 (EJ)')
plt.ylabel('Cumulative Emissions up to 2050 (MtCO$_{2eq}$)')
#plt.xlim(0,4.3)
plt.grid(b=True)
#plt.axhline(y=21.7, ls='--', c='red')
plt.savefig('Fig4.png', bbox_inches="tight")
plt.savefig('Fig4.pdf', bbox_inches="tight")
plt.show()
#plt.scatter(ResultsDF.Energy,ResultsDF.Emissions,c=ResultsDF['Modal Shift'],s=2)

fig, ax = plt.subplots(figsize=(11,8))
plt.grid()
mask= ResultsDF['Regulated EV manufacture:'] == 0
cmap=plt.cm.get_cmap('viridis', 6)
im=ax.scatter(ResultsDF[mask]['Emissions'],ResultsDF[mask]['Cumulative Tailpipe Emissions'], marker='_', c=color,cmap=cmap ,s=30, vmax=30,vmin=-90)
im2=ax.scatter(ResultsDF[~mask]['Emissions'],ResultsDF[~mask]['Cumulative Tailpipe Emissions'], marker='|', c=color2,cmap=cmap,s=30, vmax=30,vmin=-90 )
#im=ax.scatter(ResultsDF[mask]['Energy']/1e12,ResultsDF[mask]['Emissions'], marker='_')
#ax.scatter(ResultsDF[~mask]['Energy']/1e12,ResultsDF[~mask]['Emissions'], marker='|' )
plt.legend(['No Regulated EV Manufacture','Regulated EV Manufacture','test3'])
fig.colorbar(im, ax=ax,label='Car Travel Activity (%)')
plt.plot([0,300],[63.25,63.25],linewidth=1,color='black',ls='--')
plt.text(1.35,64,'CCC Balanced Pathway',fontsize='small')
plt.plot([0,300],[46.42,46.42],linewidth=1,color='black',ls='--')
plt.text(1.5,47,'CCC ~50% 1.5°C ',fontsize='small')
plt.plot([0,300],[72.05,72.05],linewidth=1,color='black',ls='--')
plt.text(1.55,73,'CCC >66% 2°C',fontsize='small')
plt.plot([0,300],[32,32],linewidth=1,color='black',ls='--')
plt.text(1.05,32.5,'Element Energy Accelerated Green',fontsize='small')
plt.plot([0,300],[27.5,27.5],linewidth=1,color='black',ls='--')
plt.text(1.15,28,'Element Energy No Constraints',fontsize='small')
plt.plot([0,300],[21.7,21.7],linewidth=1,color='black',ls='--')
plt.text(1.75,22,'Tyndall',fontsize='small')
plt.xlabel('Cumulative Emissions up to 2050 (EJ)')
plt.ylabel('Cumulative Tailpipe Emissions up to 2050 (MtCO$_{2eq}$)')
#plt.xlim(0,4.3)
plt.grid(b=True)
#plt.axhline(y=21.7, ls='--', c='red')
plt.savefig('Fig4.png', bbox_inches="tight")
plt.savefig('Fig4.pdf', bbox_inches="tight")
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
plt.savefig('EnergyEmissionsPlot.png')
plt.xlabel('Cumulative Energy Demand up to 2050 (EJ)')
plt.ylabel('Cumulative Emissions up to 2050 (MtCO$_{2eq}$)')
plt.xlim(0,2)
plt.grid(b=True)
#plt.axhline(y=21.7, ls='--', c='red')
plt.savefig('Fig4_tailpipe.png', bbox_inches="tight")
plt.savefig('Fig4_tailpipe.pdf', bbox_inches="tight")
plt.show()
#plt.scatter(ResultsDF.Energy,ResultsDF.Emissions,c=ResultsDF['Modal Shift'],s=2)
"""
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

#code for bubble plot with just tailpipe emissions
count=[]
avg_cta=[]
tail_emiss=[]
for i in bins_tot:
    results_bin=ResultsDF[ResultsDF['Tailpipe Bin Array'] == i]
    tail_emiss.append(results_bin['Tailpipe Emissions'].sum(axis=0)/len(results_bin))
    count.append(len(results_bin))
    avg_cta.append(results_bin['Modal shift:'].sum(axis=0)/len(results_bin))

df = pd.DataFrame({
    'X': tail_emiss,
    'Y': tail_emiss,
    'Colors': avg_cta,
    "bubble_size":count})

cmap=plt.cm.get_cmap('viridis')

colorlist=["navy", "tab:orange"]
cmap = LinearSegmentedColormap.from_list('testCmap', colors=colorlist, N=256)

#scatter=plt.scatter('X', 'Y', s='bubble_size',c='Colors',alpha=0.5, data=df,label=avg_cta)
#plt.legend(handles=scatter.legend_elements()[0], 
#           labels=avg_cta,
 #          title="CTA")
#plt.show()

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



print(tail_emiss)
print(type(tail_emiss))
print(avg_cta)
print(type(avg_cta))

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
im=sns.scatterplot(x='X',y= 'Y', size='bubble_size', sizes=(minsize, maxsize),data=df,alpha=0.9,hue='bubble_colors',palette=cmap)
#print('this is im',im.legend_elements)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm,label='Car Travel Activity (%)')
h, l = plt.gca().get_legend_handles_labels()
print('h is',h)
print('l is',l)
plt.legend(h[7:], l[7:],labelspacing=1.2, title="Possible Policy Combinations",bbox_to_anchor=(0.99,1.17),ncol=5)
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

from matplotlib.lines import Line2D

fig, ax = plt.subplots(figsize=(11,8))
minsize = min(df['bubble_size'])**1.2
maxsize = max(df['bubble_size'])**1.2
im=sns.scatterplot(x='X',y= 'Y', size='bubble_size', sizes=(minsize,maxsize),data=df,alpha=0.9,hue='bubble_colors',palette=cmap)
#print('this is im',im.legend_elements)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm,label='Car Travel Activity (%)')
h, l = plt.gca().get_legend_handles_labels()
print('h is',h)
print(vars(h[7]))
print('l is',l)
legend_handles=[Line2D([0], [0], marker='o', color='w', label='Scatter',markerfacecolor=(0.2,0.2,0.2,1), markersize=9)]+h[7:]
legend_labels=['0']+l[7:]
print(legend_handles)
print(legend_labels)
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