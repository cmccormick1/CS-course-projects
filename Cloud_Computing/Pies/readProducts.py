#! /usr/bin/python3

import cgi
import MySQLdb
import passwords

# Connect to database and select entire products table
conn = MySQLdb.connect(host = passwords.SQL_HOST, user = passwords.SQL_USER, \
                       passwd = passwords.SQL_PASSWD, db = "projects_database")
cursor = conn.cursor()
cursor.execute("SELECT * FROM products;")
results = cursor.fetchall()
cursor.close()

# Start HTML page
print("Content-Type: text/html")
print("Status: 200 OK")
print()

print("<html>")
print("<head><title>View Products</title></head>")
print("<body>")
print("<center>")

# Display a table of products in the database
print("<p>Current Products:")

print("<table border=1>")
print("<tr><th>Product ID</th><th>Pie Name</th><th>Price ($)</th><th>Calories (entire pie)</th></tr>")

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
conn.close()
