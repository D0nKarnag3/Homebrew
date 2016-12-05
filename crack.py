#!/usr/bin/python2.7

import sys
import hashlib
import getopt

def usage():
	print "-h"

def load_word_list(path_to_word_list):
	with open(path_to_word_list) as f:
		return f.read().splitlines()

def crack(hash_to_match, word_list):
	result = "Could not crack password from the given information"
	for i in range(len(word_list)):
		if hash_to_match == hashlib.md5(word_list[i]).hexdigest():
			result = "Password found!\r\n{0}: {1}".format(hash_to_match, word_list[i])
			break
	print result

def main():
	if not len(sys.argv[1:]):
		usage()
		sys.exit()
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hm:w:", ["help", "match", "wordlist"])
	except getopt.GetoptError as err:
		print str(err)
		usage()
		sys.exit(2)
	
	hash_to_match = ""
	path_to_word_list = ""
	for o, a in opts:
		if o in ("-h", "--help"):
			usage()
			sys.exit()
		elif o in ("-m", "--match"):
			hash_to_match = a
		elif o in ("-w", "--wordlist"):
			path_to_word_list = a
		else:
			assert False, "Unhandled option"
	
	word_list = load_word_list(path_to_word_list)
	crack(hash_to_match, word_list)
	

if __name__ == "__main__":
	main()
