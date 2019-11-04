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
