#!/usr/bin/ python
# -*- coding:utf-8 -*-
"""
项目：ARL-Finger-ADD-Pro
文件：ARL_API.py
功能描述：ARL相关API功能实现
Author: BigYoung
Blog: https://sec.bigyoung.cn/article/ARL-Finger-ADD-Pro/
创建时间: 2023-11-22 19:52:49
"""
import json
import sys
import traceback

import requests
from loguru import logger

requests.packages.urllib3.disable_warnings()


class ARL_API():
    """
    ARL API功能集合
    """

    def __init__(self, options=None):
        self.url = options.url
        if self.url.endswith("/"):
            self.url = self.url[:-1]
        if self.url.startswith("http://"):
            self.url = self.url.replace("http://", "https://")
        if options.auth:
            self.username = options.auth.split(":")[0]
            self.password = options.auth.split(":")[1]
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
            "Connection": "close",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Content-Type": "application/json; charset=UTF-8"
        }
        self.token = self.login(options)

    def add_Finger(self, name, rule):
        url = "{}/api/fingerprint/".format(self.url)
        data = {"name": name, "human_rule": rule}
        data_json = json.dumps(data)

        try:
            response = requests.post(url, data=data_json, headers=self.headers, verify=False)
            if response.status_code == 200:
                print(''' Add: [\033[32;1m+\033[0m]  {}\n Rsp: [\033[32;1m+\033[0m] {}'''.format(data_json,
                                                                                                 response.text))
        except Exception as e:
            traceback.print_exc()
            print(e)

    def upload_Finger(self, json_file):
        try:
            url = "{}/api/fingerprint/upload/".format(self.url)
            data = {}
            headers = {
                "Accept": "application/json",
                "Token": "{}".format(self.headers["Token"]),
            }
            files = {'file': open(f'{json_file}', 'rb')}
            response = requests.post(url, data=data, headers=headers, files=files, verify=False)
            if response.status_code == 200 and response.json()['code'] == 200:
                logger.info(
                    f"Json文件: {json_file} 上传成功！\n 返回信息: {response.text}")
            else:
                logger.error(f"Json文件：{json_file}，上传失败！失败原因：{response.text}")
        except Exception as e:
            traceback.print_exc()
            logger.error(f"ARL Finger upload API出错， 报错信息：{e}")

    def login(self, options):
        if options.token:
            self.headers["Token"] = options.token
        str_data = {"username": self.username, "password": self.password}
        login_data = json.dumps(str_data)
        login_res = requests.post(url=f"{self.url}/api/user/login", headers=self.headers, data=login_data,
                                  verify=False)
        # 判断是否登陆成功：
        if "401" not in login_res.text:
            token = login_res.json()['data']['token']
            logger.info("[+] Login Success!!")
            self.headers["Token"] = token
        else:
            logger.error("[-] login Failure! ")
            sys.exit(0)

    def get_all_finger(self):
        """获取所有指纹ID，用于删除指纹"""
        try:
            page = 1
            size = 1000
            url = "{url}/api/fingerprint/?page={page}&size={size}"
            data = {}
            headers = {
                "Accept": "application/json",
                "Token": "{}".format(self.headers["Token"]),
            }
            finger_id_list = []
            response = requests.get(url.format(url=self.url, page=page, size=size), data=data, headers=headers,
                                    verify=False)
            if response.status_code == 200 and response.json()['code'] == 200:
                total = response.json()['total']
                for i in response.json()['items']:
                    finger_id_list.append(i['_id'])
                while page * size < total:
                    page = response.json()['page'] + 1
                    response = requests.get(url.format(url=self.url, page=page, size=size), data=data, headers=headers,
                                            verify=False)
                    if response.status_code == 200 and response.json()['code'] == 200:
                        total = response.json()['total']
                        for i in response.json()['items']:
                            finger_id_list.append(i['_id'])
            else:
                logger.warning(f"获取所有指纹ID失败！失败原因：{response.text}")
            logger.info(f"获取所有指纹ID成功！共计：{len(finger_id_list)}")
            return finger_id_list
        except Exception as e:
            logger.error(f"ARL Finger upload API出错， 报错信息：{e}")
            sys.exit(0)

    def del_all_finger(self):
        """删除所有指纹"""
        url = "{url}/api/fingerprint/delete/".format(url=self.url)
        all_finger_list = self.get_all_finger()
        if all_finger_list:
            # 备份指纹
            self.export_finger()
            data = {"_id": all_finger_list}
            res = requests.post(url=url, data=json.dumps(data), headers=self.headers, verify=False).json()
            if res['code'] == 200:
                logger.info(f"删除所有指纹成功！")
            else:
                logger.error(f"删除所有指纹失败！失败原因：{res['message']}")
        else:
            logger.warning(f"ARL中没有指纹,无需删除！")

    def export_finger(self):
        url = "{url}/api/fingerprint/export/".format(url=self.url)
        res = requests.get(url=url, headers=self.headers, verify=False)
        if res.status_code == 200:
            with open("ARL_API_finger_bak.yml", "w", encoding="utf-8") as f:
                f.write(res.text)
            logger.info(f"导出ARL指纹成功！")
        else:
            logger.warning("导出指纹接口请求失败！")


if __name__ == '__main__':
    pass
