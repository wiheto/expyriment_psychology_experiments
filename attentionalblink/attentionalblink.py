import expyriment as epy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

exp = epy.design.Experiment(name="Attentional Blink")
stimLength = 90


# Experiment Parameters
response_keys = [epy.misc.constants.K_1, epy.misc.constants.K_2] #First button is 1, second button is 2.
response_enter = [epy.misc.constants.K_RETURN]
# GLobal Parameters
epy.control.defaults.window_mode = True
epy.control.defaults.initialize_delay = 5
epy.control.defaults.initialize_delay = False
epy.control.defaults.window_size = (1920,1060)

#Get premade RSVP stimuli. Should be of rows = trials, columns = stimuli. second to last column = lags of stimuli. last column = 1 or 2 stimuli present.
stim = pd.read_csv('/home/william/projects/experiments/attentional blink/stimuli/rvsp.csv')
wordsPerTrials = stim.shape[1]-2

block = epy.design.Block()
for stimrows in stim.iterrows():
    trial = epy.design.Trial()
    trlLetters = list(stimrows[1][0:wordsPerTrials])
    [trial.set_factor("l" + str(i), n) for i,n in enumerate(trlLetters)]
    trial.set_factor('distance', stimrows[1][-2])
    trial.set_factor('correct', stimrows[1][-1])
    block.add_trial(trial, copies=1)
    exp.add_block(block)
block.shuffle_trials()

fixcross=epy.stimuli.FixCross()


# start the experiment

epy.control.initialize(exp)

resultsCorrect=np.zeros(block.n_trials)
resultsLag=np.zeros(block.n_trials)
fixcross.preload()


epy.control.start()

intro = epy.stimuli.TextScreen('Instructions','Attentional Blink: many stimuli are presented in a row. \n You should try and see if there is a j, k or both in the sequence. \n Report either 1 or 2 after each sequence. \n Press ENTER to begin.')
intro.present()
button,rt = exp.keyboard.wait(keys=response_enter)

for t in range(0,block.n_trials):
    fixcross.present()
    exp.clock.wait(1000)
    for w in range(0,wordsPerTrials):
        digit = block.trials[t].factor_dict.get('l' + str(w))
        target = epy.stimuli.TextLine(text=str(digit), text_size=60)
        target.preload()
        exp.clock.wait(stimLength)
        target.present()
    target = epy.stimuli.TextLine(text='1 or 2?', text_size=60)
    target.present()
    button,rt = exp.keyboard.wait(keys=response_keys)
    if response_keys[block.trials[t].factor_dict.get('correct')-1]==button:
        resultsCorrect[t]=1
    else:
        resultsCorrect[t]=0
    resultsLag[t]=block.trials[t].factor_dict.get('distance')


#load previous results
previous_results = pd.read_csv('./results.csv')

#Collect experiments results
results=pd.DataFrame(data={'correct': resultsCorrect,'T2_distance': resultsLag*stimLength})
results_merge = pd.concat([previous_results,results])
#Save new compbined results
results_merge.to_csv('./results.csv')

epy.control.end()

#create and plot new figurer
fig,ax = plt.subplots(1)
resultsAvg = results.groupby('T2_distance').mean()
previous_resultsAvg = previous_results.groupby('T2_distance').mean()
grupp=ax.plot(resultsAvg.index[1:],100*resultsAvg.correct[1:],color='red')
klass=ax.plot(previous_resultsAvg.index[1:],100*previous_resultsAvg.correct[1:],color='blue')
ax.set_xlabel('T2 Distance (ms)')
ax.set_ylabel('Correct (%)')
ax.set_ylim(0,110)
ax.set_xlim(0,stimLength*5+50) #This might have to be changed if more stimuli are added.
ax.legend((grupp[0],klass[0]),('Grupp','Klass'))
fig.savefig('./plot.png')
