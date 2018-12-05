# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"[£€]"

test_str = "$16.32 12.19 £16.29 €18.29  €18,29"

subst = "$"

# You can manually specify the number of replacements by changing the 4th argument
result = re.sub(regex, subst, test_str, 0, re.MULTILINE)

if result:
    print (result)

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
