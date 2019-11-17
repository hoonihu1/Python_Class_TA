import re
text = "파이썬 공부를 해보아요. 정말 즐겁죠?"
regex = re.compile("공부를")
mo = regex.search(text)
if mo != None:
    print(mo.group())a