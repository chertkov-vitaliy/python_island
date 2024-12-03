class Car:
    #__slots__ = [ "color", "age", "vin"]
    def __iter__(self):
        return self

    def __init__(self):
        self.counter = 0
        self.age = 120
        self.vin = '1RUmmnmdsn34'

    def __next__(self):
        limit = len(self.__dict__)
        keys = self.__dict__.keys()

        if self.counter < limit:
            # res = self.__dict__[list(self.__dict__)[self.counter]]
            res = list(self.__dict__)[self.counter]
            self.counter += 1
            return res
        else:
            raise StopIteration

    # def __str__(self):
    #     return 'STR'
    #
    # def __repr__(self):
    #     return 'REPR'
    # def __eq__(self, obj):
    #     return self.color == obj.color


car1 = Car()
print(car1.__dict__)
for el in car1:
    print(el)


from abc import ABC, abstractmethod
#Mortal Kombat
class AFighter(ABC):
    def __init__(self, damage, hp=100):
        self.damage = damage
        self.hp = hp

    @abstractmethod
    def kick(self):
        pass

    @abstractmethod
    def punch(self):
        pass

    ''' f1  >=  f2 '''
    def __ge__(self, f2):
        f2.hp = f2.hp - self.kick()

    ''' f1  <=  f2 '''
    def __le__(self, f2):
        self.hp = self.hp - f2.kill()

        print('f1',self )
        print('f2', f2 )

    def __repr__(self):
        return f"hp: {self.hp} class {self.__class__} "

class Scorpion(AFighter):
    def __init__(self):
        super(Scorpion, self).__init__(10)
        self.lowkick = 20

    def kick(self):
        return self.lowkick

    def punch(self):
        return self.damage


class Subzero(AFighter):
    def __init__(self):
        super(Subzero, self).__init__(11)
        self.iceball = 25

    def kick(self):
        pass

    def punch(self):
        pass

    def kill(self):
        return self.iceball


f_sco = Scorpion()
f_sub = Subzero()

f_sco >= f_sub
f_sco <= f_sub
print(f_sub)
print(f_sco)
