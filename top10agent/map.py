#!/usr/bin/python

import sys
import StringIO
import csv
count=0
revenue=0
tip_percentage=0


for line in sys.stdin:

    agent, attributes=line.strip().split('\t')
    count, revenue, tip_percentage = attributes.strip().split(' ')
    count=int(count)
    revenue=float(revenue)
    tip_percentage=float(tip_percentage[:-1])


    print "%s\t%.2f" % (agent,tip_percentage)
    count=0
    revenue=0
    tip_percentage=0


