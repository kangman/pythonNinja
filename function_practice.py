from even_utils import is_even

def filter_out_odds (numbers):
    """
    takes a list of numbers and returns just the odds
    """
    evens = []
    for i in numbers:
        if is_even(i):
            evens.append(i)

    return evens
