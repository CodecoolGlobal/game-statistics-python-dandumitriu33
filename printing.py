from reports import *

THE_FILE = 'game_stat.txt'


def print_all():
    selected_year = input('Enter the year to see if there are games from then in the list: ')
    selected_genre = input('Enter a genre to count how many games it has in the list: ')
    selected_title = input('Enter a title to see what number it is in the list: ')
    print('The total number of games is %d.' % count_games(THE_FILE))
    print('Are there games from {} in the list?'.format(selected_year), decide(THE_FILE, selected_year))
    print('The latest game on the list is %s.' % get_latest(THE_FILE))
    print('There are {} {} games.'.format(count_by_genre(THE_FILE, selected_genre), selected_genre))
    print('{} is number {} in the list.'.format(selected_title, get_line_number_by_title(THE_FILE, selected_title)))
    print('Here are the games, alphabetically ordered:', sort_abc(THE_FILE))
    print('Here are the genres, alphabetically ordered:', get_genres(THE_FILE))
    print('The top most sold First-person shooter game was released in {}.'.format(when_was_top_sold_fps(THE_FILE)))


print_all()
