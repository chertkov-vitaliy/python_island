class Cache:
    def __init__(self):
        self.__storage = {}

    @property
    def storage(self):
        return self.__storage

    def storage_by_key(self, key):
        if key in self.__storage:
            return self.__storage[key]
        else:
            return None

    @storage.setter
    def storage(self, dict):
        key, value = dict
        self.__storage[key] = value

obj = Cache()
obj.storage = ('token', 'dfasdf776fds8kjhsdf687a6sfbs')
print(obj.storage_by_key('token'))
