import re

phonenumbereg=re.compile(r'\d{3}-\d{3}-\d{4}')
mo=phonenumbereg.search('My number is 123-456-8888 and 231-654-9999')
print('--------------\n')
print('最基本的匹配，返回第一个match的项')
print('Base string:My number is 123-456-8888 and 231-654-9999')
print('Phone number found:'+mo.group())

#用括号来对匹配出来的数据进行拆分
phonenumbereg=re.compile(r'(\(\d{3}\))-(\d{3}-\d{4})')
mo=phonenumbereg.search('My number is 123-456-8888 and (231)-654-9999')
print('--------------\n')
print('用括号来对匹配出来的数据进行拆分')
print('Base string:My number is 123-456-8888 and (231)-654-9999')
print('Phone number found:'+mo.group())
print('number group1:'+mo.group(1))#分组1
print('number group2:'+mo.group(2))#分组2

#用？来进行可选的匹配
phonenumbereg=re.compile(r'(\(?\d{3}\))-(\d{3}-\d{4})')
mo=phonenumbereg.search('My number is （123-456-8888 and (231)-654-9999')
print('--------------\n')
print('用？来进行可选的匹配,比如第1个可以是括号，可以不是括号，第4个必须是括号')
print('Base string:My number is （123-456-8888 and (231)-654-9999')
print('Phone number found:'+mo.group())

#用findall来查找所有符合的字符串
phonenumbereg=re.compile(r'\d{3}-\d{3}-\d{4}')
mo=phonenumbereg.findall('My number is 123-456-8888 and 231-654-9999')
print('--------------\n')
print('用findall来查找所有符合的字符串')
print('Base string:My number is 123-456-8888 and 231-654-9999')
print('Phone number found \''+str(len(mo))+'\' matched number')
for i in range(0,len(mo)):
	print('match number'+str(i+1)+': '+mo[i])

#通过参数设置re.DOTALL，可以用.来匹配换行符
print('--------------\n')
print('通过参数设置re.DOTALL，可以用.来匹配换行符')
noNewLineRegex=re.compile(r'.*')
mo=noNewLineRegex.search('Serve the public.\nProtect the innocent.\nUpload the law.')
print('Base string:Serve the public.\nProtect the innocent.\nUpload the law.')
print('--没有匹配换行符的效果--')
print(mo.group())
newlineRegex=re.compile(r'.*',re.DOTALL)
mo=newlineRegex.search('Serve the public.\nProtect the innocent.\nUpload the law.')
print('--用re.DOTALL匹配换行符--')
print(mo.group())

#re.I或re.IGNORECASE,忽略大小写的，进行匹配查找
print('--------------\n')
print('re.I或re.IGNORECASE,忽略大小写的，进行匹配查找')
ignorecaseRegex=re.compile(r'([a])',re.I)
mo=ignorecaseRegex.findall('A dog chasing a cat')
for i in range(0,len(mo)):
	print('match character'+str(i+1)+': '+mo[i])

#用sub方法来进行字符串替换
print('--------------\n')
print('用sub方法来进行字符串替换')
strReplaceRegex=re.compile(r'[E]')
strnew=strReplaceRegex.sub('Edifier','E is a good speaker')
print('Base string:E is a good speaker')
print('Use "Edifier" repalce "E"')
print('New String is:'+strnew)

agentNameRegex=re.compile(r'Agent (\w)\w*')
strnew=agentNameRegex.sub(r'Agent \1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a  double agent')
print('--------------\n')
print('Base string:Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a  double agent')
print('对分组匹配的结果进行替换')
print('New String is:'+strnew)