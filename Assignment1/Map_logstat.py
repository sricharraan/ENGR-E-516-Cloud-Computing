import re
import sys
import fileinput

def map_logstat():
	pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+.).*?"\w+ (?P<subdir>.*?)')
	for line in fileinput.input(files = 'access.log'):
		match = pat.search(line)
		#print(match)
		if match:
			#print ('%s\t%s' % (match.group('ip'),1))
			f = open("Mapper.txt","a")
			f.write(str(match.group('ip'))+"\t" + str(1) + "\n")
			f.close()


def map_logstat2():
	pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
	for line in fileinput.input(files = 'access.log'):
		match = pat.search(line)
		#print(match)
		if match:
			#print ('%s\t%s' % ('[' +match.group('hour') + ':00' +']' + match.group('ip'),1))
			f = open("Mapper2.txt","a")
			#print("file created")
			f.write(str(match.group('hour') + ':00')+ "\t" + str(match.group('ip'))+"\t" + str(1) + "\n")
			f.close()