def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    letter_to_swap = to_swap.swapcase()
    phrase_list = [letter.swapcase() if letter.lower() == to_swap.lower() else letter for letter in phrase]
    return ''.join(phrase_list)
    
