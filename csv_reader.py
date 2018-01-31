import csv
import sys

def read_csv_file(filename):
	data_list = list()
	title_list = list()
	with open(filename, newline='') as csvfile:
		filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in filereader:
			for i in range(0, len(row)):
				data_list.append(list())
				title_list.append(row[i].strip())
			break
		for row in filereader: 
			for i in range(0, len(row)):
				data_list[i].append(int(row[i]))
	return (title_list, data_list)


def main():
	data = read_csv_file(sys.argv[1])
	print(data)

if __name__ == '__main__':
    main()