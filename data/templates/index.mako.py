# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457038809.02584
_enable_loop = True
_template_filename = '/Volumes/NO NAME/gardenFB/gardenfreshbox/templates/index.mako'
_template_uri = '/index.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\r\n<html lang="en">\r\n\r\n\t<head>\r\n\t\t<meta charset="utf-8">\r\n\t\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n\t\t<meta name="viewport" content="width=device-width, initial-scale=1">\r\n\t\t<meta name="description" content="Garden Fresh Box">\r\n\t\t<meta name="author" content="Fruitful Community Solutions">\r\n\r\n\t\t<title>Garden Fresh Box</title>\r\n\r\n\t\t<!-- Bootstrap Core CSS -->\r\n\t\t<link href="css/bootstrap.min.css" rel="stylesheet">\r\n\r\n\t\t<!-- Custom CSS -->\r\n\t\t<link href="css/custom.css" rel="stylesheet">\r\n\t</head>\r\n\r\n\t<body>\r\n\t\t<!-- jQuery -->\r\n\t\t<script src="js/jquery.js"></script>\r\n\t\t<!-- Bootstrap Core JavaScript -->\r\n\t\t<script src="js/bootstrap.min.js"></script>\r\n\r\n\r\n\t\t<div class="body_div">\r\n\r\n\t\t\t<!-- header file containing the main nav bar and logo -->\r\n\t\t\t')
        runtime._include_file(context, u'header.mako', _template_uri)
        __M_writer(u'\r\n\r\n\r\n\t\t\t<div class="content">\r\n\r\n\t\t\t\t<!-- <div><h1>HomePage</h1></div> -->\r\n\t\t\t\t<div class="hero_image">\r\n\t\t\t\t\t<img src="../images/BannerImage.jpg" class="hero_image">\t\t\t\t\t\r\n\t\t\t\t</div>\r\n\r\n\t\t\t\t<div class="summary_buttons">\r\n\t\t\t\t\t<div class="summary_end">\r\n\t\t\t\t\t\t<a href="/shop/buy">\r\n\t\t\t\t\t\t\t<div class="summary_button" id="summary_buy_garden_fresh_box">\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t<div class="summary_heading">\r\n\t\t\t\t\t\t\t\t\t<h2 class="summary_button">\r\n\t\t\t\t\t\t\t\t\tBuy a Garden Fresh Box\r\n\t\t\t\t\t\t\t\t\t</h2>\r\n\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t<div class="summary_description">\r\n\t\t\t\t\t\t\t<p class="summary_button">\r\n\t\t\t\t\t\t\t\tShop for a Garden Fresh Box for yourself or your family.\r\n\t\t\t\t\t\t\t\t<br>\r\n\t\t\t\t\t\t\t\t<a href="/shop/buy">\r\n\t\t\t\t\t\t\t\tLearn More\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</p>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</div>\r\n\r\n\t\t\t\t\t<div class="summary_mid">\r\n\t\t\t\t\t\t<a href="/info">\r\n\t\t\t\t\t\t\t<div class="summary_button" id="summary_about_garden_fresh_box">\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t<div class="summary_heading">\r\n\t\t\t\t\t\t\t\t\t<h2 class="summary_button">\r\n\t\t\t\t\t\t\t\t\tAbout the Program\r\n\t\t\t\t\t\t\t\t\t</h2>\r\n\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t<div class="summary_description">\t\t\t\t\t\r\n\t\t\t\t\t\t\t<p class="summary_button">\r\n\t\t\t\t\t\t\t\tLearn more about the Garden Fresh Box Program and how we\'re helping Guelph.\r\n\t\t\t\t\t\t\t\t<br>\r\n\t\t\t\t\t\t\t\t<a href="/info">\r\n\t\t\t\t\t\t\t\tLearn More\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</p>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</div>\r\n\r\n\t\t\t\t\t<div class="summary_end">\r\n\t\t\t\t\t\t<a href="/contact">\r\n\t\t\t\t\t\t\t<div class="summary_button" id="summary_feedback_image">\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t<div class="summary_heading">\r\n\t\t\t\t\t\t\t\t\t<h2 class="summary_button">\r\n\t\t\t\t\t\t\t\t\tLeave Feedback\r\n\t\t\t\t\t\t\t\t\t</h2>\r\n\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t<div class="summary_description">\r\n\t\t\t\t\t\t\t<p class="summary_button">\r\n\t\t\t\t\t\t\t\tAre we doing a good job? Did you enjoy one of our recipes? Let the community know by leaving some feedback!\r\n\t\t\t\t\t\t\t\t<br>\r\n\t\t\t\t\t\t\t\t<a href="/contact">\r\n\t\t\t\t\t\t\t\tLearn More\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</p>\r\n\t\t\t\t\t\t</div>\t\t\t\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div><!-- End of summary buttons -->\r\n\r\n\t\t\t</div><!-- End of the content div -->\r\n\r\n\r\n\t\t\t')
        runtime._include_file(context, u'footer.mako', _template_uri)
        __M_writer(u'\r\n\t\t</div>\r\n\r\n\r\n\t</body>\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 26, "17": 0, "22": 1, "23": 30, "24": 30, "25": 110, "26": 110}, "uri": "/index.mako", "filename": "/Volumes/NO NAME/gardenFB/gardenfreshbox/templates/index.mako"}
__M_END_METADATA
"""
