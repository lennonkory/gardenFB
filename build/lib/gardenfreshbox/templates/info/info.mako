<!DOCTYPE html>
<html lang="en">

	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="description" content="Garden Fresh Box">
		<meta name="author" content="Fruitful Community Solutions">

		<title>Garden Fresh Box - Information</title>

		<!-- Bootstrap Core CSS -->
		<link href="../css/bootstrap.min.css" rel="stylesheet">

		<!-- Custom CSS -->
		<link href="../css/custom.css" rel="stylesheet">
			<style>
			table, th, td {
			    border: 1px solid black;
			    border-collapse: collapse;
			}
			th, td {
			    padding: 5px;
			}
			</style>
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

				<div><h1>Garden Fresh Box</h1></div>

					<div>
						<h1>About</h1>
					</div>
					<div>
						<p>The Garden Fresh Box Program is a non-profit, fresh produce buying service created to help people access affordable fresh fruits and vegetables and also to support our local farmers. We are affiliated with the Guelph Wellington Local Food. It is delivered to their neighbourhood on the third Wednesday of the month. Payment must be received at the site no later than noon on the first Friday of the month.</p>
					</div>

					<div>
						<h1>Due & Delivery Dates</h1>
					</div>
					<div>
						<table style="width:100%">
							<tr>
								<th>ORDERS DUE BY FRIDAY</th>
								<th>PICK UP DUE ON WEDNESDAY</th>		
							</tr>
								<tr>
								<th>2014</td>
								<th>2014</td>		
							</tr>
								<tr>
								<td>November 7</td>
								<td>November 19</td>		
							</tr>
							<tr>
								<td>December 5</td>
								<td>December 17</td>		
							</tr>
							<tr>
								<th>2015</td>
								<th>2015</td>		
							</tr>
							<tr>
								<td>January 9</td>
								<td>January 21</td>		
							</tr>
							<tr>
								<td>February 6</td>
								<td>February 18</td>		
							</tr>
							<tr>
								<td>March 6</td>
								<td>March 18</td>		
							</tr>
							<tr>
								<td>April 3</td>
								<td>April 15</td>		
							</tr>
							<tr>
								<td>May 8</td>
								<td>May 20</td>		
							</tr>
						</table>
					</div>

			</div>

			<%include file="../footer.mako"/>

		</div><!--End of body_div-->

	</body>

</html>
