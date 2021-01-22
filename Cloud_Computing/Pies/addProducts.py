#! /usr/bin/python3

import cgi
import MySQLdb
import passwords

# Connect to database
conn = MySQLdb.connect(host = passwords.SQL_HOST, user = passwords.SQL_USER, \
                       passwd = passwords.SQL_PASSWD, db = "projects_database")
cursor = conn.cursor()

product_name = None
pie_price = None
cals = None

# Check if the user had previously entered data (stored in cgi fields)
form = cgi.FieldStorage()
if "productName" in form:
	product_name = form["productName"].value
if "price" in form:
	try:
		pie_price = float(form["price"].value)
	except:
		pie_price = None
if "calories" in form:
	try:
		cals = int(form["calories"].value)
	except:
		cals = None

# Start HTML page
print("Content-Type: text/html")
print("Status: 200 OK")
print()

print("<html>")
print("<head><title>Add Product to Database</title></head>")
print("<body>")
print("<center>")

if product_name != None and pie_price != None:
	# If product_name and price given (calories can be null), then insert new record
	cursor.execute("INSERT INTO products(product_name,price,calories) VALUES (%s, %s, %s);", \
                       (product_name, pie_price, cals))
	# Display the data entered by the user
	print("<p>Data entered:")
	print("<p>Product Name: " + product_name)
	print("<p>Pie Price ($): " + "{:0,.2f}".format(pie_price))
	print("<p>Calories (if known): " + str(cals))
elif product_name == None and pie_price == None:
	# If product_name and price are not given, then prompt user to enter data
	print("<p>Enter the pie name, price of the whole pie, and calories (if known).")
	print("<br>e.g. Blueberry pie, 12.25, 2900")
	print("<form action='/cgi-bin/addProducts.py' method='post'>")
	print("<label for='productName'>Product Name:</label><br>")
	print("<input type='text' id='productName' name='productName'><br>")
	print("<label for='price'>Price ($):</label><br>")
	print("<input type='text' id='price' name='price'><br>")
	print("<label for='calories'>Calories:</label><br>")
	print("<input type='text' id='calories' name='calories'><br>")
	print("<input type='submit' value='Add Product'>")
	print("</form>")
else:
	# If user enters wrong data types or leaves an essential field blank, then
	# display an error message and prompt them to try again
	print("<p>Missing one or more fields. <a href='/cgi-bin/addProducts.py'>Try again</a>")

# Link back to home page
print("<p><a href='/index.html'>Go back to the home page</a>")

print("</center>")
print("</body>")
print("</html>")

# Commit changes to database and close connection
cursor.close()
conn.commit()
conn.close()
