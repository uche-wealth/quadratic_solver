import math
import cmath
import matplotlib.pyplot as plt
import numpy as np
import logging
from typing import Tuple


logging.basicConfig(level=logging.INFO)

class QuadraticFunctions:
	"""Model Quadratic Functions."""
	def __init__(self, a, b, c):
		""" Initialise attributes of quadratic functions"""
		self.a = a
		self.b = b
		self.c = c

	def convert_to_float(self) ->Tuple[float, float, float] | str:
		""" Return float values of user input"""
		try:
			self.a = float(self.a)
			self.b = float(self.b)
			self.c = float(self.c)
		except Exception as exc:
			logging.error('An error occured: %s' % exc)
		else:
			logging.info("a=%s b=%s c=%s" % (self.a, self.b, self.c))
			return self.a, self.b, self.c
		return '\n'


	def vertex(self) ->Tuple[float, float] | str:
		"""Return Tuple containing the vertex of the quadratic function"""
		qf = QuadraticFunctions(self.a, self.b, self.c)
		qf.convert_to_float()
		try:
			x = (-self.b) / (2*self.a)
			y = self.a*(x**2) + (self.b*x) + self.c
		except Exception as exc:
			logging.error('An error occured: %s' % exc)
		else:
			ordered_pair = (x, y)
			logging.info(ordered_pair)
			return ordered_pair
		return '\n'


	def discriminant(self) ->float | str:
		"""Return the value of the discriminant"""
		qf = QuadraticFunctions(self.a, self.b, self.c)
		qf.convert_to_float()
		try:
			quadratic_discriminant = (self.b**2) - (4*self.a*self.c)
		except Exception as exc:
			logging.error('An error occured: %s' % exc)
		else:
			logging.info('Quadratic Discriminant %s' % quadratic_discriminant)
			return quadratic_discriminant
		return '\n'

	def quadratic_formula(self) ->Tuple[float, float] | str:
		"""Model the quadratic formula"""
		qf = QuadraticFunctions(self.a, self.b, self.c)
		v = qf.vertex()
		d = qf.discriminant()
			# If the discriminant is non-negative, it will have real roots and 
				# will require python's math library.
		try:
			if d >= 0:
				x_1 = (-self.b + math.sqrt(d))/(2*self.a)
				x_2 = (-self.b - math.sqrt(d))/(2*self.a)

			# If discriminant is negative, it will have complex roots and will 
				# require python's complex math library.
			else:
				x_1 = (-self.b + cmath.sqrt(d))/(2*self.a)
				x_2 = (-self.b - cmath.sqrt(d))/(2*self.a)
		except Exception as exc:
			logging.error('An error occured: %s' % exc)
		else:

			logging.info(
				f'''
				The roots are {x_1} and {x_2}
				Discriminant: {d}
				Vertex: {v}
				Axis of Symmetry: x = {v[0]}
				'''
				)
			
			return(
					f'''
					The roots are {x_1} and {x_2}
					Discriminant: {d}
					Vertex: {v}
					Axis of Symmetry: x = {v[0]}
					'''
					)
		return '\n'

	def style_graph(self):
		"""Style the graph"""
		plt.style.use("grayscale")
		plt.xlabel('x', loc='right', c='r')
		plt.ylabel('y', loc='top', c='r')
		plt.grid(True, linestyle=':')
		plt.title(f"Graph of ${self.a}x^2 + {self.b}x + {self.c}$", 
			fontsize=16, c='r')


	def plot_and_display_graph(self):
		"""Plot and display graph of the quadratic function."""
		qf = QuadraticFunctions(self.a, self.b, self.c)
		qf.style_graph()
		x = np.linspace(-10, 10, 50)
		y = (self.a*(x)**2) + (self.b*x) + self.c
		show_roots = np.roots([self.a, self.b, self.c])
		show_x_values = [show_roots[0], show_roots[1]]
		show_y_values = [0, 0]
		plt.scatter(show_x_values, show_y_values, s=100, c='r', 
				alpha=1, label='roots')
		plt.legend()
		plt.plot(x, y, 'b', linewidth=3)
		plt.show()





