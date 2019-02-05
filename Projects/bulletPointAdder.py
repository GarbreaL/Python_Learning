#! python3
# bulletPointAdder.py 获取剪贴版上的数据，在每行数据前加上"* ",再返回给剪贴板

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* '+lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
print('数据调整完成，请进行粘贴操作！')
