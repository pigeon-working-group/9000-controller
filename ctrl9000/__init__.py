from socket import create_connection
from json import dumps, JSONEncoder

class StateEncoder(JSONEncoder):
	def default(self, obj):
		if isinstance(obj, State):
			return {
				"power" : obj.power,
				"cycle_time" : obj.cycle_time,
				"operating_ratio" : obj.operating_ratio
			}
		return JSONEncoder.default(self, obj)


class State:
	def __init__(self, power=False, cycle_time=100.0, 
		operating_ratio=1.0):
		
		self.power = power
		self.cycle_time = cycle_time
		self.operating_ratio = operating_ratio


class Pigeon:
	def __init__(self, address=("pigeon9000.local", 1630)):
		self.sock = create_connection(address)

	def push(self, state):
		if type(state) is State:
			self.sock.send(
				dumps(state, cls=StateEncoder).encode() + b"\n")
		else:
			raise TypeError(
				"expected type '%s', got '%s'" % (
					State.__name__, type(state).__name__))