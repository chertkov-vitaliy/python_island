class HTMLBuilder:
    def __init__(self):
        self.page = Page()
    def build_head(self):
        self.page.head = """
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        """
        return self

    def build_body(self):
        self.page.body = """
            <body>
                <h1>Паттерны проектирования! </h1>
            </body>
            """
        return self

    def get_page(self):
        return self.page

class Page():
    head = None
    body = None

    def __str__(self):
        return  f"""
             <!DOCTYPE html>
             <html lang="en">
                  { self.head }  
                  { self.body } 
             </html>
        """

bld = HTMLBuilder()
page = bld.build_head().build_body().get_page()
print(page)



# class HouseBuilder:
#     def __init__(self):
#         self.house = House()
#
#     def build_walls(self):
#         self.house.walls = "Brick"
#         return self
#
#     def build_roof(self):
#         self.house.roof = "Tile"
#         return self
#
#     def build_windows(self):
#         self.house.windows = "Glass"
#         return self
#
#     def get_house(self):
#         return self.house
#
# class House:
#     walls = None
#     roof = None
#     windows = None
#
#     def __str__(self):
#         return f"House with {self.walls} walls, {self.roof} roof, and {self.windows} windows."
#
# # Использование
# builder = HouseBuilder()
# house = builder.build_walls().build_roof().build_windows().get_house()
# print(house)