#! python3
# pw.py - 把网站和密码进行保存，形成字典；通过pyperclip复制到剪贴板中
# 调用方式：在命令窗口中输入 py.exe D:\GitHub\Python_Learning\Projects\pw.py email
# 打开一个文本文档，或者直接在窗口进行粘贴操作，就会得到12364*abc
#  效果参考ScreenImages\PW运行效果图(注意截图的时候，文件并没有调整到Projects文件夹下面)

PASSWORD={'email':'12364*abc',
		  				'blog':'12345@sdwe',
		  				'luggage':'000DASDG23423'}

import  sys
import pyperclip
if len(sys.argv)>2:
	print('Usage:python pw.py [account] - copy account password ')
	sys.exit()

account=sys.argv[1]
if account in PASSWORD:
	pyperclip.copy(PASSWORD[account])
	print('Password for '+account+' copied to clipboard. ')
else:
	print('There is no account named '+account)
