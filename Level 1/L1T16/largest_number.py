def largest_number (list):
    """Returns the largest number in a given list"""
    if len(list) == 0:
        print("Error - list is empty!")
    else:
        list_len = len(list)
        if list_len == 1:
            return list[0]
        else:
            if list[0] > list[1]:
                list.pop(1)
            else:
                list.pop(0)
            return largest_number(list)
   
# Function arguments
list_nums = [4, 5, 7, 9, 23, 1, 4, 78, 3, 0, 1]
# ===============

print(largest_number(list_nums))