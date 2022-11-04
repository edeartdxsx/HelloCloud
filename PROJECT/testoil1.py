import requests
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType,CHAR,VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from bs4 import BeautifulSoup
import time
engine = create_engine('postgresql://webadmin:OVNase26154@node36512-kongphop.proen.app.ruk-com.cloud:5432/project')
Base = declarative_base()



url = 'http://gasprice.kapook.com/gasprice.php#top'
req = requests.get(url)
req.encoding = 'utf-8'
soup = BeautifulSoup(req.text,'lxml')



league_table = soup.find('article', class_="gasprice ptt").find_all('em')
oil = []

print(league_table)
for i in league_table:
    oil.append(i.string)
#print(oil[0])

class Oil_T(Base):
    __tablename__ = "oilprice"
    id = Column(Integer,primary_key = True)  
    datex = Column(String)
    gname = Column(String) 
    gprice = Column(String,nullable=False)
  
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# gname1 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="GASOHOL 95", gprice = oil[0]) 
# gname2 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="GASOHOL E20",gprice = oil[1]) 
# gname3 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="GASOHOL E85",gprice = oil[2]) 
# gname4 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="GASOHOL 91",gprice = oil[3]) 
# gname5 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="BENZINE 95",gprice = oil[4]) 
# gname6 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="DIESEL B7",gprice = oil[5]) 
# gname7 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="DIESEL PREMIUM",gprice = oil[6]) 
# gname8 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="DIESEL B20",gprice = oil[7]) 
# gname9 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="DIESEL",gprice = oil[8]) 
# gname10 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="SUPERPOWER GASOHOL 95",gprice = oil[9]) 
# gname11 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="GASOHOL 95 PREMIUM",gprice = oil[10]) 

# session.add_all([gname1,gname2,gname3,gname4,gname5,gname6,gname7,gname8,gname9,gname10,gname11])
# session.commit()

while True:
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    gname1 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="GASOHOL 95", gprice = oil[0]) 
    gname2 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="GASOHOL E20",gprice = oil[1]) 
    gname3 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="GASOHOL E85",gprice = oil[2]) 
    gname4 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="GASOHOL 91",gprice = oil[3]) 
    gname5 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="BENZINE 95",gprice = oil[4]) 
    gname6 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="DIESEL B7",gprice = oil[5]) 
    gname7 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="DIESEL PREMIUM",gprice = oil[6]) 
    gname8 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="DIESEL B20",gprice = oil[7]) 
    gname9 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="DIESEL",gprice = oil[8]) 
    gname10 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="SUPERPOWER GASOHOL 95",gprice = oil[9]) 
    gname11 = Oil_T(datex=soup.find('h2',{'class':'sub-title'}).text,gname="GASOHOL 95 PREMIUM",gprice = oil[10]) 

    
    session.add_all([gname1,gname2,gname3,gname4,gname5,gname6,gname7,gname8,gname9,gname10,gname11])
    session.commit()
    print("successfully")
    time.sleep(86000)

