####################################################################################
## Copyright (c) 2017 CSR
## Apache-2.0 License
## Author: TinBacon from BUPT
## Initialize on 6 Feb 2017
## Update on
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
    def addPerson(self, id, grd, name, sex, phn, qq, mail, home, assc, deg, uni, coll, edu_year, dur, org=null, work_year=null):

        person = DBPerson(id, grd, name, sex, phn, qq, mail, home, assc)
        self.session.add(person)
        self.session.commit()

        self.addEdu(id, deg, uni, coll, edu_year, dur)

        if not org == null:
            self.addWork(id, org, work_year)

    # Delete Person
    def deletePerson(self, id):

        self.session.query(DBPerson).filter(DBPerson.id == id).delete()
        self.session.commit()

        self.deleteEdu(id)
        self.deleteWork(id)

    # Edit Person
    def editPerson(self, id, grd=null, name=null, sex=null, phn=null, qq=null, mail=null, home=null, assc=null,
                   deg=null, uni=null, coll=null, edu_year=null, dur=null, org=null, work_year=null):

        person = self.session.query(DBPerson).filter(DBPerson.id == id)

        if not grd == null:
            person.update({'graduation':grd})
        if not name == null:
            person.update({'name':name})
        if not sex == null:
            person.update({'sex':sex})
        if not phn == null:
            person.update({'phone':phn})
        if not qq == null:
            person.update({'qq':qq})
        if not mail == null:
            person.update({'mail':mail})
        if not home == null:
            person.update({'home':home})
        if not assc == null:
            person.update({'association':assc})

        self.session.commit()

        self.editEdu(id, deg, uni, coll, edu_year, dur)
        self.editWork(id, org, work_year)

    # Search Person
    def queryPerson(self, id=null, grd=null, name=null, sex=null, phn=null, qq=null, mail=null, home=null, assc=null):

        person = self.session.query(DBPerson)

        if not id == null:
            person = person.filter(DBPerson.id == id)
        if not grd == null:
            person = person.filter(DBPerson.graduation == grd)
        if not name == null:
            person = person.filter(DBPerson.name == name)
        if not sex == null:
            person = person.filter(DBPerson.sex == sex)
        if not phn == null:
            person = person.filter(DBPerson.phone == phn)
        if not qq == null:
            person = person.filter(DBPerson.qq == qq)
        if not mail == null:
            person = person.filter(DBPerson.mail == mail)
        if not home == null:
            person = person.filter(DBPerson.home == home)
        if not assc == null:
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
    def editEdu(self, id, deg=null, uni=null, coll=null, year=null, dur=null):

        edu = self.session.query(DBEducation).filter(DBEducation.id == id)

        if not deg == null:
            edu.update({'degree':deg})
        if not uni == null:
            edu.update({'university':uni})
        if not coll == null:
            edu.update({'college':coll})
        if not year == null:
            edu.update({'year':year})
        if not dur == null:
            edu.update({'duration':dur})

        self.session.commit()

    # Search Education Information of Person
    def queryEdu(self,id=null, deg=null, uni=null, coll=null, year=null, dur=null):

        edu = self.session.query(DBEducation)

        if not id == null:
            edu = edu.filter(DBEducation.id == id)
        if not deg == null:
            edu = edu.filter(DBEducation.degree == deg)
        if not uni == null:
            edu = edu.filter(DBEducation.university == uni)
        if not coll == null:
            edu = edu.filter(DBEducation.college == coll)
        if not year == null:
            edu = edu.filter(DBEducation.year == year)
        if not dur == null:
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
    def editWork(self, id, org=null, year=null):

        work = self.session.query(DBWork).filter(DBWork.id == id)

        if not org == null:
            work.update({'orgnization':org})
        if not year == null:
            work.update({'year':year})

        self.session.commit()

    # Search Work Information of Person
    def queryWork(self, id=null, org=null, year=year):

        work = self.session.query(DBWork)

        if not id == null:
            work = work.filter(DBWork.id == id)
        if not org == null:
            work = work.filter(DBWork.orgnization == org)
        if not year == null:
            work = work.filter(DBWork.year == year)

        return work

# Initialize
if __name__ == '__main__':

    my_db = DBEngine()