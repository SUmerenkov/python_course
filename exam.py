#1

def len(lst: list):
    a=0
    for n in lst:
        a += 1
    return a
print(len([1,2,3,4,5,6]))


#2
def reserved(lst: list):
    return lst[::-1]
print(reserved([1,2,3,4,5,6]))

#3


#4
def to_title(string):
    str= [s.capitalize() for s in string.split(' ')]
    return(" ".join(el+' ' for el in str))
print(to_title('orlov ilya evgenyevich'))

#5
def count_symbol(srting, symbol):
    count = 0
    for i in srting:
        if (i == symbol):
            count +=1
    return (count)
print(count_symbol('Hi, Elvis, I am here!', 'i'))

#6
def format(string, agrument):
    string_len = len(string)
    

#7
import os.path
def copy_file(source, dest):
    if not os.path.exists(source):
        raise FileNotFoundError
    if os.path.exists(dest):
        raise FileExistsError
    with open(source, 'rb') as file:
        f= file.read()
    with open(dest, 'wb') as file:
        file.write(f)

copy_file('./111.txt', '/222.txt')


#8
import shutil
def copydir(source1, dest1):
    if not os.path.exists(source1):
        raise FileNotFoundError
    if os.path.exists(dest1):
        raise FileExistsError
    shutil.copytree(source1, dest1)

copydir('111', '222')

#9
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age


class Worker(User):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    def setSalary(self, salary):
        self.salary = salary
    def getSalary(self):
        return self.salary

John = Worker('John', 25, 1000)
Jack = Worker('Jack', 26, 2000)
print(f'Summary salary is {John.getSalary() + Jack.getSalary()}')

#10
class Money:
    def __init__(self, money):
        self.rub = int(money)
        self.kop = round(money - self.rub, 2)
    def __present__(self):
        return f"{self.rub},{self.kop * 100}"
    def summ(self, other):
        return Money(self.money() + other.)







#dop 1
#Перебор быстрее работает с tupl, так как он является не изменяемым, и данные расположены последовательно в памяти.

#dop 2
#В случае x создается три ссылки на один объект. При изменении x изменение отразится на всех выводимых элементах.

#dop 3
class Count:
    i = 0
    def __init__(self):
        self.i +=1
    @classmethod
    def count(cls):
        return cls.i

#dop4
def dict(arg, kward):
    dic = {}
    for i in enumerate(arg):
        if i < len(kward):
            dic(arg) = None
    return dic

print(dict([1,2,3,4], ['a','b','c']))