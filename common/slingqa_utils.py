import datetime
import re
import os

class utils:
    def __init__(self):
        print("Initializing utils")

    def get_timestamp(self):
        now = datetime.datetime.now()
        now = str(now)
        year = now[:4]
        month = now[5:7]
        day = now[8:10]
        hour = now[11:13]
        minute = now[14:16]
        sec = now[17:19]

        time_string = year + '.' + month + '.' + day + '_' + hour + '.' + minute + '.' + sec
        # print time_string
        return time_string

    def convert_to_file_name_string(self, word_list):
        result = ""
        for word in word_list:
            new_word = re.sub(r'\W+', '', word)
            result = result + new_word
        return result


    def dump_to_text_file(self, text, file_name, directory = "../logs/"):
        if not os.path.exists(directory):
            os.makedirs(directory)
            print("Creating directory " + directory)
        timestamp = self.get_timestamp()

        file_path = directory + file_name + '_' + timestamp + '.txt'
        print("Writing to {}.".format(file_path))

        text_file = open(file_path, "w")
        text_file.write(text)
        text_file.close()






