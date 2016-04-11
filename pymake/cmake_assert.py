import os


class CMakeAsserts(object):
	def __init__(self):
		pass

	def cmake_list(self, opts):
		for listing in os.listdir(opts.cwd):
			print(listing)