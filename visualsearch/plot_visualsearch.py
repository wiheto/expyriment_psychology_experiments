import pandas as pd
import matplotlib.pyplot as plt


# #create and plot new figurer
fig,ax = plt.subplots(1)

#Sort the results. This is not the best way to do it
popout_present=results.where(results.Tpresent==1).where(results.featuretypes==1).dropna().sort('featureN')
popout_absent=results.where(results.Tpresent==0).where(results.featuretypes==1).dropna().sort('featureN')
search_present=results.where(results.Tpresent==1).where(results.featuretypes==3).dropna().sort('featureN')
search_absent=results.where(results.Tpresent==0).where(results.featuretypes==3).dropna().sort('featureN')

pp=ax.plot(popout_present.featureN,popout_present.rt,color='red')
pa=ax.plot(popout_absent.featureN,popout_absent.rt,color='red',linestyle='--')
sp=ax.plot(search_present.featureN,search_present.rt,color='blue')
sa=ax.plot(search_absent.featureN,search_absent.rt,color='blue',linestyle='--')

ax.set_xlabel('Number of items')
ax.set_ylabel('Reaction Time (ms)')
ax.set_ylim(0,5000)
ax.set_xlim(0,60)

ax.legend((pp[0],pa[0],sp[0],sa[0]),('Pop Out (T present)','1 distractor (T absent)', '3 distractors (T present)', '3 distractors (T absent)'))
fig.savefig('./plot.png')



# #create and plot new figurer
fig,ax = plt.subplots(1)

#Sort the results. This is not the best way to do it
popout_present=results.where(results.Tpresent==1).where(results.featuretypes==1).dropna().sort('featureN').groupby('featureN').mean()
popout_absent=results.where(results.Tpresent==0).where(results.featuretypes==1).dropna().sort('featureN').groupby('featureN').mean()
search_present=results.where(results.Tpresent==1).where(results.featuretypes==3).dropna().sort('featureN').groupby('featureN').mean()
search_absent=results.where(results.Tpresent==0).where(results.featuretypes==3).dropna().sort('featureN').groupby('featureN').mean()

pp=ax.plot(popout_present.index.values,popout_present.rt,color='red')
pa=ax.plot(popout_absent.index.values,popout_absent.rt,color='red',linestyle='--')
sp=ax.plot(search_present.index.values,search_present.rt,color='blue')
sa=ax.plot(search_absent.index.values,search_absent.rt,color='blue',linestyle='--')

ax.set_xlabel('Number of items')
ax.set_ylabel('Reaction Time (ms)')
ax.set_ylim(0,5000)
ax.set_xlim(0,60)

ax.legend((pp[0],pa[0],sp[0],sa[0]),('Pop Out (T present)','1 distractor (T absent)', '3 distractors (T present)', '3 distractors (T absent)'))
fig.savefig('./plot_group.png')
