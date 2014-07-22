Let's start with some motivation.

## Why automation

If we have a process for doing something, such as archiving our work, doing analysis or generating figures, we would like that process to be easily repeatable and deterministic.

If we wanted to create a report of the data that we've gathered so far, we could open the CSV in some spreadsheet software and manually ask the software to. We would modify attributes, such as color and the type of graph, by hand. That process is time consuming and error-prone.  

## Why make

We could write a shell script to produce the plots that we are after. Make will be smarter than running the job over all of the input data. It will only process those input files that have been update since it was last run.

Make provides a number of useful tools for reducing the number of keystrokes that we need to enter. 
