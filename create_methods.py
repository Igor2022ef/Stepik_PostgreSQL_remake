from sqlalchemy import or_, and_, not_, desc
from create_class import Author, Genre, Book, City, Client, Buy, Buy_book, Step, Buy_step
from pandas import Timestamp
from create_tables_val import *

def methods_take_inform(session):
# 1.2 Выборка данных
# Все записи из таблицы Author или другой
    all_data_table=(session.query(Author).all())
    print(f"Все записи из таблицы Author: {all_data_table}")
#Показывает сырой запрос
    print(f"Сырой запрос записи из таблицы Author:{session.query(Book)}")
    print(100*'-')

# Записи из отдельных столбцов
# Вариант 1
    q1=session.query(Book).all()
    for c in q1:
        print(f"Записи из отдельных столбцов Вариант 1 author_id: {c.author_id}, title: {c.title}")
    print(100 * '-')
#Вариант 2
    different_column = (session.query(Book.id, Book.price).all())
    print(f"Записи из отдельных столбцов Вариант 2 Book.id и Book.price: {different_column}")
    print(f"Сырой запрос 'Записи из отдельных столбцов Вариант 2' {session.query(Book.id, Book.author_id)}")
    print(100*'-')
# count() возвращает количество элементов в результате.
    count_element_column = (session.query(Book.title).count())
    print(f"Количество элементов в столбце Book.title: {count_element_column}")
    print(100*'-')
# first() возвращает первый результат запроса или None, если последний не вернул данных.
    first_result = session.query(Book.title).first()
    first_result_row = session.query(Book).first()
    print(f"Первый результат в столбце Book.title: {first_result}")
    print(f"Первая строка в таблице Book: {first_result_row}")
    print(100*'-')
# get() возвращает экземпляр с соответствующим первичным ключом или None, если такой объект не был найден.
    prim_key_result = session.query(Book).get(6)
    print(f"Данные из столбца с перв. ключем 6 в Book: {prim_key_result}")
    print(100*'-')

def group_methods_take_inform(session):
# Метод filter() позволяет отфильтровать результаты, добавив оператор WHERE, принимает колонку, оператор и значение.
    filter_where = session.query(Buy_step).filter(Buy_step.buy_id > 2, Buy_step.id < 7).all()
    print(f"filter() по условиям для buy_id и id из Buy_step: {filter_where}")
    filter_where_1 = session.query(Buy_step).filter(Buy_step.buy_id > 2, Buy_step.id < 7)
    print(f"Сырой запрос filter() по условиям для buy_id и id из Buy_step: {filter_where_1}")
    print(100*'-')
#Вариант с иным вариантом записи фильтра, использубщим логические функции:
    filter_where_differ_1 = session.query(Book).filter(or_(Book.id > 3, Book.price > 500)).all()
    print(f"Все книги с id>3 или ценой > 500 из Book:{filter_where_differ_1}")
    filter_where_differ_11 = session.query(Book).filter(or_(Book.id > 3, Book.price > 500))
    print(f"Сырой запрос filter() Все книги с id>3 или ценой > 500 из Book: {filter_where_differ_11}")
    print(100 * '-')

#Более сложная форма запроса:
    filter_where_differ_2 = session.query(Book).filter(and_(Book.id > 3,
                                                    not_(Book.price < 500)
                                                    )).all()
    print(f"Все книги с id>3 и ценой > 500 из Book: {filter_where_differ_2}")
    filter_where_differ_21 = session.query(Book).filter(and_(Book.id > 3,
                                                    not_(Book.price < 500)
                                                    ))
    print(f"Сырой запрос filter() Все книги с id>3 и ценой > 500 из Book: {filter_where_differ_21}")
    print(100 * '-')
#Использование списков, метод in:
    filter_in = session.query(Book).filter(Book.title.notin_(['Идиот', 'Игрок'])).all()
    print(f"Список книг с названиями не в списке 'Идиот', 'Игрок' {filter_in}")
    filter_in = session.query(Book).filter(Book.title.notin_(['Идиот', 'Игрок']))
    print(f"Сырой запрос Список книг с названиями не в списке 'Идиот', 'Игрок'{filter_in}")
    print(100 * '-')
