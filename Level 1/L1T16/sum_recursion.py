def adding_up_to (num_list, in_ref):
    """Returns sum of numbers in a list all the way to an index"""
    if in_ref >= len(num_list):
        print(f"Error - index needs to be less than {len(list_nums)}")
    else:
        if in_ref == 0:
            return 1
        else:
            return num_list[in_ref] + adding_up_to(num_list, in_ref-1)

# Function arguments
list_nums = [1, 5 ,5, 6, 9]
index = 2
# ===============

print(adding_up_to(list_nums, index))