README for proj04: SQL

Author: Caroline McCormick\
Course: CSC 346, Fall 2020\
Purpose: For this project, I created a website for a pie shop (Caroline's Pies) which keeps
         track of products they sell and orders that have been made. The website allows the
         user to view all of the products the shop offers, view all of the orders that have
         been made, add products to the database, add orders to the database, and search
         for orders based on the product ID number.
         
Files:\
   index.html --> static home page for the website; it contains links to the other pages\
   readProducts.py --> cgi script that displays a table of all products in the database\
   readOrders.py --> cgi script that displays a table of all orders in the database\
   addProducts.py --> cgi script that allows a product to be added to the database; MUST
                      PROVIDE THE PRODUCT ID AND PRICE (calories is optional; format like
                      example)\
   addOrders.py --> cgi script that allows an order to be added to the database; MUST
                    PROVIDE ALL FIELDS (format like example)\
   searchOrders.py --> cgi script that displays all orders in the database that include
                       the given product ID; MUST GIVE A NUMBER FOR THE PRODUCT ID\
   TABLES.txt --> shows the MySQL configurations for the orders and products tables\
                       
 URL to home page:\
   http://ec2-3-89-159-48.compute-1.amazonaws.com/index.html
             
