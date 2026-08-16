class User:
    __numberOfUsers = 0

    def __init__(self, name):
        self.name = name
        self.id = User.__numberOfUsers
        User.__numberOfUsers +=1

    @classmethod
    def getNumberOfUsers(cls):
        return cls.__numberOfUsers

if __name__ == '__main__':
    user1 = User("Alice")
    user2 = User("Bob")
    user3 = User("Charlie")
    print(f"# of users: {User.getNumberOfUsers()}")