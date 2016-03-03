from operator import itemgetter
import json

class HostSite():
	
	def __init__(self):
		self.id = None
		self.name = None
		self.address = None
		self.city = None
		self.province = None
		self.postal_code = None
		self.phone = None
		self.email = None
		self.coordinatorIDs = None
		self.hours_of_operation = {}


	def __init__(self, name, address, city, province, postal_code, coordinatorIDs, hours_of_operation):
		
		values = [None, '']

		self.phone = None
		self.email = None

		if name in values:
			self.name = None
		else:
			self.name = name

		if address in values:
			self.address = None
		else:
			self.address = address

		if city in values:
			self.city = None
		else:
			self.city = city

		if province in values:
			self.province = None
		else:
			self.province = province

		if postal_code in values:
			self.postal_code = None
		else:
			self.postal_code = postal_code

		if coordinatorIDs in values:
			self.coordinatorIDs = None
		else:
			self.coordinatorIDs = coordinatorIDs

		if hours_of_operation in values:
			self.hours_of_operation = None
		else:
			self.hours_of_operation = hours_of_operation