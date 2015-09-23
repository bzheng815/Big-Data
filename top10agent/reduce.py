#!/usr/bin/python

import sys

current_key = None
current_total=0
total_list=[]
for i in range(59):
    total_list.append([0,''])

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    key, total = line.strip().split('\t')
    try:
        total=float(total)
    except ValueError:
        continue

    if key == current_key:
        current_total=current_total+total
    else:
        if current_key:
            total_list.sort(reverse=True)
	    if current_total>total_list[58][0]:
		total_list[58][0]= current_total
		total_list[58][1]=current_key
        current_key = key
        current_total=total
total_list.sort(reverse=True)
if current_total>total_list[58][0]:
    total_list[9]=[current_total,current_key]

for i in range(59):
    print "%s\t%.2f" % (total_list[i][1],total_list[i][0])


