from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer, String, Text, DateTime, Float, Boolean, PickleType , CHAR, VARCHAR

Base = declarative_base()
db_uri = 'sqlite:///Homework.sqlite3'
engine = create_engine(db_uri, echo=False)

class Table_Students(Base):
    __tablename__ = 'Students' 
    student_id = Column(String(13),primary_key = True,nullable = True) 
    f_name = Column(String(30),nullable = False) 
    l_name = Column(String(30),nullable=False) 
    e_mail = Column(String(50), nullable=False) 

    def __repr__(self):
        return '<User(student_id = {}, f_name = {}, l_name = {}, e_mail ={})>'.format(self.student_id, self.f_name, self.l_name, self.e_mail)
        

class Table_Registration(Base):
    __tablename__ = 'Registration' 
    id = Column(Integer(), primary_key = True)
    student_id = Column(String(13)) 
    subject_id = Column(String(15),nullable = False) 
    year = Column(String(4),nullable=False) 
    semester = Column(String(1),nullable=False)  
    grade = Column(String(2))

    def __repr__(self):
        return '<User(student_id = {}, subject_id = {}, year = {}, semester ={}, grade={})>'.format(self.student_id, \
            self.subject_id, self.year , self.semester, self.grade)

class Table_Subjects(Base):
    __tablename__ = 'Subjects' 
    subject_id = Column(String(15),primary_key = True) 
    subject_name = Column(String(50),nullable = False) 
    credit = Column(Integer(),nullable=False) 
    teacher_id = Column(String(3),nullable=False) 
    def __repr__(self):
        return '<User(subject_id = {}, subject_name = {}, credit = {}, teacher_id ={})>'.format(self.subject_id, \
            self.subject_name, self.credit , self.teacher_id)

class Table_Teacher(Base):
    __tablename__ = 'Teachers' 
    teacher_id = Column(String(3),primary_key=True, nullable=True)
    f_name = Column(String(50), nullable=True)
    l_name = Column(String(30), nullable=True)
    e_mail = Column(String(50), nullable=True)

    def __repr__(self):
            return '<User(teacher_id = {} , f_name= {} , l_name = {} , e_mail = {})>'.format(self.teacher_id,\
                    self.f_name, self.l_name , self.e_mail)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

first_p = Table_Students(
    student_id ='6406022610015',
    f_name='Kongphop',
    l_name='Sri-on',
    e_mail ='6406022610015@fitm.kmutnb.ac.th')

second_p = Table_Students(
    student_id ='6406022620029',
    f_name='Thanet',
    l_name='Suwannapirom',
    e_mail ='6406022620029@fitm.kmutnb.ac.th')

third_p = Table_Students(
    student_id ='6406022610023',
    f_name='Nititat',
    l_name='Bangpra',
    e_mail ='6406022610023@email.kmutnb.ac.th')

r1 = Table_Registration(
    student_id ='6406022610015',
    subject_id='060233113',
    year='2565',
    semester ='1',
    grade = 'A')

r2 = Table_Registration(
    student_id ='6406022610015',
    subject_id='060233201',
    year='2565',
    semester ='1',
    grade = 'A') 
regis_a = Table_Registration(
    student_id ='6406022610015',
    subject_id='060233112',
    year='2565',
    semester ='1',
    grade = 'A')

r3 = Table_Registration(
    student_id ='6406022620029',
    subject_id='060233113',
    year='2565',
    semester ='1',
    grade = 'B+')

r4 = Table_Registration(
    student_id ='6406022620029',
    subject_id='060233201',
    year='2565',
    semester ='1',
    grade = 'B+')  

regis_b = Table_Registration(
    student_id ='6406022620029',
    subject_id='060233112',
    year='2565',
    semester ='1',
    grade = 'B+' )

r5 = Table_Registration(
    student_id ='6406022610023',
    subject_id='060233113',
    year='2565',
    semester ='1',
    grade = 'C')

r6 = Table_Registration(
    student_id ='6406022610023',
    subject_id='060233201',
    year='2565',
    semester ='1',
    grade = 'C') 

regis_c = Table_Registration(
    student_id ='6406022610023',
    subject_id='060233112',
    year='2565',
    semester ='1',
    grade = 'C')

s1 = Table_Subjects(subject_id ='060233113',subject_name='ADVANCED COMPUTER PROGRAMMIN',credit='3',teacher_id ='AMK')
s2 = Table_Subjects(subject_id ='060233201',subject_name='NETWORK ENGINEERING LABORATO',credit='1',teacher_id ='WKN')
s3 = Table_Subjects(subject_id ='060233112',subject_name='DATA ENGINEERING',credit='3',teacher_id ='STS')

T1 = Table_Teacher(teacher_id='AMK',f_name='Anirach',l_name='Mingkhwan',e_mail='Anirach@gmail.com')
T2 = Table_Teacher(teacher_id='WKN',f_name='Watcharachai',l_name='Kongsiriwattana',e_mail='Watcharachai@gmail.com')
T3 = Table_Teacher(teacher_id='STS',f_name='Sarayoot',l_name='Tanessakulwattana',e_mail='Sarayoot@gmail.com') 

session.add_all([first_p,second_p,third_p,r1,r2,regis_a,r3, r4,regis_b,r5, r6,regis_c,s1 ,s2,s3,T1,T2,T3])
session.commit()