# -*- coding:utf-8 -*-
"""
项目：ARL-Finger-ADD-Pro
文件：FingerprintHub.py
功能描述：FingerprintHub指纹转换为ARL指纹
Author：BigYoung
Blog：https://sec.bigyoung.cn/article/ARL-Finger-ADD-Pro/
创建时间：2023/11/28
"""
import json

from loguru import logger

from .utils import write_to_yml


#
def transform_map(original_map):
    """
    将FingerprintHub_finger.json文件中的数据转换为tmp_finger.json文件中的数据
    :param original_map:
    :return:
    """
    rule = {}
    rule["name"] = original_map["name"]
    tmp_rule = ''
    if original_map["request_method"] == "get":
        # body 和 Title指纹
        if original_map["keyword"] and (not original_map["headers"]):
            for i in original_map["keyword"]:
                i = json.dumps(i)[1:-1]
                tmp_rule = tmp_rule + 'body="' + i + '" && '
            tmp_rule = tmp_rule.rstrip(' && "')
        # header 指纹
        if original_map["headers"]:
            for k, v in original_map["headers"].items():
                k = json.dumps(k)[1:-1]
                v = json.dumps(v)[1:-1]
                tmp_rule = tmp_rule + 'header="' + k + '" && '
                if v != "*":
                    tmp_rule = tmp_rule + 'header="' + v + '" && '
            tmp_rule = tmp_rule.rstrip(' && "')
        # icon_hash指纹
        if original_map["favicon_hash"]:
            for i in original_map["favicon_hash"]:
                tmp_rule = tmp_rule + 'icon_hash="' + i + '" || '
            tmp_rule = tmp_rule.rstrip(' || "')  # 去掉最后一个" || "
        # if "\\u" in tmp_rule:
        tmp_rule = (tmp_rule + '"').encode('utf-8').decode('unicode_escape')
        rule["rule"] = tmp_rule
    return rule


def FingerpringHub_import(file, arl):
    """
    FingerprintHub指纹转换，并导入ARL指纹
    :param file:
    :param arl:
    :return:
    """
    with open(f"{file}", "r", encoding="utf-8") as f:
        original_finger_map = json.loads(f.read())
        tmp_list = []
        for original_map in original_finger_map:
            rule = transform_map(original_map)
            if rule and ("rule" in rule.keys()):
                tmp_list.append(rule)

        res, file = write_to_yml(tmp_list)
        if res:
            logger.info("[+] ARL Finger Json File Create Success!!")
            arl.upload_Finger(f"{file}")
            logger.info("[+] ARL Finger Json File Upload Success!!")
        else:
            logger.error("[-] ARL Finger Json File Create Failed!!")


if __name__ == '__main__':
    FingerpringHub_import()
