#!/usr/bin/python

from __future__ import print_function
import sys

wait=[]
k=1
m=3

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    if len(line)<2:
	continue
    if line[:9]=='medallion':
	title=line.strip().split(',')
    else:
    	line = line.strip().split(',')
    	for word in line:
	    if k<4:
	    	print(word,end=' ')
	    	k=k+1
            # output goes to STDOUT (stream data that the program writes)
	    if k==4:
		k=k+1
		continue
	    if k==5 and len(word)<8:
		m=1
	    elif k==5 and len(word)>8:
		m=0
	    if m==1:
	        if k==7:
            	    print(word,end='\t')
	    	else:
		    wait.append(word)
	    	k =k+1
	        if k==16:
		    for i in range(9):
		        print(wait[i],end=',')
		    print(wait[9],end='\n')
		    wait=[]
		    k=1
		    m=3
	    elif m==0:
		if k==5:
		    print(word,end='\t')
		else:
		    wait.append(word)
                k =k+1
                if k==13:
                    for i in range(6):
                        print(wait[i],end=',')
                    print(wait[6],end='\n')
                    wait=[]
                    k=1
		    m=3



