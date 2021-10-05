import copy

first_list = [1,2,[3,4],5]
second_list = copy.deepcopy(first_list)
print('First List:',first_list)
print('Second List:',second_list)
print('Id of First List:',id(first_list))
print('Id of Second List:',id(second_list))

first_list[2][0]=6
first_list.append(7)
print('First List:',first_list)
print('Second List:',second_list)

