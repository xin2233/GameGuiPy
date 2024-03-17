# coding:utf-8

###########################
#物联1602zjx
###########################
###########################
# 绘制树叶图案
###########################
import turtle as t

t.pensize(4)
# t.hideturtle()
t.color('black', 'green')
t.setup(500, 500)  # 图片大小
t.speed(10)  # 画笔速度


def curvemove():  # 半圆
    for i in range(200):
        t.right(1)
        t.forward(1)


def gofoward():  # 弯曲的直线 第一笔
    for i in range(130):
        t.rt(0.1)  # 向右转 0.1
        t.fd(1)  # 前进 1


def backward():  # 弯曲的直线 回来的一笔
    for i in range(100):
        t.lt(0.1)  # 向左
        t.fd(1)


def xian():  # 树叶内部的线
    for i in range(120):
        t.lt(0.3)
        t.fd(1)


def shuzhi():  # 画树枝
    for i in range(260):
        t.lt(0.1)
        t.fd(1)


# 第一片叶子
t.pu()  # 起笔
t.goto(0, 10)  # 移动位置
t.pd()  # 放笔
t.seth(60)  # 笔尖朝向
t.begin_fill()
gofoward()
curvemove()
t.lt(120)
curvemove()
backward()
t.end_fill()

# 第二片叶子
t.pu()  # 起笔
t.goto(0, 10)  # 移动位置
t.pd()  # 放笔
t.seth(-60)  # 笔尖朝向
t.begin_fill()
gofoward()
curvemove()
t.lt(120)
curvemove()
backward()
t.end_fill()

# 第三片叶子
t.pu()  # 起笔
t.goto(0, 10)  # 移动位置
t.pd()  # 放笔
t.seth(-180)  # 笔尖朝向
t.begin_fill()
gofoward()
curvemove()
t.lt(120)
curvemove()
backward()
t.end_fill()

# 画树叶线
t.pu()  # 起笔
t.goto(0, 10)  # 移动位置
t.pd()  # 放笔
t.seth(-10)  # 笔尖朝向
xian()

t.pu()  # 起笔
t.goto(0, 10)  # 移动位置
t.pd()  # 放笔
t.seth(-130)  # 笔尖朝向
xian()

t.pu()  # 起笔
t.goto(0, 10)  # 移动位置
t.pd()  # 放笔
t.seth(120)  # 笔尖朝向
xian()

# 画树枝
t.pensize(10)
t.pu()  # 起笔
t.goto(0, 10)  # 移动位置
t.pd()  # 放笔
t.seth(-60)  # 笔尖朝向
shuzhi()
t.seth(0)
t.fd(10)


t.done()  # 结束
