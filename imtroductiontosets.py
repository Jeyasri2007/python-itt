def average(array):
    distinct_heights = set(array)
    avg = sum(distinct_heights) / len(distinct_heights)
    return avg


