from reports import *

THE_FILE = 'game_stat.txt'
THE_TITLE = input('Enter a title to see all its information: ')


def print_get_most_played():
    return 'The most played game is %s.' % get_most_played(THE_FILE)


def print_sum_sold():
    return 'The total number of games sold is %d million.' % sum_sold(THE_FILE)


def print_get_selling_avg():
    return 'The average number of game copies sold is %d million.' % get_selling_avg(THE_FILE)


def print_count_longest_title():
    return 'The longest game title has %d characters.' % count_longest_title(THE_FILE)


def print_get_date_avg():
    return 'The best release year (average releases date) was %d.' % get_date_avg(THE_FILE)


def print_get_game():
    return '{} information: sold {} million copies, was released in {}, its genre is {} and it was published by {}.'.format(THE_TITLE, get_game(THE_FILE, THE_TITLE)[1], get_game(THE_FILE, THE_TITLE)[2], get_game(THE_FILE, THE_TITLE)[3], get_game(THE_FILE, THE_TITLE)[4])


def print_count_grouped_by_genre():
    print_dict = count_grouped_by_genre(THE_FILE)
    print_list = []
    for key in print_dict.keys():
        print_list.append(key)
        print_list.append(': ')
        print_list.append(str(print_dict[key]))
        print_list.append(', ')
    print_list.pop()
    temp_string = ''
    print_string = temp_string.join(print_list)
    return 'The list has the following number of games, by genre: {}.'.format(print_string)


def print_get_date_ordered():
    returned_list = get_date_ordered(THE_FILE)
    print_list = []
    for i in returned_list:
        print_list.append(i)
        print_list.append(', ')
    print_list.pop()
    temp_string = ''
    print_string = temp_string.join(print_list)
    return 'The list of games, ordered alphabetically and by release year: {}.'.format(print_string)


def print_all():
    print(print_get_most_played())
    print(print_sum_sold())
    print(print_get_selling_avg())
    print(print_count_longest_title())
    print(print_get_date_avg())
    print(print_get_game())
    print(print_count_grouped_by_genre())
    print(print_get_date_ordered())


print_all()
