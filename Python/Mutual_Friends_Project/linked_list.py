"""
    File: linked_list.py
    Author: Caroline McCormick
    Course: CSC 120, Section 1A
    Purpose: This program define two classes: a LinkedList class and a Node
    class.
"""

class LinkedList:
    """
    This class represents a linked list of nodes.

    Parameters: None

    Returns: None

    Pre-condition: None
  
    Post-condition: None
    """
    def __init__(self):
        """
        This method initializes the linked list as empty.

        Parameters: None

        Returns: None

        Pre-condition: None
      
        Post-condition: None
        """
        self._head = None

    def add_to_end(self, name):
        """
        This method adds a new node of a person to the end of a linked list.

        Parameters: name is the name of the person in the friends file that is
        currently being evaluated.

        Returns: None

        Pre-condition: name must be a string.
      
        Post-condition: A node containing a person's information will be added
        to the linked list.
        """
        node = Node(name)
        if self.is_empty():
            self._head = node
        else:
            current = self._head
            flag = False
            while current._next != None:
                if current._name.lower() == name.lower():
                    flag = True
                current = current._next
            if current._name.lower() == name.lower():
                flag = True
            if not flag:
                current._next = node

    def add_friend(self, friend1, friend2):
        """
        This method adds a person's friend to their friend linked list attribute.

        Parameters: friend1 and friend2 are two people's names who need to be
        added to each others friends lists.

        Returns: None

        Pre-condition: Both friends need to be in the main linked list.
      
        Post-condition: Each person will have at least one friend in their
        friend attribute linked list.
        """
        current = self._head
        while current != None:
            if current._name.lower() == friend1.lower():
                if current._friends == None:
                    friend1_llist = LinkedList()
                    friend1_llist.add_to_end(friend2)
                    current._friends = friend1_llist
                else:
                    current._friends.add_to_end(friend2)
            elif current._name.lower() == friend2.lower():
                if current._friends == None:
                    friend2_llist = LinkedList()
                    friend2_llist.add_to_end(friend1)
                    current._friends = friend2_llist
                else:
                    current._friends.add_to_end(friend1)
            current = current._next

    def get_friend_llists(self, name1, name2):
        """
        This method finds and returns the friend attribute linked list for each
        person given by the user.

        Parameters: name1 and name2 are the two people that the user wants to
        know if they have mutual friends.

        Returns: name1_friends and name2_friends are the linked lists of the
        friends of name1 and name2, respectively.

        Pre-condition: None
      
        Post-condition: None
        """
        name1_friends = LinkedList()
        name2_friends = LinkedList()
        current = self._head
        while current != None:
            if current._name.lower() == name1.lower():
                name1_friends = current._friends
            elif current._name.lower() == name2.lower():
                name2_friends = current._friends
            current = current._next
        return name1_friends, name2_friends
    
    def is_empty(self):
        """
        This method checks to see if the linked list is emtpy.

        Parameters: None

        Returns: Either True or False depending on if the linked list is empty
        or not.

        Pre-condition: None
      
        Post-condition: None
        """
        return self._head == None

    def get_head(self):
        return self._head

    def __str__(self):
        return 'Head --> ' + self._head.__str__()
    

class Node:
    """
    This class represents a node in a linked list containing a person in the
    friend file, a linked list of the person's friends, and the reference to
    the next node.

    Parameters: None

    Returns: None

    Pre-condition: None
  
    Post-condition: None
    """
    def __init__(self, name):
        """
        This method initializes a node with attributes of a name from the friends
        file, None for the linked list of friends, and None for the reference to
        the next node in the linked list.

        Parameters: name is the name of the person in the friends file that is
        currently being evaluated.

        Returns: None

        Pre-condition: None
      
        Post-condition: None
        """
        self._name = name
        self._friends = None
        self._next = None

    def get_name(self):
        return self._name

    def get_friends(self):
        return self._friends

    def get_next(self):
        return self._next

    def __str__(self):
        if self._next == None or self._friends == None:
            return 'Name: ' + self._name + ' Friends: None Next: None'
        return 'Name: ' + self._name + ' Friends: ' + self._friends.__str__()\
               + ' Next: ' + self._next._name

    
