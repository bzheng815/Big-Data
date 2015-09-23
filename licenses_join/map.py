#!/usr/bin/python

import sys
k=1

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    if len(line)<2:
	continue
    if line[:9]=='medallion':
	title= line.strip().split(',')
    else:
	if line[32]==' ':
	    key, attributes =line.strip().split('\t')
	    medallion, lisence, type, date, time=key.split(' ')
	    print "%s\t%s,%s,%s %s,%s" % (medallion,lisence,type,date,time,attributes)
	    
	elif line[32]==',':
            attributes=''
	    line=line.strip().split(',')
	    for word in line:
		if k==1:
		    medallion=word
		    k=k+1
		elif k==2:
		    attributes=word
		    k=k+1
		else:
		    attributes=attributes+','+word
		    k=k+1
	    print "%s\t%s" % (medallion,attributes)
	    k=1

