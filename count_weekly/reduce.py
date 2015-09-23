#!/usr/bin/python

import sys
import datetime

current_key = None
f2_sum= 0
f3_sum=0
f5_sum=0
f6_sum=0
sum = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    key, f2,f3,f5,f6 = line.strip().split('\t')
    try:
        f2 = float(f2)
        f3= float(f3)
        f5= float(f5)
        f6=float(f6)
        year=int(key[:4])
        month=int(key[5:7])
        day=int(key[8:])
        key=datetime.datetime(year,month,day)
        y,key,d=datetime.date.isocalendar(key)
    except ValueError:
        continue

    if key == current_key:
        f2_sum=f2_sum+f2
        f3_sum=f3_sum+f3
        f5_sum=f5_sum+f5
        f6_sum=f6_sum+f6
        sum = sum + f2 +f3+f5+f6
    else:
        if current_key:
            # output goes to STDOUT (stream data that the program writes)
            if sum!=0:
                print "%s\t%.2f %.2f %.2f %.2f %.2f %.2f%%" %( current_key,f2_sum,f3_sum,f5_sum,f6_sum, sum, float(f5_sum)/sum*100)
            else:
                print "%s\t%.2f %.2f %.2f %.2f 0 0" %( current_key,f2_sum,f3_sum,f5_sum,f6_sum)
        current_key = key
        f2_sum=f2
        f3_sum=f3
        f5_sum=f5
        f6_sum=f6
        sum = f2+f3+f5+f6

# output goes to STDOUT (stream data that the program writes)
if sum!=0:                        
    print "%s\t%.2f %.2f %.2f %.2f %.2f %.2f%%" %( current_key,f2_sum,f3_sum,f5_sum,f6_sum, sum, float(f5_sum)/sum*100)
else:                             
    print "%s\t%.2f %.2f %.2f %.2f 0 0" %( current_key,f2_sum,f3_sum,f5_sum,f6_sum)

