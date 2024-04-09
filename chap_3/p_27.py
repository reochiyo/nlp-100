import p_20
import re

text = p_20.get_UK_text()

template = re.findall('\|(.+?)\s=\s*(.+)', text)

delete_template = []
for field, value in template:
    cleaned_value = re.sub("''+", "", value)
    cleaned_value_2 = re.sub("\[\[(.+?)\]\]", "\\1", cleaned_value)
    delete_template.append((field, cleaned_value_2))
print(delete_template)
