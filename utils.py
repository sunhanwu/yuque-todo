"""

"""

import re
from typing import List
import argparse

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