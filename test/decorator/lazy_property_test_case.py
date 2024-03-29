"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import unittest
import utilities.decorator

class LazyPropertyTestCase(unittest.TestCase):
	class DummyClass(object):
		def __init__(self):
			self._dummy_attribute = None

		dummy_property = utilities.decorator.lazy_property()

		@dummy_property.loader
		def dummy_property(self):
			self._dummy_attribute = "loaded!"

		@dummy_property.getter
		def dummy_property(self):
			return self._dummy_attribute

		@dummy_property.setter
		def dummy_property(self, value):
			self._dummy_attribute = value

		@dummy_property.deleter
		def dummy_property(self):
			del self._dummy_attribute

	def test_load(self):
		dummy_object = LazyPropertyTestCase.DummyClass()

		self.assertEqual(dummy_object.dummy_property, "loaded!")

	def test_set(self):
		dummy_object = LazyPropertyTestCase.DummyClass()
		dummy_object.dummy_property = "some string"

		self.assertEqual(dummy_object.dummy_property, "some string")

	def test_del(self):
		dummy_object = LazyPropertyTestCase.DummyClass()
		success = False
		del dummy_object.dummy_property

		try:
			self.assertEqual(dummy_object.dummy_property, None)
		except AttributeError:
			success = True

		self.assertTrue(success)
