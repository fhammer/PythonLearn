import pandas as pd


# data = pd.read_csv(r'./csv/terms_count.csv', encoding='utf-8', names=['A', 'B'])
# data.A.to_csv(r'./csv/test_result.csv', header=False, index=False)

def str_sub(str):
    # strs = str.split(r'/')
    # return strs[2] + strs[0]
    return '210801'


print('---------------------------')
data = pd.read_csv(r'./csv/toutiao_data.csv', encoding='utf-8')
print(data.shape)
df_data = pd.DataFrame()
df_data['A'] = data['class_code']
df_data['B'] = data['new_title']
df_data["A"] = df_data.apply(lambda x: str_sub(x['A']), axis=1)
df_data.to_csv('./csv/201802.csv', header=False, index=False)
