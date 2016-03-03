import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from ast import literal_eval
from gardenfreshbox.lib.base import BaseController, render
from gardenfreshbox.model.cookie import Cookie

log = logging.getLogger(__name__)

class SalesController(BaseController):

	def index(self):
		return render('/tools/cashSales.mako')

	def donate(self):
		return render('/donate/donate.mako')

	def sales(self):
		#look at cookie
		cookie = request.cookies.get("FCS_GFB_Cookie")
		if(cookie == None):
			print "There is no cookie for user"
			# return None
			return "list of cash sales in JSONO format";
		else:
			creds = Cookie.decryptCookie(cookie)		
			if(creds.get('role') == '2') or (creds.get('role') == '1'):
				#This will need to be updated when the front end knows what parms its using
				if (request.method == "GET"):
					order_list = None

					hostSiteID = request.params['hostSiteID']
					beginDate = request.parms['beginDate']
					endDate = request.parms['endDate']
					paid = request.parms['paid']#may need to change this
					cancel = request.parms['cancel']
					
					if cancel == True:
						#order_list = db.etAllCanceledOrdersByDistributionDate(beginDate,endDate)
						pass
					elif hostSiteID == None:
						if paid == True:
							# order_list = db.getAllPaidOrdersByDistributionDate(beginDate,endDate)
							pass
						elif paid == False:
							#order_list = db.getAllUnpaidOrdersByDistributionDate(beginDate, endDate)
							pass
						else:
							#order_list = db.getAllOrdersByDistributionDate(beginDate, endDate)
							pass
					else:
						if paid == True:
							# order_list = db.getPaidOrdersByDistributionDate(hostSiteID, beginDate, endDate)
							pass
						elif paid == False:
							#order_list = db.getUnpaidOrdersByDistributionDate(hostSiteID, beginDate, endDate)
							pass
						else:
							#order_list = db.getOrderByDistributionDate(hostSiteID, beginDate, endDate)
							pass

					#return json.dumps(order_list)
					return "order_list in json format"
		
			else:
				return None

	def customers(self):
		#look at cookie
		cookie = request.cookies.get("FCS_GFB_Cookie")
		if(cookie == None):
			print "There is no cookie for user"
			# return None
			return "customer list in JSON format"
		else:
			#List is based on C or A status
			creds = Cookie.decryptCookie(cookie)	
			if(creds.get('role') == '2') or (creds.get('role') == '1'):

				customer_list = None
				#\this is a weird one. You need to get an order and filter out the customer

				return "customer list in JSON format"
			else:
				return None

	def donors(self):
		#look at cookie
		cookie = request.cookies.get("FCS_GFB_Cookie")
		if(cookie == None):
			print "There is no cookie for user"
			# return None
			return "list of donors in JSON format";
		else:
			#analyze the cookie
			creds = Cookie.decryptCookie(cookie)
			if(creds.get('role') == '2'):
				return None
			elif (creds.get('role') == '1'):
				return "list of donors in JSON format";
			else:
				return None