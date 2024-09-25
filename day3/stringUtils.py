#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :Untitled-2
@说明        :
@时间        :2024/09/24 16:54:31
@作者        :chenyang
@版本        :1.0
'''


class StringUtils:
    @staticmethod
    def is_palindrome(s):
        s = s.lower().replace(" ", "")
        return s == s[::-1]

result = StringUtils.is_palindrome("A man a plan a canal Panama")
print(result)  # 输出：True 