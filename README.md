# Using Markov Analysis to Write Movie Scripts
This is the base repository for my third mini project on text mining. For this mini project, I used the Internet Movie Script Database (IMSDb) and Markov analysis to generate a movie script and study the accuracies of a simple Markov model. To generate a 500-word movie script, run the following line in terminal: $ python3 main.py.

## Prerequisites
To use this program, you must have the following packages installed: Requests and Beautiful Soup.

## Harvesting scripts from IMSDb
The find_scripts.py script will harvest all scripts from IMSDb under a particular movie genre. This genre is specified on line 86 of the script, where the function save_all_scripts() is called. For now, the script is harvesting all of IMSDb's Romance movies scripts.

## Manually parsing through Scripts
I'll be honest, the find_scripts.py is not perfect. Due to inconsistencies in formatting across the movie scripts posted on IMSDb, it was difficult to create a program that could perfectly capture each script. For this reason, I went through and manually parsed through each script to ensure that certain markers existed, such as an "EXT." and a "THE END." For your convenience, 50 of those scripts are already included in the scripts folder. Unless you would like to harvest scripts from another genre, I recommend that you use the scripts in the scripts folder rather than running  find_scripts.py.

## Generating a script using Markov Analysis
The main.py script will generate a movie script using Markov analysis. The number of words it generates is specified on line 81 of the script, where the function markov_analysis() is called. For now, the script is generated 500-word movie scripts. 
