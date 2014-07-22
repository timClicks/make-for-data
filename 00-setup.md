Lesson Setup
============

As we will be using `make` as a tool for creating data pipelines, we should start 
by creating some data input files.

We will be generating CSV files from statistics on your computer. The end result 
will be that everyone in the room will have a slightly different set of statistics.


### Step 1: Download Dependencies


To begin, open the shell and install the `psutil` module. It is a cross-portable
way of gathering system statistics.

    pip install psutil

### Step 2: Generate Statistics

You are now able to run `generate_stats.py`. That script will create a CSV file &ndash;
named `systemstats.csv` by default &ndash; with a report on CPU usage, available memory,
and network traffic.

    python generate_stats.py --duration 120

All going well, you will see a stream of numbers beginning to scroll across your screen.
This should give us nice time series data that `make` will be able to process for us. 

