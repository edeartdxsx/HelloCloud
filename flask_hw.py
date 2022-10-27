from flask import Flask,render_template,request  
from flask_sqlalchemy import SQLAlchemy 
from main_pro import Table_Students ,Table_Registration,Table_Subjects,Table_Teacher, session
app =  Flask(__name__)

@app.route('/')
def index():
    ex = session.query(Table_Students.student_id,Table_Students.f_name,Table_Students.l_name,Table_Students.e_mail,Table_Registration.subject_id,Table_Subjects.subject_name,Table_Registration.grade,
    Table_Teacher.tf_name,Table_Teacher.tl_name)\
        .join(Table_Registration,Table_Students.student_id == Table_Registration.student_id).join(Table_Subjects,Table_Registration.subject_id == Table_Subjects.subject_id)\
        .join(Table_Teacher,Table_Subjects.teacher_id == Table_Teacher.teacher_id)
    return render_template('index_x.html',TEST = ex) 
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)