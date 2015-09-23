#!/usr/bin/python
import sys
import datetime
current_key=None
k=0

# input comes from STDIN
for line in sys.stdin:
    key,attributes=line.strip('\n').split('\t')
    if key==current_key:
        k=k+1
        if k==3:
    
            key_print=key[:4]+'-'+key[4:6]+'-'+key[6:8]
            weekdate=datetime.datetime(int(key[:4]),int(key[4:6]),int(key[6:8]))
            y,w,d=datetime.date.isocalendar(weekdate)
            print ('%s\t%s') % (w,attributes)
            #print ('%s\t%s') % (key_print,attributes)
            current_key=key
    else:
        k=1
        current_key=key
        

