#import file handling libraries
import csv

#open and read dataset into dictreader
file = open('activity_dataset.csv', 'r', encoding='utf-8')
file_to_dict = csv.DictReader(file)

