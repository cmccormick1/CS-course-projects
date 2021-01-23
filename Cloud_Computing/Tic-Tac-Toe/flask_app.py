import cgi
import random
import passwords
import MySQLdb
from flask import Flask, request, render_template, url_for, redirect, make_response

app = Flask(__name__)


def get_cursor():
	# Connect to database
	conn = MySQLdb.connect(host = passwords.SQL_HOST, user = passwords.SQL_USER, \
                               passwd = passwords.SQL_PASSWD, db = "projects_database")
	cursor = conn.cursor()
	return cursor, conn


def check_session():
	# Check to make sure the session stored in the cookie exists and hasn't expired
	if "sessionID" in request.cookies:
		session_id = request.cookies.get("sessionID")
		cursor, conn = get_cursor()
		cursor.execute("SELECT * FROM sessions WHERE sessionID=%s AND expiration > NOW();", (session_id,))
		results = cursor.fetchall()
		cursor.close()
		if len(results) > 0:
			return True
	return False


def check_for_winner(board, xcoord, ycoord, marker):
	# Check for column win
	for i in range(0, 3):
		if board[xcoord][i] != marker:
			break
		if i == 2:
			return True

	# Check for row win
	for j in range(0, 3):
		if board[j][ycoord] != marker:
			break
		if j == 2:
			return True

	# Check for diagonal win
	if xcoord == ycoord:
		for k in range(0, 3):
			if board[k][k] != marker:
				break
			if k == 2:
				return True

	# Check for backwards diagonal win
	if (xcoord + ycoord) == 2:
		for m in range(0, 3):
			if board[m][2-m] != marker:
				break
			if m == 2:
				return True
	return False


@app.route("/", methods=['GET', 'POST'])
def root():
	# Show the contents of the home page
	if request.method == 'GET':
		if not check_session():
			return render_template("index.html")
		else:
			return redirect(url_for("startGame"))
	else:
		# Create session ID
		ID = random.randint(0, 16**64)
		ID_str = "%064x" % ID
		# Get username
		if "username" in request.form:
			username = request.form["username"]
			# Update sessions table with session number and username
			cursor, conn = get_cursor()
			cursor.execute("INSERT INTO sessions(sessionID, username, expiration) VALUES(%s,%s, ADDTIME(NOW(), '00:30:00'));", \
                                       (ID_str, username))
			conn.commit()
			cursor.close()
			resp = redirect(url_for("startGame"))
			resp.set_cookie("sessionID", ID_str)
			return resp
		# Redirect to start game
		return redirect(url_for("startGame"))


@app.route("/startGame", methods=['GET', 'POST'])
def startGame():
	# Display contents of page with all existing games and create new game button
	if request.method == 'GET':
		if not check_session():
			return redirect(url_for("root"))
		else:
			# Get username for this session
			session_id = request.cookies.get("sessionID")
			cursor, conn = get_cursor()
			cursor.execute("SELECT username FROM sessions WHERE sessionID=%s AND expiration > NOW();", \
                                       (session_id,))
			user_query = cursor.fetchall()
			username = user_query[0][0]
			cursor.close()

			# Get game ID and players for each existing game where username is one of the players
			cursor, conn = get_cursor()
			cursor.execute("SELECT gameID,player1,player2 FROM games WHERE player1=%s OR player2=%s;", \
                                       (username, username))
			results = cursor.fetchall()
			cursor.close()
			rows = {}
			for i in range(len(results)):
				if results[i][1] == username:
					rows[results[i][0]] = results[i][2]
				else:
					rows[results[i][0]] = results[i][1]
			resp = make_response(render_template("startGame.html", user=username, rows=rows))
			resp.set_cookie("sessionID", session_id)
			return resp
	else:
		if not check_session():
			return redirect(url_for("root"))
		else:
			# Get logged in person's username and opponent entered
			session_id = request.cookies.get("sessionID")
			player1 = ""
			player2 = ""
			if "Opponent" in request.form:
				player2 = request.form["Opponent"]
			cursor, conn = get_cursor()
			cursor.execute("SELECT username FROM sessions WHERE sessionID=%s AND expiration > NOW();", \
                                       (session_id,))
			results = cursor.fetchall()
			cursor.close()

			# Start new game by assigning logged in user to player1 (X) and opponent to player2 (O)
			player1 = results[0][0]
			if player1 == "" or player2 == "":
				resp = redirect(url_for("startGame"))
				resp.set_cookie("sessionID", session_id)
				return resp
			cursor, conn = get_cursor()
			cursor.execute("INSERT INTO games(player1, player2, player1_marker, player2_marker) VALUES" \
                                       + "(%s,%s,%s,%s);", (player1, player2, "X","O"))
			conn.commit()
			cursor.close()
			resp = redirect(url_for("startGame"))
			resp.set_cookie("sessionID", session_id)
			return resp



