#import step
from sqlalchemy import create_engine, ForeignKey,Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = "people" #table name
    ssn = Column("ssn", Integer, primary_key=True) #column with name ssn
    firstname = Column("firstname",String)
    lastname = Column("lastname",String)
    gender = Column("gender",CHAR)
    age = Column("age",Integer)
    
    def __init__(self,ssn,first,last,gender,age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age


    def __repr__(self):
        return f"({self.ssn} {self.firstname} {self.lastname} {self.gender} {self.age})"

engine = create_engine("sqlite:///fasterdb.db",echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
#p1 = Person(12313,"Saunak","Mukherjee","F",19)
#p2 = Person(12445,"Para","pal","M",19)

#session.add(p2)
#session.add(p1)


#session.commit()

from fastapi import FastAPI
app = FastAPI()

# URL/hello is an endpoint (slash something)
@app.get("/") #this is app.route in flask
def home():
    return None
# @app.route("/sex/<user>") in flask
@app.get("/{ssn}/{fname}/{lname}/{gender}/{age}")
def result(ssn,fname,lname,gender,age):
    data = {"ssn":ssn,
            "firstname":fname,
            "lastname":lname,
            "gender":gender,
            "age":age}


    p = Person(data["ssn"],data["firstname"],data["lastname"],data["gender"],data["age"])
    session.add(p)
    session.commit()
    
    return data
