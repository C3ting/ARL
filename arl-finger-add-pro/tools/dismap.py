# -*- coding:utf-8 -*-
"""
项目：ARL-Finger-ADD-Pro
文件：dismap.py
功能描述: 获取dismap项目里的web指纹导入到ARL系统。dismap：https://github.com/zhzyker/dismap
Author：BigYoung
Blog：https://sec.bigyoung.cn/article/ARL-Finger-ADD-Pro/
创建时间：2023/12/17
"""
import json

from tools.utils import write_to_yml


# 读取all_fingers/dismap_rule.go文件内容
def get_dismap_finger():
    with open('all_fingers/dismap_rule.go', 'r', encoding='utf-8') as f:
        data = f.read()
    json_list = []
    # 逐行读取../all_fingers/dismap_rule.go文件内容
    for line in data.split('\n'):
        tmp_finger = {
            "rule": {
                "html": [
                    ""
                ],
                "title": [],
                "headers": [],
                "favicon_hash": []
            },
            "name": ""
        }
        # 判断是否为注释行
        if line.startswith('//') or not line.strip():
            continue
        # rule0：第一段
        rule0, tmp = line.split(", InStr{", 1)
        # rule1：第二段  req_method：第三段
        rule1, req_method = tmp.split('}, ReqHttp{', 1)

        if "POST" in req_method:  # ARL暂不支持POST请求
            continue
        # tmp_rule0：第一段拆分
        tmp_rule0 = rule0.split(',')
        # tmp_rule0：
        name = tmp_rule0[1].strip('"').strip(" ").strip('"').strip(" ")
        content_type = tmp_rule0[2]  # 指纹特征所在位置，body、header
        tmp_rule1 = rule1.split(',')
        tmp_rule = ''
        if "body" in content_type:
            body = tmp_rule1[0].strip('""()').replace("\\", "").split("|")
            tmp_finger["rule"]["html"] = body
            for i in body:
                tmp_rule = tmp_rule + 'body=' + json.dumps(i) + ' && '
            tmp_rule = tmp_rule.rstrip(' && ')
        elif "header" in content_type:
            header = tmp_rule1[1].strip('""()" ').replace('(', "").replace("\\", "").split("|")
            # tmp_finger["rule"]["headers"] = header
            for i in header:
                tmp_rule = tmp_rule + 'header=' + json.dumps(i) + ' && '
            tmp_rule = tmp_rule.rstrip(' && ')
        elif "ico" in content_type:  # ARL的icon哈希，不知道则怎么计算的，没研究，有空再说，先注释掉了
            ico = tmp_rule1[2].strip('""()').replace('(', "").strip('" ').split("|")
            # tmp_finger["rule"]["icon_hash"] = ico
            for i in ico:
                tmp_rule = tmp_rule + 'icon_hash=' + json.dumps(i) + ' || '
            tmp_rule = tmp_rule.rstrip(' || ')
        if "\\u" in tmp_rule:
            tmp_rule = tmp_rule.encode('gbk').decode('unicode_escape')
        tmp_finger["rule"] = tmp_rule
        tmp_finger["name"] = name

        json_list.append(tmp_finger)
    return json_list


def dismap_import(arl):
    from loguru import logger
    res, file = write_to_yml(get_dismap_finger())
    if res:
        logger.info("[+] ARL Finger Json File Create Success!!")
        arl.upload_Finger(f"{file}")
        logger.info("[+] ARL Finger Json File Upload Success!!")
    else:
        logger.error("[-] ARL Finger Json File Create Failed!!")


if __name__ == '__main__':
    get_dismap_finger()
