# -*- coding: utf-8 -*-
import pandas as pd

# 读csv文件
data = pd.read_csv('weibo.csv')
# print data

# 返回前n行
first_rows = data.head(n=5)
# print first_rows

# 返回全部列名
cols = data.columns
# print cols

# 返回维度
dimensision = data.shape
# print dimensision

# 返回所有数据 numpy格式
# print data.values

# 返回每一列数据类型
# print data.dtypes

# 返回指定行数据
# print data.loc[1]

# 返回制定行制定类数据
# print data.loc[:,['disease']]

# 去掉有缺失值的行
#data.dropna(how='any')
# 对缺失值进行填充
#data.fillna(values='null')
