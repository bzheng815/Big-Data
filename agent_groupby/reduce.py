#!/usr/bin/python

import sys

current_key = None
current_count= 0
current_total=0
current_tip=0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    key, attributes = line.strip().split('\t')
    count, f2,f3,f5,f6,tip, total =attributes.strip().split(' ')
    try:
        count = int(count)
        total=float(total)
        tip=float(tip)
    except ValueError:
        continue

    if key == current_key:
        current_count=current_count+count
        current_total=current_total+total
        current_tip=current_tip+tip
    else:
        if current_key:
            if current_total!=0:
                # output goes to STDOUT (stream data that the program writes)
                print "%s\t%d %.2f %.2f%%" %( current_key,current_count, current_total, current_tip/current_total*100)
            else:
                print "%s\t%d 0 0" %(current_key, current_count)
        current_key = key
        current_count=count
        current_total=total
        current_tip=tip
if current_total!=0:
    # output goes to STDOUT (stream data that the program writes)
    print "%s\t%d %.2f %.2f%%" %( current_key,current_count, current_total, current_tip/current_total*100)
else:
    print "%s\t%d 0 0" % (current_key, current_count)

