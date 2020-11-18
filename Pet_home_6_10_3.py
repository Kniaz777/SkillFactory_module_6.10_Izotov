class Pet_home_client:
    def __init__(self, name, soname, balance):
        self.name = name
        self.soname = soname
        self.balance = balance

    def __str__(self):
        return 'Client: "{0} {1}". Balance: {2}'.format(self.name, self.soname, self.balance)


client = Pet_home_client('Иван', 'Петров', 50)
print(client)
print()

