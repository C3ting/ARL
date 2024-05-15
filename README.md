## ARL(Asset Reconnaissance Lighthouse)资产侦察灯塔系统
[![Python 3.6](https://img.shields.io/badge/python-3.6-yellow.svg)](https://www.python.org/)
[![Docker Images](https://img.shields.io/docker/pulls/tophant/arl.svg)](https://hub.docker.com/r/tophant/arl)
[![Github Issues](https://img.shields.io/github/issues/TophantTechnology/ARL.svg)](https://github.com/TophantTechnology/ARL/issues)
[![Github Stars](https://img.shields.io/github/stars/TophantTechnology/ARL.svg)](https://github.com/TophantTechnology/ARL/stargazers)

**备份说明：本项目所有内容均来自**

**[TophantTechnology/ARL](https://github.com/TophantTechnology/ARL)**

# 灯塔工具推荐：

### ARL-Finger-ADD-Pro

## 主要功能

批量添加ARL指纹，支持：`ARL V2.6.1版本`

## 已支持导入的指纹库列表，共计：9001个

1. [Ehole3.1](https://github.com/EdgeSecurityTeam/EHole/releases/tag/v3.1)自带的指纹文件，Finger有1007个
2. [Finger](https://github.com/EASY233/Finger/blob/main/library/finger.json) 截止2023年3月11日最新版，Finger有1007个
3. [FingerprintHub](https://github.com/0x727/FingerprintHub/blob/main/web_fingerprint_v3.json) 截止2023年11月23日最新版，Finger有2839个
4. [dismap](https://github.com/zhzyker/dismap/blob/main/readme-zh.md#-rulelab) 截止2023年12月17日最新版，Finger有4598个

## 用法:

```
提示：本工具只适配此项目源码下的Finger指纹，网上下载的Finger指纹可能不适配，如需使用网上下载的Finger指纹，需要自行修改代码。

Usage: ARL_Finger_Add_Plus.py [options]

Options:
  -h, --help                  show this help message and exit
  -u URL, --url=URL           Please Enter the ARL Site Url
  -a AUTH, --auth=AUTH        Please Enter Your ARL username password
  -f FINGER, --finger=FINGER  Please Enter You Want import Finger, eg:
                              1：Ehole3.1_finger.json        2：Finger_finger.json
                              3：FingerprintHub_finger.json  4：Dismap_rule.go
                              all: 导入工具支持的所有指纹
  -t TOKEN, --token=TOKEN     Please Enter Your ARL Auth Token
  -d DELETE_F, --delete_f=DELETE_F
                              此参数用于删除ARL中已有的指纹，请谨慎使用此参数。删除前默认备份指纹到当前目录下的ARL_API_finger.yml文件


使用示例：

ARL API Key 用法：
python3 ARL_Finger_Add_Plus.py -u https://192.168.1.1:8888 -t 1234567890abcdefg -f all

ARL 用户名密码 用法：
python3 ARL_Finger_Add_Plus.py -u https://192.168.1.1:8888 -a admin:arlpass -f all

```

## 常见问题

Q：导入指纹库时，返回报错信息：**413错误**

A：这是因为ARL的Nginx默认配置，未设置上传文件的大小限制。解决办法：需要先修改ARL的Nginx配置，具体修改方法如下：

```
# 以下内容针对ARL容器部署的情况，如果是源码部署的，同理

1. 进入到arl-web容器里，执行：docker exec -it arl-web /bin/bash

2. vim /etc/nginx/nginx.conf

3. 在http块下，添加以下内容：
    client_max_body_size 20m;

4. 重启nginx：nginx -s reload

5. 退出容器：exit

6. 重新运行脚本
```

Q：为什么指纹库列表说是9000+，导入后没有这么多？

A：因为使用的是ARL的指纹文件导入接口，此接口支持去重功能，如果使用单个指纹导入接口，没有去重功能，应该是9000+，但是那样没有意义。[](https://vip.bdziyi.com/10464.html)

### 简介

旨在快速侦察与目标关联的互联网资产，构建基础资产信息库。
协助甲方安全团队或者渗透测试人员有效侦察和检索资产，发现存在的薄弱点和攻击面。

在开始使用之前，请务必阅读并同意[免责声明](Disclaimer.md)中的条款，否则请勿下载安装使用本系统。



# ARL

### 特性
1. 域名资产发现和整理
2. IP/IP 段资产整理
3. 端口扫描和服务识别
4. WEB 站点指纹识别
5. 资产分组管理和搜索
6. 任务策略配置
7. 计划任务和周期任务
8. Github 关键字监控
9. 域名/IP 资产监控
10. 站点变化监控
11. 文件泄漏等风险检测
12. nuclei PoC 调用
13. [WebInfoHunter](https://C3ting.github.io/ARL-doc/function_desc/web_info_hunter/) 调用和监控

### 系统要求

目前暂不支持Windows，初次体验可采用Docker方式运行，长期使用建议采用源码安装方式运行。系统配置建议：CPU:4线程 内存:8G 带宽:10M。  
由于自动资产发现过程中会有大量的的发包，建议采用云服务器可以带来更好的体验。

### Docker 启动


```
cd /opt/
mkdir docker_arl
wget -O docker_arl/docker.zip https://github.com/C3ting/ARL/releases/download/v2.6.2/docker.zip
cd docker_arl
unzip -o docker.zip
docker volume create arl_db
docker compose pull
docker compose up -d
```


Ubuntu 下可以直接执行 `apt-get install docker.io docker-compose -y` 安装相关依赖

详细说明可以参考: [Docker 环境安装 ARL](https://C3ting.github.io/ARL-doc/system_install/)

### 截图

1. 登录页面     
默认端口5003 (https), 默认用户名密码admin/arlpass  
![登录页面](./image/login.png)

2. 任务页面
![任务页面](./image/task.png)

3. 子域名页面
![子域名页面](./image/domain.png)

4. 站点页面
![站点页面](./image/site.png)

5. 资产监控页面
![资产监控页面](./image/monitor.png)
详细说明可以参考：[资产分组和监控功能使用说明](https://github.com/C3ting/ARL/wiki/%E8%B5%84%E4%BA%A7%E5%88%86%E7%BB%84%E5%92%8C%E7%9B%91%E6%8E%A7%E5%8A%9F%E8%83%BD%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E)

6. 策略页面
![策略配置页面](./image/policy.png)

7. 筛选站点进行任务下发
![筛选站点进行任务下发](./image/scan.png)
详细说明可以参考： [2.3-新添加功能详细说明](https://github.com/C3ting/ARL/wiki/ARL-2.3-%E6%96%B0%E6%B7%BB%E5%8A%A0%E5%8A%9F%E8%83%BD%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)

8. 计划任务
![计划任务](./image/task_scheduler.png)
详细说明可以参考： [2.4.1-新添加功能详细说明](https://github.com/C3ting/ARL/wiki/ARL-2.4.1-%E6%96%B0%E6%B7%BB%E5%8A%A0%E5%8A%9F%E8%83%BD%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)

9. GitHub 监控任务
![GitHub 监控任务](./image/github_monitor.png)

### 任务选项说明
| 编号 |      选项      |                                       说明                                        |
| --- | -------------- | -------------------------------------------------------------------------------- |
| 1    | 任务名称        | 任务名称                                                                          |
| 2    | 任务目标        | 任务目标，支持IP，IP段和域名。可一次性下发多个目标                                      |
| 3    | 域名爆破类型    | 对域名爆破字典大小, 大字典：常用2万字典大小。测试：少数几个字典，常用于测试功能是否正常        |
| 4    | 端口扫描类型    | ALL：全部端口，TOP1000：常用top 1000端口，TOP100：常用top 100端口，测试：少数几个端口 |
| 5    | 域名爆破        | 是否开启域名爆破                                                                   |
| 6    | DNS字典智能生成 | 根据已有的域名生成字典进行爆破                                                      |
| 7    | 域名查询插件    |  已支持的数据源为13个，`alienvault`, `certspotter`,`crtsh`,`fofa`,`hunter` 等        |
| 8    | ARL 历史查询    | 对arl历史任务结果进行查询用于本次任务                                                |
| 9    | 端口扫描        | 是否开启端口扫描，不开启站点会默认探测80,443                                         |
| 10   | 服务识别        | 是否进行服务识别，有可能会被防火墙拦截导致结果为空                                     |
| 11   | 操作系统识别    | 是否进行操作系统识别，有可能会被防火墙拦截导致结果为空                                 |
| 12   | SSL 证书获取    | 对端口进行SSL 证书获取                                                             |
| 13   | 跳过CDN       | 对判定为CDN的IP, 将不会扫描端口，并认为80，443是端口是开放的                             |
| 14   | 站点识别        | 对站点进行指纹识别                                                                 |
| 15   | 搜索引擎调用    | 利用搜索引擎搜索下发的目标爬取对应的URL和子域名                                                       |
| 16   | 站点爬虫        | 利用静态爬虫对站点进行爬取对应的URL                                                  |
| 17   | 站点截图        | 对站点首页进行截图                                                                 |
| 18   | 文件泄露        | 对站点进行文件泄露检测，会被WAF拦截                                                  |
| 19   | Host 碰撞        | 对vhost配置不当进行检测                                                |
| 20    | nuclei 调用    | 调用nuclei 默认PoC 对站点进行检测 ，会被WAF拦截，请谨慎使用该功能                |
| 21   | WIH 调用      | 调用 WebInfoHunter 工具在JS中收集域名,AK/SK等信息                     |
| 22   | WIH 监控任务   | 对资产分组中的站点周期性 调用 WebInfoHunter 工具在JS中域名等信息进行监控  |

### 配置参数说明

Docker环境配置文件路径 `docker/config-docker.yaml`

|       配置        |                 说明                 |
| ----------------- | ------------------------------------ |
| CELERY.BROKER_URL | rabbitmq连接信息                      |
| MONGO             | mongo 连接信息                        |
| QUERY_PLUGIN      | 域名查询插件数据源Token 配置             |
| GEOIP             | GEOIP 数据库路径信息                  |
| FOFA              | FOFA API 配置信息                     |
| DINGDING          | 钉钉消息推送配置                     |
| EMAIL              | 邮箱发送配置                     |
| GITHUB.TOKEN      |  GITHUB 搜索 TOKEN                 |
| ARL.AUTH          | 是否开启认证，不开启有安全风险          |
| ARL.API_KEY       | arl后端API调用key，如果设置了请注意保密 |
| ARL.BLACK_IPS     | 为了防止SSRF，屏蔽的IP地址或者IP段      |
| ARL.PORT_TOP_10     | 自定义端口，对应前端端口测试选项      |
| ARL.DOMAIN_DICT     | 域名爆破字典，对应前端大字典选项      |
| ARL.FILE_LEAK_DICT     | 文件泄漏字典      |
| ARL.DOMAIN_BRUTE_CONCURRENT     | 域名爆破并发数配置      |
| ARL.ALT_DNS_CONCURRENT     | 组合生成的域名爆破并发数      |
| PROXY.HTTP_URL     | HTTP代理URL设置      |
| FEISHU | 飞书消息推送配置 |
| WXWORK | 企业微信消息推送 |


### 忘记密码重置

当忘记了登录密码，可以执行下面的命令，然后使用 `admin/admin123` 就可以登录了。
```
docker exec -ti arl_mongodb mongo -u admin -p admin
use arl
db.user.drop()
db.user.insert({ username: 'admin',  password: hex_md5('arlsalt!@#'+'admin123') })
```


### 源码安装

仅仅适配了 centos 7 ，且灯塔安装目录为/opt/ARL
如果在其他目录可以创建软连接，且安装了四个服务分别为`arl-web`, `arl-worker`, `arl-worker-github`, `arl-scheduler`

```
wget https://raw.githubusercontent.com/C3ting/ARL/master/misc/setup-arl.sh
chmod +x setup-arl.sh
./setup-arl.sh
```


### FAQ

请访问如下链接[FAQ](https://C3ting.github.io/ARL-doc/faq/)

### 写在最后

目前ARL仅仅只是完成了对资产的部分维度的发现和收集，自动发现过程中难免出现覆盖度不全、不精准、不合理等缺陷的地方还请反馈至我们。  

![公众号](./image/logo.jpg)
