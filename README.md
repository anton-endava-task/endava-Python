---


---

<h1 id="endava-junior-devops-challenge">Endava Junior Devops Challenge</h1>
<h2 id="task-description">Task description</h2>
<ol>
<li>Create public git repository</li>
<li>Chose your favorite scripting language and create script that will do the following</li>
</ol>
<ul>
<li>Save the content of 10 random websites index pages to 10 files</li>
<li>Count number of matching lines with the string “href=” in each of the 10 files</li>
<li>Save result of “href=” matches in new 10 files, using logical naming convention</li>
<li>Delete the newly created 10 files with results</li>
<li>Measure execution time</li>
</ul>
<ol start="3">
<li>Commit the code in the repository</li>
<li>Send us link to it!</li>
</ol>
<p>Dont forget to document it properly!</p>
<h1 id="slution">Slution</h1>
<p>In this repository you can see two files:</p>
<ul>
<li>a text file <strong>weblist</strong></li>
<li>a python script <strong><a href="http://task.py">task.py</a></strong></li>
</ul>
<p><strong>weblist</strong> is a file that contains a list of 10 random websites</p>
<pre><code>https://linuxacademy.com
https://docs.ansible.com
https://github.com
https://bitbucket.org
https://lucidchart.com
https://jenkins.io
https://aws.amazon.com
https://kubernetes.io
https://docker.com
https://apache.org
</code></pre>
<p><strong><a href="http://task.py">task.py</a></strong> is the script that complete point 2 from the <strong>Endava Junior Devops Challenge</strong></p>
<pre><code>#!/usr/bin/env python3.6

import time
import requests
import os

start_time = time.time()                            
counter = 0                                          
with open('weblist') as webs:                   
    for web in webs:                                 
        response = requests.get(web.rstrip())        
        name = 'index' + str(counter)                
        counter += 1
        with open(name,'w+b') as web_content:       
            web_content.write(response.content)      
        with open(name) as web_content:             
            match = 0
            name += '_count'                         
            with open(name,'w') as match_counter:    
                for line in web_content:             
                    if 'href=' in line:
                        match += 1                   
                match_counter.write(str(match))      

for i in range(0,10):                               
   newer_file = max([f for f in os.scandir()], 
           key=lambda x: x.stat().st_mtime).name    
   os.remove(newer_file)                            

print("Execution time: %s seconds" % (time.time() - start_time))
</code></pre>
<h3 id="what-we-need-to-do-to-run-the-scrip-correctly">What we need to do to run the scrip correctly?</h3>
<ul>
<li>We need root privilege</li>
<li>We need <strong><a href="http://task.py">task.py</a></strong> and <strong>weblist</strong> in the same folder</li>
<li><code>export PATH="$PATH":"$PWD"</code> If your current directory is not a part of $PATH</li>
</ul>
<h3 id="what-we-expect-as-output">What we expect as output?</h3>
<p>You can’t watch web content downloading:<br>
After the script finish the job you can see measured execution time<br>
<img src="https://lh3.googleusercontent.com/JYTi4-3gBgfC7846k1wZiiUqJJK9fgq48D26ATaWpaXO1pNkB22YqxfJ7S9k0WmxsSgquvRdib32" alt="enter image description here"><br>
If you list the current directory you can see 10 files appeared.</p>
<pre><code>  ls -al
</code></pre>
<p><img src="https://lh3.googleusercontent.com/bCNrl1CM8F1RSLJzlHx1FIEpVgQWJtdM7KF8Fkd6QhGaqgLk4XR0p7l6M1r70O8EHt6aSF_ox4RJ" alt="enter image description here"></p>
<p>If you skip the part of the script that delete newer 10 files created,</p>
<pre><code>for i in range(0,10):                               
   newer_file = max([f for f in os.scandir()], 
           key=lambda x: x.stat().st_mtime).name    
   os.remove(newer_file)
</code></pre>
<p>you can see all 10 <strong>“index”</strong> and 10 <strong>“index_count”</strong> files.</p>
<p><strong>index</strong> files store webpage index.html content<br>
<strong>index_count</strong> files store the <strong>count</strong> of lines included the text <strong>"href="</strong></p>
<p><img src="https://lh3.googleusercontent.com/2fw5XQsgVH6afTNMde1yhTLApH9N0d90CNbHzBQbaIHX6OFpltIvBOXb9Im0ZkrgXjgepOa3Fa_w" alt="enter image description here"></p>

