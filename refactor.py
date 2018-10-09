
import os
import sys

# Lists all files in a given path with a given extension
def files_in_dir(path, extension):
	all_files = []
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.endswith('.' + extension):
				all_files.append(os.path.join(root, file))

	return all_files

path = sys.argv[1]
extension = sys.argv[2]

all_files = files_in_dir(path, extension)

for file in all_files:
	file_data = open(file, 'r')
	# Do whatever you want here!