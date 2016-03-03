import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from ast import literal_eval
from gardenfreshbox.lib.base import BaseController, render

from gardenfreshbox.model.cookie import Cookie
from gardenfreshbox.model.hostsite import HostSite
from gardenfreshbox.model.GFBDatabaseController import GFBDatabaseController as DB

log = logging.getLogger(__name__)

class HostsitesController(BaseController):

	# TODO :: probably use cookies here, make sure that the client cookie actually comes through
	def host_site(self):
		db = DB()

		# this method will return either one or all users based on id
		# if id == * all users are returned
		if (request.method == "GET"):
			hs_id = request.params['hostSiteID']
			if hs_id == '*':
				# host_sites = db.getAllHostSites()
				return "returns all host sites"
			else:
				# host_site = db.getHostSite(hostSiteID)
				return "returns host site with id " + hs_id

		elif (request.method == "PUT"):
			hs_id = request.params['hostSiteID']
			if(hs_id == ""):
				# New host site
				hs = HostSite(request.params['name'], request.params['address'], request.params['city'], request.params['province'], request.params['postal_code'], request.params['coordinatorIDs'], request.params['hours_of_operation'])
				# db.addHostSiteModel(hs)
				return "{\"success\":\"true\"} - New host site"
			else:
				# update host site
				hs = HostSite(request.params['name'], request.params['address'], request.params['city'], request.params['province'], request.params['postal_code'], request.params['coordinatorIDs'], request.params['hours_of_operation'])
				hs.id = hs_id
				# db.updateHostSiteModel(hs)
				return "{\"success\":\"true\"} - update host site"

		elif (request.method == "DELETE"):
			hs_id = request.params['hostSiteID']
			if (hs_id == "") or (hs_id == '*'):
				return "{\"success\":\"false\", \"message\":\"Bad Host Site ID\"}"
			else:
				# db.removeHostSite(hs_id)
				return "{\"success\":\"true\"} - delete host site"