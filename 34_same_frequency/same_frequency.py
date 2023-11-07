def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_list = [int(i) for i in str(num1)]
    num2_list = [int(i) for i in str(num2)]
    num1_list.sort()
    num2_list.sort()
    return num1_list == num2_list