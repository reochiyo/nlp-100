import p_20
import re

text = p_20.get_UK_text()

category_names = re.findall('\[\[Category:(.*?)(?:\||\]\])', text)

for name in category_names:
    print(name)