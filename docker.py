#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys
def massage():
    print('--------\033[1;31;40mDocker节点命令\033[0m--------')
    print('\033[1;32;40m1\033[0m:创建新版容器-端口偏移')
    print('\033[1;32;40m2\033[0m:创建新版容器-端口偏移-解锁Netflix')
    print('\033[1;32;40m3\033[0m:创建原版容器-单端口/多端口')
    print('\033[1;32;40m4\033[0m:创建原版容器-单端口/多端口-解锁Netflix')
    print('---------\033[1;31;40mDocker命令\033[0m---------')
    print('\033[1;32;40m5\033[0m:删除指定容器')
    print('\033[1;32;40m6\033[0m:重启Docker')
    print('---------\033[1;31;40m其他命令\033[0m---------')
    print('\033[1;32;40m7\033[0m:节点服务器端口偏移量计算')
    print('\033[1;32;40m8\033[0m:Debian系统开通指定端口')
    print('\033[1;32;40m9\033[0m:V2ray免费版对接SSP')
    print('\033[1;32;40m10\033[0m:V2ray付费版对接SSP')
    print('\033[1;32;40m11\033[0m:关闭防火墙')
    print('\033[1;32;40m12\033[0m:安装wget')
    print('\033[1;32;40m13\033[0m:安装curl')
    print('\033[1;32;40m14\033[0m:安装vim')
    print('\033[1;32;40m15\033[0m:安装BBR')
    print('\033[1;32;40m0\033[0m:退出程序')
    try:
        result = input('----请选择:')
        return result
    except:
        print('\n您没有选择正确的选项：')
        sys.exit()

Num  = massage()
if Num == 1:#运行容器新版端口偏移
    name = raw_input('请输入容器名称(默认super):')
    if len(name) ==0:
        name = 'super'
    node = raw_input('请输入节点ID(默认100):')
    if len(node) == 0:
        node = '100'  
    port_ob = raw_input('请输入端口偏移量(默认0):')
    if len(port_ob) == 0:
        port_sev = '11111'  
    else:
        port_ob = int(port_ob)
        port_sev = 11111 + port_ob
        port_sev = str(port_sev)
    port_web = raw_input('请输入网站偏移端口(默认11111):')
    if len(port_web) == 0:
        port_web = '11111'  
    url = raw_input('请输入网站地址(默认https://www.baidu.com):')
    if len(url) == 0:
        url = 'https://www.baidu.com'
    os.system('docker run -d --name='+name+' -e NODE_ID='+node+' -e MU_SUFFIX=cloudfront.com -e MU_REGEX=%5m%id.%suffix -e API_INTERFACE=modwebapi -e WEBAPI_URL='+url+' -e SPEEDTEST=0 -e WEBAPI_TOKEN=XiaoDaren --log-opt max-size=50m --log-opt max-file=3 -p '+port_sev+':'+port_web+'/tcp -p '+port_sev+':'+port_web+'/udp  --restart=always jiaowoxiaotete/docker-new')
    sys.exit()

if Num == 2:#运行容器新版端口偏移-解锁Netflix
    name = raw_input('请输入容器名称(默认super):')
    if len(name) ==0:
        name = 'super'
    node = raw_input('请输入节点ID(默认100):')
    if len(node) == 0:
        node = '100'
    port_ob = raw_input('请输入端口偏移量(默认0):')  
    if len(port_ob) == 0:
        port_sev = '11111'  
    else:
        port_ob = int(port_ob)
        port_sev = 11111 + port_ob
        port_sev = str(port_sev)
    port_web = raw_input('请输入网站偏移端口(默认11111):')
    if len(port_web) == 0:
        port_web = '11111'
    dns = raw_input('请输入DNS服务器地址(默认172.81.99.87):')  
    if len(dns) == 0:
        dns = '172.81.99.87'  
    url = raw_input('请输入网站地址(默认https://www.baidu.com):')  
    if len(url) == 0:
        url = 'https://www.baidu.com'
    os.system('docker run -d --name='+name+' -e NODE_ID='+node+' -e MU_SUFFIX=cloudfront.com -e MU_REGEX=%5m%id.%suffix -e API_INTERFACE=modwebapi -e WEBAPI_URL='+url+' -e SPEEDTEST=0 -e WEBAPI_TOKEN=XiaoDaren --log-opt max-size=50m --log-opt max-file=3 -p '+port_sev+':'+port_web+'/tcp -p '+port_sev+':'+port_web+'/udp -e DNS_1='+dns+' -e DNS_2='+dns+' --restart=always jiaowoxiaotete/docker-new')
    sys.exit()

