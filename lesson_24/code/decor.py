def decorator_count(fn):
    pass
    def wrapper(*arg):
        print("Действия до вызова функции!")
        fn(*arg)
        print("Действия после вызова функции!")
    return wrapper


def insert(*str):
    print(f"Вставка! {str[0]}")

decorator_count(insert)

@decorator_count
def render(*str):
    print(f"render! {str[0]}")


print(render(2))
# res = decorator_count(insert)
#
# res('insert into t', 'fdsfds')
# res('insert into t2', 'fdsfds' )


