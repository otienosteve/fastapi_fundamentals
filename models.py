from sqlalchemy import Column, create_engine, String, Integer,DateTime, Date
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__= 'students'
    id = Column(Integer, primary_key=True)
    first_name= Column(String)
    last_name= Column(String)
    email = Column(String)
    dob = Column(Date)


engine =create_engine('sqlite:///school.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()
