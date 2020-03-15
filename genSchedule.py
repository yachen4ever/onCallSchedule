#/usr/bin/python3 

from random import shuffle

staff = ["宋汉文", "李梦思", "唐连堂", "韩倩倩", "王旭晨", "马啸", "王红婧", "郭茂银", "吴军红"]
shuffle(staff) 
cntWeekday = cntWeekend = [0] * 9 #记录每个人出现的次数
tWeekday = tWeekend = 0 #记录轮到第几个了
kWeekday = kWeekend = 1 #输出第几周

while 1:
	print("第"+str(kWeekday)+"周",end=": ")
	for i in range(5):
		p = i + tWeekday
		if p > 8:
			p -= 9
		cntWeekday[p]+=1
		print(staff[p], end=' ')
	print()
	kWeekday += 1
	tWeekday += 5
	if tWeekday > 8:
		tWeekday -= 9
	
	flagTmp = True
	for i in range(8):
		if (cntWeekday[i + 1] != cntWeekday[0]):
			flagTmp = False
			break
	if flagTmp == True:
		break

print("----------------")
shuffle(staff)
while 1:
	print("第"+str(kWeekend)+"周",end=": ")
	for i in range(2):
		p = i + tWeekend
		if p > 8:
			p -= 9
		cntWeekend[p]+=1
		print(staff[p], end=' ')
	print()
	kWeekend += 1
	tWeekend += 2
	if tWeekend > 8:
		tWeekend -= 9
	
	flagTmp = True
	for i in range(8):
		if (cntWeekend[i + 1] != cntWeekend[0]):
			flagTmp = False
			break
	if flagTmp == True:
		break
