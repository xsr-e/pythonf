prices = [10, 20, 50, 20, 100, 30]
print(prices)

def get_avg(a):
    """
    :param a: array with numbers
    :return: average of array elements
    """
    sum_of = sum(a)
    len_of = len(a)
    return sum_of / len_of


def get_avg_without_outliers(a):
    sorted_l = sorted(a)
    sum_of = sum(sorted_l[1:-1]) # sum of array elements without min and max value
    len_of = len(a)-2 # remove min and max from total count
    return sum_of/len_of


print(get_avg(prices))
print(get_avg_without_outliers(prices))