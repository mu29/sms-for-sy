#-*- coding: utf-8 -*-

from flask import *
from flask.ext.sqlalchemy import SQLAlchemy
import requests
import os
from models import *

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        gender = request.form['gender'].encode('utf-8')
        school = request.form['school'].encode('utf-8')
        subject = request.form['subject'].encode('utf-8')
        limit = int(request.form['limit'])
        content = request.form['content'].encode('utf-8')

        teachers = db.session.query(Teacher).\
                    filter(Teacher.school.like('%' + school + '%')).\
                    filter(Teacher.subject.like('%' + subject + '%')).\
                    order_by("id desc").\
                    limit(limit)

        for teacher in teachers:
            print teacher.name
            print teacher.phone
            send_message(teacher, content)

        return render_template('index.html', message = u'총 {0}명의 선생님에게 전송하였습니다!'.format(teachers.count()))
    else:
        return render_template('index.html')


def send_message(teacher, message):
    try:
        response = requests.post(
            url = os.environ['MESSAGE_SERVER_URL'],
            headers = {
                'x-waple-authorization': os.environ['MESSAGE_API_KEY'],
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            },
            data = {
                'subject': '안녕하세요!',
                'msg_body': message,
                'send_phone': os.environ['PHONE'],
                'dest_phone': teacher.phone,
            },
        )
        if response.status_code == 200:
            print u'{0} 선생님에게 메시지 전송'.format(teacher.name)
        else:
            print ('Error ' + response.status_code)
    except requests.exceptions.RequestException:
        print(u'메시지 전송 실패')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
