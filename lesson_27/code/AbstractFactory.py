from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

class WinFactory(AbstractFactory):
    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()

class MacFactory(AbstractFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

class AbstractButton(ABC):
    @abstractmethod
    def render(self):
        pass

class WinButton(AbstractButton):
    def render(self):
        print("Rendering Windows button")

class MacButton(AbstractButton):
    def render(self):
        print("Rendering macOS button")

class AbstractCheckbox(ABC):
    @abstractmethod
    def render(self):
        pass

class WinCheckbox(AbstractCheckbox):
    def render(self):
        print("Rendering Windows checkbox")

class MacCheckbox(AbstractCheckbox):
    def render(self):
        print("Rendering macOS checkbox")

# Клиентский код
factory = WinFactory()
button = factory.create_button()
checkbox = factory.create_checkbox()
button.render()
checkbox.render()

factory = MacFactory()
button = factory.create_button()
checkbox = factory.create_checkbox()
button.render()
checkbox.render()