import MySQLdb

#ip(domain), userid, password, database
db = MySQLdb.connect('localhost', 'root', '12345', 'test', charset='utf8')
cur = db.cursor(MySQLdb.cursors.DictCursor)

# insert
cur.execute("insert into student values ({0}, '{1}', '{2}')"
        .format(3, 'FullName', '1997-12-08'))
db.commit() #commint!!

# select
cur.execute('SELECT * FROM student')

while True:
    student = cur.fetchone() #커서를 한줄 씩 읽는 것
    if not student: break

    print(student)

cur.close()
db.close()