import random

r = random.randint(1,100)
c = 0
while True:
    num = input('請猜數字: ')
    num = int(num)
    c += 1
    if num < r:
    	print('比答案來的小')
    elif num > r:
    	print('比答案來的大')
    elif num == r:
    	print('終於猜對了！')
    	print('這是你猜的第', c, '次')
    	break
    print('這是你猜的第', c, '次')