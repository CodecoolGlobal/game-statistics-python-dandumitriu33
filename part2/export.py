from printing import *


def export_to_file():
    with open('part2_report.txt', 'wt') as f:
        f.write(print_get_most_played() + '\n')
    with open('part2_report.txt', 'at') as f:
        f.write(print_sum_sold() + '\n')
        f.write(print_get_selling_avg() + '\n')
        f.write(print_count_longest_title() + '\n')
        f.write(print_get_date_avg() + '\n')
        f.write(print_get_game() + '\n')
        f.write(print_count_grouped_by_genre() + '\n')
        f.write(print_get_date_ordered() + '\n')


export_to_file()