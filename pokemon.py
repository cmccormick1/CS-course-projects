"""
    File: pokemon.py
    Author: Caroline McCormick
    Course: CSC 120, Section 1A
    Purpose: This program takes in a file containing data about different
    Pokemon, organizes this data, calculates average values for each category
    of data, and processes queries provided by the user, printing out the
    results.
"""

def main():
    poke_dict, num_of_stats = create_dataset()
    average_dict = calculate_averages(poke_dict, num_of_stats)
    max_avg_dict = highest_averages(average_dict, num_of_stats)
    query(max_avg_dict)


def create_dataset():
    """
    This function sorts information from a file containing Pokemon fighting
    statistics based on the types of Pokemon and the individual Pokemon. 

    Parameters: None

    Returns: Poke_dict is a 2D dictionary that sorts all of the Pokemon of a
    each type, then all of the statistics in a list for each Pokemon.
    Len(stats_list) is the number of statistics that the Pokemon have.

    Pre-condition: The user must provide a valid Pokemon file in CSV format.
  
    Post-condition: The information in the file will be categorized as
    described above.
    """
    data_file = open(input()).readlines()
    poke_dict = {}
    for line in data_file:
        data = line.split(',')
        data.remove(data[0])
        data.remove(data[2])
        data.remove(data[-2])
        data.remove(data[-1])
        if data[0].lower() != 'name':
            name = data[0]
            poke_type = data[1]
            stats_list = [data[i] for i in range(2, len(data))]
            if poke_type in poke_dict.keys():
                poke_dict[poke_type][name] = stats_list
            else:
                poke_dict[poke_type] = {name:stats_list}
    return poke_dict, len(stats_list)


def calculate_averages(poke_dict, num_of_stats):
    """
    This function calculates and stores the average value across all of the
    Pokemon in each type of Pokemon for each category in the statistics list.

    Parameters: Poke_dict provides the sorted file of all the Pokemon information.
    Num_of_stats is used to indicate how many categories of statistics are in
    the data file.

    Returns: Average_dict is a dictionary that has the Pokemon type as the keys
    and a list of the average values for each statistic for all the Pokemon of
    that type as the values.

    Pre-condition: None
  
    Post-condition: The average values can now be compared to determine the
    highest average value for each statistic category over the whole file.
    """
    average_dict = {}
    for poke_type in poke_dict.keys():
        poke_stats_dict = poke_dict[poke_type]
        type_averages = []
        for i in range(0, num_of_stats):
            total = 0
            for stats_list in poke_stats_dict.values():
                total += int(stats_list[i])
            type_averages.append(total / len(poke_stats_dict))
        average_dict[poke_type] = type_averages
    return average_dict


def highest_averages(average_dict, num_of_stats):
    """
    This function determines the highest average value for each category of
    statistic over every type of Pokemon.

    Parameters: Average_dict is a dictionary that has the Pokemon type as the
    keys and a list of the average values for each statistic for all the Pokemon
    of that type as the values. Num_of_stats is used to indicate how many
    categories of statistics are in the data file.

    Returns: Max_avg_dict is a dictionary that has the categories of statistics
    as the keys and an inner dictionary as the values that contains the Pokemon
    type mapped to the corresponding maximum average for that category. 

    Pre-condition: None
  
    Post-condition: The maximum average for each category along with the type
    of Pokemon at that maximum average is stored so that it can be referenced
    depending on what category the user inputs.
    """
    max_avg_dict = {}
    categories = ['Total', 'HP', 'Attack', 'Defense', 'SpecialAttack',
                  'SpecialDefense', 'Speed']
    for i in range(0, num_of_stats):
        pokemon_type = ''
        max_average = 0
        output = {}
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
    This function repeatedly prompts the user who inputs a category of
    statistic, and it prints out the maximum average and the type of Pokemon
    that has the maximum average.

    Parameters: Max_avg_dict is a dictionary that has the categories of
    statistics as the keys and an inner dictionary as the values that contains
    the Pokemon type mapped to the corresponding maximum average for that
    category.

    Returns: None

    Pre-condition: The user must input a valid category of statistic to expect
    values printed out.
  
    Post-condition: The maximum average value and the type of Pokemon at that
    value is printed out based on the category that the user inputs. If there
    is a tie in maximum average values, all are printed out in alphabetical
    order based on the Pokemon type.
    """
    user_query = input()
    while user_query != '':
        for category in max_avg_dict.keys():
            if user_query.lower() == category.lower():
                output = max_avg_dict[category]
                for poke_type in sorted(output.keys(), key=str.lower):
                    print("{}: {}".format(poke_type, str(output[poke_type])))
        user_query = input()
        


main()
