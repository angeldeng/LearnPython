import sys

import pygame

from _settings import Settings

from _ship import Ship

def run_game():
    #初始化游戏，创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))

    pygame.display.set_caption("外星人入侵")

    #创建一艘飞船
    ship=Ship(screen)

    #设置背景颜色
    bg_color=(230,230,230)

    #开始程序主循环
    while True:
    #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

        #每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()