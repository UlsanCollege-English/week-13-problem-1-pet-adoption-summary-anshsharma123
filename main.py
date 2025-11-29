def summarize_adoptions(adoptions):
    """
    Given a list of animal type strings, return a dictionary mapping each
    distinct animal type to how many times it appears in the list.
    """
    result = {}  # dictionary to store counts

    # Loop through each animal in the list
    for animal in adoptions:
        if animal in result:
            result[animal] += 1  # increase count if already exists
        else:
            result[animal] = 1   # first time seen, start count at 1

    return result
