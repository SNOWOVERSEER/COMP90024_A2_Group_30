import csv
import json
import re
import sys

# Variables
state_dict = {
    '1': 'New South Wales',
    '2': 'Victoria',
    '3': 'Queensland',
    '4': 'South Australia',
    '5': 'West Australia',
    '6': 'Tasmania',
    '7': 'Northern Territory',
    '8': 'Australian Capital Territory',
}

state_count_dict = {
    'New South Wales': 0,
    'Victoria': 0,
    'Queensland': 0,
    'South Australia': 0,
    'West Australia': 0,
    'Tasmania': 0,
    'Northern Territory': 0,
    'Australian Capital Territory': 0
}



def process_data(row):
    id, data = row[0], row[1]
    if id[0] in '12345678':
        state_count_dict[state_dict[id[0]]] += int(data)



def main(filename):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)

        next(csv_reader)

        for row in csv_reader:
            process_data(row)

    json_str = json.dumps(state_count_dict, indent=4)
    print(json_str)

    with open('state_new_migration.json', 'w') as f:
        f.write(json_str)


if __name__ == '__main__':
    try:
        filename = sys.argv[1] # read filename from command line argument
        main(filename)
    except:
        main('abs_regional_population_lga_2001_2021-5650805521010608891.csv')