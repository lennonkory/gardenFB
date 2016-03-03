import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from ast import literal_eval
from gardenfreshbox.lib.base import BaseController, render
from gardenfreshbox.model.cookie import Cookie
from gardenfreshbox.model.order import Order
from gardenfreshbox.model.GFBDatabaseController import GFBDatabaseController as DB
import json

log = logging.getLogger(__name__)

class OrdersController(BaseController):

	def orders(self):
		db = DB()
		# this method will return either one or all users based on id
		# if id == * all users are returned
		if (request.method == "GET"):
			order_id = request.params['id']
			if order_id == '*':
				return "returns all orders"
			else:
				return "returns order with id " + order_id

		# this method works for real - just need to figure out host site links to people in the database
		# should this return the order's ID? 
		elif (request.method == "PUT"):
			print request.params['creation_date']
			# order_id = request.params['order_id']
			# if(db.orderExists(order_id)):
			# 	# Update order
			# 	# db.createNewOrder(request.params['order_id'], request.params['creation_date'], request.params['dist_date'], request.params['first_name'], request.params['last_name'], request.params['email'], request.params['phone'], request.params['notify'], request.params['num_sm'], request.params['num_lg'], request.params['donation'], request.params['donation_reciept'], request.params['mail_address'], request.params['amt_paid'], request.params['hs_pickup'], request.params['hs_ordered'], request.params['vouchers']): Boolean
			# 	return "update order" # unimplemented until db is ready
			# else:
				# TODO check for errors from database
				# TODO input validation, types?
				# Add new order
				# db.createNewOrder(request.params['creation_date'], request.params['dist_date'], request.params['first_name'], request.params['last_name'], request.params['email'], request.params['phone'], request.params['notify'], request.params['num_sm'], request.params['num_lg'], request.params['donation'], request.params['donation_reciept'], request.params['mail_address'], request.params['amt_paid'], request.params['hs_pickup'], request.params['hs_ordered'], request.params['vouchers']): Boolean
				
				# return "{'success':'true'}"
			return "{\"success\":\"true\"}"
			return "{\"success\":\"false\", \"message\":[\"Unable to complete order.\"]}"

		# we might not implement this
		elif (request.method == "DELETE"):
			order_id = request.params['id']
			# db.removeOrder(order_id)
			return "{\"success\":\"true\"} - delete order}"
		
		else:
			return "{\"success\":\"false\",\"message\":\"Bad request method\"}"

	def distribution(self):
		#look at cookie
		cookie = request.cookies.get("FCS_GFB_Cookie")
		if(cookie == None):
			print "There is no cookie for user"
			# return None
			return "orders to distribute, some JSON"
		else:
			row = cookie
			if(row.get('role') == 'C') or (row.get('role') == 'A'):
				# this will be JSON
				return "orders to distribute, some JSON"
			else:
				return None
