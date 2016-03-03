import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from ast import literal_eval
from gardenfreshbox.lib.base import BaseController, render
from gardenfreshbox.model.cookie import Cookie

log = logging.getLogger(__name__)

class ToolsController(BaseController):

	def index(self):
		#look at cookie
		cookie = request.cookies.get("FCS_GFB_Cookie")
		if(cookie == None):
			return "{\"success\":\"false\", \"message\":\"You must be logged in to see this page\"}"
		else:
			creds = Cookie.decryptCookie(cookie)
			if(creds.get('role') == '2'):
				return render('/tools/coordDash.mako')
			elif (creds.get('role') == '1'):
				return render('/tools/adminDash.mako')
			else:
				return "{\"success\":\"false\", \"message\":\"You must be a coordinator or administrator to see this page\"}"

	def manageHS(self):
		#look at cookie
		cookie = request.cookies.get("FCS_GFB_Cookie")
		if(cookie == None):
			return "{\"success\":\"false\", \"message\":\"You must be logged in to see this page\"}"
		else:
			creds = Cookie.decryptCookie(cookie)
			if(creds.get('role') == '2') or (creds.get('role') == '1'):
				return render("/tools/manageHS.mako");
			else:
				return "{\"success\":\"false\", \"message\":\"You must be a coordinator or administrator to see this page\"}"

	def manageAccounts(self):
		#look at cookie
		cookie = request.cookies.get("FCS_GFB_Cookie")
		if(cookie == None):
			return "{\"success\":\"false\", \"message\":\"You must be logged in to see this page\"}"
		else:
			creds = Cookie.decryptCookie(cookie)
			if(creds.get('role') == '2'):
				return None
			elif (creds.get('role') == '1'):
				return render('/tools/manageAccounts.mako')
			else:
				return "{\"success\":\"false\", \"message\":\"You must be a coordinator or administrator to see this page\"}"
