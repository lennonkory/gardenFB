# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457039931.730169
_enable_loop = True
_template_filename = '/Users/kory/Documents/Code/gfb/gardenFB/gardenfreshbox/templates/login.mako'
_template_uri = '/login.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\r\n<html lang="en">\r\n\r\n\t<head>\r\n\t\t<meta charset="utf-8">\r\n\t\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n\t\t<meta name="viewport" content="width=device-width, initial-scale=1">\r\n\t\t<meta name="description" content="Garden Fresh Box">\r\n\t\t<meta name="author" content="Fruitful Community Solutions">\r\n\r\n\t\t<title>Garden Fresh Box - Login</title>\r\n\r\n\t\t<!-- Bootstrap Core CSS -->\r\n\t\t<link href="css/bootstrap.min.css" rel="stylesheet">\r\n\r\n\t\t<!-- Custom CSS -->\r\n\t\t<link href="css/custom.css" rel="stylesheet">\r\n\t</head>\r\n\r\n\t<body>\r\n\t\t<!-- jQuery -->\r\n\t\t<script src="js/jquery.js"></script>\r\n\r\n\t\t<!-- Bootstrap Core JavaScript -->\r\n\t\t<script src="js/bootstrap.min.js"></script>\r\n\r\n\r\n\t\t<div class="body_div">\r\n\r\n\t\t\t<!-- header file containing the main nav bar and logo -->\r\n\t\t\t')
        runtime._include_file(context, u'header.mako', _template_uri)
        __M_writer(u'\r\n\r\n\t\t\t<div class="content">\r\n\t\t\t\t<div class="login_page">\r\n\t\t\t\t\t<h1 class="login_page">Login</h1>\r\n\t\t\t\t\t<p class="content">\r\n\t\t\t\t\t\tPlease enter your email address and password to log in.\r\n\t\t\t\t\t</p>\r\n\t\t\t\t</div>\r\n\r\n\t\t\t\t<!-- <div class="login_page"> -->\r\n\t\t\t\t\t<div class="login_page_form">\r\n\t\t\t\t\t\t<label class="form_label">Email address</label>\r\n\t\t\t\t\t\t<input class="form_label_box" type="text" id="username" size="55em">\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<div class="login_page_form">\r\n\t\t\t\t\t\t<label class="form_label">Password</label>\r\n\t\t\t\t\t\t<input class="form_label_box" type="password" id="password" size="55em">\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<!-- <input id="submit" type="submit" class="btn btn-submit"> -->\r\n\t\t\t\t\t<div class="login_button_div">\r\n\t\t\t\t\t\t<input id="submit" type="submit" class="button_general">\r\n\t\t\t\t\t</div>\r\n\t\t\t\t<!-- </div> -->\r\n\t\t\t</div>\r\n\r\n\t\t\t')
        runtime._include_file(context, u'footer.mako', _template_uri)
        __M_writer(u'\r\n\r\n\t\t</div><!--End of body_div-->\r\n\r\n\t<script type="text/javascript">\r\n\t\t$("#submit").click(function(e) {\r\n\t\t\t$.ajax({\r\n\t\t\t\ttype: \'get\',\r\n\t\t\t\turl: \'/user/auth\',\r\n\t\t\t\tdata: {\r\n\t\t\t\t\tusername : $("#username").val(),\r\n\t\t\t\t\tpassword : $("#password").val()\r\n\t\t\t\t},\r\n\t\t\t\tsuccess: function(response) {\r\n\t\t\t\t\t//response will be JSON. response[\'success\'] = false, message will have a list of bad fields\r\n\t\t\t\t\talert(response);\r\n\t\t\t\t}\r\n\t\t\t});\r\n\t\t});\r\n\t</script>\r\n\r\n\r\n\t</body>\r\n\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 26, "17": 0, "22": 1, "23": 31, "24": 31, "25": 57, "26": 57}, "uri": "/login.mako", "filename": "/Users/kory/Documents/Code/gfb/gardenFB/gardenfreshbox/templates/login.mako"}
__M_END_METADATA
"""
