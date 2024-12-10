from sqlalchemy import text
from model import User, Account, db, app

account = Account(login="admin", password="123")


with app.app_context():
    db.session.add(account)
    db.session.commit()
    #
    # user = db.session.execute(db.select(Account).filter_by(login="admin")).scalars()
    # print(user)
    # for obj in user:
    #     print(obj.login)
    #     print(obj.password)
        # print(obj.index)
        # print(obj.keys())

    sql = text("select login, password from account where id = :id")
    result = db.session.execute(sql, {"id": 1})
    print(result)
    for i in result:
        print(i)
