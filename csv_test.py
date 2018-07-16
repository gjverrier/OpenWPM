import csv
import sys

afile = open('/home/icebox/PycharmProjects/OpenWPM/data/top_500_rankless.csv')
reader = csv.reader(afile)

sites = []
for row in reader:
	sites.append(row)
print(len(sites))
afile.close() 





