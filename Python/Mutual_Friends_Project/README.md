Mutual Friends Project
-----------------------

**Purpose:**  
This project implements a linked list, which stores node objects containing information about the person it represents as well as pointers to the next node in the main list and to the list of that person's friends. This linked list of nodes is then traversed to determine friend relationships between people. If a name appears in two different people's friend lists, then they are said to have a mutual friend. The program will prompt the user to provide an input friend file and two names. If any exist, the program will print out any mutual friend between those two provided people.

**Input File Structure:**  
  * The friend file given contains two names per line separated by a space, and this indicates that those two people are friends.  
  * Example:  
    Taylor Jessica  
    Ben James  
    James Jessica
  
**Errors/Exceptions:**  
  * friends.py will print the error message "ERROR: Could not open file FILENAME" and exit the program if an incorrect file name is given by the user.  
  * friends.py will print the error message "ERROR: Unknown person NAME" and exit the program if the person provided as input by the user is not in the main list of possible people.
  
