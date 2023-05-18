import json
import re
import sys
import couchdb
import logging


# Variables
state_dict = {
    'new south wales': 'New South Wales',
    'sydney': 'New South Wales',
    'wollongong': 'New South Wales',
    'newcastle': 'New South Wales',
    'lithgow': 'New South Wales',
    'victoria': 'Victoria',
    'geelong': 'Victoria',
    'sunbury': 'Victoria',
    'melbourne': 'Victoria',
    'queensland': 'Queensland',
    'brisbane': 'Queensland',
    'gold coast': 'Queensland',
    'south australia': 'South Australia',
    'adelaide': 'South Australia',
    'albany': 'South Australia',
    'west australia': 'West Australia',
    'western australia': 'West Australia',
    'perth': 'West Australia',
    'tasmania': 'Tasmania',
    'hobart': 'Tasmania',
    'northern territory': 'Northern Territory',
    'darwin': 'Northern Territory',
    'australian capital territory': 'Australian Capital Territory',
    'canberra': 'Australian Capital Territory',
}

state_count_dict = {
    'New South Wales': {},
    'Victoria': {},
    'Queensland': {},
    'South Australia': {},
    'West Australia': {},
    'Tasmania': {},
    'Northern Territory': {},
    'Australian Capital Territory': {}
}


def process_data(instance):
    # Retrieve the state from each instance
    pattern_address = '"full_name": "([^\"]*)",'
    address = re.findall(pattern_address, instance)[0].split(", ")

    # Retrieve the language from each instance
    pattern_language = ' "lang": "([^\"]*)",'
    language = re.findall(pattern_language, instance)[0]

    if language != 'en' and language != 'und':
        for each_string in address:
            if each_string.lower() in state_dict.keys():
                if language not in state_count_dict[state_dict[each_string.lower()]]:
                    state_count_dict[state_dict[each_string.lower()]][language] = 1
                else:
                    state_count_dict[state_dict[each_string.lower()]][language] += 1
                break


def main(filename):

    # 配置日志输出到文件
    logging.basicConfig(filename='update_state.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    # 在终端打印的内容也会输出到日志文件中
    logging.info('Update information of state')


    with open(filename, 'r', encoding="utf-8") as f:
        temp_str = ""
        while True:
            each_line = f.readline()
            if each_line == "  },\n" or each_line == "  }\n":
                temp_str += each_line
                try:
                    process_data(temp_str)
                except:
                    pass
                if not each_line:
                    break
                temp_str = ""
            if not each_line:
                break
            else:
                temp_str += each_line

    for key in state_count_dict.keys():
        temp = sorted(state_count_dict[key].items(), key=lambda x: x[1], reverse=True)
        state_count_dict[key] = dict(temp[:10])
        state_count_dict[key]["total"] = sum(state_count_dict[key].values())

    # Add id to the state_count_dict
    print(json.dumps(state_count_dict, indent=4))
    logging.info("")
    print()

    server_address = "http://admin:password@172.26.129.1:5984"
    try:
        print("==" * 40)
        logging.info("==" * 40)

        print(f"Connecting to server: {server_address}")
        logging.info(f"Connecting to server: {server_address}")
        couch = couchdb.Server(server_address)

        # Select the database
        db = couch['state']

        # Get the document
        doc_id = 'state'

        doc = db.get(doc_id)

        # Change document content
        for key, value in state_count_dict.items():
            doc[key] = value

        # Save document
        db.save(doc)
        print("Successfully updated!\n")
        logging.info("Successfully updated!")

        print("The content after the update:")
        logging.info("The content after the update:")
        print(json.dumps(dict(db.get(doc_id).items()), indent=4))
        logging.info(json.dumps(dict(db.get(doc_id).items()), indent=4))

    except Exception as e:
        print(f"CouchDB change encountered an: {e}")
        logging.info(f"CouchDB change encountered an: {e}")



if __name__ == '__main__':
    try:
        filename = sys.argv[1]  # read filename from command line argument
        main(filename)
    except:
        main('smallTwitter.json')
