class Account():
    def __init__(self, username, password):
        # username, password là thuộc tính
        self.username = username
        self.password = password

    # Phương thức login
    def login(self, u_input, p_input):
        # u_input là username nhập
        # p_input là password nhập
        if u_input == self.username and p_input == self.password:
            return True
        else:
            return False
        
    def __str__(self):
        return f'[{self.username}, [{self.password}]]'

