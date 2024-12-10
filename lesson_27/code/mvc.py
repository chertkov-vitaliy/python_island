class Model():
    def get_data(self):
        return [{id:1, "name":'Peter'}, {id:2, "name":'Luna'} ]

class View():
    @staticmethod
    def render(data):
        return View.engine(data)

    @staticmethod
    def engine(data ):
        str = "<ol>"
        for user in data:
            str += '<li>' + user['name'] + '</li>'
        str += "</ol>"
        return str

class Controller():
    def index(self):
        md = Model()
        data = md.get_data()
        partial = View.render(data)
        bld = HTMLBuilder()
        page = bld.build_head().build_body(partial).get_page()
        page.save_html()




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

    def build_body(self, partial):
        self.page.body = f"""
            <body>
                <h1>Паттерны проектирования! </h1>
                {partial}
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
    def save_html(self):
        with open('index.html', 'w+') as fd:
            fd.write(str(self))






cnt = Controller()
cnt.index()