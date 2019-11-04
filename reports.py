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


def count_games(file_name):
    data_dict = file_to_dict(file_name)
    return len(data_dict)


def decide(file_name, year):
    data_dict = file_to_dict(file_name)
    for value in data_dict.values():
        if str(year) in value:
            return True
    return False


def get_latest(file_name):
    data_dict = file_to_dict(file_name)
    pos_title_year = []
    for i in data_dict.keys():
        pos_title_year.append((i, data_dict[i][0], data_dict[i][2]))
    sorted_year = sorted(pos_title_year, key = lambda x: x[2])
    latest_year = sorted_year[-1][2]
    most_recent_games = []
    for j in sorted_year:
        if j[2] == latest_year:
            most_recent_games.append(j)
    sorted_recent_games_by_pos = sorted(most_recent_games, key = lambda x: x[0])
    return sorted_recent_games_by_pos[0][1]


def count_by_genre(file_name, genre):
    data_dict = file_to_dict(file_name)
    game_counter = 0
    for i in data_dict.values():
        if genre in i:
            game_counter += 1
    return game_counter
