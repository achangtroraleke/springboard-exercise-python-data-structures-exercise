def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    formatted_phrase = phrase.replace(' ', '').lower()
    
    list_form = list(formatted_phrase)
    reverse_list = list_form.copy()
    reverse_list.reverse()
    
    if list_form == reverse_list:
        return True
    else:
        return False
    