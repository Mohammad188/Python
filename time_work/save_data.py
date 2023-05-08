from file import file_address

class Save:
    def __init__(self, work:str, time:str):
        self.work = work 
        self.time = time
        self.writing_in_file()

    def writing_in_file(self):
        with open(file_address, 'a') as file_:
            file_.write(self.work + ", " + self.time + "\n")
            file_.close()


    


