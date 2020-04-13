import random
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字結束值: ')
start = int(start)
end = int(end)

r = random.randint(start,end)
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