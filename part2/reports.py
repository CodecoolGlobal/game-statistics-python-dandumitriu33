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
    data_dict = file_to_dict(file_name)
    id_title_sales = []
    for key in data_dict:
        id_title_sales.append((key, data_dict[key][0], float(data_dict[key][1])))
    ordered_by_id = sorted(id_title_sales, key=lambda x: x[0])
    ordered_by_sales_id = sorted(ordered_by_id, key=lambda x: x[2])
    return ordered_by_sales_id[-1][1]


def sum_sold(file_name):
    data_dict = file_to_dict(file_name)
    sales = []
    for i in data_dict.values():
        sales.append(float(i[1]))
    sum_of_sales = sum(sales)
    return sum_of_sales


def get_selling_avg(file_name):
    data_dict = file_to_dict(file_name)
    sales = []
    for i in data_dict.values():
        sales.append(float(i[1]))
    average_of_sales = sum(sales) / len(sales)
    return average_of_sales


def count_longest_title(file_name):
    data_dict = file_to_dict(file_name)
    titles = []
    for i in data_dict.values():
        titles.append(i[0])
    length_ordered_titles = sorted(titles, key=lambda x: len(x))
    return len(length_ordered_titles[-1])


def get_date_avg(file_name):
    data_dict = file_to_dict(file_name)
    years = []
    for i in data_dict.values():
        years.append(float(i[2]))
    average_of_years = round(sum(years) / len(years))
    return average_of_years


def get_game(file_name, title):
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
