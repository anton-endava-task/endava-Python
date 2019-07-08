#!/usr/bin/env python3.6

import time
import requests
import os

start_time = time.time()                             # Starting StopWatch
counter = 0                                          
with open('weblist') as webs:                  
    for web in webs:                                 # Reading website names from the file
        response = requests.get(web.rstrip())        
        name = 'index' + str(counter)               
        counter += 1
        with open(name,'w+b') as web_content:        # Create a file storing web content
            web_content.write(response.content)     
        with open(name) as web_content:              
            match = 0
            name += '_count'                         
            with open(name,'w') as match_counter:    
                for line in web_content:             
                    if 'href=' in line:
                        match += 1                  
                match_counter.write(str(match))      # Create a file storing the number of matches found

for i in range(0,10):                                # Remove newer 10 files
   newer_file = max([f for f in os.scandir()], 
           key=lambda x: x.stat().st_mtime).name     
   os.remove(newer_file)                             
                                                      # Printing execution time
print('Execution time: {:.2f} seconds'.format((time.time() - start_time)))
