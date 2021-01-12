import random
from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Constants for generating
FIRST_NAMES = ["Alexey", "Dmitry", "Vladimir", "Vsevolod", "Stanislav", "Victor",
               "Petr", "Ilya", "Fedor", "Anton", "Vadim"]
SECOND_NAMES = ["Alexeev", "Dmitriev", "Vladimirov", "Vsevolodov", "Stasov",
                "Victorov", "Petrov", "Ilyin", "Fedorov", "Antonov", "Vadimov"]
PROFILES = ["Software Engineering", "Hardware Engineering", "Fundamental Mathematics",
           "Physics", "Biology", "Chemistry", "Astronomy", "History"]
STATUSES = ["Bachelor",  "PhD", "Magiser"]

#Method for generating
def generate():
    firstNamesCount = len(FIRST_NAMES)
    secondNamesCount = len(SECOND_NAMES)
    profilesCount = len(PROFILES)
    statusesCount = len(STATUSES)

    firstName = FIRST_NAMES[random.randint(0, firstNamesCount - 1)]
    secondName = SECOND_NAMES[random.randint(0, secondNamesCount - 1)]
    profile = PROFILES[random.randint(0, profilesCount - 1)]
    year = random.randint(1, 4)

    if year >= 4:
        status = "banchelor"
    elif year >= 3:
        status = STATUSES[random.randint(0, 2)]
    else:
        status = STATUSES[random.randint(0, statusesCount) - 1]

    student = Student(firstName=firstName, secondName=secondName, profile=profile,
                      year=year, status=status)

    return student



engine = create_engine("sqlite:///students_db.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    firstName = Column(String(30))
    secondName = Column(String(30))
    profile = Column(String(40))
    year = Column(Integer)
    status = Column(String(30))



if __name__ == "__main__":
    Base.metadata.create_all(engine)
    for i in range(10000):
        currentStudent = generate()
        session.add(currentStudent)


    session.commit()


