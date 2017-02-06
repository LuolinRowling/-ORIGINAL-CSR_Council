####################################################################################
## Copyright (c) 2017 CSR
## Apache-2.0 License
## Author: TinBacon from BUPT
## Initialize on 6 Feb 2017
## Update on 7 Feb 2017
####################################################################################

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()

####################################################################################
## Database tables
## ORM objects
####################################################################################

# Person table
class DBPerson(Base):

    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    graduation = Column(Integer)
    name = Column(String)
    sex = Column(Integer)
    phone = Column(Integer)
    qq = Column(Integer)
    mail = Column(String)
    home = Column(String)
    association = Column(String)

    def __init__(self, id, grd, name, sex, phn, qq, mail, home, assc):
        self.id = id
        self.graduation = grd
        self.name = name
        self.sex = sex
        self.phone = phn
        self.qq = qq
        self.mail = mail
        self.home = home
        self.association = assc

# Education table
class DBEducation(Base):

    __tablename__ = 'education'

    id = Column(Integer)
    degree = Column(Integer)
    university = Column(String)
    college = Column(String)
    year = Column(Integer)
    duration = Column(Integer)

    def __init__(self, id, deg, uni, coll, year, dur):
        self.id = id
        self.degree = deg
        self.university = uni
        self.college = coll
        self.year = year
        self.duration = dur

# Work table
class DBWork(Base):

    __tablename__ = 'work'

    id = Column(Integer)
    orgnization = Column(String)
    year = Column(Integer)

    def __init__(self, id, org, year):
        self.id = id
        self.orgnization = org
        self.year = year

####################################################################################
## Engine
## Database Operation
####################################################################################
class DBEngine(object):

    def __init__(self):

        self.engine = create_engine('sqlite:///DB/db.sqlite', echo=False)

        db_session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.session = db_session()

    def closeDB(self):

        self.session.close()

    ####################################################################################
    # DBPerson
    ####################################################################################

    # Add Person
    def addPerson(self, id, grd, name, sex, phn, qq, mail, home, assc, deg, uni, coll, edu_year, dur, org=None, work_year=None):

        person = DBPerson(id, grd, name, sex, phn, qq, mail, home, assc)
        self.session.add(person)
        self.session.commit()

        self.addEdu(id, deg, uni, coll, edu_year, dur)

        if not org == None:
            self.addWork(id, org, work_year)

    # Delete Person
    def deletePerson(self, id):

        self.session.query(DBPerson).filter(DBPerson.id == id).delete()
        self.session.commit()

        self.deleteEdu(id)
        self.deleteWork(id)

    # Edit Person
    def editPerson(self, id, grd=None, name=None, sex=None, phn=None, qq=None, mail=None, home=None, assc=None,
                   deg=None, uni=None, coll=None, edu_year=None, dur=None, org=None, work_year=None):

        person = self.session.query(DBPerson).filter(DBPerson.id == id)

        if not grd == None:
            person.update({'graduation':grd})
        if not name == None:
            person.update({'name':name})
        if not sex == None:
            person.update({'sex':sex})
        if not phn == None:
            person.update({'phone':phn})
        if not qq == None:
            person.update({'qq':qq})
        if not mail == None:
            person.update({'mail':mail})
        if not home == None:
            person.update({'home':home})
        if not assc == None:
            person.update({'association':assc})

        self.session.commit()

        self.editEdu(id, deg, uni, coll, edu_year, dur)
        self.editWork(id, org, work_year)

    # Search Person
    def queryPerson(self, id=None, grd=None, name=None, sex=None, phn=None, qq=None, mail=None, home=None, assc=None):

        person = self.session.query(DBPerson)

        if not id == None:
            person = person.filter(DBPerson.id == id)
        if not grd == None:
            person = person.filter(DBPerson.graduation == grd)
        if not name == None:
            person = person.filter(DBPerson.name == name)
        if not sex == None:
            person = person.filter(DBPerson.sex == sex)
        if not phn == None:
            person = person.filter(DBPerson.phone == phn)
        if not qq == None:
            person = person.filter(DBPerson.qq == qq)
        if not mail == None:
            person = person.filter(DBPerson.mail == mail)
        if not home == None:
            person = person.filter(DBPerson.home == home)
        if not assc == None:
            person = person.filter(DBPerson.association == assc)

        return person

    ####################################################################################
    # DBEducation
    ####################################################################################

    # Add Education Information of Person
    def addEdu(self, id, deg, uni, coll, year, dur):

        edu = DBEducation(id, deg, uni, coll, year, dur)
        self.session.add(edu)
        self.session.commit()

    # Delete Education Information of Person
    def deleteEdu(self, id):

        self.session.query(DBEducation).filter(DBEducation.id == id).delete()
        self.session.commit()

    # Edit Education Information of Person
    def editEdu(self, id, deg=None, uni=None, coll=None, year=None, dur=None):

        edu = self.session.query(DBEducation).filter(DBEducation.id == id)

        if not deg == None:
            edu.update({'degree':deg})
        if not uni == None:
            edu.update({'university':uni})
        if not coll == None:
            edu.update({'college':coll})
        if not year == None:
            edu.update({'year':year})
        if not dur == None:
            edu.update({'duration':dur})

        self.session.commit()

    # Search Education Information of Person
    def queryEdu(self,id=None, deg=None, uni=None, coll=None, year=None, dur=None):

        edu = self.session.query(DBEducation)

        if not id == None:
            edu = edu.filter(DBEducation.id == id)
        if not deg == None:
            edu = edu.filter(DBEducation.degree == deg)
        if not uni == None:
            edu = edu.filter(DBEducation.university == uni)
        if not coll == None:
            edu = edu.filter(DBEducation.college == coll)
        if not year == None:
            edu = edu.filter(DBEducation.year == year)
        if not dur == None:
            edu = edu.filter(DBEducation.duration == dur)

        return edu

    ####################################################################################
    # DBWork
    ####################################################################################

    # Add Work Information of Person
    def addWork(self, id, org, year):

        work = DBWork(id, org, year)
        self.session.add(work)
        self.session.commit()

    # Delete Work Information of Person
    def deleteWork(self, id):

        self.session.query(DBWork).filter(DBWork.id == id).delete()
        self.session.commit()

    # Edit Work Information of Person
    def editWork(self, id, org=None, year=None):

        work = self.session.query(DBWork).filter(DBWork.id == id)

        if not org == None:
            work.update({'orgnization':org})
        if not year == None:
            work.update({'year':year})

        self.session.commit()

    # Search Work Information of Person
    def queryWork(self, id=None, org=None, year=year):

        work = self.session.query(DBWork)

        if not id == None:
            work = work.filter(DBWork.id == id)
        if not org == None:
            work = work.filter(DBWork.orgnization == org)
        if not year == None:
            work = work.filter(DBWork.year == year)

        return work

# Initialize
if __name__ == '__main__':

    my_db = DBEngine()