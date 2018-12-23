#!/usr/bin/python3
import csv
import os
from os.path import isfile, join
from pprint import pprint
from statistics import mean,median,stdev
import operator

onlydirs = [f for f in os.listdir("files/") if not isfile(f)]

file_prefix = "files/" + onlydirs[0] + "/" + onlydirs[0]
file_path = file_prefix + "NET.csv"


divs = {}
with open(file_path, "r") as file:
	reader = csv.reader(file, delimiter=',')
	next(reader, None)
	for row in reader:
		if row[3] in divs:
			divs[row[3]].append((row[2],int(row[0])))
		else:
			divs[row[3]] = [(row[2],int(row[0]))]

div_stats = {}
for key, value in divs.items():
	div_ranks = [value[x][1] for x in range(0,len(value)-1)]

	avg = round(mean(div_ranks),2) #calling these returns by the function names causes issues
	maximum = int(max(div_ranks))
	minimum = int(min(div_ranks))
	med = int(median(div_ranks))
	std = round(stdev(div_ranks),2)
	diff_med_avg = round(med - avg,2)

	
	div_stats[key] = [med, avg, std, maximum, minimum, diff_med_avg]

sorted_div_stats = sorted(div_stats.items(), key = operator.itemgetter(0))
pprint(sorted_div_stats)

print("Conference | Median | Average | Standard Deviation | Worst | Best | Diff between Med. and Avg.")
print("--- | --- | --- | --- | --- | --- | ---")
for item in sorted_div_stats:
	print(item[0] + "|" + str(item[1][0]) + "|" + str(item[1][1]) + "|" + str(item[1][2]) + "|" + str(item[1][3]) + "|" + str(item[1][4]) + "|" + str(item[1][5]))


