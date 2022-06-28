from flask import Flask, request, g
from utils import parseTodos, parse_arguments, loadHashBucket, hashItem
from mail import sendMail

app = Flask(__name__)


@app.route('/', methods=['POST'])
def getTodo():
    data = request.get_json()
    update_date = data['data']['updated_at'][:-17]
    todos = parseTodos(data['data']['body'])
    print(todos)
    global args
    global hashBucket
    for todo in todos:
        itemHash = hash(update_date + todo['date'] + todo['msg'])
        isHash, hashBucket = hashItem(hashBucket, itemHash, todo, update_date)
        if isHash:
            continue
        subject = "{} {}".format(todo['date'], todo['msg'])
        sendMail(fromAddr=args.fromAddr, toAddr=args.didaAddr, password=args.password,
                subject=subject, msg="", smtpServer=args.smtpServer, stmpPort=args.smtpPort)
    return ""

if __name__ == '__main__':
    args = parse_arguments()
    hashBucket = loadHashBucket()
    app.run(host="0.0.0.0", port=args.port)