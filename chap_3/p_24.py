import p_20
import re

text = p_20.get_UK_text()

result = re.findall('\[\[ファイル:(.*?)(?:\||\]\])', text)

print(result)