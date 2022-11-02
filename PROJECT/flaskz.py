from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2
app = Flask(__name__)
@app.route('/')
def index():
    connection = psycopg2.connect(user='webadmin',
                                    password='OVNase26154',
                                    host='node36512-kongphop.proen.app.ruk-com.cloud',
                                    port='5432',
                                    database='project')
    cursor1 = connection.cursor() 


    select1 = 'select * from oilprice '
    
    
    cursor1.execute(select1)  

    data1 = cursor1.fetchall()  
    connection.commit()
    
    return render_template('main.html',data = data1)

if __name__  == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)