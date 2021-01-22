#! /usr/bin/python3

import cgi
import random


# Initial health and trip count
jack_health = 100
jill_health = 100
trip_count = 0

# Get updated health and trip data (from last trip)
form = cgi.FieldStorage()
if "JackHealth" in form:
	jack_health = int(form["JackHealth"].value)

if "JillHealth" in form:
	jill_health = int(form["JillHealth"].value)

if "TripCount" in form:
	trip_count = int(form["TripCount"].value)

# Calculate damage and how much Jill heals
damage = random.randint(1, 20)
heal = random.randint(1, damage)
jack_new_health = jack_health - damage
jill_new_health = jill_health - damage + heal
trip_new_count = trip_count + 1


# Start html page
print("Content-Type: text/html")
print("Status: 200 OK")
print()

print("<html>")
print("<head><title>Jack and Jill Game</title></head>")
print("<body>")
print("<center>")

button_msg = "Send Jack and Jill up the hill!"
if trip_count == 0:
	# Initial screen
	print("<p>Welcome to the Jack and Jill game!</p>")
elif jack_health <= 0 or jill_health <= 0:
	# When either Jack or Jill dies
	print("<p>Game over</p>")
	button_msg = "Start game over"
	# Reset health and trip count
	jack_new_health = 100
	jill_new_health = 100
	trip_new_count = 0
else:
	# In the middle of a game
	print("<p>Jack and Jill went up the hill!</p>")
	print("<p>Jack and Jill fell down the hill!</p>")

# Display current health and trip count and save data from this round
print("<form action='/cgi-bin/jackJill.py' method='post'>")
print("<label for='JackHealth'>Jack\'s Health: {}</label><br>".format(jack_health))
print("<input type='hidden' id='JackHealth' name='JackHealth' value='{}'>".format(jack_new_health))
print("<label for='JillHealth'>Jill\'s Health: {}</label><br>".format(jill_health))
print("<input type='hidden' id='JillHealth' name='JillHealth' value='{}'>".format(jill_new_health))
print("<label for='TripCount'>Number of Trips Up and Down the Hill: {}</label><br><br>".format(trip_count))
print("<input type='hidden' id='TripCount' name='TripCount' value='{}'>".format(trip_new_count))
print("<input type='submit' value='{}'>".format(button_msg))
print("</form>")

print("</center>")
print("</body>")
print("</html>")
