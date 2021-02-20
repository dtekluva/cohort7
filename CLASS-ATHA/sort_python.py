my_list = [["a",2],["c",1],["s",5],["w",5],["q",3],["a",2],["e",10]]

# my_list.sort(reverse = True)
# print(my_list)
# my_list.sort(reverse = False)
# print(my_list)

my_list.sort(key= lambda value: value[1], reverse = True)
print(my_list[:3])
