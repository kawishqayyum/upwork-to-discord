import shelve


class StateManager:
	def __init__(self, file):
		self.file = file

	def add_value(self, key, value):
		with shelve.open(self.file) as d: 
			d[key] = value

	def get_value(self, key):
		with shelve.open(self.file) as d:
			return d[key] if (key in d) else False
