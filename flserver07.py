from flask import Flask, render_template, request
import MySQLdb as mysql

# Flask 객체 인스턴스 생성
app = Flask(__name__)

db = mysql.connect('localhost', 'root', '12345', 'test', charset='utf8')
cur = db.cursor(mysql.cursors.DictCursor)

@app.route('/')  # 접속하는 최초 url
def index():
    cur.execute('SELECT * FROM student')
    result = []
    while True:
        student = cur.fetchone() #커서를 한줄 씩 읽는 것
        if not student: break
        result.append(student)
        #print(student)
    cur.close()
    db.close()
    # 백엔드에서 데이터를 프론트엔드로 전달
    return render_template('mysqldata.html', row=result)  # post
    # return render_template('index.html') # get

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)    # 디버깅하기 위해 debug값 추가