elif Num == 3:#运行容器原版
    name = raw_input('请输入容器名称(默认super):')
    if len(name) ==0:
        name = 'super'
    node = raw_input('请输入节点ID(默认100):')
    if len(node) == 0:
        node = '100'
    url = raw_input('请输入网站地址(默认https://www.baidu.com):')  
    if len(url) == 0:
        url = 'https://www.baidu.com'
    os.system('docker run -d --name='+name+' -e NODE_ID='+node+' -e SPEEDTEST=0 -e MU_SUFFIX=cloudfront.com -e MU_REGEX=%5m%id.%suffix -e API_INTERFACE=modwebapi -e WEBAPI_URL='+url+' -e WEBAPI_TOKEN=XiaoDaren --network=host --log-opt max-size=50m --log-opt max-file=3 --restart=always jiaowoxiaotete/docker-old')
    sys.exit()

elif Num == 4:#运行容器原版解锁Netflix
    name = raw_input('请输入容器名称(默认super):')
    if len(name) ==0:
        name = 'super'
    node = raw_input('请输入节点ID(默认100):')
    if len(node) == 0:
        node = '100'
    dns = raw_input('请输入DNS服务器地址(默认172.81.99.87-日本):')  
    if len(dns) == 0:
        dns = '172.81.99.87'
    url = raw_input('请输入网站地址(默认https://www.baidu.com):')  
    if len(url) == 0:
        url = 'https://www.baidu.com'
    os.system('docker run -d --name='+name+' -e NODE_ID='+node+' -e SPEEDTEST=0 -e MU_SUFFIX=cloudfront.com -e MU_REGEX=%5m%id.%suffix -e API_INTERFACE=modwebapi -e WEBAPI_URL='+url+' -e WEBAPI_TOKEN=XiaoDaren --network=host --log-opt max-size=50m --log-opt max-file=3 -e DNS_1='+dns+' -e DNS_2='+dns+' --restart=always jiaowoxiaotete/docker-old')
    sys.exit()

elif Num == 5:
    name = raw_input('请输入容器名称(默认super):')
    if len(name) == 0:
        name = 'super'
    os.system('docker rm -f '+name)
    sys.exit()

elif Num == 6:
    os.system('docker restart docker')
    sys.exit()

elif Num == 7:#偏移量计算
    port = input('请输入节点服务器开通端口(必填):')
    port = port - 11111
    print('您的偏移量为%d'% port)
    sys.exit()

elif Num == 8:#端口防火墙
    port = raw_input('请输入节点服务器开通端口(必填):')
    os.system('/sbin/iptables -I INPUT -p tcp --dport '+port+' -j ACCEPT')
    os.system('/sbin/iptables -I INPUT -p udp --dport '+port+' -j ACCEPT')
    sys.exit()

elif Num == 9:#V2ray免费版一键对接
    url = raw_input('请输入对接网址(默认baidu):')
    if len(url) ==0:
        url = 'https://www.baidu.com'
    else:
        print('您的对接网址为：%s'% url)
    token = raw_input('请输入对接Token(默认XiaoDaren):')
    if len(token) == 0:
        token = 'XiaoDaren'  
    else:
        print('你的Token为：%s'% token)
    nodeid = raw_input('请输入节点ID:')  
    if len(nodeid) == 0:
        sys.exit()  
    os.system('wget -N --no-check-certificate https://raw.githubusercontent.com/NS-Sp4ce/V2Ray-With-SSpanel/master/install-release.sh')
    os.system('bash install-release.sh --panelurl '+url+' --panelkey '+token+' --nodeid '+nodeid)
    #增加开机自启功能
    os.system('systemctl enable v2ray')
    os.system('systemctl restart v2ray')
    sys.exit()

elif Num == 10:#V2ray付费版一键对接 脚本内已经开启了开机自启功能
    os.system('wget -N --no-check-certificate https://gist.github.com/Indexyz/3b541518e16aadc314af4b6e82e628bc/raw/bf959d40f3df630f8a8d0dc44413c34d2626503c/webapi.sh && chmod +x webapi.sh && bash webapi.sh')
    sys.exit()

elif Num == 11:#Centos 关闭防火墙
    os.system('systemctl stop firewalld.service')
    os.system('systemctl disable firewalld.service')
    sys.exit()

elif Num == 12:#Centos 安装wget
    os.system('yum -y install wget')
    sys.exit()

elif Num == 13:#Centos 更新curl
    os.system('yum update nss curl')
    sys.exit()

elif Num == 14:#Centos 安装vim
    os.system('yum install vim -y')
    sys.exit()

elif Num == 15:#BBR加速
    os.system('wget -N --no-check-certificate "https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh" && chmod +x tcp.sh && ./tcp.sh')
    sys.exit()

elif Num == 0:
    sys.exit() 

else:
    print('\n对不起没有该功能！！！\n')
