import re
from typing import List
import argparse
import json
import hashlib
import logging

def parse_arguments():
    """

    :param argv:
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', required=False, default="5000", type=int, help="webhook port")
    parser.add_argument('--fromAddr', required=True, type=str, help="mail address")
    parser.add_argument('--password', required=True, type=str, help="authorization code")
    parser.add_argument('--didaAddr', required=True, type=str, help="dida address")
    parser.add_argument('--smtpServer', required=False, type=str, default="smtp.qq.com", help="smtp server host")
    parser.add_argument('--smtpPort', required=False, type=int, default=465, help="smtp server port")
    parser.add_argument('--didaUsername', required=False, type=str, help="dida username")
    parser.add_argument('--didaPassword', required=False, type=str, help="dida password")
    return parser.parse_args()


def parseTodos(body:str) -> List[dict]:
    """
    parse all todo items from yuque body
    :param body: str
    :return: list
    """
    items = re.findall(r'-\s{1}\[\s{1}\]\s{1}(.*)[:：](.*)滴答', body)
    result = []
    for item in items:
        tmp = {"msg": item[1],
               "date": item[0]}
        result.append(tmp)
    return result

def hashItem(hashBucket:dict, hash:str, todo:dict, date: str):
    """

    :param date:
    :param item:
    :return:
    """
    if hash in hashBucket.keys():
        return True, hashBucket
    else:
        hashBucket[hash] = (date, todo)
        saveHashBucket(hashBucket)
        return False, hashBucket

def loadHashBucket() -> dict:
    """
    load hash bucket dict from hash.json
    :return: hash bucket dict
    """
    with open('./hash.json', 'r', encoding='UTF-8') as f:
        hashBucket = json.load(f)
    if hashBucket:
        return hashBucket
    else:
        return {}

def saveHashBucket(hashBucket:dict):
    """
    save hash bucket into hash.json file
    :return: None
    """
    with open('./hash.json', 'w') as fp:
        json.dump(hashBucket, fp)


def md5hash(s:str)->str:
    """
    string to md5 digest
    :param s: string
    :return: md5 digest
    """
    md5 = hashlib.md5()
    md5.update(s.encode("utf8"))
    return md5.hexdigest()

def sendWechatMessage(message):
    print("Wechat Alert {}".format(message))

