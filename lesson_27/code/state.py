from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

class RedState(State):
    def handle(self, context):
        print("Красный свет. Стоп.")
        context.transition_to(YellowState())

class YellowState(State):
    def handle(self, context):
        print("Желтый свет. Приготовьтесь.")
        context.transition_to(GreenState())

class GreenState(State):
    def handle(self, context):
        print("Зеленый свет. Езжайте.")
        context.transition_to(RedState())

class TrafficLightContext:
    def __init__(self, state: State):
        self.state = state

    def transition_to(self, state: State):
        print("Переключение состояния...")
        self.state = state

    def handle(self):
        self.state.handle(self)

# Использование
traffic_light = TrafficLightContext(RedState())
for _ in range(3):
    traffic_light.handle()