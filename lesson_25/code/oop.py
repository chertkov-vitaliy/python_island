from abc import ABC, abstractmethod

class Car(ABC):
    def move(self):
        print("Go to phila")

    @abstractmethod
    def render(self):
        print('abstractmethod')

# cl = Car()
class Vaz(Car):
    def render(self):
        super().render()
        print('render')
    pass


obj = Vaz()
obj.render()


# class A:
#     age = 100
#     concert = []
#     def __init__(self, note):
#         self.note = note
#
#     @staticmethod
#     def sound():
#         for elm in A.concert:
#             print(f'self {elm.note}')
#
#     @classmethod
#     def Mozart(cls):
#         cls.concert.append(cls('Fuga Cmoll'))
#
#     @classmethod
#     def  Bash(cls):
#         cls.concert.append(cls('Fuga Cmoll'))
#
#
# A.Bash()
# A.Mozart()
# A.sound()

# a = A()
# a.render()
#
#
# a = A()
# a.sound()