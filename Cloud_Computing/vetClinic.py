#! /usr/bin/python3

import passwords
import cgi
import MySQLdb
import os
import json
import sys


def main():
	# Connect to database
	conn = MySQLdb.connect(host = passwords.SQL_HOST, user = passwords.SQL_USER, \
                               passwd = passwords.SQL_PASSWD, db = "projects_database")

	website = "http://ec2-3-89-159-48.compute-1.amazonaws.com/cgi-bin/vetClinic.py"
	my_path = ""
	# Check if PATH_INFO exists
	if "PATH_INFO" in os.environ:
		my_path = os.environ["PATH_INFO"]

	if my_path.startswith("/people"):
		if os.environ["REQUEST_METHOD"] == "GET":
			people_GET(conn, website, my_path)
		elif os.environ["REQUEST_METHOD"] == "POST":
			people_POST(conn, website)
		elif os.environ["REQUEST_METHOD"] == "DELETE":
			people_DELETE(conn, website, my_path)
		else:
			send_bad_request()
	elif my_path.startswith("/pets"):
		if os.environ["REQUEST_METHOD"] == "GET":
			pets_GET(conn, website, my_path)
		elif os.environ["REQUEST_METHOD"] == "POST":
			pets_POST(conn, website)
		elif os.environ["REQUEST_METHOD"] == "PUT":
			pets_PUT(conn, website, my_path)
		else:
			send_bad_request()
	else:
		print("Status: 404 Not Found")
		print()

	conn.close()


def people_GET(conn, website, my_path):
	# Get ID from path if provided
	people_id = -1
	if my_path[7:] != "" and my_path[7:] != "/":
		try:
			people_id = int(my_path[8:])
		except:
			print("Status: 404 Not Found")
			print()
			return

	cursor = conn.cursor()
	if people_id == -1:
		# Select all people from the database if no ID is given
		cursor.execute("SELECT * FROM people;")
	else:
		# Select person from the database with given ID
		cursor.execute("SELECT * FROM people WHERE peopleID=%s;", (people_id,))
	results = cursor.fetchall()
	cursor.close()

	# If ID is invalid
	if len(results) == 0 and people_id != -1:
		print("Status: 404 Not Found")
		print()
		return

	# Format JSON object(s) with person link
	people_arr = []
	for i in range(len(results)):
		person = {}
		person["peopleID"] = results[i][0]
		person["last_name"] = results[i][1]
		person["first_name"] = results[i][2]
		person["address"] = results[i][3]
		person["link"] = website + "/people/" + str(results[i][0])
		people_arr.append(person)

	# Display JSON object(s)
	print("Content-Type: application/json")
	print("Status: 200 OK")
	print()

	print(json.dumps(people_arr, indent=2))


def people_POST(conn, website):
	# Read input JSON object as a Python dictionary
	input_data = sys.stdin.read()
	data_arr = json.loads(input_data)
	for person in data_arr:
		# If last name and/or first name is not provided
		if "last_name" not in person.keys() or "first_name" not in person.keys():
			print("Status: 400 Bad Request")
			print()
			return
		last_name = person["last_name"]
		first_name = person["first_name"]
		if "address" not in person.keys():
			# If address is not providede, set to default value
			address = "100 default address way"
		else:
			address = person["address"]

		# Insert new record into people table
		cursor = conn.cursor()
		cursor.execute("INSERT INTO people(last_name,first_name,address) VALUES(%s,%s,%s);", \
                               (last_name, first_name, address))
		conn.commit()
		cursor.close()

	# Redirect to /people (GET /people)
	print("Status: 302 Redirect")
	print("Location: " + website + "/people")
	print()


def people_DELETE(conn, website, my_path):
	# Get ID from path (must be provided)
	people_id = -1
	if my_path[7:] != "" and my_path[7:] != "/":
		try:
			people_id = int(my_path[8:])
		except:
			print("Status: 404 Not Found")
			print()
			return

	cursor = conn.cursor()
	if people_id >= 0:
		# Make sure people ID is valid
		cursor.execute("SELECT * FROM people WHERE peopleID=%s;", (people_id,))
		results = cursor.fetchall()
		if len(results) == 0:
			print("Status: 404 Not Found")
			print()
			return

		# Delete the person of the given ID and their pets
		cursor.execute("DELETE FROM pets WHERE peopleID=%s;", (people_id,))
		cursor.execute("DELETE FROM people WHERE peopleID=%s;", (people_id,))
	else:
		# If no ID is given
		print("Status: 400 Bad Request")
		print()
		return
	conn.commit()
	cursor.close()

	# Redirect to /people (GET /people)
	print("Status: 302 Redirect")
	print("Location: " + website + "/people")
	print()


