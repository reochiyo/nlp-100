import p_20
import re

text = p_20.get_UK_text()

template = re.findall('\|(.+?)\s=\s*(.+)', text)
print(template)