#Метод like() выполняет поиск с учетом регистра.
    filter_like = session.query(Book).filter(Book.title.like('И%')).all()
    print(f"Список книг, названия начинаются на И: {filter_like}")
#Метод ilike() выполняет поиск без учета регистра.
    filter_ilike = session.query(Book).filter(Book.title.ilike('м%')).all()
    print(f"Список книг, названия начинаются на м: {filter_ilike}")
    filter_ilike_1 = session.query(Book).filter(Book.title.ilike('м%'))
    print(f"Сырой запрос Список книг, названия начинаются на м: {filter_ilike_1}")
    print(100 * '-')
#Метод order_by() сортировка колонок результата, по умолчанию по возрастанию:
    orderby_column = session.query(Book).filter(Book.price < 600.00, (Book.id > 5)).order_by(Book.title).all()
    print(f"Сортировка по title сложного запроса: {orderby_column}")
    orderby_column_1 = session.query(Book).filter(Book.price < 600.00, (Book.id > 5)).order_by(Book.title)
    print(f"Сырой запрос Сортировка по title сложного запроса: {orderby_column_1}")
    print(100 * '-')
#Метод order_by() сортировка колонок результата по убыванию:
    orderby_column_2 = session.query(Book).filter(Book.price < 600.00).order_by(desc(Book.title)).all()
    print(f"Сортировка по убыванию по title запроса для Book: {orderby_column_2}")
    print(100 * '-')

def wow_join_weth(session):
#Метод join() используется для создания SQL INNER JOIN.
# Он принимает название таблицы, с которой нужно выполнить SQL JOIN.



def other_common_methods(session):
#Метод limit() добавляет оператор LIMIT к запросу. Он принимает количество записей, которые нужно вернуть.
    limit_rows = session.query(Author).limit(2).all()
    print(f"limit() Первые две строки из Author: {limit_rows}")
    limit_rows_1 = session.query(Author).limit(2)
    print(f"Сырой запрос limit() Первые две строки из Author: {limit_rows_1}")
    print(100 * '-')
#Метод offset() добавляет оператор OFFSET к запросу. Он принимает в качестве аргумента значение смещения.
# Часто используется с оператором limit().
    offset_limit = session.query(Book).limit(2).offset(2).all()
    print(f"Первые две строки из Book со смещением на 2 стр.: {offset_limit}")






def methods_calculate_inform(session):
#Создание вычисляемого столбца
    add_column=(session.query(Book.price * Book.amount).all())
    print(f"Значение вычисляемого столбца Book.price*Book.amount: {add_column}")
    print(100*'-')

#Математические функции                                        #ВОПРОС: Надо всегда иметь в виду, что мы работаетм с кортежем?
    math_func=session.query(Book.amount).all()
    for c in math_func:
        b=abs(c[0])
        print(f"Математические функции Значение abs(Book.amount[i]): {b}")
    print(100*'-')

#Выборка данных с вычисляемыми столбцами
    add_column_take=session.query(Book.title, Book.price*0.7).all()
    print(f"Выборка данных с вычисляемыми столбцами Book.title и Book.price*0.7: {add_column_take}")
    for c in add_column_take:
        print(c)
    print(f"Сырой запрос 'Выборка данных с вычисляемыми столбцами Book.title и Book.price*0.7' "
          f"{session.query(Book.title, Book.price * 0.7)}")
    print(100*'-')

    '''
                                                                    ВОПРОС: Как организовать запрос ниже без ошибки??
    '''

#Выборка данных, вычисляемые столбцы, логические функции
    # a=Author()
    # q = session.query(Book).filter(or_(a.book.name_author=="Булгаков М.А.",
    #                                    Book.name_author=='Есенин С.А.')).all()

    '''
                                                                На код ниже PyCh ругается, уточни, что там должно быть
    '''
    # for c in q:
    #     print(c)
    # q = session.query(Book).filter(or_(
    # print(session.query(Book).filter(or_(Book.title=="Мастер и Маргарита",
    #                                    Book.title=='Черный человек')))




