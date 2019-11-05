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
