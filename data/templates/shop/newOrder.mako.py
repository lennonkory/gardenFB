# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457038820.299221
_enable_loop = True
_template_filename = '/Volumes/NO NAME/gardenFB/gardenfreshbox/templates/shop/newOrder.mako'
_template_uri = '/shop/newOrder.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\r\n<html lang="en">\r\n\r\n<head>\r\n\t<meta charset="utf-8">\r\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\r\n\t<meta name="description" content="Garden Fresh Box">\r\n\t<meta name="author" content="Fruitful Community Solutions">\r\n\r\n\t<title>Garden Fresh Box</title>\r\n\r\n\t<!-- Bootstrap Core CSS -->\r\n\t<link href="../css/bootstrap.min.css" rel="stylesheet">\r\n\r\n\t<!-- Custom CSS -->\r\n\t<link href="../css/custom.css" rel="stylesheet">\r\n</head>\r\n\r\n<body>\r\n\r\n\t<!-- jQuery -->\r\n\t<script src="../js/jquery.js"></script>\r\n\r\n\t<!-- Bootstrap Core JavaScript -->\r\n\t<script src="../js/bootstrap.min.js"></script>\r\n\r\n\r\n\r\n\t<div class="body_div">\r\n\r\n\t\t\t<!-- header file containing the main nav bar and logo -->\r\n\t\t\t')
        runtime._include_file(context, u'../header.mako', _template_uri)
        __M_writer(u'\r\n\r\n\t\t\t<div class="content">\r\n\r\n\r\n\t\t\t\t<div><h1>Shopping new order</h1></div>\r\n\t\t\t\t<div>\r\n\t\t\t\t\tCreation Date: <br>\r\n\t\t\t\t\t<input type="text" id="creation_date" value="">\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\tDistributed Date: <br>\r\n\t\t\t\t\t<input type="text" id="dist_date" value="">\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\tFirst Name: <br>\r\n\t\t\t\t\t<input type="text" id="first_name" value="">\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\tLast Name: <br>\r\n\t\t\t\t\t<input type="text" id="last_name" value="">\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\tEmail: <br>\r\n\t\t\t\t\t<input type="text" id="email" value="">\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\tAddress: <br>\r\n\t\t\t\t\t<input type="text" id="mail_address" value="">\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\tPhone Number: <br>\r\n\t\t\t\t\t<input type="text" id="phone" value="">\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\tNumber of Small Boxes: <br>\r\n\t\t\t\t\t<input type="text" id="num_sm" value="">\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\tNumber of Large Boxes: <br>\r\n\t\t\t\t\t<input type="text" id="num_lg" value="">\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\tNotify: <br>\r\n\t\t\t\t\t<input type="text" id="notify" value="">\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\tDonation: <br>\r\n\t\t\t\t\t<input type="text" id="donation" value="">\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\tDonation Reciept: <br>\r\n\t\t\t\t\t<input type="text" id="donation_receipt" value="">\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\tAmount Paid: <br>\r\n\t\t\t\t\t<input type="text" id="amt_paid" value="">\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\tHost Site Pickup: <br>\r\n\t\t\t\t\t<input type="text" id="hs_pickup" value="">\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\tHost Site Ordered: <br>\r\n\t\t\t\t\t<input type="text" id="hs_ordered" value="">\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\tVoucher: <br>\r\n\t\t\t\t\t<input type="text" id="vouchers" value="">\r\n\t\t\t\t\t<br>\r\n\t\t\t\t\t<input type="submit" id="submitButton" value="Submit Order" class="btn btn-submit">\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\r\n\t\t\t')
        runtime._include_file(context, u'../footer.mako', _template_uri)
        __M_writer(u'\r\n\r\n\t\t</div><!--End of body_div-->\r\n\r\n\t<script type="text/javascript">\r\n\t\t$("#submitButton").click(function(e) {\r\n\t\t\t$.ajax({\r\n\t\t\t\ttype: \'put\',\r\n\t\t\t\turl: \'/order\',\r\n\t\t\t\tdata: {\r\n\t\t\t\t\tcreation_date : $("#creation_date").val(),\r\n\t\t\t\t\tdist_date : $("#dist_date").val(),\r\n\t\t\t\t\tfirst_name : $("#first_name").val(),\r\n\t\t\t\t\tlast_name : $("#last_name").val(),\r\n\t\t\t\t\temail : $("#email").val(),\r\n\t\t\t\t\tmail_address : $("#mail_address").val(),\r\n\t\t\t\t\tphone : $("#phone").val(),\r\n\t\t\t\t\tnum_sm : $("#num_sm").val(),\r\n\t\t\t\t\tnum_lg : $("#num_lg").val(),\r\n\t\t\t\t\tnotify : $("#notify").val(),\r\n\t\t\t\t\tdonation : $("#donation").val(),\r\n\t\t\t\t\tdonation_receipt : $("#donation_receipt").val(),\r\n\t\t\t\t\tamt_paid : $("#amt_paid").val(),\r\n\t\t\t\t\ths_pickup : $("#hs_pickup").val(),\r\n\t\t\t\t\ths_ordered : $("#hs_ordered").val(),\r\n\t\t\t\t\tvouchers : $("#vouchers").val(),\r\n\t\t\t\t\torder_id : ""\r\n\t\t\t\t},\r\n\t\t\t\tsuccess: function(response) {\r\n\t\t\t\t\t//not doing response checking\r\n\t\t\t\t\tvar resp = JSON.parse(response);\r\n\t\t\t\t\tif (resp.success == "false"){\r\n\t\t\t\t\t\talert(resp.message);\r\n\t\t\t\t\t}\r\n\t\t\t\t}\r\n\t\t\t});\r\n\t\t});\r\n\t</script>\r\n\r\n\t</body>\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 26, "17": 0, "22": 1, "23": 33, "24": 33, "25": 92, "26": 92}, "uri": "/shop/newOrder.mako", "filename": "/Volumes/NO NAME/gardenFB/gardenfreshbox/templates/shop/newOrder.mako"}
__M_END_METADATA
"""
