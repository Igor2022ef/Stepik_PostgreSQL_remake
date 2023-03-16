from sqlalchemy import create_engine, Integer, String, \
    Column, ForeignKey, Numeric, DateTime
from pandas import Timestamp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
# import psycopg2

engine = create_engine("postgresql+psycopg2://postgres:34567890@localhost/sqlalchemy_stepik_online_bookstore")
Base = declarative_base()

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer(), primary_key=True)
    name_author = Column(String(50), nullable=False)
    '''
                            ВОПРОС:Строка ниже звучит так: Объект A класса Author вызывает метод book, который
                                                            из таблицы Book вернет все переменные
                                                              с параметром autor (a.book())???????

    '''

    book = relationship("Book", backref="author")
    def __repr__(self):
        return "%s: %s" % (
            self.id, self.name_author
        )
class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer(), primary_key=True)
    name_genre = Column(String(50), nullable=False)
    book = relationship("Book", backref="genre")
    def __repr__(self):
        return "%s: %s" % (
            self.id, self.name_genre
        )
class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer(), primary_key=True)
    title = Column(String(50), nullable=False)
    author_id = Column(Integer(), ForeignKey('author.id'))
    genre_id = Column(Integer(), ForeignKey('genre.id'))
    price = Column(Numeric(10, 2),nullable=False)
    amount = Column(Integer())
    buy = relationship('Buy_book', backref='book')
    # author = relationship('Author', backref="book")
    def __repr__(self):
        return "%s: %s,%s,%s,%s,%s" % (
            self.id, self.title, self.author_id, self.genre_id, self.price, self.amount
        )
class City(Base):
    __tablename__ = 'city'
    id = Column(Integer(), primary_key=True)
    name_city = Column(String(50), nullable=False)
    days_delivery = Column(Integer())
    client = relationship('Client', backref='city')
    def __repr__(self):
        return "%s: %s,%s" % (
            self.id, self.name_city,self.days_delivery
        )
class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer(), primary_key=True)
    name_client = Column(String(100), nullable=False)
    city_id = Column(Integer(), ForeignKey('city.id'))
    email = Column(String(200),nullable=False)
    buy = relationship('Buy', backref='client' )
    def __repr__(self):
        return "%s: %s,%s,%s" % (
            self.id, self.name_client,self.city_id,self.email
        )
class Buy(Base):
    __tablename__ = 'buy'
    id = Column(Integer(), primary_key=True)
    buy_description = Column(String(100))
    client_id = Column(Integer(), ForeignKey('client.id'))
    book = relationship('Buy_book', backref='buy')
    '''
                                                        ВОПРОС: Уточнить бы, что записано в строке ниже
    '''
    step = relationship('Buy_step', backref='buy')
    def __repr__(self):
        return "%s: %s,%s" % (
            self.id, self.buy_description,self.client_id
        )
class Buy_book(Base):
    __tablename__ = 'buy_book'
    id = Column(Integer(), primary_key=True)
    buy_id = Column(Integer(), ForeignKey('buy.id'))
    book_id = Column(Integer(), ForeignKey('book.id'))
    amount = Column(Integer())
    def __repr__(self):
        return "%s: %s,%s,%s" % (
            self.id, self.buy_id,self.book_id,self.amount
        )
class Step(Base):
    __tablename__ = 'step'
    id = Column(Integer(), primary_key=True)
    name_step = Column(String(50), nullable=False)
    buy = relationship('Buy_step',backref='step')
    def __repr__(self):
        return "%s: %s" % (
            self.id, self.name_step
        )
class Buy_step(Base):
    __tablename__ = 'buy_step'
    id = Column(Integer(), primary_key=True)
    buy_id = Column(Integer(), ForeignKey('buy.id'))
    step_id = Column(Integer(), ForeignKey('step.id'))

                                                                         # Может быть правильно через DateTime()????:
                                                                        #  Ex: Column(DateTime(), default=datetime.now, onupdate=datetime.now)
                                                                        # Так реализовано в примере: https://pythonru.com/biblioteki/shemy-v-sqlalchemy-orm

    date_step_beg = Column(DateTime())
    date_step_end = Column(DateTime())
    def __repr__(self):
        return "%s: %s,%s,%s,%s" % (
            self.id, self.buy_id, self.step_id, self.date_step_beg, self.date_step_end
        )






