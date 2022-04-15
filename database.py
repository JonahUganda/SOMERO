from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

class datacon:

    def __init__(self):
        self.database_setput()

    def database_setput(self):

        self.engine = create_engine('sqlite:///college.db', echo=True)
        self.meta = MetaData()

        self.students = Table(
            'Student_details', self.meta,
            Column('id', Integer, primary_key=True),
            Column('Sirname', String),
            Column('secondname', String),
            Column('othernames', String),
            Column('date_of_birth', String),
            Column('gender', String),
            Column('level', String),
            Column('residance', String),
            Column('nationality', String),
            Column('former_school', String),
            Column('mothers_name', String),
            Column('mothers_contact', String),


        )
        self.id_range = Table(
            'id_range', self.meta,
            Column('id', Integer, primary_key=True),
            Column('Start', Integer),
            Column('Stop', Integer),
        )
        self.Fees_paid = Table(
            'Fees_paid', self.meta,
            Column('id', Integer, primary_key=True),
            Column('Student_ID',String),
            Column('Firstname', String),
            Column('lastname', String),
            Column('gender', String),
            Column('level', String),
            Column('amount_paid', String),
            Column('received by', String),
            Column('Term', String),
            Column('date', String),
        )



        self.meta.create_all(self.engine)
        #print(f"the table has the following columns {self.students.columns.keys()}")
        return self.students

    def reg_new_pupil(self,a,b,c,d,e,f,g,h,i,j,k):
        self.a1=a
        self.b1=b
        self.c1=c
        self.d1=d
        self.e1=e
        self.f1=f
        self.g1=g
        self.h1=h
        self.i1 = i
        self.j1 = j
        self.k1 = k

        self.ins = self.students.insert()
        self.ins = self.students.insert().values(

            Sirname=self.a1,
            secondname=self.b1,
            othernames=self.c1,
            date_of_birth=self.d1,
            gender=self.e1,
            level=self.f1,
            residance=self.g1,
            nationality=self.h1,
            former_school=self.i1,
            mothers_name=self.j1,
            mothers_contact=self.k1
        )
        self.conn = self.engine.connect()
        self.result = self.conn.execute(self.ins)

    def view_stable_d(self):
        self.s =  self.students.select()
        self.conn = self.engine.connect()

        self.Session=sessionmaker(bind=self.engine)
        self.session= self.Session()
        self.result = self.session.query(self.students).all()
        print(self.result[2])

        return self.result
        #
        # for row in self.result:
        #     print(f'{row.Sirname}   {row.secondname}    ')
