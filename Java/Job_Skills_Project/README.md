Job Skills Project
------------------

**Purpose:** This project displays the use and manipulation of a dictionary, an abstract data structure that is implemented by a HashMap here. This project also displays reading in a data file, specifically a file containing job information, and organizing the information contained in the data file. It will read in a job data file and print out information about the different jobs in the file depending on what command is provided by the user.

**Running PA2Main.java from the command line:**
  $ java PA2Main infileName COMMAND optional
    where infileName is the name of the data file, COMMMAND is either CATCOUNT or LOCATIONS, and optional is one of the categories in the
    data file (note: optional is only provided if the command LOCATIONS is given).
    
**Output:**
  Depending on the given command, this program will output different information from the data file.
    CATCOUNT - for each job category in the data file, the program will print out the category name and the number of jobs in that
               category.
    LOCATIONS - provided that the user gives a job category for the "optional" parameter, the program will print out all the locations
                that offer a position in that given category. It also prints how many positions are open at that location for that
                category.
    
**Errors/Exceptions:**
  This program will display the error message "Invalid Command" if the command provided is not CATCOUNT or LOCATIONS.
  This program will throw a FileNotFoundException if the input data file does not exist.
