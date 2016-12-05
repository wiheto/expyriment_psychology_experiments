import expyriment as epy
import pandas as pd
import matplotlib.pyplot as plt

exp = epy.design.Experiment(name="Visual Search")

epy.control.initialize(exp)
# Experiment Parameters
response_keys = [epy.misc.constants.K_LEFT, epy.misc.constants.K_RIGHT] #First button is left (276), second button is right (275).
response_enter = [epy.misc.constants.K_RETURN]
# GLobal Parameters
epy.control.defaults.window_mode = True
epy.control.defaults.initialize_delay = 5
epy.control.defaults.initialize_delay = False
epy.control.defaults.window_size = (1920,1060)

#Get premade RSVP stimuli. Should be of rows = trials, columns = stimuli. second to last column = lags of stimuli. last column = 1 or 2 stimuli present.
stim = pd.read_csv('./stim/vs.csv')
wordsPerTrials = stim.shape[1]-2

block = epy.design.Block(name='block')
for n in range(0,stim.shape[0]):
    trial = epy.design.Trial()
    s = epy.stimuli.Picture('./stim/images/' + str(stim.iloc[n].features) + '_' + str(stim.iloc[n].correct) + '_' + str(stim.iloc[n].diff_features) + '.png',position=(-1000,0)) #Poistion should be made better
    s.preload()
    trial.add_stimulus(s)
    trial.set_factor('response', int(stim.iloc[n].response_key))
    trial.set_factor('featuren', int(stim.iloc[n].features))
    trial.set_factor('featuretypes', int(stim.iloc[n].diff_features))
    trial.set_factor('answer', int(stim.iloc[n].correct))
    block.add_trial(trial, copies=1)
exp.add_block(block)
block.shuffle_trials()

fixcross=epy.stimuli.FixCross()


# start the experiment

epy.control.initialize(exp)
fixcross.preload()


epy.control.start()

intro = epy.stimuli.TextScreen('Instructions','Visual Search: Identify whether there is a green T. \n Press RIGHT ARROW if there is a green T. \n LEFT ARROW if there is no green T. Be as quick and accurate as you can. \n Press ENTER to begin.')
intro.present()
button,rt = exp.keyboard.wait(keys=response_enter)

i=0
res_answer = []
res_rt = []
res_featuretypes = []
res_featuren = []
lim = len(block.trials)
while i < lim:
    fixcross.present()
    exp.clock.wait(1000)

    block.trials[i].stimuli[0].present()
    button,rt = exp.keyboard.wait(keys=response_keys)
    if block.trials[i].factor_dict.get('response')==button:
        feedback = 'Correct'
        res_answer.append(block.trials[i].factor_dict.get('answer'))
        res_rt.append(rt)
        res_featuretypes.append(block.trials[i].factor_dict.get('featuretypes'))
        res_featuren.append(block.trials[i].factor_dict.get('featuren'))
    else:
        trial = epy.design.Trial()
        trial.add_stimulus(block.trials[i].stimuli[0])
        trial.set_factor('response', block.trials[i].factor_dict.get('response'))
        trial.set_factor('featuren', block.trials[i].factor_dict.get('featuren'))
        trial.set_factor('featuretypes', block.trials[i].factor_dict.get('featuretypes'))
        trial.set_factor('answer', block.trials[i].factor_dict.get('answer'))
        block.add_trial(trial, copies=1)
        feedback = 'Incorrect!'
        lim=lim+1
    fb = epy.stimuli.TextLine(feedback,text_size=60)
    fb.present()
    exp.clock.wait(1500)

    i+=1

# #load previous results
previous_results = pd.read_csv('./results.csv')
#
# #Collect experiments results
results=pd.DataFrame(data={'featureN': res_featuren,'rt': res_rt,'featuretypes': res_featuretypes,'Tpresent': res_answer})
results_merge = pd.concat([previous_results,results])
# #Save new compbined results
results_merge.to_csv('./results.csv')


epy.control.end()


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
