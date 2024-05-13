# -*- coding:utf-8 -*-
"""
项目：ARL-Finger-ADD-Pro
文件：utils.py
功能描述：
Author：BigYoung
Blog：https://sec.bigyoung.cn/article/ARL-Finger-ADD-Pro/
创建时间：2023/11/28
"""
import optparse
import os
import sys

from loguru import logger

TMP_LIST = []

import yaml


def write_to_yml(data):
    """
    :param data: [{},{}]
    :param file_path:
    :return:
    """
    file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/all_fingers/tmp_arl_finger.yml"
    # 写入到YAML文件
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            # with open('data.yml', 'w') as file:
            yaml.dump(data, file, allow_unicode=True)
        return 1, file_path
    except Exception as e:
        logger.error(f"ARL Finger YML File 创建失败，报错信息：{e}")
        return 0, file_path


class CommandLines():

    def cmd(self):
        parse = optparse.OptionParser()
        parse.add_option('-u', '--url', dest='url', help='Please Enter the ARL Site Url')
        parse.add_option('-a', '--auth', dest='auth', help='Please Enter Your ARL username password')
        parse.add_option('-f', '--finger', dest='finger', default="all",
                         help='Please Enter You Want import Finger, eg:1：Ehole3.1_finger.json  2：Finger_finger.json 3：FingerprintHub_finger.json all: 导入工具支持的所有指纹')
        parse.add_option('-t', '--token', dest='token', help='Please Enter Your ARL Auth Token')
        parse.add_option('-d', '--delete_f', dest='delete_f', default=False,
                         help='此参数用于删除ARL中已有的指纹，请谨慎使用此参数。删除前默认备份指纹到当前目录下的ARL_API_finger.yml文件')
        (options, args) = parse.parse_args()
        if options.url == None or (options.token == None and options.auth == None):
            parse.print_help()
            print("""
使用示例：

ARL API Key 用法：
python3 ARL_Finger_Add_Plus.py -u http://192.168.1.1:8888 -t 1234567890abcdefg -f all

ARL 用户名密码 用法：
python3 ARL_Finger_Add_Plus.py -u http://192.168.1.1:8888 -a admin:arlpass -f all
            """)
            sys.exit(0)
        return options
