import mysql.connector as ct

class GFBDatabaseController():
	def __init__(self):
		f = open('gardenfreshbox/model/db_config.csv', 'r')       
		f.readline()
		params = f.readline()
		params_split = params.split(',')
		params_split[-1] = params_split[-1][:-1]

		self.cnx = ct.connect(host=params_split[0], user=params_split[1], password=params_split[2], database=params_split[3])
		self.cursor = self.cnx.cursor()

	#####################
	###  USER METHODS ###
	#####################

	def userExists(self, email):
		if email is False:
			return False
		email = '"' + email + '"'
		q = "SELECT * FROM Users WHERE email=%s;" % email
		self.cursor.execute(q)
		results = self.cursor.fetchall()
		if not results:
			return False
		else:
			return True

	def addUser(self, email, password, firstName, lastName, credentials, phoneNumber=None):
		q = "INSERT INTO Users (email, password, first_name, last_name, credentials, phone_number) VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % (email,password,firstName,lastName,credentials,phoneNumber)
		print q
		self.cursor.execute(q)
		self.cnx.commit()

	def addUserModel(self, user):
		return self.addUser(user.email, user.password, user.first_name, user.last_name, user.credentials_idFK, user.phone_number)

	def authUser(self, email, password):
		return True

	def updateUser(email, newEmail, newPassword, newFirstName, newLastName, newPhoneNumber, hostSites, credentials):
		return True

	def getUsers():
		return True

	def getUser(email):
		return True

	##########################
	###  HOST SITE METHODS ###
	##########################

	# Need a get host site by name method

	def getCoordinatorList(hostSiteID):
		return True

	def hostSiteNameExists(name):
		return True

	def addHostSite(name, address, city, province, postalCode, coordinatorIDs, hoursOfOperation):
		return True

	def addHostSiteModel(self, hostSite):
		self.addHostSite(hostSite.name, hostSite.address, hostSite.city, hostSite.province, hostSite.postal_code, hostSite.coordinatorIDs, hostSite.hours_of_operation)

	def updateHostSite(hostSiteID, name, address, city, province, postalCode, coordinatorIDs, hoursOfOperation):
		return True

	def removeHostSite(hostSiteID):
		return True

	# TODO - relationship between host sites and coordinators
	def getHostSiteList(coordinatorID):
		return True

	def getAllHostSites():
		return True

	def getHostSite(hostSiteID):
		return True


	######################
	###  ORDER METHODS ###
	######################

	def createNewOrder(dateCreated, dateToDistribute, firstName, lastName, email, phoneNumber, shouldSendNotifications, smallBoxQuantity,largeBoxQuantity, donations, donationReceipt, address, totalPaid, hostSitePickupID, hostSiteOrderID, vouchers):
		return True

	def updateOrder(orderID, dateCreated, dateToDistribute, firstName, lastName, email, phoneNumber, shouldSendNotifications, smallBoxQuantity,largeBoxQuantity, donations, totalPaid, hostSitePickupID, hostSiteOrderID, vouchers):
		return True

	def removeOrder(orderID):
		return True

	def cancelOrder(orderID):
		return True

	def getAllCanceledOrdersByDistributionDate(beginDate, endDate):
		return True

	def getAllCanceledOrdersByDistributionDate(beginDate, endDate):
		return True

	def getOrderByDistributionDate(hostSiteID, beginDate, endDate):
		return True

	def getAllOrdersByDistributionDate(beginDate, endDate):
		return True

	def getUnpaidOrdersByDistributionDate(hostSiteID, beginDate, endDate):
		return True

	def getAllUnpaidOrdersByDistributionDate(beginDate, endDate):
		return True

	def getPaidOrdersByDistributionDate(hostSiteID, beginDate, endDate):
		return True

	def getAllPaidOrdersByDistributionDate(beginDate, endDate):
		return True
		 
# controller = GFBDatabaseController()
# controller.addUser('hind.shawn@gmailm', 'adfasd', 'adfasdf', 'adsfasdfas', '1', 'adsfasdf')
