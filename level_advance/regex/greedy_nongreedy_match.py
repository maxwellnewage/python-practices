"""
Testeando greedy y non-greedy matches
"""

import re


def bat_regex_exec(bat_regex):
    print(bat_regex.search('The Adventures of Batman'))
    print(bat_regex.search('The Adventures of Batwoman'))
    print(bat_regex.search('The Adventures of Batwowowowoman'))


bat_regex_exec(re.compile(r'Bat(wo)?man'))  # 0 or 1
bat_regex_exec(re.compile(r'Bat(wo)*man'))  # 0 or more
bat_regex_exec(re.compile(r'Bat(wo)+man'))  # 1 or more
bat_regex_exec(re.compile(r'Bat(wo){4}man'))  # 4 times
bat_regex_exec(re.compile(r'Bat(wo){4,5}man'))  # range 4 to 5 times
