from cmake_command import CMakeCommand
import cmakeast
import os
from cmake_utils import get_cmakelists_file


class CMakeListCommand(CMakeCommand):
	def __init__(self):
		CMakeCommand.__init__(self)
		self.name = "list"
		self.help = "list all targets specified in CMakeLists.txt"

	def config(self, subparsers):
		# create the parser for the "list" command
		parser = subparsers.add_parser(self.name, help=self.help)
		parser.add_argument('--json', action='store_true', help='output target info to json', default=False)
		parser.add_argument('--ast', action='store_true', help='output target info to ast', default=False)
		parser.set_defaults(func=self)

	def run(self):
		# if ast
		if self.options.ast:
			# get file
			contents = get_cmakelists_file()

			# if not found, exit
			if contents is None:
				print("error: CMakeLists file not found on '{}'".format(os.getcwd()))
			
			# parse ast 
			ast = cmakeast.ast.parse(contents)
			
			# pprint ast 
			self.pprint_ast(ast)

	def pprint_ast(self, ast):
		pass