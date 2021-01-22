#! /usr/bin/python3

import cgi
import MySQLdb
import passwords

# Connect to database
conn = MySQLdb.connect(host = passwords.SQL_HOST, user = passwords.SQL_USER, \
                       passwd = passwords.SQL_PASSWD, db = "projects_database")
cursor = conn.cursor()

product_id = None
cust_name = None
ship_addr = None
total_price = None

# Check if the user had previously entered data (stored in cgi fields)
form = cgi.FieldStorage()
if "productID" in form:
	try:
		product_id = int(form["productID"].value)
	except:
		product_id = None
	# Check if the product_id given is in the products table
	if product_id != None:
		cursor.execute("SELECT productID FROM products WHERE productID=%s", (product_id,))
		if len(cursor.fetchall()) == 0:
			product_id = None
if "customerName" in form:
	cust_name = form["customerName"].value
if "shipAddr" in form:
	ship_addr = form["shipAddr"].value
if "totalPrice" in form:
	try:
		total_price = float(form["totalPrice"].value)
	except:
		total_price = None

# Start HTML page
print("Content-Type: text/html")
print("Status: 200 OK")
print()

print("<html>")
print("<head><title>Add Orders to Database</title></head>")
print("<body>")
print("<center>")

if product_id != None and cust_name != None and ship_addr != None and total_price != None:
	# If all fields are given and valid, then insert new record and display given information
	cursor.execute("INSERT INTO orders(productID,customer_name,shipping_addr,total_price) VALUES (%s, %s, %s, %s);",\
                       (product_id, cust_name, ship_addr, total_price))
	# Display the data entered
	print("<p>Data entered:")
	print("<p>Product ID: " + str(product_id))
	print("<p>Customer Name: " + cust_name)
	print("<p>Shipping Address: " + ship_addr)
	print("<p>Total Price ($): " + "{:0,.2f}".format(total_price))
elif product_id == None and cust_name == None and ship_addr == None and total_price == None:
	# If none of the fields are given, then prompt user to enter data
	cursor.close()
	# Show the products table to given the user product IDs to choose from
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM products;")
	results = cursor.fetchall()
	print("<p>Choose the product ID of the pie you want to order:")
	print("<table border=1>")
	print("<tr><th>Product ID</th><th>Pie Name</th><th>Price ($)</th><th>Calories (entire pie)</th></tr>")
	for i in range(len(results)):
		print("<tr>")
		for j in range(len(results[i])):
			print("<td style='text-align:center'>" + str(results[i][j]) + "</td>")
		print("</tr>")
	print("</table>")

	# Prompt user to enter data
	print("<p>Enter the product ID, customer\'s name, shipping address, and total price of the order" \
              + "(pie price + $2 shipping).")
	print("<br>e.g. 1, Caroline, 123 Pie Lane, 11.50")
	print("<form action='/cgi-bin/addOrders.py' method='post'>")
	print("<label for='productID'>Product ID:</label><br>")
	print("<input type='text' id='productID' name='productID'><br>")
	print("<label for='customerName'>Customer\'s Name:</label><br>")
	print("<input type='text' id='customerName' name='customerName'><br>")
	print("<label for='shipAddr'>Shipping Address:</label><br>")
	print("<input type='text' id='shipAddr' name='shipAddr'><br>")
	print("<label for='totalPrice'>Total Price ($):</label><br>")
	print("<input type='text' id='totalPrice' name='totalPrice'><br>")
	print("<input type='submit' value='Add Order'>")
	print("</form>")
else:
	# If user enters wrong data types or leaves a field blank, then display an error message and prompt
	# them to try again
	print("<p>Missing one or more fields, provided invalid product ID, or gave incorrect data format.")
	print("<a href='/cgi-bin/addOrders.py'>Try again.</a>")

# Link back to home page
print("<p><a href='/index.html'>Go back to the home page</a>")

print("</center>")
print("</body>")
print("</html>")

# Commit changes to database and close connection
cursor.close()
conn.commit()
conn.close()

