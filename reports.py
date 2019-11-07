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


def bubble_srt(list_name):
    '''
    Sorts and returns the sorted list of elements. In this
    exercise, the use of sort() and sorted() was not allowed.

    >>> bubble_srt([5, 3, 1, 7])
    [1, 3, 5, 7]
    >>> bubble_srt(['acc', 'mnp', 'add', 'abc', 'zfg'])
    ['abc', 'acc', 'add', 'mnp', 'zfg']
    '''
    for i in range(len(list_name)):
        for j in range(0, len(list_name) - i - 1):
            if list_name[j] > list_name[j+1]:
                list_name[j], list_name[j+1] = list_name[j+1], list_name[j]
    return list_name


def count_games(file_name):
    '''
    Returns the length of a dictionary (number of keys).
    The dictionary is extracted from a given file via file_to_dict().

    >>> count_games('game_stat.txt')
    24
    '''
    data_dict = file_to_dict(file_name)
    return len(data_dict)


def decide(file_name, year):
    '''
    Checks if there are entries in the list with the given year.

    >>> decide('game_stat.txt', 2011)
    True
    >>> decide('game_stat.txt', 2008)
    False
    >>> decide('game_stat.txt', 2004)
    True
    '''
    data_dict = file_to_dict(file_name)
    for value in data_dict.values():
        if str(year) in value:
            return True
    return False


def get_latest(file_name):
    '''
    Returns the title of the latest game as a string.

    >>> get_latest('game_stat.txt')
    'Diablo III'
    '''
    data_dict = file_to_dict(file_name)
    just_years = []
    pos_title_year = []
    for i in data_dict.keys():
        just_years.append(data_dict[i][2])
        pos_title_year.append((i, data_dict[i][0], data_dict[i][2]))
    srt_just_years = bubble_srt(just_years)
    latest_year = srt_just_years[-1]
    most_recent_games = []
    for j in pos_title_year:
        if j[2] == latest_year:
            most_recent_games.append(j)
    srt_recent_games_by_pos = bubble_srt(most_recent_games)
    return srt_recent_games_by_pos[0][1]


def count_by_genre(file_name, genre):
    '''
    Returns the number of games in the list that are the given genre.

    >>> count_by_genre('game_stat.txt', 'RPG')
    5
    >>> count_by_genre('game_stat.txt', 'Real-time strategy')
    7
    >>> count_by_genre('game_stat.txt', 'Simulation')
    3
    '''
    data_dict = file_to_dict(file_name)
    game_counter = 0
    for i in data_dict.values():
        if genre in i:
            game_counter += 1
    return game_counter


def get_line_number_by_title(file_name, title):
    '''
    Returns the number the game is in the list, its line number.

    >>> get_line_number_by_title('game_stat.txt', 'Diablo III')
    4
    >>> get_line_number_by_title('game_stat.txt', 'EverQuest')
    19
    >>> get_line_number_by_title('game_stat.txt', 'StarCraft')
    8
    '''
    data_dict = file_to_dict(file_name)
    game_doesnt_exist = False
    for i in data_dict.keys():
        if title in data_dict[i]:
            return i
        else:
            game_doesnt_exist = True
    if game_doesnt_exist is True:
        raise ValueError('The game is not in the list.')


def sort_abc(file_name):
    data_dict = file_to_dict(file_name)
    titles = [i[0] for i in data_dict.values()]
    bubble_srt(titles)
    return titles


def get_genres(file_name):
    data_dict = file_to_dict(file_name)
    genres = [i[3] for i in data_dict.values()]
    set_genres = set(genres)
    genres = bubble_srt(list(set_genres))
    return genres


def when_was_top_sold_fps(file_name):
    '''
    Returns the top sold First-person shooter release year.

    >>> when_was_top_sold_fps('game_stat.txt')
    1999
    '''
    data_dict = file_to_dict(file_name)
    copies_sold = []
    title_copies_year_genre = []
    for i in data_dict.values():
        if i[3] == 'First-person shooter':
            copies_sold.append(float(i[1]))
            title_copies_year_genre.append((i[0], float(i[1]), i[2], i[3]))
    if title_copies_year_genre == []:
        raise ValueError('Game genre does not exist in the list.')
    top_sold = max(copies_sold)
    for j in title_copies_year_genre:
        if j[1] == top_sold:
            return int(j[2])
