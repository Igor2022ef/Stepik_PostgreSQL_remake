from create_class import *
# from create_tables_val import *
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# import psycopg2
from sqlalchemy.orm import Session, sessionmaker
from create_methods import *

def main():
    Base.metadata.create_all(engine)
    Session=sessionmaker(bind=engine)
    session=Session()
    A,G,B,C,Cl,Bu,Bb,S,Bs=create_table(session)

def make_methods():
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # methods_take_inform(session)
    # group_methods_take_inform(session)
    wow_join_weth(session)
    # other_common_methods(session)
    # methods_calculate_inform(session)

def clear_base():
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    # main()
    make_methods()
    # clear_base()
