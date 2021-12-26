def average_rating(lst):
    if not lst:
        return 0
    else:
        return round(sum(lst)/len(lst))