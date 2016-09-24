import sqlite3

conn = sqlite3.connect('the sql connection goes here')
cur = conn.cursor()

cur.execute('CREATE TABLE STUDENT(cwid int, age int, major text(255))')
cur.execute('CREATE TABLE DEPARTMENT (name TEXT(255), chair TEXT(255))')
cur.execute('INSERT INTO STUDENT(20096020, 24, \'Cybersecurity\')')

cur.execute('SELECT st.cwid, dp.chair FROM student st, department dp, faculty fc, class cl WHERE st.cwid = cl.stud AND cl.fac = fc.name AND fc.dept = dp.name')
cur.execute('SELECT st.cwid FROM student st, department dp, faculty fc, class cl WHERE st.cwid = cl.stud AND cl.fac = fc.name AND fc.dept = dp.name AND fc.name = \'CS\'')

conn.close()