# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wanjie time:2018/7/7 0007


g = open('new_poetry.txt', 'w', encoding='utf-8')
with open('poetry.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = str(line).strip()
        if not line.startswith('卷'):
            g.write(line)
        if line.startswith('卷'):
            g.write('\n')
g.close()

# with open('new_poetry.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         line = line.strip()
#         if not line.startswith('\n'):
#             print(line)
