# !/user/bin/python
# -*- coding: UTF-8 -*-
# 查询相同或不同的数
with open('new_code.csv', 'r', encoding='utf-8') as r:
    data = r.read().splitlines(False)[0:]
    result = [(f) for f in data]
with open('old_code.csv','r', encoding='utf-8') as q:
    data = q.read().splitlines(False)[0:]
    data.sort()
    result1 = [(f) for f in data]
for i in result1:
    if i not in result:
        print(i)
