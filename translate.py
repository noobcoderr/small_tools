import requests
import hashlib
import sys


def main():
    """
    param1：查询字符,为自动判断
    param2：目的字符,可选参数有
    zh:中文
    en:英文
    yue:粤语
    wyw:文言文
    """
    if sys.argv[1] == "-h":
        print(main.__doc__)
    else:
        sign = join()
        q = sys.argv[1]
        From = "auto"
        to = sys.argv[2]
        appid = 20180922000210716
        salt = 15010110083

        url1 = "http://api.fanyi.baidu.com/api/trans/vip/translate?q={}&from={}&to={}&appid={}&salt={}&sign={}".\
            format(q, From, to, appid, salt, sign)

        result_all = requests.get(url1).json()
        result_dst = result_all["trans_result"][0]["dst"]
        print(result_dst)


def join():
    """将一些列必备的参数拼接到一起,并进行md5加密"""
    appid = 20180922000210716
    q = sys.argv[1]
    salt = 15010110083
    pwd = "wPXi4FtJeSwIK_QeRZxW"

    str1 = str(appid) + q + str(salt) + pwd

    hash = hashlib.md5()
    hash.update(str1.encode("utf-8"))
    return hash.hexdigest()


if __name__ == '__main__':
    main()
