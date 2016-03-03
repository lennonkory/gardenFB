import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from ast import literal_eval
from gardenfreshbox.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ShopController(BaseController):

	def home(self):
		return render("/shop/home.mako");
	
	def newOrder(self):
		return render("/shop/newOrder.mako");
