import os

def get_cmakelists_file():
	# get current dir
	cwd = os.getcwd()

	# try to open CMakeLists.txt
	cmake_file = os.path.join(cwd, 'CMakeLists.txt')
	try:
		with open(cmake_file) as f:
			contents = f.read()
			return contents
	except Exception:
		return None