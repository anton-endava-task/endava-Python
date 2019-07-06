#!/usr/bin/env python3.6

import time
import requests
import os

# Starting StopWatch
start_time = time.localtime()

counter = 0                             # This couner is used for file name creation
index = open('weblist')                 # Open weblist for reading

for line in index:                      # Reading website names from the file
    web = line.rstrip() 
    response = requests.get(web)        # Downloading web content
    name = 'index' + str(counter)       # Creating a name
    counter += 1
    index_content = open(name,'w+b')          # Create a file with that name opened for writing content
    index_content.write(response.content)     # Writing the content to the file
    index_content.close()
    index_content = open(name)                # Open the same file for reading

    match = 0
    name += '_count'                    # Prepaing a name for the file that will store a count of future match found 
    temp_counter = open(name,'w')       # Create a file with that name opened for writing

# Start searching the lines of the file for matches
    for line in index_content:
        if 'href=' in line:
            match += 1                  # Counting lines tith maches found
    temp_counter.write(str(match))      # Write the number of matches found in the file
    temp_counter.close()

index.close()

# Start searching for the last 10 modified files in current folder
for i in range(0,10):
   newer_file = max([f for f in os.scandir(".")], key=lambda x: x.stat().st_mtime).name      # Newer file found
   os.remove(newer_file)                                                                     # Removed

# Stop StopWatch   
stop_time = time.localtime()
execution_time = time.mktime(stop_time) - time.mktime(start_time)                           # Calculating execution time

print(f"Total time: {execution_time} seconds")


