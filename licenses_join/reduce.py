#!/usr/bin/python

import sys

current_key = None
current_attr=[]
wait=[]

# input comes from STDIN (stream data taht goes to the program)
for line in sys.stdin:
    key, attributes =line.strip().split('\t')
    if key == current_key:
	if '/' in attributes:
	    if len(wait)==0:
		wait=[attributes]
	    else:
		wait.append(attributes)
	else:
	    if len(current_attr)==0:
		current_attr=[attributes]
	    else:
	        current_attr.append(attributes)
    else:
	if current_key:
	    # output goes to STDOUT (stream data that the program writes)
	    if len(current_attr)!=0:
		if len(wait)!=0:
	            for i in range(len(current_attr)):
		        for j in range((len(wait))):
	    	            print "%s\t%s\t%s" % (current_key,current_attr[i],wait[j])
	current_key = key
	if '/' in attributes:
	    wait=[attributes]
	    current_attr=[]
	else:
	    current_attr=[attributes]
	    wait=[]
# output goes to STDOUT (stream data that the program writes)
if len(current_attr)!=0:
    if len(wait)!=0:
        for i in range(len(current_attr)):
            for j in range((len(wait))):
                print "%s\t%s\t%s" % (current_key,current_attr[i],wait[j])
