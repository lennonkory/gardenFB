import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from ast import literal_eval
from gardenfreshbox.lib.base import BaseController, render

log = logging.getLogger(__name__)

class IndexController(BaseController):

	def index(self):
		return render('/index.mako');

	def contact(self):
		return render('/contact/contact.mako')

	def info(self):
		return render('info/info.mako')