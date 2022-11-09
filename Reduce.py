#! /usr/bin/python3.8
"""Reduce.py"""
import re
import sys 
import fileinput
from operator import itemgetter

dict_ip_count = {}
abc = set()
for line in sys.stdin:
	line = line.strip()
	print(line)
	#print(line.split('\t'))
	hour,ip,num = line.split('\t')
	abc.add(hour)

	try:
		num = int(num)
		z = (hour,ip)
		dict_ip_count[z] = dict_ip_count.get(z,0) + num
	except ValueError:
		pass
	#print(abc)
	sorted_dict_ip_count = sorted(dict_ip_count.items(), key = itemgetter(0))
sorted_array_ip_hour_count = []
for z,count in sorted_dict_ip_count:
	#print ('%s\t%s' % (z,count))
	tran = list(z)
	tran.append(count)
	sorted_array_ip_hour_count.append(tran)

#print(sorted_array_ip_hour_count)
Res = sorted(sorted_array_ip_hour_count, key=lambda x: (x[0],x[2]))
#for i in Res:
#print(i)
for i in abc:
	print(i)
	hourly_array = []
	for j in Res:
		if j[0] == i:
			hourly_array.append(j)
	print(str(hourly_array[-3:][::-1]))
