
from sys import argv
from save_data import Save 
from file import File


def main():
	try:
		work = argv[1]
		time = argv[2]
		File()
		Save(work, time)
	except IndexError:
		print('you have to enter two arguments(work, time) :)')


if __name__ == "__main__":
	main()