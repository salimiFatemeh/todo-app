# waiting_list=["john","marry"]
# name=input("Enter name: ")
#
# if name in waiting_list:
#     number=waiting_list.index(name)
#     print(f"{name}'s turn is {number}")
# else:
#     print(f"{name}'s not in the list")

try:
    waiting_list=["john","marry"]
    name=input("Enter name: ")
    number=waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print("Sorry, we can't find that person")