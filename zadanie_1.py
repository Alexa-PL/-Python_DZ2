my_int = 5
my_float = 1.2
my_str = "Привет Александра!"
my_list = ['a', '4']
my_tuple = ('b', '5')
my_dict = {'city': 'Korolev', 'country': 'Russia'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')
