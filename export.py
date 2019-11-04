from printing import *


def export_to_file():
    body_of_text = print_all()
    with open('report.txt', 'wt') as f:
        f.write(print_count_games() + '\n')
    with open('report.txt', 'at') as f:
        f.write(print_decide() + '\n')
        f.write(print_get_latest() + '\n')
        f.write(print_count_by_genre() + '\n')
        f.write(print_get_line_number_by_title() + '\n')
        f.write(print_sort_abc() + '\n')
        f.write(print_get_genres() + '\n')
        f.write(print_when_was_top_sold_fps() + '\n')


export_to_file()
