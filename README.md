# expyriment_psychology_experiments
A couple of experiments using expyriment.

These are more for demonstration purposes than research purposes and were created for teaching.


### What do these results do.

There are versions of the visual search and attentional blink paradigms. Results are automatically saved in results.csv and can be plotted automatically to plot.png.

Visual search is commented and easiest to use. Attentional blink will be cleaned up soon.

### How hard is it to get these to work on my computer?

It can be a little tricky to get expyriment to work on your computer. However, once expyriment is set up, it becomes considerably easy to run the different experiments.

__Requires:__

- python3.5 (or greater)
- pandas
- matplotlib
- numpy
- pygame
- PyOpenGl
- Expyriment 

I recommend to install python via anaconda (https://www.continuum.io/downloads then you get pandas, numpy and matplotlib, pyOpenGL installed automatically. pygame can be installed by pip or conda. In the terminal write `pip install expyriment`.

### How to use:

Step 1:
Download/clone the files here. (If you don't use git, the zip files is [here](https://github.com/wiheto/expyriment_psychology_experiments/archive/master.zip))

Step 2:
Make sure you download everything in "requires" above

Step 3:
Navigate to specific experiment directory (e.g. visualsearch). __This is important!__

Step 4:
To run, in terminal (OSX/Linux) type: `python visualsearch.py` - or whatever the experiment is called (e.g. attentionalblink). (For windows and graphically in OSX/Linux run visualsearch.py as program (I think, never used windows))

Step 5:
To plot the results, in terminal (OSX/Linux) type: `python plot_visualsearch.py` and it creates a plot `plot.png` automatically.


### I want to edit these experiments, what do I do?

Open up visualsearch.py or attentionalblink.py and edit the files there. If something is confusing, let me know via the issues here.

More experiments may be added with time.

### Why are these just for demonstration purposes?

I have not optimized the timings of the code and some testing needs to be done to make sure that milliseconds are not lost here and there. This was not a priority for me at the moment (as this is to show conceptual what these experiments are). But if for serious research use, some work on timings should be done (and I may get round to it at sometime).  
