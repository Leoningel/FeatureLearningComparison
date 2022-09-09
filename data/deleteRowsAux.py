"""
Auxilary file to delete certain data points 
"""
import csv

with open('colic.csv', 'r') as inp, open('colic2.csv', 'w') as out, open('colic3.csv', 'w') as out2:
    writer = csv.writer(out)
    writer2 = csv.writer(out2)
    count = 0
    count2= 0;
    for row in csv.reader(inp):
        #pain column, surgery column, outcome column
        if ("0" not in (row[10], row[1], row[-2])):
            writer.writerow(row)
        if ("0" not in (row[10], row[1], row[-2], row[8] , row[11] , row[12] , row[14] , row[6])):
            writer2.writerow(row)
        
        #counting zeros
        #if (row[8]) == "0":
        #  count += 1
    
        
    print(count)