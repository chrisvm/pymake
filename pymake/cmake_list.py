import cmakeast
import os
from cmake_command import CMakeCommand
from collections import deque
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
		# get file
		contents = get_cmakelists_file(self.options.file)

		# if not found, exit
		if contents is None:
			print("error: CMakeLists file not found on '{}'".format(os.getcwd()))
			exit()

		# parse ast
		ast = cmakeast.ast.parse(contents)

		# if ast
		if self.options.ast:
			# pprint ast 
			self.pprint_ast(ast)
			return

	def pprint_ast(self, ast):
		t_bracket, l_bracket = 0x02EA, 0x02EB
		nodes = [{"name": "TopLevelBody", "ast": ast, "indent": 0}]

		# start loop
		while len(nodes) != 0:
			node = nodes.pop()

			# if block
			if node['name'] == 'TopLevelBody' or node['name'] == 'Body':
				print(' ' * node['indent'], '', node['name'])

				for stmt in node['ast'].statements:
					tnode = {'ast': stmt, 'indent': node['indent'] + 4}
					tnode['name'] = self.get_node_name(tnode['ast'])
					nodes.insert(0, tnode)

			# if function call
			if node['name'] == 'FunctionCall':
				print(' ' * node['indent'], chr(t_bracket), node['name'], '(name={})'.format(node['ast'].name))
				node['ast'].arguments.reverse()
				for arg in node['ast'].arguments:
					tnode = {'ast': arg, 'indent': node['indent'] + 4}
					tnode['name'] = self.get_node_name(tnode['ast'])
					nodes.append(tnode)

			# if word
			if node['name'] == 'Word':
				print(' ' * node['indent'], chr(t_bracket), node['ast'])


	def get_node_name(self, node):
		opts = {
			"FunctionCall": cmakeast.ast.FunctionCall,
			"Word": cmakeast.ast.Word
		}
		for k,v in opts.items():
			if isinstance(node, v):
				return k
		return 'None'