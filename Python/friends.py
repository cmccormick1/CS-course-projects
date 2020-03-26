"""
    File: friends.py
    Author: Caroline McCormick
    Course: CSC 120, Section 1A
    Purpose: This program takes a file that contains pairs of friends and
    organizes those pairs in such a way that given two names by the user, the
    program will tell if those people have any mutual friends.
"""

from linked_list import *
import sys


def main():
    fname = input('Input file: ')
    llist = organize_data(fname)
    name1 = input('Name 1: ').strip()
    name2 = input('Name 2: ').strip()
    mutual_friends(llist, name1, name2)
    
def organize_data(fname):
    """
    This function reads in the friends file and creates a main linked list of
    every person in the file and subsequent linked lists off each person containing
    their friends.

    Parameters: fname is the name of the friends file given.

    Returns: llist is the main linked list that contains each person in the file
    once.

    Pre-condition: The friends file must be a valid file type in the valid format.
  
    Post-condition: A LinkedList object will be created containing all the people
    in the file grouped with their friends.
    """
    llist = LinkedList()
    try:
        friends_file = open(fname).readlines()
    except:
        print('ERROR: Could not open file ' + fname)
        sys.exit(1)
    for line in friends_file:
        friends_list = line.strip('\n').split()
        llist.add_to_end(friends_list[0])
        llist.add_to_end(friends_list[1])
        llist.add_friend(friends_list[0], friends_list[1])
    return llist

def mutual_friends(llist, name1, name2):
    """
    This method loops through each of the given people's friends lists and
    prints out any mutual friends, if they have any.

    Parameters: name1 and name2 are the two names given by the user.

    Returns: None

    Pre-condition: Each name given by the user must be a valid name (i.e. it
    must be in the main linked list).
      
    Post-condition: All of the mutual friends between the two people will be
    printed out.
    """
    name1_friends, name2_friends = llist.get_friend_llists(name1, name2)
    if name1_friends._head == None:
        print('ERROR: Unknown person ' + name1)
        sys.exit(1)
    elif name2_friends._head == None:
        print('ERROR: Unknown person ' + name2)
        sys.exit(1)
    flag = False
    current1 = name1_friends._head
    while current1 != None:
        current2 = name2_friends._head
        while current2 != None:
            if current1._name.lower() == current2._name.lower():
                if not flag:
                    print('Friends in common:')
                print(current1._name)
                flag = True
            current2 = current2._next
        current1 = current1._next

main()
