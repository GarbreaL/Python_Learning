#! python3
<<<<<<< HEAD
# bulletPointAdder.py 从一个TXT文件中读取里面的内容，并在每一行内容前加上“* ”
# 再将调整后的内容更新回去。
=======
# bulletPointAdder.py 获取剪贴版上的数据，在每行数据前加上"* ",再返回给剪贴板

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* '+lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
print('数据调整完成，请进行粘贴操作！')
>>>>>>> 7d5d7794d91b98e9bdb2f486eb365d92a577ff27
