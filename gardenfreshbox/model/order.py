from operator import itemgetter
import json

class Order():
	
	def __init__(self):
		self.id = None
		self.distribution_date = None
		self.creation_date = None
		self.customer_first_name = None
		self.customer_last_name = None
		self.customer_email = None
		self.customer_phone = None
		self.email_notifications = None
		self.large_quantity = None
		self.small_quantity = None
		self.customer_email = None
		self.donation = None
		self.donation_receipt = None
		self.total_paid = None
		self.hostsitepickup_idFK = None
		self.hostsitecreated_idFK = None
		self.vouchers = None
		self.address = None


	def __init__(self, creation_date, distribution_date, customer_first_name, customer_last_name, customer_email, customer_phone, email_notifications, small_quantity, large_quantity, donation, donation_receipt, address, total_paid, hostsitepickup_idFK, hostsitecreated_idFK, vouchers):
		
		values = [None,'']

		self.id = None

		if distribution_date in values:
			self.distribution_date = None
		else:
			self.distribution_date = distribution_date

		if creation_date in values:
			self.creation_date = None
		else:
			self.creation_date = creation_date

		if customer_first_name in values:
			self.customer_first_name = None
		else:
			self.customer_first_name = customer_first_name

		if customer_last_name in values:
			self.customer_last_name = None
		else:
			self.customer_last_name = customer_last_name

		if customer_email in values:
			self.customer_email = None
		else:
			self.customer_email = customer_email

		if customer_phone in values:
			self.customer_phone = None
		else:
			self.customer_phone = customer_phone

		if email_notifications in values:
			self.email_notifications = None
		else:
			self.email_notifications = email_notifications

		if small_quantity in values:
			small_quantity = 0
		else:
			self.small_quantity = small_quantity

		if large_quantity in values:
			self.large_quantity = 0
		else:
			self.large_quantity = large_quantity

		if donation in values:
			self.donation = 0
		else:
			self.donation = donation

		if donation_receipt in values:
			self.donation_receipt = None
		else:
			self.donation_receipt = donation_receipt

		if address in values:
			self.address = None
		else:
			sef.address = address

		if total_paid in values:
			self.total_paid = 0
		else:
			self.total_paid = total_paid
		
		if hostsitepickup_idFK in values:
			self.hostsitepickup_idFK = None
		else:
			self.hostsitepickup_idFK = hostsitepickup_idFK

		if hostsitecreated_idFK in values:
			self.hostsitecreated_idFK = None
		else:
			self.hostsitecreated_idFK = hostsitecreated_idFK
		
		if vouchers in values:
			self.vouchers = None
		else:
			self.vouchers = vouchers
		self.dict = {}
