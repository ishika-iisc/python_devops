import re

txt = "this is raining in india"
# var = re.findall("ai", txt)
# var = re.search("spain", txt)
var = re.split(r"\s", txt, maxsplit=1)
# print("first white space character in position:", var.start())
print(var)

