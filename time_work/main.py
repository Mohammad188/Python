import os
from sys import argv

directory = "data"
CurrentDirectory = os.getcwd()
STORAGE_PATH = os.path.join(CurrentDirectory, directory)
if not os.path.exists(STORAGE_PATH):
	os.mkdir(STORAGE_PATH)

def main():
	work = argv[1]
	time = argv[2]
	print(work+": "+time)



if __name__ == "__main__":
	main()