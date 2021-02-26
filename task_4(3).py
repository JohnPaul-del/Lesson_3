

def lettername(*list_of_names):
    res_dict = {}
    list_of_names = sorted(list_of_names)
    for st in list_of_names:
        first_n, last_n = st.split()
        lname_dict = res_dict.get(last_n[0])
        if lname_dict is None:
            lname_dict = {}
        fname_dict = lname_dict.get(first_n[0])
        if fname_dict is None:
            fname_dict = []
        fname_dict.append(st)
        lname_dict.setdefault(first_n[0], fname_dict)
        res_dict.setdefault(last_n[0], lname_dict)

    # Sorting a dictionary
    res_sort_dict = {}
    for i in sorted(res_dict.keys()):
        res_sort_dict[i] = res_dict[i]

    return res_sort_dict


print(lettername("Иван Сергеев", "Инна Серова", "Петр Алексеев",
                 "Илья Иванов", "Анна Савельева", "Юрий Войтюк",
                 "Борис Аркадьев", "Антон Серов", "Павел Анисимов", "Дмитрий Белов",
                 "Аркадий Юрьев", "Яков Романов", "Яна Шеломова"))
