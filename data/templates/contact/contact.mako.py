# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457038932.328057
_enable_loop = True
_template_filename = '/Volumes/NO NAME/gardenFB/gardenfreshbox/templates/contact/contact.mako'
_template_uri = '/contact/contact.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\r\n<html lang="en">\r\n\r\n\t<head>\r\n\t\t<meta charset="utf-8">\r\n\t\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n\t\t<meta name="viewport" content="width=device-width, initial-scale=1">\r\n\t\t<meta name="description" content="Garden Fresh Box">\r\n\t\t<meta name="author" content="Fruitful Community Solutions">\r\n\r\n\t\t<title>Garden Fresh Box - Contact Us</title>\r\n\r\n\t\t<!-- Bootstrap Core CSS -->\r\n\t\t<link href="../css/bootstrap.min.css" rel="stylesheet">\r\n\r\n\t\t<!-- Custom CSS -->\r\n\t\t<link href="../css/custom.css" rel="stylesheet">\r\n\t</head>\r\n\r\n\t<body>\r\n\r\n\t\t<!-- jQuery -->\r\n\t\t<script src="js/jquery.js"></script>\r\n\r\n\t\t<!-- Bootstrap Core JavaScript -->\r\n\t\t<script src="js/bootstrap.min.js"></script>\r\n\r\n\r\n\r\n\t\t<div class="body_div">\r\n\r\n\t\t\t<!-- header file containing the main nav bar and logo -->\r\n\t\t\t')
        runtime._include_file(context, u'../header.mako', _template_uri)
        __M_writer(u'\r\n\r\n\t\t\t<div class="content">\r\n\t\t\t\t<div>\r\n\t\t\t\t\t<h1>Contact Us</h1>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div>\r\n\t\t\t\t\t<p>Have a question, comment, or concern?</p>\r\n\t\t\t\t\t<p>(519) 821-6638 ext. 344</p>\r\n\t\t\t\t\t<p><a href="mailto:gfbox@guelphchc.ca">gfbox@guelphchc.ca</a></p>\r\n\t\t\t\t\t<p>Guelph Community Health Centre<br>\r\n\t\t\t\t\tAttn: Garden Fresh Box<br>\r\n\t\t\t\t\t176 Wyndham St. N<br>\r\n\t\t\t\t\tGuelph, ON, N1H 8N9</p>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\r\n\t\t\t')
        runtime._include_file(context, u'../footer.mako', _template_uri)
        __M_writer(u'\r\n\r\n\t\t</div><!--End of body_div-->\r\n\r\n\t</body>\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 26, "17": 0, "22": 1, "23": 33, "24": 33, "25": 50, "26": 50}, "uri": "/contact/contact.mako", "filename": "/Volumes/NO NAME/gardenFB/gardenfreshbox/templates/contact/contact.mako"}
__M_END_METADATA
"""
