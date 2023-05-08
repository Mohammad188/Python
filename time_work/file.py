from jdatetime import datetime
import os


directory = "data"
CurrentDirectory = os.getcwd()
STORAGE_PATH = os.path.join(CurrentDirectory, directory)


year = datetime.now().year
month = datetime.now().month
day = datetime.now().day
file_name = str(year) + "-" + str(month) + "-" + str(day)
file_address = CurrentDirectory + '/' + directory + '/' + file_name + '.csv'


class File:
    def __init__(self):
        # making a directory for storing data
        if not os.path.exists(STORAGE_PATH):
            os.mkdir(STORAGE_PATH)


        # making today's file
        open(str(file_address), 'a+')