#! python3
#phoneAndEmai.py 从剪贴板的文本中，查找出所有的电话号码和Emai地址

import pyperclip,re

phoneRegex=re.compile(r'''(

)''',re.VERBOSE)
