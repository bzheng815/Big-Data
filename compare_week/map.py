#!/usr/bin/python

import sys
import datetime


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    key, attributes = line.strip().split('\t')
    
    t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,f1,f2,f3,f4,f5,f6,f7 = attributes.split(',')

    medallion, license,type,key,time = key.strip().split(' ')
    year=int(key[:4])
    month=int(key[5:7])
    day=int(key[8:])
    key=datetime.datetime(year,month,day)
    y,w,d=datetime.date.isocalendar(key)
    if f1=='CRD':
        print "%d\t%s\t%s\t%s\t%s" %( d, f2,f3,f5,f6)
