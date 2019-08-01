import pygame
from pygame.locals import *
import sys
import random
#启动一个宽700，高500的图形界面
screen=pygame.display.set_mode((700,500))
#给屏幕添加名字
pygame.display.set_caption('满天星')
#使用字符串获取图片路径
star_image='D:\star5.png'
#使用路径获取图片
star=pygame.image.load(star_image)
#使用屏幕对象，将星星放在屏幕上
screen.blit(star,(100,100))
screen.blit(star,(100,150))
screen.blit(star,(100,200))




#创建300个星星
for i in range(50):
    x=random.randint(0,700-50)
    y=random.randint(0,500-50)
    screen.blit(star,(x,y))

while True:
    #获取退出的事件
    for i in pygame.event.get():
        if i.type == QUIT:
            #退出
            sys.exit()
        # 刷新界面
        pygame.display.update()


