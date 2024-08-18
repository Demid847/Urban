def print_params(a=1, b="строка", c = True):
    print(a, b, c)

print_params()
print_params(b=4)
print_params(c=[1, 2, 3])
print_params(a="end")
print_params(32,"линия",False)

values_list = [1, "end", True]
values_dict={"a":122, "b":False, "c":"Hello"}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)