from profile.user import Profile


class CreateProfile(Profile):

    def __init__(self, username: str, password: str) -> None:
        super().__init__(username, password)

    def username_validation(self) -> None:
        """ force you to make a unique username"""
        while self.is_username_exist():
            print("your user name is already exist! ")
            self.username = input("Enter your username again : ")

    def password_validation(self) -> None:
        """ force you to make a safe password"""
        while not self.safe_password():
            print("your password isn't safe .")
            self.password = input("Enter your password again : ")

    def userpass_validation(self) -> None:
        """check username and password are exist"""
        while not self.is_userpass_valid():
            print("your username or password is wrong .try again .")
            self.username = input("Enter your username again : ")
            self.password = input("Enter your password again : ")
