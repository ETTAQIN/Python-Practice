import os

products = [
    ['iPhone', 8000],
    ['mac book', 12000],
    ['bike', 500],
    ['Python Book', 100],
    ['coca', 5]
]

shopping_cart = {}
current_user_info = []

# simulate database
users_db = r'users_db.txt'

while True:

    print('''
    1. Sign in
    2. Sign up
    3. Shopping
    ''')

    choice = input(">>: ").strip()

    if choice == '1':
        # 1. Sign in
        flag = True
        count = 0
        while flag:
            username = input("Please enter your user name: ")
            password = input("Please enter your password: ")

            # if enter wrong password more than 3 times, exit this while loop to sign up
            if count == 3:
                # put this name into blacklist
                with open('blacklist.txt', 'a') as f:
                    f.write('%s\n' % username)
                    f.flush()

                print("No Login! Please sign up again.")
                break

            with open('blacklist.txt', 'r') as blacklist:
                blacklist = blacklist.read()

            if username in blacklist:
                print("No Login! Please sign up again.")
                break
            else:
                with open(users_db, 'r') as f:
                    for line in f:
                        line = line.strip('\n')
                        user_info = line.split('|')

                        username_of_db = user_info[0]
                        password_of_db = user_info[1]

                        # compare username adn password with each line
                        if username == username_of_db and password == password_of_db:
                            print("Login Success!")

                            # check the account balance
                            if len(user_info) == 3:
                                balance_of_db = user_info[2]
                                balance = balance_of_db
                                balance = int(balance)
                            else:
                                while True:
                                    salary = input("Please input your salary: ").strip()
                                    if not salary.isdigit():
                                        continue
                                    salary = int(salary)
                                    balance = salary
                                    break

                            # add username and balance to current user list
                            current_user_info = [username_of_db, balance]
                            print('Username: %s, please choose 3 to begin shopping.' % current_user_info)
                            flag = False
                            break

                    else:
                        print("Wrong username or password!")
                        count += 1

    elif choice == '2':
        # sign up
        new_name = input("Please create your username: ").strip()
        while True:
            new_password = input("Please create your password: ").strip()
            new_password2 = input("Please enter your password again: ").strip()
            if new_password == new_password2:
                print('Sign up Successful! Please choose 1 to sign in')
                break
            else:
                print("Passwords are inconsistent.")

        with open(users_db, 'a') as f:
            f.write('%s|%s\n' % (new_name, new_password))
            f.flush()

    elif choice == '3':
        # shopping
        # if current_user_info is empty, hint sign in
        if not current_user_info:
            print('Please sign in!')
        else:
            # Begin shopping
            username_of_db = current_user_info[0]
            balance = current_user_info[1]

            # Present user information
            print('Hello, {}! Your balance is {}. Enjoy your shopping!'.format(username_of_db, balance))

            flag = True
            while flag:
                # Print products information after each action
                index_list = []
                for index, product in enumerate(products):
                    index_list.append(index)
                    print(index, product)

                choice3 = input("Please enter the product you want to buy or enter 'q' to quit: ").strip()

                if choice3.isdigit():
                    choice = int(choice3)
                    if choice not in index_list:
                        continue

                    product_name = products[choice][0]
                    product_price = products[choice][1]

                    # check balance
                    if balance > product_price:
                        if product_name in shopping_cart:
                            shopping_cart[product_name]['count'] += 1
                        else:
                            shopping_cart[product_name] = {'product_price': product_price, 'count': 1}

                        balance -= product_price
                        current_user_info[1] = balance

                        print('Add product' + product_name + 'into your shopping cart. Your current balance is ' + str(balance))

                    else:
                        print("Your balance is not enough! Product price is {}, {} needed.".format(
                            product_price,
                            product_price - balance
                        ))

                    print('Your shopping cart: %s' % shopping_cart)

                elif choice3 == 'q':
                    if not shopping_cart:
                        print("Thanks for your shopping!")
                    else:
                        print('''
                        ------------------------------------ Purchased Products List -------------------------------------
                        ID              Products              Quantity              Price               Amount
                        ''')

                        total_cost = 0
                        for i, key in enumerate(shopping_cart):
                            print('%22s%22s%20s%20s%22s' % (
                                i,
                                key,
                                shopping_cart[key]['count'],
                                shopping_cart[key]['product_price'],
                                shopping_cart[key]['count'] * shopping_cart[key]['product_price']
                            ))
                        total_cost += shopping_cart[key]['count'] * shopping_cart[key]['product_price']

                        print('''
                        Total cost: {}
                        Your balance: {}
                        ----------------------------------------------- END --------------------------------------------
                        '''.format(total_cost, balance))

                        while flag:
                            decision = input("Confirm your shopping[yes/no?]: ").strip()
                            if decision not in ['Y', 'N', 'y', 'n', 'yes', 'no']: continue
                            if decision in ['Y', 'y', 'yes']:
                                # write balance into database
                                src_file = users_db
                                dst_file = r'%s.swap' % users_db
                                with open(src_file, 'r') as read_f, open(dst_file, 'w') as write_f:
                                    for line in read_f:
                                        if line.startswith(username_of_db):
                                            user_info_line_list = line.strip('\n').split("|")
                                            balance_of_db = balance
                                            balance_of_db = str(balance_of_db)
                                            if len(user_info_line_list) == 2:
                                                user_info_line_list.append(balance_of_db)
                                            else:
                                                user_info_line_list[-1] = balance_of_db
                                                line = '|'.join(user_info_line_list) + '\n'

                                        write_f.write(line)

                                os.remove(src_file)
                                os.rename(dst_file, src_file)

                                print('Purchase Successfully!')

                            shopping_cart = {}
                            current_user_info = []
                            flag = False

                else:
                    print('Wrong input!')

    else:
        print('Wrong access!')