@app.route("/gameBoard", methods=['GET', 'POST'])
def gameBoard():
	# Display the contents of the current game board (including past moves for a game)
	if request.method == 'GET':
		if not check_session():
			return redirect(url_for("root"))
		else:
			session_id = request.cookies.get("sessionID")
			arr = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
			game_id = request.args["gameID"]

			# Get all past game moves (if any)
			cursor, conn = get_cursor()
			cursor.execute("SELECT * FROM gameMoves WHERE gameID=%s;", (game_id,))
			results = cursor.fetchall()
			cursor.close()

			# Get players' usernames
			cursor, conn = get_cursor()
			cursor.execute("SELECT player1,player2 FROM games WHERE gameID=%s;", (game_id,))
			user_results = cursor.fetchall()
			cursor.close()

			# Populate game board with all moves up until now
			for i in range(len(results)):
				location = results[i][2]
				chosen_by = results[i][3]
				for x in range(0, 3):
					for y in range(0, 3):
						if int(location[1]) == x and int(location[3]) == y:
							arr[x][y] = chosen_by

			# Check for a winner or a tie
			last_x = 0
			last_y = 0
			marker = "a"
			if len(results) > 0:
				last_x = int(results[-1][2][1])
				last_y = int(results[-1][2][3])
				marker = results[-1][3]
			win = check_for_winner(arr, last_x, last_y, marker)
			winner = ""
			turn = ""
			# Indicate a winner or the player who has the next turn
			if len(results) == 9 and not win:
				turn = "tie"
			elif len(results) % 2 == 0:
				if win:
					winner = user_results[0][1]
				else:
					turn = user_results[0][0]
			else:
				if win:
					winner = user_results[0][0]
				else:
					turn = user_results[0][1]

			resp = make_response(render_template("gameBoard.html", winner=winner, turn=turn, \
                                             gameID=game_id, arr=arr))
			resp.set_cookie("sessionID", session_id)
			return resp
	else:
		if not check_session():
			return redirect(url_for("root"))
		else:
			session_id = request.cookies.get("sessionID")
			game_id = request.form["gameID"]
			# Grab the game board location for the move chosen
			for i in range(0, 3):
				for j in range(0, 3):
					if "loc" + str(i) + str(j) in request.form:
						loc = "(" + str(i) + "," + str(j) + ")"

			# Get all moves until this point in the game
			cursor, conn = get_cursor()
			cursor.execute("SELECT COUNT(*) FROM gameMoves WHERE gameID=%s;", (game_id,))
			results = cursor.fetchall()
			cursor.close()

			# Decide who made the current move
			num_moves = results[0][0]
			if num_moves % 2 == 0:
				chosen_by = "X"
			else:
				chosen_by = "O"

			# Insert the current move into the gameMoves table
			cursor, conn = get_cursor()
			cursor.execute("INSERT INTO gameMoves(gameID,location,chosen_by) VALUES(%s,%s,%s);", \
                                       (game_id, loc, chosen_by))
			conn.commit()
			cursor.close()

			resp = redirect(url_for("gameBoard") + "?gameID=" + str(game_id))
			resp.set_cookie("sessionID", session_id)
			return resp


@app.route("/logout")
def logout():
	# Log a user out
	resp = redirect(url_for("root"))
	resp.set_cookie("sessionID", "", expires=0)
	return resp

