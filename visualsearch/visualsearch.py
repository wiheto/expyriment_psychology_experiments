# This code runs a visual search Experiment
# Must be run in visualsearch directory

# The stimuli shown are images found in ./stim/images
# an .svg for editting these stimuli can be found in stim/raw.svg (and editted in inkscape)
# a csv that controls the path names of the stimuli is found in vs.csv.

# Last edit: December 5, 2016, William H Thompson

#Import what is needed (don't touch this)
import expyriment as epy
import pandas as pd
import matplotlib.pyplot as plt

#SETUP EXPERIMENT (don't touch this)
exp = epy.design.Experiment(name="Visual Search")
epy.control.initialize(exp)

# EXPERIMENT PARAMETERS (CAN BE MODIFIED)
repeat_each_stimuli = 2 # each stimuli in ./stim/images will be shown 2 times (if 2).
position_stimuli_xaxis = -1000 # to move images left/right.(this is currently dependent on screen resolution but will be improved)
position_stimuli_yaxis = 0 # to move images up/down (this is currently dependent on screen resolution but will be improved)
# response_keys defines which buttons the subject can press.
# http://docs.expyriment.org/expyriment.misc.constants.html has a list of keys.
# Note also the default_values (these should correpsond to the values in response_key in vs.csv)
response_keys = [epy.misc.constants.K_LEFT, epy.misc.constants.K_RIGHT] # First button is left (276), second button is right (275).
# Define response key for enter (don't thouch this)
response_enter = [epy.misc.constants.K_RETURN]
#Get premade RSVP stimuli. Should be of rows = trials, columns = stimuli. second to last column = lags of stimuli. last column = 1 or 2 stimuli present.
#Don't change this unless you make a new csv file
stim = pd.read_csv('./stim/vs.csv')
#text on instruction page
instructionText = 'Visual Search: Identify whether there is a green T. \n Press RIGHT ARROW if there is a green T. \n LEFT ARROW if there is no green T. Be as quick and accurate as you can. \n Press ENTER to begin.'

# GLOBAL PARAMETERS (sholdn't need to touch, but possible)
epy.control.defaults.window_mode = False #change to true, if window mode wanted
epy.control.defaults.initialize_delay = 5
epy.control.defaults.initialize_delay = False
epy.control.defaults.window_size = (1920,1060) # Change screen resolution if in window mode and want bigger/smaller.


# DEFINE THE TRIALS (Don't touch this)
block = epy.design.Block(name='block')
for n in range(0,stim.shape[0]):
    trial = epy.design.Trial()
    #NOTE HOWEVER, here the images are called "[features]_[correct]_[diff_features].png" where each of the [...] corresponds to a column in vs.csv and this is the name of each image. Features: how many stimuli on the screen; correct: TargetPresent or Absent. diff_features: how many different types of features.
    s = epy.stimuli.Picture('./stim/images/' + str(stim.iloc[n].features) + '_' + str(stim.iloc[n].correct) + '_' + str(stim.iloc[n].diff_features) + '.png',position=(position_stimuli_xaxis,position_stimuli_yaxis))
    s.preload()
    trial.add_stimulus(s)
    trial.set_factor('response', int(stim.iloc[n].response_key))
    trial.set_factor('featuren', int(stim.iloc[n].features))
    trial.set_factor('featuretypes', int(stim.iloc[n].diff_features))
    trial.set_factor('answer', int(stim.iloc[n].correct))
    block.add_trial(trial, copies=repeat_each_stimuli)
exp.add_block(block)
block.shuffle_trials()
fixcross=epy.stimuli.FixCross()


# START THE EXPERIMENT
epy.control.initialize(exp)
fixcross.preload()
epy.control.start()

intro = epy.stimuli.TextScreen('Instructions',instructionText)
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
    #Time fixation cross is on screen
    exp.clock.wait(1000)

    block.trials[i].stimuli[0].present()
    button,rt = exp.keyboard.wait(keys=response_keys)
    # Checks if trial was correct
    if block.trials[i].factor_dict.get('response')==button:
        #Add to result lists
        feedback = 'Correct'
        res_answer.append(block.trials[i].factor_dict.get('answer'))
        res_rt.append(rt)
        res_featuretypes.append(block.trials[i].factor_dict.get('featuretypes'))
        res_featuren.append(block.trials[i].factor_dict.get('featuren'))
    else:
        #If incorrect, the trial gets added on att the end
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
    #Time feedback is on screen
    exp.clock.wait(1500)
    i+=1

#load previous results
previous_results = pd.read_csv('./results.csv')
# Collect experiments results
results=pd.DataFrame(data={'featureN': res_featuren,'rt': res_rt,'featuretypes': res_featuretypes,'Tpresent': res_answer})
# merge results
results_merge = pd.concat([previous_results,results])
results_merge.reindex()
# Save new compbined results
results_merge.to_csv('./results.csv')


epy.control.end()
