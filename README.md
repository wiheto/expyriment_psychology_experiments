# expyriment_psychology_experiments
A couple of experiments using expyriment. 

These are more for demonstration purposes than research purposes and were created for teaching. 

The experiments here take the results from the input and plot the results as a figure results.png. If there is already saved data, it take the average data of the previous subject(s), averages it, and plots against the new subject.  

### Requires: 

- Expyriment (http://www.expyriment.org/ - python3 version: https://github.com/expyriment/expyriment/tree/python3)
- Python3.x (2.7 should be fine, see below) 
- Pandas 
- Matplotlib
- numpy

Recommend to install python via anaconda (https://www.continuum.io/downloads - then you get pandas and matplotlib installed as well)

*Note that I have written these in python3 and (at least when I installed expyriment, the python3 was on a developers branch. So this may get tricky. But it all __should__ work for python2 and let me know if something doesn't work - also if it works!).* 


### How to use: 

Step 1: 
Download/clone the files here. (If you don't use git, the zip files is [here](https://github.com/wiheto/expyriment_psychology_experiments/archive/master.zip))

Step 2: 
Make sure you download everything in "requires" above

Step 3: 
Navigate to specific experiment directory (e.g. visualsearch). 

Step 4:
To run, in terminal (OSX/Linux) type: `python visualsearch.py` - or whatever the experiment is called (e.g. attentionalblink)

(For windows and graphically in OSX/Linux run visualsearch.py as program (I think))

### I want to edit these experiments, what do I do? 

Open up visualsearch.py or attentionalblink.py and edit the files there. There are some comments, but it could be better. 

I will comment the cod  a bite more with time and add more structure (a little chaotic at the moment). If you get stuck, let me know. 

More experiments may be added with time. If something is confusing, let me know via the issues here. 

### Why are these just for demonstration purposes? 

I have not optimized the timings of the code and some testing needs to be done to make sure that millieseconds are not lost here and there. This was not a priotiy for me at the moment (as this is to show conceptual what these experiments are). But if for serious research use, some work on timings should be done (and I may get round to it at sometime).  

