lst = [1,2,3,4,5]

my_str = "Hello, World!"

my_int = 42

# print(type(lst))
# print(type(my_str))
# print(type(my_int))

from oops_proj import chatbook


#getter and setter example
# user2 = chatbook()
# print(user2.get_name())
# user2.set_name("Alice")
# print(user2.get_name())

user1 = chatbook()
print(user1.id)

chatbook.set_id(100)
# print(chatbook.get_id(user1))
user2 = chatbook()
print(user2.id)

# user3 = chatbook()
# print(user3.id)