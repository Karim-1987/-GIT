class Client:

    def __init__(self, name, city, balance):
        self.name = name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"{self.name}. {self.city}. Баланс: {self.balance} руб. "

    def corporate_guest(self):
        return f"{self.name} г.{self.city}"


person_1 = Client(name="Иван Петров",
                  city="Москва",
                  balance="50")
person_2 = Client(name="Иван Сидоров",
                  city="Казань",
                  balance="100")
person_3 = Client(name="Петр Иванов",
                  city="Самара",
                  balance="150")

print(person_1.__str__())
clients = [person_1, person_2, person_3]
for guest in clients:
    print(guest.corporate_guest())




