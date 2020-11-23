# Basic data set statistic and normality testing

This project is a continuation of previous work in creating a package to calculate normality for a user defined random integer dataset.

To run this package follow the next steps:

1) Clone this repository to your local machine using by:

~~~
]$ cd ~                                                           # Change to your home directory
]$ mkdir github_repos                                             # Make a directory to store this repo
]$ git clone https://github.com/madmolecularman/basic_stats.git   # Clone repo (This should be copied from the code dropdown)
]$ cd [repository_name]                                           # Change into the directory you created.
~~~

2) Open up a python specific command line and navigate to the directory containing the folder


3) Run the setup script, we call the following from the command line

    python setup.py install
    
3) Import the pacakge and run the help function to see what it does

    import norm_testing
    
    help(norm_testing)
    
4) Run the script

    norm_testing.summary_stats(25)
    
5) View results in command line and open figure in normality_testing.png

If you have any questions put in an issue post within the page.

