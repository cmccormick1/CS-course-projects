**README for proj07: Flask and Cookies**

**Author:** Caroline McCormick\
**Course:** CSC 346, Fall 2020\
**Purpose:** This project uses a Flask application to implement the game of Tic-Tac-Toe. Cookies are
             used to track a user's session throughout the website. There are three webpages for this 
             game: a login screen, the main game menu, and the game board. Three tables in a database 
             are used to keep track of the user's logged in session, the games played, and the game 
             moves for each game.
         
**Files:**
   * flask_app.py --> this file contains the flask code to handle each webpage's GET and POST operations.
   * flask_app.wsgi --> this file loads the flask_app.py file.
   * templates/index.html --> the main login page where the user is prompted to enter a username 
   (and a session is created).
   * templates/startGame.html --> the page that lists all current/previous games for the logged in user,
   and it shows a text box to enter an opponent to start a new game.
   * templates/gameBoard.html --> the page that shows the current state of the game board, shows which
   player's turn it is, and shows who won (or if the players tied).
   * proj07_tables.pdf --> a document explaining the database design and what is included in each table.
   * Visual/login_page.PNG --> what the login page to the website looks like.
   * Visual/create_game_page.PNG --> what the main page-where you can create a new or select an existing
   game-looks like.
   * Visual/start_game_page.PNG --> what the Tic-Tac-Toe board looks like at the start of the game.
   * Visual/winner_page.PNG --> what the Tic-Tac-Toe board looks like when there is a winner.
   * Visual/tie_page.PNG --> what the Tic-Tac-Toe board looks like when there is a tie.
   
**URL to Login Page:**
   * http://3.89.159.48/flask_proj07/
   
**URL to Game Menu Page:**
   * http://3.89.159.48/flask_proj07/startGame
   
**URL to Game Board Page:**
   * http://3.89.159.48/flask_proj07/gameBoard?gameID=<ID>
