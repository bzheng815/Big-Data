#!/usr/bin/python

import sys

current_key = None
current_trip= []
current_fare=[]
current_attr=''


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    key, attributes = line.strip('\n').split('\t')

    if key == current_key:

	if attributes[0] not in '0123456789':
            current_fare.append(attributes)
	else:
	    current_trip.append(attributes)
    else:
	
        if current_key:
            # output goes to STDOUT (stream data that the program writes)
	    if len(current_trip)!=0:
                if len(current_fare)!=0:
                    for i in range(len(current_trip)):
            	        for j in range(len(current_fare)):
                	    print "%s\t%s,%s" % (current_key, current_trip[i], current_fare[j])
 
        current_key = key
	if attributes[0] not in '0123456789':
	    current_trip=[]
	    current_fare=[attributes]
        else:
	    current_fare=[]
	    current_trip=[attributes] 
	

# output goes to STDOUT (stream data that the program writes)
if len(current_trip)!=0:
    if len(current_fare)!=0:
        for i in range(len(current_trip)):
            for j in range(len(current_fare)):
                print "%s\t%s,%s" % (current_key, current_trip[i], current_fare[j])

