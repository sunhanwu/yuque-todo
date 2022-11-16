from flask import Flask, request, g
from utils import parseTodos, parse_arguments, loadHashBucket, hashItem, md5hash, sendWechatMessage
from mail import sendMail
from time import sleep
from ticktick import check, login
from datetime import datetime, timezone, timedelta
from schedule import s

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
        itemHash = md5hash(update_date + todo['date'] + todo['msg'])
        isHash, hashBucket = hashItem(hashBucket, itemHash, todo, update_date)
        if isHash:
            continue
        subject = "{} {}".format(todo['date'], todo['msg'])
        sendMail(fromAddr=args.fromAddr, toAddr=args.didaAddr, password=args.password,
                 subject=subject, msg="", smtpServer=args.smtpServer, stmpPort=args.smtpPort)
    sleep(30)
    token = login(args.didaUsername, args.didaPassword)
    didaList = check(token)
    for todo in todos:
        for item in didaList:
            if todo['msg'] in item[0]:
                utc_time = datetime.strptime(item[1][:-9], '%Y-%m-%dT%H:%M:%S')
                cst_time = utc_time.astimezone(timezone(timedelta(hours=-8))).strftime("%Y-%m-%d %H:%M:%S")
                s.addTask(sendWechatMessage, time=cst_time, args=["hello world"])
                print("{}:{}".format(cst_time, item[0]))

    return ""

if __name__ == '__main__':
    args = parse_arguments()
    hashBucket = loadHashBucket()
    app.run(host="0.0.0.0", port=args.port, debug=False)
