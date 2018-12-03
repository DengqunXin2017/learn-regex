import re
import os


regex = r"(([a-zA-Z]+)|([\u4e00-\u9fa5])) {0,}\1"

test_str = open('/Users/snowman/PycharmProjects/learn-regex/text.txt').read()

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    