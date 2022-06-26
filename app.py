from flask import Flask, request
from utils import parseTodos, parse_arguments
from mail import sendMail


app = Flask(__name__)
@app.route('/', methods=['POST'])
def getTodo():
    data = request.get_json()
    todos = parseTodos(data['data']['body'])
    print(todos)
    global args
    for todo in todos:
        subject = "{} {}".format(todo['date'], todo['msg'])
        sendMail(fromAddr=args.fromAddr, toAddr=args.didaAddr, password=args.password,
                subject=subject, msg="", smtpServer=args.smtpServer, stmpPort=args.smtpPort)
    return "hello world"

if __name__ == '__main__':
    args = parse_arguments()
    app.run(host="0.0.0.0", port=args.port)