from create_class import Author, Book, Genre, City, Client, Buy, Buy_book, Step, Buy_step
from pandas import Timestamp

def create_table(session):
    a1 = Author(name_author="Булгаков М.А.")
    a2 = Author(name_author="Достоевский Ф.М.")
    a3 = Author(name_author="Есенин С.А.")
    a4 = Author(name_author="Пастернак Б.Л.")
    a5 = Author(name_author="Лермонтов М.Ю.")

    g1 = Genre(name_genre='Роман')
    g2 = Genre(name_genre='Поэзия')
    g3 = Genre(name_genre='Приключения')

    b1 = Book(title='Мастер и Маргарита', price=670.99, amount=3)
    b2 = Book(title='Белая гвардия', price=540.50, amount=5)
    b3 = Book(title='Идиот', price=460.00, amount=10)
    b4 = Book(title='Братья Карамазовы', price=799.01, amount=2)
    b5 = Book(title='Игрок', price=480.50, amount=10)
    b6 = Book(title='Стихотворения и поэмы', price=650.00, amount=15)
    b7 = Book(title='Черный человек', price=570.20, amount=6)
    b8 = Book(title='Лирика', price=518.99, amount=2)

    c1 = City(name_city='Москва', days_delivery=5)
    c2 = City(name_city='Санкт-Петербург', days_delivery=3)
    c3 = City(name_city='Владивосток', days_delivery=12)

    cl1 = Client(name_client='Баранов Павел', email='baranov@test')
    cl2 = Client(name_client='Абрамова Катя', email='abramova@test')
    cl3 = Client(name_client='Семенонов Иван', email='semenov@test')
    cl4 = Client(name_client='Яковлева Галина', email='yakovleva@test')

    bu1 = Buy(buy_description='Доставка только вечером')
    bu3 = Buy(buy_description='Упаковать каждую книгу по отдельности')

    bb1 = Buy_book(amount=1)
    bb2 = Buy_book(amount=2)
    bb3 = Buy_book(amount=1)
    bb4 = Buy_book(amount=2)
    bb5 = Buy_book(amount=2)
    bb6 = Buy_book(amount=1)
    bb7 = Buy_book(amount=1)
    bb8 = Buy_book(amount=1)

    s1 = Step(name_step='Оплата')
    s2 = Step(name_step='Упаковка')
    s3 = Step(name_step='Транспортировка')
    s4 = Step(name_step='Доставка')

    bs1 = Buy_step(date_step_beg=2, date_step_end=3)  # Expected type 'datetime', got 'tuple[int, int, int]' instead?????????
    bs2 = Buy_step(date_step_beg=2, date_step_end=4)
    bs3 = Buy_step(date_step_beg=2, date_step_end=5)
    bs4 = Buy_step(date_step_beg=5, date_step_end=11)
    bs5 = Buy_step(date_step_beg=10, date_step_end=17)
    bs6 = Buy_step(date_step_beg=7, date_step_end=3)
    bs7 = Buy_step(date_step_beg=4)
    bs9 = Buy_step(date_step_beg=8, date_step_end=12)
    bs10 = Buy_step(date_step_beg=3, date_step_end=7)
    bs11 = Buy_step(date_step_beg=2, date_step_end=6)
    bs12 = Buy_step(date_step_beg=21)
    bs13 = Buy_step(date_step_beg=16)

    A = session.add_all([a1, a2, a3, a4, a5])
    G = session.add_all([g1, g2, g3])
    B = session.add_all([b1, b2, b3, b4, b5, b6, b7, b8])
    C = session.add_all([c1, c2, c3])
    Cl = session.add_all([cl1, cl2, cl3, cl4])
    Bu = session.add_all([bu1, bu3])
    Bb = session.add_all([bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8])
    S = session.add_all([s1, s2, s3, s4])
    Bs = session.add_all([bs1, bs2, bs3, bs4, bs5, bs6, bs7, bs9, bs10, bs11, bs12, bs13])

    # session.new
    session.commit()
    session.close()

    return A, G, B, C, Cl, Bu, Bb, S, Bs

# if __name__ == '__main__':
#     create_table()
