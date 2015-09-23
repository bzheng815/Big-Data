#!/usr/bin/python

from __future__ import print_function
import sys
import csv

k=0
m=0

# input comes from STDIN
with open('weatherData.csv','rU') as csvfile:
    data = csv.reader(csvfile,delimiter=',',dialect=csv.excel_tab)
    for line in data:
        k=0
        if m==0:
            m=m+1
            continue
        else:
           # line = line.strip().split(',')
            for word in line:
                if k==5:
                    print (word,end='\t')
                if k==6:
                    print (word,end=' ')
                if k==11:
                    print (word,end=' ')
                if k==16:
                    print (word,end=' ')
                if k==21:
                    print (word,end=' ')
                if k==26:
                    print (word,end=' ')
                if k==31:
                    print (word,end=' ')
                if k==36:
                    print (word,end=' ')
                if k==41:
                    print (word,end=' ')
                if k==46:
                    print (word,end=' ')
                if k==51:
                    print (word,end='\n')
                k=k+1

