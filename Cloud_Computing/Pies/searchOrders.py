#! /usr/bin/python3

import cgi
import MySQLdb
import passwords

# Connect to database
conn = MySQLdb.connect(host = passwords.SQL_HOST, user = passwords.SQL_USER, \
                       passwd = passwords.SQL_PASSWD, db = "projects_database")
cursor = conn.cursor()

product_id = None

# Check if the user had previously entered data (stored in cgi fields)
form = cgi.FieldStorage()
if "productID" in form:
	try:
		product_id = int(form["productID"].value)
	except:
		product_id = "incorrect type"

# Start HTML page
print("Content-Type: text/html")
print("Status: 200 OK")
print()

print("<html>")
print("<head><title>Search for Orders</title></head>")
print("<body>")
print("<center>")

if product_id == "incorrect type":
	# If the user enters the wrong data type (e.g. words instead of a number), then display
	# an error message and prompt them to try again
	print("<p>Incorrect product ID entered - please enter an integer.")
	print("<a href='/cgi-bin/searchOrders.py'>Try again</a>")
elif product_id == None:
	# If product_id is not given, then prompt user to enter product_id
	print("<p>Enter the product ID number to find orders of that product:")
	print("<form action='/cgi-bin/searchOrders.py' method='post'>")
	print("<label for='productID'>Product ID:</label><br>")
	print("<input type='text' id='productID' name='productID'><br>")
	print("<input type='submit' value='Search'>")
	print("</form>")
else:
	# If product_id is given, then select records from orders table joined with data from
	# the products table for the given product_id
	cursor.execute("SELECT * FROM orders,products WHERE orders.productID=%s AND" + \
                       " orders.productID=products.productID;", (product_id,))
	results = cursor.fetchall()

	# Display the results of the search in a table
	print("<table border=1>")
	print("<tr><th>Order ID</th><th>Product ID</th><th>Customer Name</th><th>Shipping Address</th>")
	print("<th>Total Price ($)</th><th>Product ID</th><th>Pie Name</th><th>Price ($)</th><th>Calories</th></tr>")
	for i in range(len(results)):
		print("<tr>")
		for j in range(len(results[i])):
			print("<td style='text-align:center'>" + str(results[i][j]) + "</td>")
		print("</tr>")
	print("</table>")

# Link back to home page
print("<p><a href='/index.html'>Go back to the home page</a>")

print("</center>")
print("</body>")
print("</html>")

# Close database connection
cursor.close()
conn.close()

