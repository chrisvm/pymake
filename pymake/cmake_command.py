class CMakeCommand(object):
	def __init__(self):
		# config parser
		self.name = None
		self.help = None
		self.options = None

	def start(self, options):
		self.options = options
		# run command
		self.run()

	def config(self, subparsers):
		pass

	def run(self):
		pass
