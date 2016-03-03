from operator import itemgetter
import json

class User():
	
	def __init__(self):
		self.id = None
		self.credentials_idFK = None
		self.email = None
		self.first_name = None
		self.last_name = None
		self.phone_number = None
		self.password = None
		self.host_sites = []
		self.new_email = None

	def __init__(self, email, password, first_name, last_name, credentials_idFK, phone_number):
		
		values = [None, ''] 

		self.host_sites = None
		self.new_email = None

		if email in values:
			self.email = None
		else:
			self. email = email

		if password in values:
			self.password = None
		else:
			self.password = password

		if first_name in values:
			self.first_name = None
		else:
			self.first_name = first_name

		if last_name in values:
			self.last_name = None
		else:
			self.last_name = last_name

		if credentials_idFK in values:
			self.credentials_idFK = None
		else:
			self.credentials_idFK = credentials_idFK

		if phone_number in values:
			self.phone_number = 0
		else:
			self.phone_number = phone_number
