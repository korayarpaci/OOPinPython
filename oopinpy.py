### OOP ( Object-Oriented Programming ) ( Nesne Tabanlı Programlama )
## Nesneler üzerine kurulu bir paradigmadır. Nesneler veriler/özellikler ( attributes ) ve bu verilere uygulanan davranışlar
# ( methods/behaviors) içerir

### 1 - Nesne ( Object )
## Sınıfların örnekleridir ( instances ). Attributeları ve behaviorları bir araya getirir
# Örnek

class Car:
    model = "Ford Mustang" ## Attribute

    def starting(self):
        ## Behavior
        return " Car's started"

car1 = Car()
print(car1.model) # Çıktı : Ford Mustang
print(car1.starting()) # Çıktı : Car's started

### 2 - Sınıf ( Class )
## nesneler için bir şablondur. Ortak attributelar ve behaviorlar bu şablon ile tanımlanır.
## bir class çağırırken attribute belirtilmezse ( çağırılmazsa ) memorydeki adres çıktısını verir.
# Örnek

class Human:
    def __init__(self,name,age): ## Constructor ( Yapıcı Metod )
        self.name = name
        self.age = age

    def say_hello(self): ## Behavior
        return f"Hello my name's {self.name} and i'm {self.age}"
human = Human("Koray",21) ## Çıktı:  Hello my name's Koray and i'm 21
print(human.say_hello())

### 3 - Yapıcı Metod ( Constructor )
## Nesne oluşturulurken otomatik olarak çağırılan metottur. Python'da __init__ ( initialization ) metodu ile tanımlanır.
# Örnek

class Book:
    def __init__(self,name ,author):
        self.name = name
        self.author = author
book = Book("Olasılıksız","Adam Fawer")
print(book.name, book.author) # Çıktı : Olasılıksız Adam Fawer

### 4 - Davranış ( Behavior )
## Bir nesnenin ne yapabileceğini belirler. Behaviorlar, sınıfın içinde tanımlanan metotlarla temsil edilir.
## Her nesne, sınıfın tanımladığı behaviorları kullanabilir.
# Örnek

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def sum(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num1 / self.num2

calculate = Calculator(12,12)
print(calculate.sum(), calculate.subtract(), calculate.multiply(), calculate.divide()) # Çıktı : 24 0 144 1.0

### 5 - Kapsülleme ( Encapsulation )
## Bir sınıfın verilerini ve davranışlarını gizler. Pythonda _ veya __ ile özelliğin veya metodun erişimi sınırlandırılabilir.
## " _ " Korunmuş ( Prodected ) : _ ile başlayan özellik veya metotlar, bir konvansiyon ( yazılı olmayan kural ) olarak yalnızca
## sınıfın kendisi ve alt sınıfları ( subclasses) tarafından kullanılmalıdır. Ancak teknik olarak erişimi engellenemez.
##" __ " Özel ( Private ) : __ ile başlayan özellik veya metotlar, sınıf dışından doğrudan erişimi engellemek için kullanılır.
## Kapsülleme ( Private/Prodected )  olduğu yerlerde get/set metotları kullanılır.
# Örnek

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def withdraw(self, amount):
        self.__balance = self.__balance - amount
        return f"Kalan Bakiye : {self.__balance} "

acc = BankAccount(100)
print(acc.withdraw(50)) # Çıktı : Kalan Bakiye : 50

### 6 - Miras Alma ( Inheritance )
## Bir sınıfın  başka bir sınıfın attributelarını ve behaviorlarını devralması.
## super().__init__() = Parent classın initini kullanılabilir hale getirir.
# Örnek

class Animal:
    def  make_sound(self):
        return " Bir ses çıkardı. "

class Dog(Animal):
    def make_sound(self):
        return "Hav Hav"

dog = Dog()
print(dog.make_sound()) # Çıktı : Hav Hav

### 7 - Çok Biçimlilik ( Polymorphism )
## Farklı sınıfların aynı isimli metotlara sahip olmasını sağlar
# Örnek

class Bird:
    def move(self):
        return "Uçar"
class Fish:
    def move(self):
        return "Yüzer"
def movement_definition(animal):
    print(animal.move())
bird = Bird()
fish = Fish()
movement_definition(bird) # Çıktı : Uçar
movement_definition(fish) #Çıktı Yüzer

### 8 - Soyutlama ( Abstraction )
## Gereksiz detayları gizleyerek önemli bilgileri vurgular. abc modülü kullanılarak soyut sınıflar oluşturulabilir.
## ABC = Abstract Base Class
## Abstract metotunun kullanıldığı parent classtaki tüm metotları child classta kullanmak zorundasın.
## Child classta parent classta olmayan metot tanımlanabilir.
# Örnek

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
square = Square(5)
print(square.area()) # Çıktı : 25

### 9 - Sınıf ve Statik Metotlar ( Class Methods / Static Methods )
## Sınıfa veya sınıfın örneğine bağlı olmayan davranışlardır.
# Örnek

class Factory:
    product = 0
    @classmethod
    def produce_product(cls):
        cls.product += 1
        return cls.product
    @staticmethod
    def info():
        return " Bu bir fabrika sınıfıdır."

print(Factory.produce_product()) ## Çıktı : 1
print(Factory.info()) ## Çıktı : Bu bir fabrika sınıfıdır.

### 10 - Özel Metotlar ( Special Methods )
## Dunger Methods veya Magic Methods
## Python'da __ ile başlayan ve özel anlamı olan metotlardır.
# Örnek

class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Kişi {self.name}"
person = Person("KORAY")
print(person) ## Çıktı : Kişi : KORAY

### 11 - Overriding ( Geçersiz Kılma )
## Geçersiz kılma, üzerine yazma anlamına gelir.
## Monkey sınıfı overriding methodu çağırıyor. Animal ve Monkey sınıflarında da aynı isme sahip methodlar mevcut.
## Ama çıktı olarak Animal Class ve Monkey Class geliyor.
## Böylelikle Monkey Class'ı, Animal Class'ındaki toString Methodunu geçersiz kılmış oluyor.
## Overriding ile birlikte polimorfizmde yapılır
# Örnek
class Animal:  # Parent
    def toString(self):
        print("Animal Class")


class Monkey(Animal):  # Child

    def toString(self):
        print("Monkey Class")


animal1 = Animal()
animal1.toString()

monkey1 = Monkey()
monkey1.toString()
