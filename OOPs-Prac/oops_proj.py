class chatbook:

    __user_id = 0

    def __init__(self):
        # print("Chatbook init method called")
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = "default user"
        # self.user_id = 0
        # self.user_id += 1
        self.username = ''
        self.password = ''
        self.loggedin = False
        # self.menu()
    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(value):
        chatbook.__user_id = value
        # return chatbook.__user_id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value

    def menu(self):
        user_input = input('''Welcome to Chatbook! how would you like to proceed ?
                          1. Press 1 to Signup 
                          2. Press 2 to Signin 
                          3. Press 3 to write a post
                          4. Press 4 to message a friend
                          5. Press 5 any other key to logout
                           
                           Your choice: ''')
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.my_posts()
        elif user_input == '4':
            self.sendmsg()
        else:
            exit()
    
    def signup(self):
        email = input("Enter your email id: ")
        pwd = input("setup your password : ")

        self.username = email
        self.password = pwd
        print("Signup successful!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("No user found, please signup first BY PRESS 1")
        
        else:
            uname = input("Enter your email id: ")
            pwd = input("Enter your password : ")

            if self.username == uname and self.password == pwd:
                print("Signin successful!")
                self.loggedin = True
            else:
                print("Invalid credentials, please try again")
        print("\n")
        self.menu()

    def my_posts(self):
        if self.loggedin:
            txt = input("Write your post: ")
            print("your content has been posted successfully!, post content: ", txt)
        else:
            print("Please signin to view your posts")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin:
            friend = input("Enter your friend's name: ")
            msg = input("Enter your message: ")
            print(f"Message sent to {friend}: {msg}")
        else:
            print("Please signin to send messages")
        print("\n")
        self.menu()

USER1 = chatbook()