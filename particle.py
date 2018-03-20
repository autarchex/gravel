#particle.py | roop 20180320 | particle simulation class for gravel

import vectorquantiy

class Particle:
	"""A particle is an object which has size radius, has electric charge, and has position.
	All particles start with initial velocity of zero."""
	def __init__(self, parent, radius=1, mass=1, charge=1, position=vectorquantity(x=0,y=0,z=0)):
		self.radius = radius
		self.charge = charge
		self.position = position
		self.velocity = vectorquantity(x=0,y=0,z=0)

	def step(self):
		"""Advance the simulation by one time step."""
		#TODO: not implemented!
		pass
	
	def getField(self):
		"""Calculate sum of fields this particle experiences. This consists of the cell field, plus field influence of all other particles in the cell, vector sum."
		field = vectorquantity(x=0,y=0,z=0)
		field = field + parent.field			#get the uniform external field in the cell due to external voltage 
		k = parent.medium.permittivity			#electrical permittivity of the medium between particles
		for p in parent.particles:
			r = self.position - p.position		#get displacement vector to particle
			c = abs(self.charge - p.charge)		#charge difference between this and other particle
			#TODO: calculate distance from r
			f = k * c / (r * r)			#electric field proportional k and c and inverse to square of distance
			#TODO: generate field vector field_p
			field = field + field_p

			
