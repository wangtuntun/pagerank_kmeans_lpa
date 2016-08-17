#encoding=utf-8
#不行啊
import re
string1="{\"631\":\"体育\"},{\"67119\":\"金融学\"},{\"285\":\"音乐\"}"
result=re.match(r" [\x80-\xff]",string1)
print result
