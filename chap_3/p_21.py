import p_20
import re

text = p_20.get_UK_text()

#Way1
lines = text.split('\n')
category_lines = [line for line in lines if re.search('^\[\[Category:.+\]\]$', line)]
print(category_lines)

#Way2
category_lines_2 = re.findall('^\[\[Category:.+\]\]$', text, re.MULTILINE)
print(category_lines_2)