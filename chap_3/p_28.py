import p_20
import re

text = p_20.get_UK_text()

template = re.findall('\|(.+?)\s=\s*(.+)', text)

delete_template = []
for field, value in template:
    cleaned_value = re.sub("''+", "", value)
    #cleaned_value = re.sub("\'{2,}(.+?)\'{2,}", "\\1", value)
    cleaned_value_2 = re.sub("\[\[(.+?)\]\]", "\\1", cleaned_value)
    cleaned_value_3 = re.sub("\[(.+?)\]", "\\1", cleaned_value_2)
    cleaned_value_4 = re.sub("\*+(.+?)", "\\1", cleaned_value_3)
    cleaned_value_5 = re.sub("\:+(.+?)", "\\1", cleaned_value_4)
    cleaned_value_6 = re.sub("\{\{(.+?)\}\}", "\\1", cleaned_value_5)
    delete_template.append((field, cleaned_value_6))
print(delete_template)