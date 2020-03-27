Patient Queue Project
----------------------

**Purpose:**
This project displays the implementation of two related classes. It implements an abstract data type called a priority queue that contains patient objects. Patient objects are defined to have a name and a priority. In a normal queue, elements are processed in a first in, first out order, but a priority queue preserves order based on the number priority that is assigned to each element. A binary minimum heap and an array are used to implement the priority queue in this project. A low number means a high priority; i.e. if a patient in the priority queue has a priority of 2, it will be processed before a patient with a priority of 5. A binary minimum heap preserves the priority order of the patients while making searching for a patient faster than going element by element in an array. A binary minimum heap has the properties that every element at an index, i, is gauranteed to have a higher priority than the elements at indices i x 2 and i x 2 + 1.


