# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457038809.042215
_enable_loop = True
_template_filename = u'/Volumes/NO NAME/gardenFB/gardenfreshbox/templates/header.mako'
_template_uri = u'/header.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<div class="header">\r\n\t<div class="logo_image">\r\n\t\t<a href="/">\r\n\t\t\t<img src="../images/LogoV4.png">\r\n\t\t</a>\r\n\t</div>\r\n\t<div class="regular_nav">\r\n\t\t<ul class="regular_nav">\r\n\t\t\t<li class="regular_nav">\r\n\t\t\t\t<a href="/">Home</a>\r\n\t\t\t</li>\r\n\t\t\t<li class="regular_nav">\r\n\t\t\t\t<a href="/info">Info</a>\r\n\t\t\t</li>\r\n\t\t\t<li class="regular_nav">\r\n\t\t\t\t<a href="/shop/buy">Buy</a>\r\n\t\t\t</li>\r\n\t\t\t<li class="regular_nav">\r\n\t\t\t\t<a href="/donate">Donate</a>\r\n\t\t\t</li>\r\n\t\t\t<li class="regular_nav">\r\n\t\t\t\t<a href="/contact">Contact Us</a>\r\n\t\t\t</li>\r\n\t\t</ul>\r\n\t</div>\r\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "28": 22, "22": 1}, "uri": "/header.mako", "filename": "/Volumes/NO NAME/gardenFB/gardenfreshbox/templates/header.mako"}
__M_END_METADATA
"""
