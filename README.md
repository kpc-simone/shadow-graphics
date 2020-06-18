# Shadow Graphics

Python scripts and source code for simulating aerial threats.

![shadow graphics demo](demo/demo.gif =250x)

## Installation
* Install python with the following packages:
 * [numpy 1.16.2] (https://numpy.org/install/)
 * [pywin32 223] (https://pypi.org/project/pywin32/)
* Download and extract this repository locally.
* Download a screen recorder and video editing software. 
 * Such as Windows Game Recorder (Windows 10 and up).

## Usage
`example1.py`: 

Generates a new window wherein a series of 10 identical visual looming stimuli for rodent behavioral studies appear in succession upon mouseclick.

Each stimulus in the series is 8 seconds long. 
Each stimulus consists of a disk that appears small and is stable for three seconds, undergoes
expansion for 2 seconds, and is stable at its largest for 3 seconds before disappearing.

`example2.py`: 

Generates a series of 11 visual looming stimuli with same the same timing profile as `example1.py`, however the nature of expansion varies between trials and may be one of:

* linear expansion, 
* exponential expansion,
* sigmoidal expanion,
* shrinking,
* no expansion (stable for 8 seconds)

To generate videos, first run the script. Then, start your screen recorder, and click on the new graphics window to start the stimulus presentation. Save the screen recording, and use movie editing software to trim unwanted frames. 

These scripts were tested on a Dell 1908FP monitor. 
_The size of the stimulus, as well as the default background color may need to be changed depending on your specific display and experimental setup._**