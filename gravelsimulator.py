#gravelsimulator.py  | roop 20180319 | simulator host object lives here

#the simulator object will be a one-off which contains the cell(s) and all of the simulation parameters
#at a minimum should create a Cell, and have methods for interaction with the external environment.

import Cell

class GravelSimulator:
	"""Primary simulation object class. There should never be more than one of this instantiated."""
	def __init__(self):
		self.cell = Cell()	#first, possibly only, simulation cell
		self.cell.populate(n=10,dist="normal")	#populate with n particles having a normal distribution
	

	def step(self):
		"""Advance simulation time by one t step. This propagates throughout all child objects."""
		self.cell.step()

	def draw(self):
		"""Initiate drawing of all objects in system"""
		self.cell.draw()

	def dump(filename):
		"""Dump all current simulation data to a file."""
		#not implemented!
		pass
