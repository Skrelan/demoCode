from datetime import date


def diff_in_days(start, end):
    try:
        start = map(int, start.split("-"))
        end = map(int, end.split("-"))
        d0 = date(start[0], start[1], start[2])
        d1 = date(end[0], end[1], end[2])
        delta = d1 - d0
        return delta.days, None

    except Exception as e:
        return None, "Start date : {0}, End date: {1} \n{2}".format(
            start, end, e)


def diff_in_years(start, end):
    days, err = diff_in_days(start, end)
    if err:
        return None, err
    return days / 365.0, None


def find_min_median_maximum(arr):
    try:
        arr.sort()
        maximum = arr[-1]
        minimum = arr[0]
        median = None
        if len(arr) % 2 == 0:
            median = (arr[len(arr) / 2] + arr[(len(arr) / 2) + 1]) / 2.0
        else:
            median = arr[len(arr) / 2]
        return minimum, median, maximum, None
    except Exception as e:
        return None, None, None, "Arr : {0}\n{1}".format(arr, e)
