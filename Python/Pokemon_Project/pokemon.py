"""
    File: pokemon.py
    Author: Caroline McCormick
    Course: CSC 120, Section 1A
    Purpose: This program takes in a file containing data about different
    Pokemon, organizes this data, calculates average values for each category
    of data, and processes queries provided by the user, printing out the
    results.
    
    ------------------------------------------------------------------------
    Example file input:
    #  Name	        Type 1	 Type 2	Total	HP	Attack	Defense	Sp. Atk	Sp. Def	Speed	Generation	Legendary
    1  Bulbasaur    Grass	 Poison	318	    45	49	    49	        65	    65	45	    1	        FALSE
    2  Ivysaur	    Grass	 Poison	405	    60	62	    63	        80	    80	60	    1	        FALSE
    3  Venusaur     Grass	 Poison	525	    80	82	    83	        100	    100	80	    1	        FALSE
    4  Charmander	Fire	        309	    39	52	    43	        60	    50	65	    1	        FALSE
    5  Charmeleon	Fire		    405	    58	64	    58	        80	    65	80	    1	        FALSE

"""

import sys

def main():
    poke_dict, num_of_stats = create_dataset()
    average_dict = calculate_averages(poke_dict, num_of_stats)
    max_avg_dict = highest_averages(average_dict, num_of_stats)
    query(max_avg_dict)


def create_dataset():
    """
    Purpose: This function sorts information from a file containing Pokemon fighting
    statistics based on the types of Pokemon and the individual Pokemon. 

    Parameters: None

    Returns: poke_dict is a 2D dictionary that sorts all of the Pokemon of a
    each type, then all of the statistics in a list for each Pokemon.
    len(stats_list) is the number of statistics that the Pokemon have.
    """
    try:
        data_file = open(input('Input File: ')).readlines()
    except:
        print('ERROR: Could not open file ' + data_file)
        sys.exit(1)
    poke_dict = {}
    for line in data_file:
        data = line.split(',')
        #remove unnecessary columns in data table
        data.remove(data[0])
        data.remove(data[2])
        data.remove(data[-2])
        data.remove(data[-1])
        if data[0].lower() != 'name':
            name = data[0]
            poke_type = data[1]
            #create list of statistic values per row
            stats_list = [data[i] for i in range(2, len(data))]
            #add statistics list to dictionary according to Pokemon type and name
            if poke_type in poke_dict.keys():
                poke_dict[poke_type][name] = stats_list
            else:
                poke_dict[poke_type] = {name:stats_list}
    return poke_dict, len(stats_list)


def calculate_averages(poke_dict, num_of_stats):
    """
    Purpose: This function calculates and stores the average value across all of the
    Pokemon in each type of Pokemon for each category in the statistics list.

    Parameters: poke_dict provides the sorted file of all the Pokemon information.
    num_of_stats is used to indicate how many categories of statistics are in
    the data file.

    Returns: average_dict is a dictionary that has the Pokemon type as the keys
    and a list of the average values for each statistic for all the Pokemon of
    that type as the values.
    """
    average_dict = {}
    #for each Pokemon type
    for poke_type in poke_dict.keys():
        poke_stats_dict = poke_dict[poke_type]
        type_averages = []
        for i in range(0, num_of_stats):
            total = 0
            #for each statistic column, add together the values
            for stats_list in poke_stats_dict.values():
                total += int(stats_list[i])
            #calculate average of statistic across one type of Pokemon 
            type_averages.append(total / len(poke_stats_dict))
        average_dict[poke_type] = type_averages
    return average_dict


def highest_averages(average_dict, num_of_stats):
    """
    Purpose: This function determines the highest average value for each category of
    statistic over every type of Pokemon.

    Parameters: average_dict is a dictionary that has the Pokemon type as the
    keys and a list of the average values for each statistic for all the Pokemon
    of that type as the values. num_of_stats is used to indicate how many
    categories of statistics are in the data file.

    Returns: max_avg_dict is a dictionary that has the categories of statistics
    as the keys and an inner dictionary as the values that contains the Pokemon
    type mapped to the corresponding maximum average for that category. 
    """
    max_avg_dict = {}
    categories = ['Total', 'HP', 'Attack', 'Defense', 'SpecialAttack',
                  'SpecialDefense', 'Speed']
    #for each statistical category
    for i in range(0, num_of_stats):
        pokemon_type = ''
        max_average = 0
        output = {}
        #find the maximum average value for a statistic across all Pokemon types
        for poke_type,type_averages in average_dict.items():
            if type_averages[i] > max_average:
                max_average = type_averages[i]
                pokemon_type = poke_type
            elif type_averages[i] == max_average:
                output[poke_type] = type_averages[i]
        output[pokemon_type] = max_average
        max_avg_dict[categories[i]] = output
    return max_avg_dict    


def query(max_avg_dict):
    """
    Purpose: This function repeatedly prompts the user who inputs a category of
    statistic, and it prints out the maximum average and the type of Pokemon
    that has the maximum average.

    Parameters: max_avg_dict is a dictionary that has the categories of
    statistics as the keys and an inner dictionary as the values that contains
    the Pokemon type mapped to the corresponding maximum average for that
    category.

    Returns: None
    """
    user_query = input('Category? ')
    while user_query != '':
        for category in max_avg_dict.keys():
            if user_query.lower() == category.lower():
                output = max_avg_dict[category]
                for poke_type in sorted(output.keys(), key=str.lower):
                    print("{}: {}".format(poke_type, str(output[poke_type])))
        user_query = input('Category? ')
