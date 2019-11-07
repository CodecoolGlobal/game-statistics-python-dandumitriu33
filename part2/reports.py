def file_to_dict(file_name):
    working_dict = {}
    with open(file_name, 'rt') as f:
        line_counter = 1
        for line in f:
            stats = line.strip().split('\t')
            values = stats[:]
            working_dict[line_counter] = values
            line_counter += 1
    return working_dict


def get_most_played(file_name):
    '''
    Returns the most played game name as string.

    >>> get_most_played('game_stat.txt')
    'Minecraft'
    '''
    data_dict = file_to_dict(file_name)
    id_title_sales = []
    for key in data_dict:
        id_title_sales.append((key, data_dict[key][0], float(data_dict[key][1])))
    ordered_by_id = sorted(id_title_sales, key=lambda x: x[0])
    ordered_by_sales_id = sorted(ordered_by_id, key=lambda x: x[2])
    return ordered_by_sales_id[-1][1]


def sum_sold(file_name):
    '''
    Returns the total of games sold from the list.

    >>> sum_sold('game_stat.txt')
    187.16
    '''
    data_dict = file_to_dict(file_name)
    sales = []
    for i in data_dict.values():
        sales.append(float(i[1]))
    sum_of_sales = sum(sales)
    return sum_of_sales


def get_selling_avg(file_name):
    '''
    Returns the average of sales. All sales divided by number of games.

    >>> get_selling_avg('game_stat.txt')
    7.798333333333333
    '''
    data_dict = file_to_dict(file_name)
    sales = []
    for i in data_dict.values():
        sales.append(float(i[1]))
    average_of_sales = sum(sales) / len(sales)
    return average_of_sales


def count_longest_title(file_name):
    '''
    Returns character number of the longest title in the list.

    >>> count_longest_title('game_stat.txt')
    52
    '''
    data_dict = file_to_dict(file_name)
    titles = []
    for i in data_dict.values():
        titles.append(i[0])
    length_ordered_titles = sorted(titles, key=lambda x: len(x))
    return len(length_ordered_titles[-1])


def get_date_avg(file_name):
    '''
    Returns the average of release years from the list.

    >>> get_date_avg('game_stat.txt')
    2003
    '''
    data_dict = file_to_dict(file_name)
    years = []
    for i in data_dict.values():
        years.append(float(i[2]))
    average_of_years = round(sum(years) / len(years))
    return average_of_years


def get_game(file_name, title):
    '''
    Returns a list of information about the given game.

    >>> get_game('game_stat.txt', 'Counter-Strike')
    ['Counter-Strike', 12.5, 1999, 'First-person shooter', 'Valve Corporation']
    >>> get_game('game_stat.txt', 'Doom 3')
    ['Doom 3', 3.5, 2004, 'First-person shooter', 'Activision']
    >>> get_game('game_stat.txt', 'Crysis')
    ['Crysis', 3.0, 2007, 'First-person shooter', 'Electronic Arts']
    '''
    data_dict = file_to_dict(file_name)
    for i in data_dict.values():
        if title in i:
            return [i[0], float(i[1]), int(i[2]), i[3], i[4]]


def count_grouped_by_genre(file_name):
    data_dict = file_to_dict(file_name)
    genres_dict = {}
    for i in data_dict.values():
        if i[3] in genres_dict:
            genres_dict[i[3]] += 1
        else:
            genres_dict[i[3]] = 1
    return genres_dict


def get_date_ordered(file_name):
    data_dict = file_to_dict(file_name)
    title_year = []
    for i in data_dict.values():
        title_year.append([i[0], int(i[2])])
    ordered_by_name = sorted(title_year, key=lambda x: x[0])
    ordered_by_name.reverse()
    ordered_by_year_name = sorted(ordered_by_name, key=lambda x: x[1])
    titles_ordered = []
    for j in ordered_by_year_name:
        titles_ordered.insert(0, j[0])
    return titles_ordered
