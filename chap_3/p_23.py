import p_20
import re
import collections

text = p_20.get_UK_text()

result = re.findall("(={2,4}.*?={2,4})", text)
section = {}
for result_text in result:
    c1 = collections.Counter(result_text)
    c2 = int(c1['=']/2) - 1
    result_text = result_text.replace('=', '')
    section[result_text] = c2
print(section)