"""
Auxilary file to delete certain data points 
"""
import csv

with open('daily-website-visitors.csv', 'r') as inp, open('daily-website-visitors2.csv', 'w') as out:
    writer = csv.writer(out)
    
    for row in csv.reader(inp): 
        writer.writerow((row[0], row[2], row[4].replace(",", "")))
        
