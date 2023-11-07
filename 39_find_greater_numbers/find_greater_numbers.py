def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    start = 0
    counter = 0
    counter_list = []
    while start < len(nums)-1:
        for num in nums[start:]:
            if nums[start] < num:
                counter += 1
            else:
                pass
        counter_list.append(counter)
        start += 1
        counter = 0
    return sum(counter_list)