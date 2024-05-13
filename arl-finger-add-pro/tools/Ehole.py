# -*- coding:utf-8 -*-
"""
项目：ARL-Finger-ADD-Pro
文件：Ehole.py
功能描述：Ehole3.1指纹转换为ARL指纹
Author：BigYoung
Blog：https://sec.bigyoung.cn/article/ARL-Finger-ADD-Pro/
创建时间：2023/11/28
"""
import json

from loguru import logger

from tools.utils import write_to_yml


def Ehole_or_Finger_import(file, arl):
    """
    Ehole3.1 or Finger指纹转换，并导入ARL指纹
    :param file:
    :param arl:
    :return:
    """
    f = open(f"{file}", 'r', encoding="utf-8")
    content = f.read()
    load_dict = json.loads(content)
    TMP_LIST = []
    for i in load_dict['fingerprint']:
        finger_json = json.loads(json.dumps(i))
        if len(finger_json['keyword']) != 0:  # rules 不为空再添加
            tmp_dict = {"name": finger_json['cms']}
            tmp_rule = ""
            location = finger_json['location']
            # body 规则
            if finger_json['method'] == "keyword" and location == "body":
                for rule in finger_json['keyword']:
                    tmp_rule = tmp_rule + f'body="{rule}"' + " && "
                tmp_rule = tmp_rule.strip(" && ")  # 去掉最后一个&&
            # title 规则
            elif finger_json['method'] == "keyword" and location == "title":
                for rule in finger_json['keyword']:
                    tmp_rule = tmp_rule + f'title="{rule}"' + " && "
                tmp_rule = tmp_rule.strip(" && ")  # 去掉最后一个&&
            # header 规则
            elif finger_json['method'] == "keyword" and location == "header":
                for rule in finger_json['keyword']:
                    tmp_rule = tmp_rule + f'header="{rule}"' + " && "
                tmp_rule = tmp_rule.strip(" && ")  # 去掉最后一个&&
            # faviconhash 规则
            elif finger_json['method'] == "faviconhash" and location == "body":
                for rule in finger_json['keyword']:
                    tmp_rule = tmp_rule + f'icon_hash="{rule}"' + " && "
                    tmp_rule = tmp_rule.strip(" && ")  # 去掉最后一个&&
            tmp_dict['rule'] = tmp_rule
            TMP_LIST.append(tmp_dict)
    res, file = write_to_yml(TMP_LIST)
    if res:
        arl.upload_Finger(f"{file}")
        logger.info("[+] ARL Finger Json File Upload Success!!")
    else:
        logger.error("[-] ARL Finger Json File Create Failed!!")


# 构造ARL支持的json结构


if __name__ == '__main__':
    pass
