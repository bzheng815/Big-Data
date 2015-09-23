#!/usr/bin/python

import sys
import StringIO
import csv
fare_amount=0
tip_amount=0
count=0


for line in sys.stdin:

    medallion, trip_attr, vehicle_attr=line.strip().split('\t')
    if trip_attr==['']:
        fare_amount=0
        tip_amount=0
    else:
        t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,f1,f2,f3,f4,f5,f6,f7=trip_attr.strip().split(',')

        f2=float(f2)
        f3=float(f3)
        f5=float(f5)
        f6=float(f6)
        fare_amount=fare_amount+f2+f3+f5+f6
        tip_amount=tip_amount+f5
        count=count+1

    csv_file = StringIO.StringIO(vehicle_attr)
    csv_reader = csv.reader(csv_file)
    for record in csv_reader:
        key=record[9]
    if f1=='CRD':
        print "%s\t%d %.2f %.2f %.2f %.2f %.2f %.2f" % (key,count,f2,f3,f5,f6,tip_amount,fare_amount)
    fare_amount=0
    tip_amount=0
    count=0


