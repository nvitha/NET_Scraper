#!/usr/bin/python3
import requests
import csv
import os
from datetime import datetime
from bs4 import BeautifulSoup
from pprint import pprint

x = datetime.now()
time_string = str(x.year) + str(x.month) + str(x.day)

directory = "files/" + time_string + "/"
if not os.path.exists(directory):
	os.makedirs(directory)


print("Downloading HTML from https://www.ncaa.com/rankings/basketball-men/d1/ncaa-mens-basketball-net-rankings")
print("This may take a few seconds depending on your download speed")
r = requests.get("https://www.ncaa.com/rankings/basketball-men/d1/ncaa-mens-basketball-net-rankings")

print("Parsing HTML")
soup = BeautifulSoup(r.text,features="lxml")
table = soup.find("table", attrs={"class":"sticky"})

headings = [th.get_text() for th in table.find("tr").find_all("th")]

teams = []
for row in table.find_all("tr")[1:]:
	dataset = []
	for td in row.find_all("td"):
		dataset.append(td.get_text())
	teams.append(dataset)

print("Writing files")

with open (directory + time_string + "NET.html", "w+") as file:
	file.write(r.text)
	
with open(directory + time_string + "NET.csv", "w+") as file:
	writer = csv.writer(file, delimiter=',')
	writer.writerow(headings)
	for team in teams:
		writer.writerow(team)
