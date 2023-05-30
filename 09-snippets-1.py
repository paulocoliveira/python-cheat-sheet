import csv

# Reading CSV File
with open('testdata.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing to CSV File
data = [['Name', 'Age'], ['John', 30], ['Jane', 25]]
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
