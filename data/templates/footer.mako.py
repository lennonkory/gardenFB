# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457038809.055663
_enable_loop = True
_template_filename = u'/Volumes/NO NAME/gardenFB/gardenfreshbox/templates/footer.mako'
_template_uri = u'/footer.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<div class="footer">\r\n\r\n\t<div class="footer_main">\r\n\r\n\t\t<div class="footer_contact">\r\n\t\t\t<div class="contact_us_heading">\r\n\t\t\t\t<h2 class="contact_us_heading">\r\n\t\t\t\t\tContact Us:\r\n\t\t\t\t</h2>\r\n\t\t\t</div>\r\n\t\t\t<div class="contact_us_info">\r\n\t\t\t\t<p class="contact_us">\r\n\t\t\t\t\tPhone: (519) 821-6638 ext. 344<br>\r\n\t\t\t\t\tEmail: <a href="mailto:gfbox@guelphchc.ca?Subject=Garden%20Fresh%20Box%20Feedback" target="_top">gfbox@guelphchc.ca</a><br>\r\n\t\t\t\t\tMailing: 176 Wyndham St. N, Guelph, ON, N1H 8N9\r\n\t\t\t\t\t<br>\r\n\t\t\t\t</p>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\r\n\t\t<div class="footer_login">\r\n\r\n\t\t\t<a href="/login" class="footer_login">\r\n\t\t\t\t<!-- <button class="btn btn-default">Login</button> -->\r\n\t\t\t\tLogin\r\n\t\t\t</a>\r\n\t\t</div>\r\n\t</div>\r\n\r\n\t<div class="footer_images">\r\n\t\t<img src="../images/GuelphCHCLogo.png" class="footer_images">\r\n\t\t<img src="../images/MinistryOfChildrenAndYouthServices.png" class="footer_images">\r\n\t\t<img src="../images/WaterlooWellingtonLocalHealthNetwork.png" class="footer_images">\r\n\t\t<img src="../images/OntarioCommunityHealth.png" class="footer_images">\r\n\t</div>\r\n\r\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "28": 22, "22": 1}, "uri": "/footer.mako", "filename": "/Volumes/NO NAME/gardenFB/gardenfreshbox/templates/footer.mako"}
__M_END_METADATA
"""
