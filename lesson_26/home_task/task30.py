#  1. Реализовать класс DB - синглтон. Экземляр класса(подключение) к PostgreSQL
#  должно быть единственным.

#  2. Реализовать  фабрику которая создает модели различных производителей

class Car:
    def __init__(self, brand, model):
        """Инициализируйте атрибуты brand и model"""

    def make_lada():
        "реализуйте метод для создания  автомобиля Lada"

    def make_mercedes():
        "реализуйте метод для создания  автомобиля Mercedes"

    def make_toyota():
        "реализуйте метод для создания создания Toyota"

    def __repr__(self):
        "Реализуйте логику дандера"



# 3. Реализовать для класса Car абстрактный класс который содержит
# aбстрактные методы sold, discount

    def sold(self):
        """Автомобиль продан"""
        print(f"Автомобиль {self.brand} {self.model} продан ")
    
    def discount(self):
        """Скидка на автомобиль"""
        print(f"На автомобиль {self.brand} {self.model} скидка 5%")