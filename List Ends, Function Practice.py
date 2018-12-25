# This function prints the first and last vlaues in a list.

a_list = [5, 10, 15, 20, 25]

def get_end(a_list):
    return [a_list[0], a_list[len(a_list)-1]]

print(get_end(a_list))
