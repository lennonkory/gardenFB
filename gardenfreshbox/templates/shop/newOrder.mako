<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="Garden Fresh Box">
	<meta name="author" content="Fruitful Community Solutions">

	<title>Garden Fresh Box</title>

	<!-- Bootstrap Core CSS -->
	<link href="../css/bootstrap.min.css" rel="stylesheet">

	<!-- Custom CSS -->
	<link href="../css/custom.css" rel="stylesheet">
</head>

<body>

	<!-- jQuery -->
	<script src="../js/jquery.js"></script>

	<!-- Bootstrap Core JavaScript -->
	<script src="../js/bootstrap.min.js"></script>



	<div class="body_div">

			<!-- header file containing the main nav bar and logo -->
			<%include file="../header.mako"/>

			<div class="content">


				<div><h1>Shopping new order</h1></div>
				<div>
					Creation Date: <br>
					<input type="text" id="creation_date" value="">
					<br>
					Distributed Date: <br>
					<input type="text" id="dist_date" value="">
					<br>
					First Name: <br>
					<input type="text" id="first_name" value="">
					<br>
					Last Name: <br>
					<input type="text" id="last_name" value="">
					<br>
					Email: <br>
					<input type="text" id="email" value="">
					<br>
					Address: <br>
					<input type="text" id="mail_address" value="">
					<br>
					Phone Number: <br>
					<input type="text" id="phone" value="">
					<br>
					Number of Small Boxes: <br>
					<input type="text" id="num_sm" value="">
					<br>
					Number of Large Boxes: <br>
					<input type="text" id="num_lg" value="">
					<br>
					Notify: <br>
					<input type="text" id="notify" value="">
					<br>
					Donation: <br>
					<input type="text" id="donation" value="">
					<br>
					Donation Reciept: <br>
					<input type="text" id="donation_receipt" value="">
					<br>
					Amount Paid: <br>
					<input type="text" id="amt_paid" value="">
					<br>
					Host Site Pickup: <br>
					<input type="text" id="hs_pickup" value="">
					<br>
					Host Site Ordered: <br>
					<input type="text" id="hs_ordered" value="">
					<br>
					Voucher: <br>
					<input type="text" id="vouchers" value="">
					<br>
					<input type="submit" id="submitButton" value="Submit Order" class="btn btn-submit">
				</div>
			</div>

			<%include file="../footer.mako"/>

		</div><!--End of body_div-->

	<script type="text/javascript">
		$("#submitButton").click(function(e) {
			$.ajax({
				type: 'put',
				url: '/order',
				data: {
					creation_date : $("#creation_date").val(),
					dist_date : $("#dist_date").val(),
					first_name : $("#first_name").val(),
					last_name : $("#last_name").val(),
					email : $("#email").val(),
					mail_address : $("#mail_address").val(),
					phone : $("#phone").val(),
					num_sm : $("#num_sm").val(),
					num_lg : $("#num_lg").val(),
					notify : $("#notify").val(),
					donation : $("#donation").val(),
					donation_receipt : $("#donation_receipt").val(),
					amt_paid : $("#amt_paid").val(),
					hs_pickup : $("#hs_pickup").val(),
					hs_ordered : $("#hs_ordered").val(),
					vouchers : $("#vouchers").val(),
					order_id : ""
				},
				success: function(response) {
					//not doing response checking
					var resp = JSON.parse(response);
					if (resp.success == "false"){
						alert(resp.message);
					}
				}
			});
		});
	</script>

	</body>

</html>
