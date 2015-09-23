#!/usr/bin/python

import sys
total=0

for line in sys.stdin:
    agent, attributes=line.strip().split('\t')
    total=total+float(attributes)
print total
