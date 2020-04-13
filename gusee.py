import random

r = random.randint(1,100)
while True:
    num = input('請猜數字: ')
    num = int(num)
    if num < r:
    	print('比答案來的小')
    elif num > r:
    	print('比答案來的大')
    elif num == r:
    	print('終於猜對了！')
    	break