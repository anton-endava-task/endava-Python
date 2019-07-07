#!/usr/bin/env python3.6

import time
import requests
import os

start_time = time.time()                             # Starting StopWatch
counter = 0                                          # This couner is used for file name creation
with open('weblist','rt') as webs:                   # Open weblist for reading
    for web in webs:                                 # Reading website names from the file
        response = requests.get(web.rstrip())        # Downloading web content
        name = 'index' + str(counter)                # Creating a name
        counter += 1
        with open(name,'w+b') as web_content:        # Create a file with that name opened for writing content
            web_content.write(response.content)      # Writing the content to the file
        with open(name) as web_content:              # Open the same file for reading
            match = 0
            name += '_count'                         # Prepaing a name for the file that will store a count of future match found 
            with open(name,'w') as match_counter:    # Create a file with that name opened for writing
                for line in web_content:             # Start searching the lines of the file for matches
                    if 'href=' in line:
                        match += 1                   # Counting lines tith maches found
                match_counter.write(str(match))      # Write the number of matches found in the file

for i in range(0,10):                                # Start searching for the last 10 modified files in current folder
   newer_file = max([f for f in os.scandir(".")], 
           key=lambda x: x.stat().st_mtime).name     # Newer file found
   os.remove(newer_file)                             # Removed

print("Execution time: %s seconds" % (time.time() - start_time))
