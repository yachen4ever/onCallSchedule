#/usr/bin/python3 

from random import shuffle

staff = ["宋汉文", "李梦思", "韩倩倩", "王旭晨",  "王红婧", "郭茂银", "唐连堂","陈/陆"]

staff2 = ["宋汉文", "李梦思", "韩倩倩", "王旭晨",  "王红婧", "郭茂银", "唐连堂"]
shuffle(staff)  # 随机排序打乱队列次序
cntWeekday = cntWeekend = [0] * 8 # 记录每个人出现的次数
tWeekday = tWeekend = 0 # 记录轮到第几个了
kWeekday = kWeekend = 1 # 用于输出第几周

while 1:
	print("第"+str(kWeekday)+"周",end=": ")
	for i in range(5): # 每周5个
		p = i + tWeekday # p用于记录当前轮到谁了
		if p > 7: # 如果p>8了重新从0开始记录
			p -= 8
		cntWeekday[p]+=1 # 该人值班次数+1
		print(staff[p], end=' ')
	print()
	kWeekday += 1 # 周数+1
	tWeekday += 5 
	if tWeekday > 7:
		tWeekday -= 8
	
	flagTmp = True # 设置flag
	for i in range(7): # 判断每个人值班次数是否相同
		if (cntWeekday[i + 1] != cntWeekday[0]):
			flagTmp = False
			break
	if flagTmp == True: # 如果相同直接跳出循环
		break

print("----------------")
shuffle(staff2)
while 1:
	print("第"+str(kWeekend)+"周",end=": ")
	for i in range(2):
		p = i + tWeekend
		if p > 6:
			p -= 7
		cntWeekend[p]+=1
		print(staff2[p], end=' ')
	print()
	kWeekend += 1
	tWeekend += 2
	if tWeekend > 6:
		tWeekend -= 7
	
	flagTmp = True
	for i in range(6):
		if (cntWeekend[i + 1] != cntWeekend[0]):
			flagTmp = False
			break
	if flagTmp == True:
		break
