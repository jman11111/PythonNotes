import csv
#reads csv and prints it
with open('Homework.csv', newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print (', '.join(row))
