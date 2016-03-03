# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457038817.287493
_enable_loop = True
_template_filename = '/Volumes/NO NAME/gardenFB/gardenfreshbox/templates/info/info.mako'
_template_uri = 'info/info.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\r\n<html lang="en">\r\n\r\n\t<head>\r\n\t\t<meta charset="utf-8">\r\n\t\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n\t\t<meta name="viewport" content="width=device-width, initial-scale=1">\r\n\t\t<meta name="description" content="Garden Fresh Box">\r\n\t\t<meta name="author" content="Fruitful Community Solutions">\r\n\r\n\t\t<title>Garden Fresh Box - Information</title>\r\n\r\n\t\t<!-- Bootstrap Core CSS -->\r\n\t\t<link href="../css/bootstrap.min.css" rel="stylesheet">\r\n\r\n\t\t<!-- Custom CSS -->\r\n\t\t<link href="../css/custom.css" rel="stylesheet">\r\n\t\t\t<style>\r\n\t\t\ttable, th, td {\r\n\t\t\t    border: 1px solid black;\r\n\t\t\t    border-collapse: collapse;\r\n\t\t\t}\r\n\t\t\tth, td {\r\n\t\t\t    padding: 5px;\r\n\t\t\t}\r\n\t\t\t</style>\r\n\t</head>\r\n\r\n\t<body>\r\n\r\n\t\t<!-- jQuery -->\r\n\t\t<script src="js/jquery.js"></script>\r\n\r\n\t\t<!-- Bootstrap Core JavaScript -->\r\n\t\t<script src="js/bootstrap.min.js"></script>\r\n\r\n\r\n\r\n\t\t<div class="body_div">\r\n\r\n\t\t\t<!-- header file containing the main nav bar and logo -->\r\n\t\t\t')
        runtime._include_file(context, u'../header.mako', _template_uri)
        __M_writer(u'\r\n\r\n\t\t\t<div class="content">\r\n\r\n\t\t\t\t<div><h1>Garden Fresh Box</h1></div>\r\n\r\n\t\t\t\t\t<div>\r\n\t\t\t\t\t\t<h1>About</h1>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<div>\r\n\t\t\t\t\t\t<p>The Garden Fresh Box Program is a non-profit, fresh produce buying service created to help people access affordable fresh fruits and vegetables and also to support our local farmers. We are affiliated with the Guelph Wellington Local Food. It is delivered to their neighbourhood on the third Wednesday of the month. Payment must be received at the site no later than noon on the first Friday of the month.</p>\r\n\t\t\t\t\t</div>\r\n\r\n\t\t\t\t\t<div>\r\n\t\t\t\t\t\t<h1>Due & Delivery Dates</h1>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<div>\r\n\t\t\t\t\t\t<table style="width:100%">\r\n\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t<th>ORDERS DUE BY FRIDAY</th>\r\n\t\t\t\t\t\t\t\t<th>PICK UP DUE ON WEDNESDAY</th>\t\t\r\n\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t<th>2014</td>\r\n\t\t\t\t\t\t\t\t<th>2014</td>\t\t\r\n\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t<td>November 7</td>\r\n\t\t\t\t\t\t\t\t<td>November 19</td>\t\t\r\n\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t<td>December 5</td>\r\n\t\t\t\t\t\t\t\t<td>December 17</td>\t\t\r\n\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t<th>2015</td>\r\n\t\t\t\t\t\t\t\t<th>2015</td>\t\t\r\n\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t<td>January 9</td>\r\n\t\t\t\t\t\t\t\t<td>January 21</td>\t\t\r\n\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t<td>February 6</td>\r\n\t\t\t\t\t\t\t\t<td>February 18</td>\t\t\r\n\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t<td>March 6</td>\r\n\t\t\t\t\t\t\t\t<td>March 18</td>\t\t\r\n\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t<td>April 3</td>\r\n\t\t\t\t\t\t\t\t<td>April 15</td>\t\t\r\n\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t<td>May 8</td>\r\n\t\t\t\t\t\t\t\t<td>May 20</td>\t\t\r\n\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t</table>\r\n\t\t\t\t\t</div>\r\n\r\n\t\t\t</div>\r\n\r\n\t\t\t')
        runtime._include_file(context, u'../footer.mako', _template_uri)
        __M_writer(u'\r\n\r\n\t\t</div><!--End of body_div-->\r\n\r\n\t</body>\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 26, "17": 0, "22": 1, "23": 42, "24": 42, "25": 105, "26": 105}, "uri": "info/info.mako", "filename": "/Volumes/NO NAME/gardenFB/gardenfreshbox/templates/info/info.mako"}
__M_END_METADATA
"""
