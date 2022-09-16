"""
Auxilary file to delete certain data points 
"""
import csv

with open('daily-website-visitors.csv', 'r') as inp, open('daily-website-visitors2.csv', 'w') as out:
    writer = csv.writer(out)

    header = next(csv.reader(inp))
    
    writer.writerow((header[0], header[2], "Month",  "Day", header[-1], """target"""))

    for row in csv.reader(inp):
        writer.writerow((row[0], row[2], row[3].split("/")[0], 
                         row[3].split("/")[1], row[-1].replace(",", ""), row[4].replace(",", "")))
