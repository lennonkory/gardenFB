<!DOCTYPE html>
<html lang="en">

	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="description" content="Garden Fresh Box">
		<meta name="author" content="Fruitful Community Solutions">

		<title>Garden Fresh Box - Donate</title>

		<!-- Bootstrap Core CSS -->
		<link href="../css/bootstrap.min.css" rel="stylesheet">

		<!-- Custom CSS -->
		<link href="../css/custom.css" rel="stylesheet">
	</head>

	<body>

		<!-- jQuery -->
		<script src="js/jquery.js"></script>

		<!-- Bootstrap Core JavaScript -->
		<script src="js/bootstrap.min.js"></script>



		<div class="body_div">

			<!-- header file containing the main nav bar and logo -->
			<%include file="../header.mako"/>

			<div class="content">


				<div><h1>Donate Homepage</h1></div>
				<div>
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
					Donation Amount: <br>
					<input type="text" id="donation" value="">
					<br>
					Donation Receipt? (Y/N): <br>
					<input type="text" id="donation" value="">
					<br>
					<input type="submit" id="confirmDonate" value="Submit Donation" class="btn btn-submit">
				</div>

			</div>

			<%include file="../footer.mako"/>

		</div><!--End of body_div-->

	<script type="text/javascript">
		$("#confirmDonate").click(function(e) {
			$.ajax({
				type: 'put',
				url: '/donate',
				data: {
					first_name : $("#first_name").val(),
					last_name : $("#last_name").val(),
					email : $("#email").val(),
					mail_address : $("#mail_address").val(),
					phone : $("#phone").val(),
					donation : $("#donation").val(),
					donation_receipt : $("#donation_receipt").val(),
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
