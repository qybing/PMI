import pandas as pd
codePath = r'GaodeCode.xlsx'
codePath2 = 'GaodeCode_python.xlsx'

df1 = pd.read_excel(codePath, sheetname='大陆adcode', dtype={'adcode': 'str', 'citycode': 'str'})
df2 = pd.read_excel(codePath, sheetname='POI分类与编码（中英文）', dtype={'NEW_TYPE': 'str'})
# 去除citycode为的省编码信息
df1 = df1[df1['citycode'].notnull()]

## 去除各城市本身代码
# 第一步，去除“市辖区”
df1 = df1[~df1['中文名'].str.contains('市辖区')]
# 第二步，去除各城市的第一顺位adcode,保留citycode为唯一的城市
gb = df1.groupby('citycode', as_index=False)


# df1_only = gb.count()
# df1_only = df1_only[df1_only['adcode']==1]
def rmFistDoc(df):
    if len(df) > 1:
        df = df[1:]
    return df


df1s = gb.apply(rmFistDoc)

## 处理POI分类与编码
gb2 = df2.groupby('大类', as_index=False)
df2s = gb2.apply(rmFistDoc)

writer = pd.ExcelWriter(codePath2)
df1s.to_excel(writer, sheet_name='大陆adcode', index=False)
df2s.to_excel(writer, sheet_name='POI分类与编码（中英文）', index=False)
writer.close()
print('执行完毕')