def linear_search(list, target):
    """
    returns the index position of the target element if found, otherwise returns none
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
