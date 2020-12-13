# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 Double Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import requests
import sqlite3


def get(url, ip):
    proxies = {
        'http': f'{ip[0]}:{ip[1]}',
        'https': f'{ip[0]}:{ip[1]}'
    }
    headers = {
        'User-Agent': '"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",'
    }
    for i in range(10):
        try:
            r = requests.get(url=url, headers=headers, proxies=proxies, timeout=2)
            yield (1, r.elapsed.microseconds / 1000000)
        except:
            yield (0, 0)


def sqlit(sql):
    connect = sqlite3.connect(r"D:\pythonLearn\Scrapy\testProject\testProject\ipData\IP.db")
    cursor = connect.cursor()
    cursor.execute(sql)
    while True:
        row = cursor.fetchone()
        if not row:
            break
        yield row
    cursor.close()
    connect.close()


# 按间距中的绿色按钮以运行脚本。
def sqlit_updata(ip, time):
    sql = f"update IP set acc={time[0]},speed={time[1]} where ip='{ip[0]}'"
    connect = sqlite3.connect(r"D:\pythonLearn\Scrapy\testProject\testProject\ipData\IP.db")
    cursor = connect.cursor()
    cursor.execute(sql)
    connect.commit()
    print('更新成功') if connect.total_changes == 1 else print('更新失败')
    cursor.close()
    connect.close()


if __name__ == '__main__':
    # 迭代读取数据库
    # 请求10次，计算请求成功率
    # 计算请求平均速度
    # 写入数据库

    sql = "select * from IP where acc is null and ip !='None'"
    url = "http://httpbin.org/ip"
    one_ip=sqlit(sql)
    while True:
        pass
    # for ip in sqlit(sql):
    #     speed = 0
    #     acc = 0
    #     for i in get(url, ip):
    #         acc += i[0]
    #         speed += i[1]
    #     t = (acc / 10, speed / acc) if acc and speed > 0 else (0, 0)
    #     sqlit_updata(ip, t)
        # print(t)
        # print(f'{ip[0]}:{ip[1]}')
