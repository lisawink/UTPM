import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

ResultsDF = pd.read_csv('sens_an2.csv')

ResultsDF['Emissions'] = ResultsDF['Cumulative Tailpipe Emissions']

"""
plt.plot(ResultsDF['Modal shift:'],ResultsDF['Emissions'],'x',linestyle='-')
plt.xlabel('Reduction in Car Travel Activity in 2050 (%)\nApplied to Highest Ambition Scenario')
plt.ylabel('Cumulative Tailpipe Emissions\nup to 2050 (MtCO$_{2eq}$)')
plt.ylim(20,28)
plt.xlim(-49,-91)
plt.grid(b=True)
#plt.axhline(y=21.7, ls='--', c='red')
plt.savefig('sens_plot.png', bbox_inches="tight")
plt.show()

plt.plot(ResultsDF['Modal shift:'],ResultsDF['Modal shift rate (years):'],'x')
plt.xlabel('Reduction in Car Travel Activity in 2050 (%)\nApplied to Highest Ambition Scenario')
plt.ylabel('Rate of CTA (years)')
#plt.ylim(20,28)
plt.xlim(-49,-91)
plt.grid(b=True)
#plt.axhline(y=21.7, ls='--', c='red')
plt.savefig('sens_plot2.png', bbox_inches="tight")
plt.show()
"""
sc=plt.scatter(ResultsDF['Modal shift:'],ResultsDF['Modal shift rate (years):'],c=ResultsDF['Emissions'],marker='x',cmap='RdYlBu_r')
plt.xlabel('Reduction in Car Travel Activity in 2050 (%)\nApplied to Highest Ambition Scenario')
plt.ylabel('Rate of CTA (years)')
#plt.ylim(20,28)
plt.xlim(-49,-91)
plt.grid(b=True)
plt.colorbar(sc,pad=0.15,label='Cumulative Tailpipe Emissions\nup to 2050 (MtCO$_{2eq}$)')
#plt.axhline(y=21.7, ls='--', c='red')
plt.savefig('sens_plot2.png', bbox_inches="tight")
plt.show()

x=np.array(ResultsDF['Modal shift:']).reshape(13,21)
y=(np.array(ResultsDF['Modal shift rate (years):'])+2022).reshape(13,21)
z=np.array(ResultsDF['Emissions']).reshape(13,21)
print(x)
print(y)
print(z)

sc=plt.contourf(x,y,z,levels=121,cmap='RdYlBu_r')
cp = plt.contour(x, y, z, colors='black', linestyles='dashed')
plt.clabel(cp, inline=True, fontsize=10,fmt='%1.1f')
plt.xlabel('Reduction in Car Travel Activity (CTA) (%)\nApplied to Highest Ambition Scenario')
plt.ylabel('Year that CTA Reduction is Achieved')
plt.ylim(2025,2042)
plt.xlim(-50,-90)
plt.yticks(np.arange(2025,2042,4))
plt.grid(b=True)
plt.colorbar(sc,pad=0.05,label='Cumulative Tailpipe Emissions\nup to 2050 (MtCO$_{2eq}$)')
#plt.axhline(y=21.7, ls='--', c='red')
plt.savefig('sens_plot2.png', bbox_inches="tight")
plt.show()