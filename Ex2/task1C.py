import csv

filename = "SampleCSVFile.csv"


def read_csv(input_file):
    with open(input_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        namelist = [row for row in csvreader]

        print(*namelist)


read_csv(filename)
