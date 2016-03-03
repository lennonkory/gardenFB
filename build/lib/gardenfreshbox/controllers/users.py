import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from ast import literal_eval
from gardenfreshbox.lib.base import BaseController, render
from gardenfreshbox.model.cookie import Cookie
from gardenfreshbox.model.user import User
from gardenfreshbox.model.GFBDatabaseController import GFBDatabaseController as DB

log = logging.getLogger(__name__)

class UsersController(BaseController):

	global true_string
	true_string = "{\"success\" : \"true\"}"

	# TODO :: probably use cookies here, make sure that the client cookie actually comes through
	def user(self):
		db = DB()

		# this method will return either one or all users based on id
		# if id == * all users are returned
		if (request.method == "GET"):
			email = request.params['email']
			if email == '*':
				# users = db.getUsers()
				# check output
				# return json.dumps(users)
				return "returns all users"
			else:
				# user = db.getUser(email)
				# check output
				# return json.dumps(user)
				return "returns user with email " + email

		# this method works for real - just need to figure out host site links to people in the database
		# should this return the user's ID?
		elif (request.method == "PUT"):
			email = request.params['email']
			if(db.userExists(email)):
				# Update user
				# db.updateUser(request.params['email'], request.params['new_email'], request.params['password'], request.params['first_name'], request.params['last_name'], request.params['role'], request.params['phone_number'])
				return "update user" # unimplemented until db is ready
			else:
				# TODO check for errors from database
				# Add new user
				user = User(request.params['email'], request.params['password'], request.params['first_name'], request.params['last_name'], request.params['role'], request.params['phone_number'])
				db.addUserModel(user)
				return "{\"success\":\"true\"}"

		# we might not implement this
		elif (request.method == "DELETE"):
			return "{\"success\":\"false\", \"message\":\"Unimplemented method\"}"

		else:
			return "{\"success\":\"false\",\"message\":\"Bad request method\"}"

	def logout(self):
		if(request.cookies.get("FCS_GFB_Cookie") != None):
			response.delete_cookie("FCS_GFB_Cookie")
		return true_string

	def login(self):
		return render('/login.mako')

	def auth(self):
		db = DB()
		if (request.method == "GET"):
			# authenticate with the database controller, assume that login is setting request params with username and password
			# I want the role
			# success = authUser(email, password)
			success = True

			if(success):
				# role, username, password
				# user = db.getUser()
				# cookie = Cookie(email, password, user.get('role'))

				cookie = Cookie('miakilborn', 'thisismypassword!', '1')
				response.set_cookie("FCS_GFB_Cookie", cookie.encryptCookie(), max_age=180*24*3600)
				return true_string
			else:
				return "{\"success\" : \"false\", \"message\" : \"Unable to login: bad username or password\"}"
		else:
			return "{\"success\" : \"false\", \"message\" : \"\"}"


	def me(self):
		cookie = request.cookies.get("FCS_GFB_Cookie")	
		if(cookie == None):
			return ''
		else:
			decode = Cookie.decryptCookie(cookie)
			return decode