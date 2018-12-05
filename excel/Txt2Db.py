import pandas as pd
import pymysql

data = pd.read_csv(r'./csv/toutiao_dict.txt', encoding='utf-8', names=['A'])
print(data.A)
# 创建连接
conn = pymysql.connect(host='ip.10.25.5.1', port=3306, user='user', passwd='password', db='club', charset='utf8')
# 创建游标
cursor = conn.cursor()
times = 0
for name in data['A']:
    print(name)
    # 执行SQL，并返回受影响行数,执行多次
    # effect_row = cursor.executemany("insert into ai_newwords(stat_date,word,count)values(%s,%s,%s)",
    #                                 [(index_key, item[0], item[1] * 1000)])
    try:
        effect_row = cursor.executemany("insert into ai_words_dict(word)values(%s)", [(name)])
        times = times + 1
        if times == 3000:
            conn.commit()
            print('-------commit-----')
            times = 0
        else:
            pass
    except:
        print("============Insert Error============")
        pass
    print("=================\n")
# 提交，不然无法保存新建或者修改的数据
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
