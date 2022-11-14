import csv
import argparse


def print_file_content(file):
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            print(row)

        print("\n")


def write_list_to_file(output_file, *inputs):
    with open(output_file, "a") as nameFile:
        for line in inputs:
            nameFile.writelines(str(data) + "\n" for data in line)


def read_csv(input_file):
    with open(input_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        namelist = [row for row in csvreader]
        return namelist


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Exercise 2.1")

    parser.add_argument("--csv", help="The name of the csv file")
    parser.add_argument("--file", default="", help="The name of the file to write results to")

    args = parser.parse_args()

    csvName = args.csv
    resultsFile = args.file

    if resultsFile == "":
        print_file_content(csvName)
    else:
        write_list_to_file(resultsFile, read_csv(csvName))


