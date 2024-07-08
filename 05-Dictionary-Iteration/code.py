# Exercise Name:
# 	05-Dictionary-Iteration
# Description:
# 	Reverse Dictionary mapping
# Given:
# 	ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
# Return:
# 	{65: 'A', 66: 'B', 67: 'C', 68: 'D'}

ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
temp_dict = {}

key_list = list(ascii_dict.keys())
value_list = list(ascii_dict.values())
i=0
for key, value in ascii_dict.items():
    new_key = value_list[i]
    new_value = key_list[i]
    i+=1

    temp_dict[new_key] = new_value

ascii_dict = temp_dict
print(ascii_dict)
