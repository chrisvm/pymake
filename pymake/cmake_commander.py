#!/usr/bin/env python3
import os
from argparse import ArgumentParser, REMAINDER
from cmake_list import CMakeListCommand


class CMakeCommander(object):
	def __init__(self):
		# subcommands
		self.subs = [CMakeListCommand()]

		# options
		self.parser = None
		self.opts = self.get_options()

	def get_options(self):

		# create parser
		parser = ArgumentParser(description='stupid simple cmake interaction')

		# add arguments
		parser.add_argument('--clean', action='store_true', help='if set, remove cmake created files on finish', default=False)

		# iterate to get subparsers
		subparsers = parser.add_subparsers(help='commands   ', dest='command')
		for s in self.subs:
			# config parser
			s.config(subparsers)

		self.parser = parser
		return parser.parse_args()

	def start(self):
		# check if no command given
		if self.opts.command is None:
			print("Error: no command given")
			self.parser.print_help()
			exit()

		# run selected command
		self.opts.func.start(self.opts)