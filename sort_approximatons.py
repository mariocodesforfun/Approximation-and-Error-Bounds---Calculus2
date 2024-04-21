from math import pi

def sort_by_similarity(single_float, float_array):
    # Calculate percentage difference of each element in the array to the single float
    similarities = {num: abs(single_float - num) / single_float * 100 for num in float_array}

    # Sort the dictionary based on percentage difference
    sorted_dict = dict(sorted(similarities.items(), key=lambda x: x[1]))

    return sorted_dict


# Example usage:
single_float = pi
float_array = [3.141791887, 3.141326804, 3.140912253]

sorted_array = sort_by_similarity(single_float, float_array)
print(sorted_array)
