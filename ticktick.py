import requests
import json
def login(username, password):
    """
    登录滴答web端，获取cookie
    """
    url = "https://api.dida365.com/api/v2/user/signon?wc=true&remember=true"
    postData = {
            "username": username,
            "password": password
            }
    header = {
            "Content-Type": "application/json",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "Origin": "https://api.dida365.com"
            }
    postData = json.dumps(postData)
    response = requests.post(url, data=postData, headers=header)
    if response.status_code != 200:
        # todo: 添加wechatbot告警
        print("login error!")
    data = json.loads(response.text)
    return data["token"]

def check(token):
    """
    check还有哪些清单未做
    """
    url = "https://api.dida365.com//api/v2/batch/check/0"
    header = {
            "Content-Type": "application/json",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "Origin": "https://api.dida365.com"
            }
    cookie = {"t": token}
    response = requests.get(url, cookies=cookie, headers=header)
    if response.status_code != 200:
        print("check error!")
    todoList = json.loads(response.text)
    todoList = todoList["syncTaskBean"]["update"]
    return todoList








if __name__ == "__main__":
    pass
