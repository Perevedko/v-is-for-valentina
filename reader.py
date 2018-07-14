import csv
import string

counter = 0
with open('pediatr.csv') as csvfile:
    schedule = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in schedule:
        print(','.join(row[:20]))
        counter += 1
        if counter == 5:
        	break
