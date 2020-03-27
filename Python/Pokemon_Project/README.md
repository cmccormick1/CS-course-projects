Pokemon Project
---------------

**Purpose:**  
This project utilizes reading in data files containing statistical information about various Pokemon and organizing this information within dictionaries for further analysis. The program creates three dictionaries to store information; the first is a dictionary with keys of Pokemon types mapped to values of another dictionary with keys of Pokemon names that belong to a type mapped to values that are lists of a Pokemon's statistics. Secondly, the program creates a dictionary with keys of Pokemon types mapped to values of lists that contain the average value for each statistic across all Pokemon in the data file of that type. Thirdly, the program creates a dictionary of maximum values for each statistical category; this dictionary has categories of statistics as keys mapped to a dictionary with keys of Pokemon types that have the maximum value for that category mapped to the maximum value statistic. Finally, the program will prompt the user for a category, and it will print out the maximum average value for that category and the type of Pokemon that has that average value. Prompting continues until the user provides an invalid category.

**Possible Categories:**  
  * Total, HP, Attack, Defense, SpecialAttack, SpecialDefense, Speed

**Errors/Exceptions:**  
  * This program will print the error message "ERROR: Could not open file FILENAME" and exit if the filename provided by the user is invalid.
