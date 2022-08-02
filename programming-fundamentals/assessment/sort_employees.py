def sort_employees(employees, sort_by):
    sort_indices = ['name', 'age', 'salary']
    sort_index = sort_indices.index(sort_by)

    return sorted(employees, key=lambda x: x[sort_index])
