Startup Files
=====================

This is inspired by all the really awesome [dotfile](https://github.com/search?o=desc&q=dotfiles&ref=simplesearch&s=stars&type=Repositories&utf8=%E2%9C%93) repos available. We need an ecosystem like this for Python. 

### Introduction

IPython has a feature that allows you to run scripts *before* the console starts. From IPython docs:

> This is the IPython startup directory

> .py and .ipy files in this directory will be run *prior* to any code or files specified
 via the exec_lines or exec_files configurables whenever you load this profile.

> Files will be run in lexicographical order, so you can control the execution order of files
with a prefix, e.g.::

>    00-first.py
    50-middle.py
    99-last.ipy

This repo contains my IPython startup files that I've found to be timesaving for my workflow.

### How it works

#### First, who is this for?

My startup scripts are focused on data analysis and prototyping enviroments, as this is my primary purpose for using Python and IPython. I have lots of examples in the `startup` folder that can be used as ag starting place for other IPython workflows. 

There is a `requirements.txt` file because some of my imports are external libraries.

#### Installation

First, clone the repo:

```
git clone https://github.com/CamDavidsonPilon/StartupFiles.git
```

#### Create Symlinks

The contents in `startup` should be added to `~/.ipython/<your_profile>/startup`. One method to do this is to create a symlink between `~/.ipython/<profile>/startup` and the `startup` folder in this repo. The script `build_symlink` will do just that:

```
./bin/build_symlink
```

will replace the `default` profile's `startup` with symlinks to the local repo. Alternatively, you can run

```
./bin/build_symlink --profile <profile>
```
to use an different profile to symlink too. 


#### Building your own

Included is a script, `./bin/ipython_analysis`, to query your IPython sqlite database. Yes, IPython stores all your commands in a sqlite database. This script will return suggestions for you to add to your startup scripts. 

![ipython](http://i.imgur.com/g1ao9yW.gif)

-------

### New %Magic Commands Included in this Repo

#### %pyplot
Get the best pieces of matplotlib, plus some extras. 

![pyplotgif](http://i.imgur.com/vMWnnmx.gif)

-------

#### %pase, %past, %pate
Are all alias to `%paste`, my most common IPython command and the one I mess up the most. 

![paste_gif](http://i.imgur.com/6dK9Q3R.gif)

-------

#### %lifelines and %stats
The former for development work on *lifelines*, the latter for general statistical work. I might add sklearn stuff here.

![statsgif](http://i.imgur.com/i4Zxcf3.gif)



