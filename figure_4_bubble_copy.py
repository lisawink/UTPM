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

mask= ResultsDF['Regulated EV manufacture:'] == 0
print((ResultsDF[mask].Energy/1e12))
print((ResultsDF[mask].Emissions))
print((ResultsDF[mask]['Modal shift:']))
color=ResultsDF[mask]['Modal shift:']
color2=ResultsDF[~mask]['Modal shift:']
print(color)

fig, ax = plt.subplots(figsize=(11,8))
mask= ResultsDF['Regulated EV manufacture:'] == 0
cmap=plt.cm.get_cmap('viridis', 6)
im=ax.scatter(ResultsDF[mask]['Energy']/1e12,ResultsDF[mask]['Emissions'], marker='_', c=color,cmap=cmap ,s=30, vmax=30,vmin=-90)
im2=ax.scatter(ResultsDF[~mask]['Energy']/1e12,ResultsDF[~mask]['Emissions'], marker='|', c=color2,cmap=cmap,s=30, vmax=30,vmin=-90 )
im=ax.scatter(ResultsDF[mask]['Cumulative Tailpipe Emissions'],ResultsDF[mask]['Emissions'], marker='_', c=color,cmap=cmap ,s=30, vmax=30,vmin=-90)
im2=ax.scatter(ResultsDF[~mask]['Cumulative Tailpipe Emissions'],ResultsDF[~mask]['Emissions'], marker='|', c=color2,cmap=cmap,s=30, vmax=30,vmin=-90 )
im3=ax.scatter(ResultsDF[mask]['Emissions'],ResultsDF[mask]['Cumulative Tailpipe Emissions'], marker='_', c=color,cmap=cmap ,s=30, vmax=30,vmin=-90)
im4=ax.scatter(ResultsDF[~mask]['Emissions'],ResultsDF[~mask]['Cumulative Tailpipe Emissions'], marker='|', c=color2,cmap=cmap,s=30, vmax=30,vmin=-90 )

#plt.savefig('Fig4.png', bbox_inches="tight")
#plt.savefig('Fig4.pdf', bbox_inches="tight")
plt.show()
#plt.scatter(ResultsDF.Energy,ResultsDF.Emissions,c=ResultsDF['Modal Shift'],s=2)

fig, ax = plt.subplots(figsize=(11,8))
mask= ResultsDF['Regulated EV manufacture:'] == 0
cmap=plt.cm.get_cmap('viridis', 6)
im=ax.scatter(ResultsDF[mask]['Cumulative Tailpipe Emissions'],ResultsDF[mask]['Emissions'], marker='_', c=color,cmap=cmap ,s=30, vmax=30,vmin=-90)
im2=ax.scatter(ResultsDF[~mask]['Cumulative Tailpipe Emissions'],ResultsDF[~mask]['Emissions'], marker='|', c=color2,cmap=cmap,s=30, vmax=30,vmin=-90 )
#im=ax.scatter(ResultsDF[mask]['Energy']/1e12,ResultsDF[mask]['Emissions'], marker='_')
#ax.scatter(ResultsDF[~mask]['Energy']/1e12,ResultsDF[~mask]['Emissions'], marker='|' )
#plt.savefig('Fig4.png', bbox_inches="tight")
#plt.savefig('Fig4.pdf', bbox_inches="tight")
plt.xticks([])
plt.yticks([])
plt.show()
#plt.scatter(ResultsDF.Energy,ResultsDF.Emissions,c=ResultsDF['Modal Shift'],s=2)

fig, ax = plt.subplots(figsize=(11,8))
mask= ResultsDF['Regulated EV manufacture:'] == 0
cmap=plt.cm.get_cmap('plasma', 6)
ax.set_facecolor('black')
im=ax.scatter(ResultsDF[mask]['Cumulative Tailpipe Emissions'],ResultsDF[mask]['Emissions'], marker='_', c=color,cmap=cmap ,s=30, vmax=30,vmin=-90)
im2=ax.scatter(ResultsDF[~mask]['Cumulative Tailpipe Emissions'],ResultsDF[~mask]['Emissions'], marker='|', c=color2,cmap=cmap,s=30, vmax=30,vmin=-90 )
#im=ax.scatter(ResultsDF[mask]['Energy']/1e12,ResultsDF[mask]['Emissions'], marker='_')
#ax.scatter(ResultsDF[~mask]['Energy']/1e12,ResultsDF[~mask]['Emissions'], marker='|' )
#plt.savefig('Fig4.png', bbox_inches="tight")
plt.xticks([])
plt.yticks([])
plt.savefig('art.pdf', bbox_inches="tight")
plt.savefig('art.png', bbox_inches="tight")
plt.show()
#plt.scatter(ResultsDF.Energy,ResultsDF.Emissions,c=ResultsDF['Modal Shift'],s=2)

fig, ax = plt.subplots(figsize=(11,8))
mask= ResultsDF['Regulated EV manufacture:'] == 0
cmap=plt.cm.get_cmap('viridis', 6)
im=ax.scatter(ResultsDF[mask]['Emissions'],ResultsDF[mask]['Cumulative Tailpipe Emissions'], marker='_', c=color,cmap=cmap ,s=30, vmax=30,vmin=-90)
im2=ax.scatter(ResultsDF[~mask]['Emissions'],ResultsDF[~mask]['Cumulative Tailpipe Emissions'], marker='|', c=color2,cmap=cmap,s=30, vmax=30,vmin=-90 )
#plt.savefig('Fig4.png', bbox_inches="tight")
#plt.savefig('Fig4.pdf', bbox_inches="tight")
plt.xticks([])
plt.yticks([])
plt.show()
#plt.scatter(ResultsDF.Energy,ResultsDF.Emissions,c=ResultsDF['Modal Shift'],s=2)
