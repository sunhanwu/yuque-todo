"""

"""

import re
from typing import List
import argparse
import json
import hashlib

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

def loadHashBucket():
    """

    :return:
    """
    with open('./hash.json', 'r', encoding='UTF-8') as f:
        hashBucket = json.load(f)
    return hashBucket

def saveHashBucket(hashBucket:dict):
    """

    :return:
    """
    with open('./hash.json', 'w') as fp:
        json.dump(hashBucket, fp)


def md5hash(s:str)->str:
    """

    :param s:
    :return:
    """
    md5 = hashlib.md5()
    md5.update(s.encode("utf8"))
    return md5.hexdigest()


