# ---------------------- Learn Class -----------------


# class Bank:
#     def __init__(self, owner_name, balance):
#         self.owner_name = owner_name
#         self.balance = balance

#     def print_balance(self):
#         print(f"Current Balance: {self.balance:.2f}")

#     def deposit(self, amount):
#         print(f"The amount {amount} deposited")
#         self.balance += amount
#         print(f"The balance updated. updated balance is: {self.balance:.2f}")


# bank = Bank("Imran", 299)
# bank.print_balance()
# bank.deposit(500)


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def greet(self):
#         print(f"Hello I am {self.name}")

#     def has_passed(self):
#         if self.marks >= 50:
#             print("Passed")
#         else:
#             print("Fail")


# std1 = Student("Imran", 34)
# std1.greet()
# std1.has_passed()


# class Book:
#     total_books = 0

#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#         Book.total_books += 1

#     def info(self):
#         print(
#             f"""
#     Here are book details:
#               Book title: {self.title}
#               Book Author: {self.author}
#               Book price: {self.price}
# """
#         )

#     def discount(self, discount):
#         return self.price - (self.price * discount / 100)

#     @classmethod
#     def show_total_books(cls):
#         print(f"Total books are: {cls.total_books}")


# b1 = Book("The Hill man", "Imran", 1500)
# b2 = Book("The Hill man", "Imran", 1500)
# print(b1.info())
# print(b2.info())
# print(Book.show_total_books())


# class Ebook(Book):
#     def __init__(self, title, author, price, file_size):
#         super().__init__(title, author, price)
#         self.file_size = file_size

#     def info(self):
#         super().info()
#         print(f"File size: {self.file_size} MB")


# ebook1 = Ebook("Python Guide", "Imran", 1200, 15)
# ebook1.info()


# class Animal:
#     animals_count = 0

#     def __init__(self, name):
#         print("WE have animals class")
#         self.name = name
#         print(f"A new animal is added: {self.name}")
#         Animal.animals_count += 1

#     def print_animals(self):
#         print(f"Total animals are : {Animal.animals_count}")


# class Sound(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def animal_sound(self,sound):
#         print(f"This animal sound like: {sound}")


# class Bird(Animal):
#     def __init__(self, name):
#         super().__init__(name)

# dog = Sound("Dog")
# dog.animal_sound("Woof!")
# cat = Sound("Cat")
# cat.animal_sound("Meow!")

# dog.print_animals()


class Animal:
    total_animals = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species
        Animal.total_animals += 1

    def info(self):
        print(f"{self.name} is a {self.species}.")

    def speak(self):
        print(f"This animal make some sound...")


class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def speak(self):
        print(f"{self.name} says: Woof! Woof!")


class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def speak(self):
        print(f"{self.name} say Meow! Meow!")


class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def speak(self):
        print(f"{self.name} say Ku Ku")


dog = Dog("Puppy", "Dog")
cat = Cat("Arina", "Cat")
bird = Bird("Papeeya", "Bird")

zoo = [dog, cat, bird]

for animal in zoo:
    animal.info()
    animal.speak()
