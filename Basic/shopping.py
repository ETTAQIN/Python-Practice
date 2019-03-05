import os
# # write the user file
# with open('users.txt', 'w') as users:
#     data = "Albert|Albert123|13000" + "\n" + "Etta|123456|6000" + "\n" + "alpha|98765|200" + "\n" + "Mike|456|30000"
#     users.write(data)

# # write blacklist file
# with open('blacklist.txt', 'w') as blacklist:
#     pass

# # write product file
# with open('products.txt', 'w') as products:
#     data = '1 '+'iPhone '+'8000' + "\n" + '2 '+'mac book '+'12000' + "\n" + '3 '+'bike '+'500'
#     products.write(data)


# read users file, and transfer it to dictionary.
with open('users.txt', 'r') as users:
    users = users.read()
users = [x.split("|") for x in users.split()]
# print(users)
keys = []
values = []
for index, item in enumerate(users):
    keys.append(users[index][0])
    values.append(users[index][1:])
user_dict = dict(zip(keys, values))
# print(user_dict)

# read blacklist file
with open('blacklist.txt', 'r') as blacklist:
    blacklist = blacklist.read()
# print(blacklist)

# read products file, and transfer it to a dictionary
with open('products.txt', 'r') as products:
    products = products.readlines()
product_list = []
for item in products:
    item = item.replace("\n", "")
    product_list.append(item.rsplit(" ", 1))

product_name = []
product_price = []

for index, item in enumerate(product_list):
    product_name.append(tuple(item[0].split(" ", 1)))
    product_price.append(item[1])
product_name = tuple(product_name)
product_dict = dict(zip(product_name, product_price))
# print(product_dict)


flag = True
while flag:
    # split new users and old users
    name = input("Please enter your name: ")
    if name in user_dict.keys() and name not in blacklist:
        i = 0
        # if user enter wrong password for more than three times, quit the program
        while i < 3:
            password = input("Please enter your password: ")
            if password == user_dict[name][0]:
                print(product_dict.keys())
                # start shopping
                user_product = []
                flag2 = True
                while flag2:
                    print("You can exit by entering 'quit' at anytime.")
                    good = input("Please enter the product you want to buy: ")
                    if good == 'quit':
                        print("Thanks for your shopping!")
                        print(["Product: ", user_product, "Balance: ", user_dict[name][1]])
                        flag2 = False
                        break
                    else:
                        for index, goods in enumerate(product_dict.keys()):
                            if good in goods:
                                if int(product_dict[goods]) < int(user_dict[name][1]):
                                    user_dict[name][1] = int(user_dict[name][1]) - int(product_dict[goods])
                                    user_product.append(good)
                                elif good == 'quit':
                                    print(["Product: ", user_product, "Balance: ", user_dict[name][1]])
                                    flag2 = False
                                else:
                                    print("Your balance is not enough to buy this product.")
                            else:
                                continue
                break
            else:
                print("Wrong password!")
                i += 1
        if i >= 3:
            print("No Login!")
            # write this user name into blacklist file
            with open('blacklist.txt') as read_blacklist, open('.blacklist.txt.swap', 'w') as write_blacklist:
                data = read_blacklist.read()
                data = data + '\n' + name
                write_blacklist.write(data)
            os.remove('blacklist.txt')
            os.rename('.blacklist.txt.swap', 'blacklist.txt')

        flag = False
    else:
        # if the name is not in the users dictionary, use the entered name to create a new account
        print("Account is not exist or invalid. Please sign up!")
        flag3 = True
        while flag3:
            new_password = input("Please create your password: ")
            new_password2 = input("Please enter your password again: ")
            if new_password == new_password2:
                # compare the two passwords, if they are the same, append this customer into user dictionary
                new_balance = input("Please enter your salary: ")
                user_dict.update({name: [new_password, new_balance]})
                flag3 = False
            else:
                print("Passwords are inconsistent.")
                continue




