from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def list_contents(self, indent=0):
        pass


class List(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def list_contents(self, indent=0):
        print("  " * indent + f"- {self.name} ({self.size} bytes)")


class Node(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def get_size(self):
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size

    def list_contents(self, indent=0):
        print("  " * indent + f"+ {self.name}/")
        for child in self.children:
            child.list_contents(indent + 1)


# Пример использования
root = Directory("root")
documents = Directory("documents")
pictures = Directory("pictures")
file1 = File("document1.txt", 1024)
file2 = File("image1.jpg", 2048)
file3 = File("document2.pdf", 512)

root.add(documents)
root.add(pictures)
documents.add(file1)
documents.add(file3)
pictures.add(file2)

root.list_contents()
print(f"Total size: {root.get_size()} bytes")