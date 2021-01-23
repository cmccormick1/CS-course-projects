**README for proj05: REST**

**Author:** Caroline McCormick\
**Course:** CSC 346, Fall 2020\
**Purpose:** This project implements a RESTful interface for a vet clinic's database\
         of pet owners and pets. Each person and pet have a unique ID which allows\
         you to search for and read information stored in the database about each \
         person or pet. You can also view all people or all pets in the database.\
         In addition, you can add new people or pets to the database; you can delete\
         people from the database (their pets get deleted automatically too); and\
         you can modify a pet's name, owner, and age.
         
**Files:**
   * vetClinic.py --> this file contains all the CGI code that represents the REST interface.
   * Visual/people_collection.PNG --> image of JSON objects representing people in the database.
   * Visual/person_by_ID.PNG --> image of JSON object representing one person (by ID) in the database. 
   * Visual/pets_collection.PNG --> image of JSON objects representing pets in the database.
   * Visual/pet_by_ID.PNG --> image of JSON object representing one pet (by ID) in the database.
   
**What Requests Are Available:**
   * GET --> allows you to read the information stored about each person or pet or all\
             people or pets
   * POST --> allows you to add a person to the people table or to add a pet to the pets\
              table in the database
   * DELETE --> (only for people) allows you to delete a person (and automatically their pets)\
                from the database
   * PUT --> (only for pets) allows you to modify information about a pet
   
**User Requirements for Requests:**
   * GET --> None
   * POST --> \
         * if adding a person...MUST INCLUDE "last_name" and "first_name" fields; "address" is optional\
              * e.g. [{"last_name":"McCormick", "first_name":"Caroline", "address":"160 Fido Rd"}]\
         * if adding a pet...MUST INCLUDE "peopleID" (pet owner's ID), "name", and "breed"; "age" is optional\
              * e.g. [{"peopleID":1, "name":"Titan", "breed":"Black Lab", "age":7}]
   * DELETE --> MUST provide a person's ID number in the URL
   * PUT --> \
         * MUST provide a pet's ID number in the URL\
         * MUST include the pet's name (peopleID, breed, and age can be changed too, but they are optional)\
              * e.g. [{"name":"Titan Jack Bauer"}]
             
   
  
                       
**URL to /people collection:**
   * http://ec2-3-89-159-48.compute-1.amazonaws.com/cgi-bin/vetClinic.py/people 
   
**URL to /people/ID:**
   * http://ec2-3-89-159-48.compute-1.amazonaws.com/cgi-bin/vetClinic.py/people/ID 
   
**URL to /pets collection:**
   * http://ec2-3-89-159-48.compute-1.amazonaws.com/cgi-bin/vetClinic.py/pets 
   
**URL to /pets/ID:**
   * http://ec2-3-89-159-48.compute-1.amazonaws.com/cgi-bin/vetClinic.py/pets/ID
   
   
 
