#This file takes the results in "results.csv" and plots them, saving it as plot.png
#Must be run in visualsearch directory

#Just run "python plot_visualsearch.py" in terminal and you should get a figure automatically generated (with a few warnings printed)

#Last updated December 5, 2016, by William H Thompson

import pandas as pd
import matplotlib.pyplot as plt

#load results
results=pd.read_csv('./results.csv')
results=results[['Tpresent','featuretypes','featureN','rt']]

#create and plot new figure
fig,ax = plt.subplots(1)

#Sort the results. (This is not the best way to do it, but fine for now)
popout_present=results.where(results.Tpresent==1).where(results.featuretypes==1).dropna().sort('featureN').groupby('featureN').mean()
popout_absent=results.where(results.Tpresent==0).where(results.featuretypes==1).dropna().sort('featureN').groupby('featureN').mean()
search_present=results.where(results.Tpresent==1).where(results.featuretypes==3).dropna().sort('featureN').groupby('featureN').mean()
search_absent=results.where(results.Tpresent==0).where(results.featuretypes==3).dropna().sort('featureN').groupby('featureN').mean()

#Plot the results. Change color and linestyle if wanted.
pp=ax.plot(popout_present.index.values,popout_present.rt,color='red')
pa=ax.plot(popout_absent.index.values,popout_absent.rt,color='red',linestyle='--')
sp=ax.plot(search_present.index.values,search_present.rt,color='blue')
sa=ax.plot(search_absent.index.values,search_absent.rt,color='blue',linestyle='--')

#Change labels x and y axis (if wanted)
ax.set_xlabel('Number of items')
ax.set_ylabel('Reaction Time (ms)')

#Change the x and y axis limits (if wanted)
ax.set_ylim(0,5000)
ax.set_xlim(0,60)

#Change figure legend (if wanted)
ax.legend((pp[0],pa[0],sp[0],sa[0]),('Pop Out (T present)','1 distractor (T absent)', '3 distractors (T present)', '3 distractors (T absent)'))

#Save figure.
fig.savefig('./plot.png')
