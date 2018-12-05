import pandas as pd
import time
import sys

src_file_path = sys.argv[1]
out_file_dir = sys.argv[2]

print(src_file_path)
print(out_file_dir)


def str_sub(str):
    strs = str.split(r'/')
    return strs[2] + strs[0]


def split_data_by_date():
    cur_date = time.time()
    print("Start read file... %f" % (cur_date))
    pd_df_data = pd.DataFrame(pd.read_excel(src_file_path))
    print("End read file... %f" % (time.time() - cur_date))
    print(pd_df_data.shape)
    df_new_data = pd.DataFrame()
    df_new_data['CommentDate'] = pd_df_data['Comment Date']
    df_new_data['Comment'] = pd_df_data['Comment']
    print(df_new_data.shape)
    # df_new_data = df_new_data.sortlevel(0, ascending=True)
    df_new_data = df_new_data.sort_index(0, by="CommentDate", ascending=True)
    print(df_new_data.shape)
    df_new_data["CommentDate"] = df_new_data.apply(lambda x: str_sub(x['CommentDate']), axis=1)
    df_new_data.to_csv(out_file_dir + "sort_values.csv", index=False)

    pd_searise = df_new_data['CommentDate']
    df_values_count = pd_searise.value_counts()
    for indexkey in df_values_count.index:
        out_file_path = out_file_dir + str(indexkey) + ".csv"
        print(out_file_path)
        df_new_data.loc[df_new_data['CommentDate'] == indexkey].to_csv(out_file_path, header=False, index=False)


if __name__ == "__main__":
    split_data_by_date()
