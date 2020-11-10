# Word list aggregate script
# Copyright (c) Jeremy Rifkin 2015 - 2019

import os
import sys
import time

def main():
	# Check that files were given
	if len(sys.argv) == 1:
		sys.stderr.write("Error: no files provided.\n")
		sys.exit(1)
	# Check that all files exist
	files = sys.argv[1:]
	for fpath in files:
		if not os.path.isfile(fpath):
			sys.stderr.write("Error: file \"{}\" does not exist.\n".format(fpath))
	
	sys.stderr.write("Starting aggregator.\n")
	start = time.time()
	
	# would use a set but for some reason a dictionary gets better performance
	words = {}

	for fpath in files:
		with open(fpath, "r") as f:
			for line in f:
				if line.strip() != "":
					words[line.strip().capitalize()] = 0
	
	words = sorted(words.keys())
	for word in words:
		print(word)

	sys.stderr.write("Done.\n")
	t = time.time() - start
	sys.stderr.write("Excecution time: {:.02f} second{}.\n".format(t, "" if t == 1 else "s"))

main()
