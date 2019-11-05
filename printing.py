from reports import *

THE_FILE = 'game_stat.txt'
THE_YEAR = input('Enter the year to see if there are games from then on the list: ')
THE_GENRE = input('Enter a genre to count how many games it has on the list: ')
THE_TITLE = input('Enter a title to see what number it is on the list: ')


def print_count_games():
    return 'The total number of games is %d.' % count_games(THE_FILE)


def print_decide():
    return f'Are there games from {THE_YEAR} on the list? {str(decide(THE_FILE, THE_YEAR))}'


def print_get_latest():
    return 'The latest game on the list is %s.' % get_latest(THE_FILE)


def print_count_by_genre():
    return 'There are {} {} games.'.format(count_by_genre(THE_FILE, THE_GENRE), THE_GENRE)


def print_get_line_number_by_title():
    return '{} is number {} on the list.'.format(THE_TITLE, get_line_number_by_title(THE_FILE, THE_TITLE))


def print_sort_abc():
    returned_list = sort_abc(THE_FILE)
    print_list = []
    for i in returned_list:
        print_list.append(i)
        print_list.append(', ')
    print_list.pop()
    temp_string = ''
    print_string = temp_string.join(print_list)
    return f'Here are the games, alphabetically ordered: {print_string}.'


def print_get_genres():
    returned_list = get_genres(THE_FILE)
    print_list = []
    for i in returned_list:
        print_list.append(i)
        print_list.append(', ')
    print_list.pop()
    temp_string = ''
    print_string = temp_string.join(print_list)
    return f'Here are the genres, alphabetically ordered: {print_string}.'


def print_when_was_top_sold_fps():
    return 'The top most sold First-person shooter game was released in {}.'.format(when_was_top_sold_fps(THE_FILE))


def print_all():
    print(print_count_games())
    print(print_decide())
    print(print_get_latest())
    print(print_count_by_genre())
    print(print_get_line_number_by_title())
    print(print_sort_abc())
    print(print_get_genres())
    print(print_when_was_top_sold_fps())


print_all()
