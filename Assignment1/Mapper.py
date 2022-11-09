#! /usr/bin/python3.8
"""Mapper.py"""
import re
import sys
import fileinput

pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
	match = pat.search(line)
	#print(match)
	if match:
		print ('%s\t%s' % ('[' +match.group('hour') + ':00' +']' +"\t" + match.group('ip'),1))
