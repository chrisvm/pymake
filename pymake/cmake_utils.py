import os


def get_cmakelists_file(dir):
	# get current dir
	cwd = os.getcwd()

	# try to open CMakeLists.txt
	cmake_file = dir
	if cmake_file is None:
		cmake_file = os.path.join(cwd, 'CMakeLists.txt')
	try:
		with open(cmake_file) as f:
			contents = f.read()
			return contents
	except Exception:
		return None