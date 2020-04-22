import sqlite3
from flask import Flask, render_template
from typing import Dict, List

db_file = "D:/MS/Stevens Institute of Technology/SSW810/Assignment12/HW12.sql"

app: Flask = Flask(__name__)

@app.route('/')
def students_summary() -> str:
    """ Returns all the rows after running the query """
    db: sqlite3.Connection = sqlite3.connect(db_file)
    query: str = """ select s.Name, s.CWID, g.Course, g.Grade, i.Name
                        from students s, grades g, instructors i
                        where s.CWID = g.StudentCWID and g.InstructorCWID = i.CWID
                        order by s.Name; """
    data: List[Dict[str, str]] = [{'name': name, 'CWID': CWID, 'course': course, 'grade': grade, 'instructor': instructor} for name, CWID, course, grade, instructor in db.execute(query)]
    
    db.close()

    return render_template('base.html', students = data)

app.run(debug=True)