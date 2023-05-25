import json
import os
import re
import sys
# from mpi4py import MPI
#
#
# # Prepare for mpi4py
# comm = MPI.COMM_WORLD
# rank = comm.Get_rank()
# size = comm.Get_size()

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
    pattern_address = '\"full_name\":\"([^\"]*)\",'
    address = re.findall(pattern_address, instance)[0].split(", ")


    # Retrieve the language from each instance
    pattern_language = '\"lang\":\"([^\"]*)\",'
    language = re.findall(pattern_language, instance)[0]


    if language != 'en' and language != 'und':
        for each_string in address:
            if each_string.lower() in state_dict.keys():
                if language not in state_count_dict[state_dict[each_string.lower()]]:
                    state_count_dict[state_dict[each_string.lower()]][language] = 1

                else:
                    state_count_dict[state_dict[each_string.lower()]][language] += 1

                break

def saving():
    state_count = {
        'New South Wales': {},
        'Victoria': {},
        'Queensland': {},
        'South Australia': {},
        'West Australia': {},
        'Tasmania': {},
        'Northern Territory': {},
        'Australian Capital Territory': {}
    }
    # state_count_result = comm.gather(state_count_dict, root=0)
    state_count_result = state_count_dict

    if True:
        for i in range(1):
            print(state_count_result)
            for item in state_count_result.keys():
                for key in state_count_result[item].keys():
                    if key not in state_count[item].keys():
                        state_count[item][key] = state_count_result[item][key]
                    else:
                        state_count[item][key] += state_count_result[item][key]
        print(state_count)

    for key in state_count.keys():
        temp = sorted(state_count[key].items(), key=lambda x: x[1], reverse=True)
        state_count[key] = dict(temp[:10])
        state_count[key]["total"] = sum(state_count[key].values())

    # Add id to the state_count_dict
    print(json.dumps(state_count, indent=4))

    with open("data.json", "w") as json_file:
        json.dump(state_count, json_file, indent=4)
    print()

def main():
    # 配置日志输出到文件
    filename = 'twitter-huge.json'
    print("start")

    with open(filename, 'r', encoding="utf-8") as f:
        # file_size = f.seek(0, 2)  # get total size
        # print(file_size)
        # offset = file_size // size
        # start_point = rank * offset
        # print('start point:', start_point)
        # end_position = start_point + offset
        # print('end point:', end_position)
        temp_str = ""
        # f.seek(start_point)
        count = 0
        while True:
            each_line = f.readline()

            if re.match('\{\s*"id"\s*:\s*"(\d+)"\s*,\s*"key"',each_line) is not None:

                while True:
                    if re.search(r".*\}\]\}\}\,",each_line) is not None:
                        count += 1
                        if count % 1000000 == 0:
                            print(count)

                        if count % 30000000 == 0:
                            saving()
                        temp_str += each_line
                        try:
                            process_data(temp_str)
                        except:
                            pass
                        temp_str = ""
                        break
                    temp_str += each_line
                    # count += len(each_line.encode('utf-8'))
                    each_line = f.readline()
                    if not each_line:
                        print(count)
                        print("end")
                        saving()
                        break


            if not each_line:
                print(count)
                print("end")
                saving()

                break
            # else:
            #     temp_str += each_line
            #     count += len(each_line.encode('utf-8'))
            # if start_point + count >= end_position:
            #     break



    # server_address = "http://admin:password@172.26.129.1:5984"
    # try:
    #     print("==" * 40)
    #     logging.info("==" * 40)
    #
    #     print(f"Connecting to server: {server_address}")
    #     logging.info(f"Connecting to server: {server_address}")
    #     couch = couchdb.Server(server_address)
    #
    #     # Select the database
    #     db = couch['state']
    #
    #     # Get the document
    #     doc_id = 'state'
    #
    #     doc = db.get(doc_id)
    #
    #     # Change document content
    #     for key, value in state_count.items():
    #         doc[key] = value
    #
    #     # Save document
    #     db.save(doc)
    #     print("Successfully updated!\n")
    #     logging.info("Successfully updated!")
    #
    #     print("The content after the update:")
    #     logging.info("The content after the update:")
    #     print(json.dumps(dict(db.get(doc_id).items()), indent=4))
    #     logging.info(json.dumps(dict(db.get(doc_id).items()), indent=4))
    #
    # except Exception as e:
    #     print(f"CouchDB change encountered an: {e}")
    #     logging.info(f"CouchDB change encountered an: {e}")
    #


if __name__ == '__main__':
    main()