def pets_GET(conn, website, my_path):
	# Get ID from path if provided
	pets_id = -1
	if my_path[5:] != "" and my_path[5:] != "/":
		try:
			pets_id = int(my_path[6:])
		except:
			print("Status: 404 Not Found")
			print()
			return

	cursor = conn.cursor()
	if pets_id == -1:
		# Select all pets from the database if no ID is given
		cursor.execute("SELECT * FROM pets;")
	else:
		# Select pet from the database with given ID
		cursor.execute("SELECT * FROM pets WHERE petID=%s;", (pets_id,))
	results = cursor.fetchall()
	cursor.close()

	# If ID is invalid
	if len(results) == 0:
		print("Status: 404 Not Found")
		print()
		return

	# Format JSON object(s) with pet and person links
	pets_arr = []
	for i in range(len(results)):
		pet = {}
		pet["petID"] = results[i][0]
		pet["name"] = results[i][2]
		pet["breed"] = results[i][3]
		pet["age"] = results[i][4]
		pet["link"] = website + "/pets/" + str(results[i][0])
		pet["owner_link"] = website + "/people/" + str(results[i][1])
		pets_arr.append(pet)

	# Display JSON object(s)
	print("Content-Type: application/json")
	print("Status: 200 OK")
	print()

	print(json.dumps(pets_arr, indent=2))


def pets_POST(conn, website):
	# Read input JSON object as a Python dictionary
	input_data = sys.stdin.read()
	data_arr = json.loads(input_data)
	for pet in data_arr:
		# If people ID and/or name and/or breed is not provided
		if "peopleID" not in pet.keys() or "name" not in pet.keys() or "breed" not in pet.keys():
			print("Status: 400 Bad Request")
			print()
			return
		peopleID = pet["peopleID"]
		name = pet["name"]
		breed = pet["breed"]
		if "age" not in pet.keys():
			# If age is not provided, set to default value
			age = 5
		else:
			age = pet["age"]

		# Insert new record into pets table
		cursor = conn.cursor()
		cursor.execute("INSERT INTO pets(peopleID,name,breed,age) VALUES(%s,%s,%s,%s);", \
                               (peopleID, name, breed, age))
		conn.commit()
		cursor.close()

	# Redirect to /pets (GET /pets)
	print("Status: 302 Redirect")
	print("Location: " + website + "/pets")
	print()


def pets_PUT(conn, website, my_path):
	# Get ID from path (must be provided)
	pets_id = -1
	if my_path[5:] != "" and my_path[5:] != "/":
		try:
			pets_id = int(my_path[6:])
		except:
			print("Status: 404 Not Found")
			print()
			return

	# Read input JSON object as a Python dictionary
	input_data = sys.stdin.read()
	data_arr = json.loads(input_data)

	# Check if pet ID given is valid
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM pets WHERE petID=%s;", (pets_id,))
	results = cursor.fetchall()
	if len(results) > 0:
		# Change the pet's name in the database
		if "name" not in data_arr[0].keys():
			print("Status: 400 Bad Request")
			print()
			return
		cursor.execute("UPDATE pets SET name=%s WHERE petID=%s;", (data_arr[0]["name"], pets_id))
		if "peopleID" in data_arr[0].keys():
			# Change the pet's owner, i.e. peopleID, if given
			cursor.execute("UPDATE pets SET peopleID=%s WHERE petID=%s;", \
                                       (data_arr[0]["peopleID"], pets_id))
		if "age" in data_arr[0].keys():
			# Change the pet's age if given
			cursor.execute("UPDATE pets SET age=%s WHERE petID=%s;", (data_arr[0]["age"], pets_id))
	else:
		print("Status: 404 Not Found")
		print()
		return
	conn.commit()
	cursor.close()

	# Redirect to /pets (GET /pets)
	print("Status: 302 Redirect")
	print("Location: " + website + "/pets")
	print()


def send_bad_request():
	# If request given is not GET, POST, PUT, or DELETE
	print("Status: 405 Method Not Allowed")
	print()


main()
