# -*- coding:utf-8 -*-
"""
项目：ARL-Finger-ADD-Pro
文件：ARL_Finger_Add_Plus.py
功能描述：
Author：BigYoung
Blog：https://sec.bigyoung.cn/article/ARL-Finger-ADD-Pro/
创建时间：2023/11/28
"""
from tools.ARL_API import ARL_API
from tools.Ehole import Ehole_or_Finger_import
from tools.FingerprintHub import FingerpringHub_import
from tools.dismap import dismap_import
from tools.utils import CommandLines


def main():
    options = CommandLines().cmd()
    arl = ARL_API(options=options)
    if options.delete_f:
        ARL_API(options=options).del_all_finger()
        exit(0)
    if options.finger == "1":
        file = "./all_fingers/Ehole3.1_finger.json"
        Ehole_or_Finger_import(file, arl=arl)
    elif options.finger == "2":
        file = "./all_fingers/Finger_finger.json"
        Ehole_or_Finger_import(file, arl=arl)
    elif options.finger == "3":
        file = "./all_fingers/FingerprintHub_finger.json"
        FingerpringHub_import(file=file, arl=arl)
    elif options.finger == "4":
        dismap_import(arl=arl)
    elif options.finger == "all":
        file = "./all_fingers/Ehole3.1_finger.json"
        Ehole_or_Finger_import(file, arl=arl)
        file = "./all_fingers/Finger_finger.json"
        Ehole_or_Finger_import(file, arl=arl)
        file = "./all_fingers/FingerprintHub_finger.json"
        FingerpringHub_import(file=file, arl=arl)
        dismap_import(arl=arl)
    else:
        print(
            "[-] 请输入正确的-f参数，1：Ehole3.1_finger.json  2：Finger_finger.json 3：FingerprintHub_finger.json all: 导入工具支持的所有指纹")
        exit(0)


if __name__ == '__main__':
    main()
