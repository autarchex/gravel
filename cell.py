#cell.py | roop 20180319 | this file contains the cell object which encapsulates the simulated media and particles
#in most sims there will be only one cell object but they are independent so there could be more

import particle
import medium
import vectorquantity

class Cell:
	"""Cell objects contain one medium and n particles.  Particles may be of various masses, charges, cross sections.
	Ideally Cell will be extended to arbitrary, imported geometry in the future, but for now, it is simply a rectangle,
	with x axis horizontal and z axis vertical; y axis is through the page and not directly simulated."""
	def __init__(temp=25,visc=1):
		"""constructor takes parameter temp, temperature in deg C, and medium viscosity, default to 1 centipois.
		Initially the cell contains no particles; call populate() to fill it with a population."""
		self.medium = Medium(temp=temp,visc=visc)		#medium has same temperature as cell. default to 1 centipois viscosity.
		self.particles = []
		self.size = vectorquantity(x=200,y=1,z=20)	#default size is in microns
		self.voltage = vectorquantity(x=0,y=0,z=0)	#initial voltage. default to no voltage
		self.field = getFieldByVoltage()		#initial electric field. Magnetic is not contemplated.

	def getFieldByVoltage(self):
		"""Compute cell internal electric field, ignoring contribution from particles, assuming infinite planar plate condition.
		In present simplistic model, this results in a uniform field oriented along the z axis only."""
		d = self.size.z			#plate separation. TODO: change this when/if arbitrary geometry is implemented!
		k = self.medium.permittivity
		v = self.voltage.z		#for now, only consider the z axis component of voltage
		f = v / d			#field intensity in volts per meter, which is also newtons per coulomb
		field = vectorquantity(x=0,y=0,z=f)
		return field

	def setField(self, field=vectorquantity(x=0,y=0,z=0)):
		"""Set overall electric field in cell, ignoring contribution from particles themselves."""
		self.field = field


	def step(self):
		"""Advance simulation by one t step."""
		#TODO: not yet implemented!
		for p in self.particles:
			p.step()
		self.medium.step()
		pass

	def populate(self, n=1, rdist="normal", cdist="normal", density=1):
		"""Populate the cell with a randomly distributed (in space) population of n particles having radius and charge
		distributions rdist and cdist, and density as defined.  Particle mass is determined by radius. Particles are
		spherical.  Distributions may be "normal" or "uniform"."""
		#TODO: not yet implemented!
		for i in range(n):
			self.particles.append(Particle(cell=self, density=density))
		#TODO: modify radius of particles to conform to chosen distribution
		#TODO: modify charge of particles to conform to chosen distribution
  		pass

		
