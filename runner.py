import math
import matplotlib.pyplot as plt


fields = ['year', 'jan', 'feb', 'march', 'april', 'may', 'june', 'july','august', 'sept', 'oct', 'nov', 'dec', 'year-middle']


def splitter(fieldnames, file):
    """special function for a specific datat set of mine
    returns list of operable values in list object + errors(also specific) count in data set"""
    middle_year_list = []
    errors = 0
    for line in file:
        elem = line.split('\t')[len(line.split('\t')) - 1]
        elem = float(elem[:len(elem)-2])

        if elem != 999.9:
            middle_year_list.append(elem)
        else:
            errors += 1
    return middle_year_list, errors




def lesser_then_lists_elements(list, pivot):

    #pivot's index should be the same as list's slice end index

    for elem in list:
        if pivot < elem:
            continue
        else:
            return 0
    return 1


def greater_then_lists_elements(list, pivot):

    #pivot's index should be the same as list's slice end index

    for elem in list:
        if pivot > elem:
            continue
        else:
            return 0
    return 1


def leveller(list):
    k = []
    l = []
    for i in range(len(list)):
        if i ==0:
            k.append('start')
            l.append('start')
        else:
            k.append(greater_then_lists_elements(list[:i], list[i]))
            l.append(lesser_then_lists_elements(list[:i],list[i]))
    return k, l


def summ_of_side_values(ks, ls):
    if len(ks) == len(ls):
        s = 0
        for i in range(len(ks)):
            if i == 0:
                continue
            s += ks[i] - ls[i]      #should check values before summing them todo
        return s
    else:
        print('lists length not equal')


def summ_of_list(list):
    s = 0
    for value in list:
        s += value
    return s


def mid_arithmethic(list):
    return summ_of_list(list)/len(list)


def mid_square_desp(list_orig, pivot):      #pivot's value of mid arithmetic value
    semi_list = [(value - pivot) ** 2 for value in list_orig]
    return math.sqrt(mid_arithmethic(semi_list))


def draw_graph(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y, lw=2, color='#539caf', alpha=1)
    ax.set_title('graph')
    plt.show()


if __name__ == "__main__":
    csv_path = "Weather.csv"
    #l = [55, 44, 33, 12, 64,70,80]

    with open(csv_path,'r') as f_obj:
        middle_list, err = splitter(fields, f_obj)
    f_obj.close()
    gr, ls = leveller(middle_list)
    d = summ_of_side_values(gr, ls)
    print(d)
    print('errors counter: ' + err.__str__())
    sig = mid_square_desp(middle_list, mid_arithmethic(middle_list))
    t = d/sig
    print(t)
    draw_graph(len(middle_list), middle_list)


#pivot's index should be the same as list's slice end index
