import csv

with open('Homework.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print (', ').join(row)

message = input()
message = message + " cool"
print(message)