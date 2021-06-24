# -*- coding: utf-8 -*-
from turtle import *
import turtle

speed(0)
penup()
seth(180)
fd(200)
seth(0)
penup()  # 外圈头
circle(150, 40)
pendown()
fillcolor('dodgerblue')
begin_fill()
circle(150, 280)
end_fill()  # 外圈头
fillcolor("red")
begin_fill()  # 外圈头
seth(0)  # 项圈
fd(200)
circle(-5, 90)
fd(10)
circle(-5, 90)
fd(210)
circle(-5, 90)
fd(10)
circle(-5, 90)
end_fill()  # 项圈
fd(183)  # 右脸
left(45)
fillcolor("white")
begin_fill()
circle(120, 100)
seth(90)  # 眼睛
a = 2.5
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a -= 0.05
        lt(3)
        fd(a)
    else:
        a += 0.05
        lt(3)
        fd(a)
penup()
seth(180)
fd(60)
pendown()
seth(90)
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a -= 0.05
        lt(3)
        fd(a)
    else:
        a += 0.05
        lt(3)
        fd(a)  # 眼睛
seth(180)
penup()
fd(60)
pendown()
seth(215)
circle(120, 100)
end_fill()  # 脸部颜色和眼睛部分
seth(0)  # 左眼珠部分
penup()
fd(40)
seth(90)
fd(170)
seth(0)
fd(5)
pendown()
fillcolor("black")
begin_fill()
circle(15, 360)
end_fill()
seth(90)
penup()
fd(5)
pendown()
seth(0)
fillcolor("white")
begin_fill()
circle(4, 360)
end_fill()  # 左眼珠部分
penup()  # 右眼珠
seth(0)
fd(58)
seth(270)
fd(15)
seth(0)
pensize(5)
circle(18, 90)
pendown()
circle(18, 180)
penup()
circle(18, 90)
pendown()
pensize(1)  # 右眼珠
penup()  # 鼻子
seth(270)
fd(7)
seth(180)
fd(27)
pendown()
fillcolor("red")
begin_fill()
circle(20)
end_fill()  # 鼻子
seth(270)  # 嘴
penup()
fd(40)
pendown()
pencolor("black")
pensize(2)
fd(90)
seth(0)
circle(120, 50)
penup()
circle(120, 260)
pendown()
circle(120, 50)  # 嘴
penup()  # 胡须
seth(90)
fd(60)
seth(0)
fd(20)
pendown()
fd(60)
penup()
fd(-60)
seth(90)
fd(20)
pendown()
seth(15)
fd(60)
penup()
fd(-60)
seth(270)
fd(40)
pendown()
seth(-15)
fd(50)
penup()
fd(-50)
seth(180)
fd(40)
pendown()
seth(-165)
fd(50)
penup()
fd(-50)
seth(90)
fd(40)
seth(165)
pendown()
fd(60)
fd(-60)
penup()
seth(280)
fd(20)
seth(180)
pendown()
fd(60)  # 胡须
penup()  # 下半身
home()
penup()
seth(180)
fd(200)
seth(0)
seth(90)
fd(36)
seth(0)
fd(98)
pendown()
fillcolor("dodgerblue")
begin_fill()
seth(50)
fd(70)
seth(40)
fd(20)
right(90)
fd(35)
right(75)
fd(105)
seth(90)
fd(10)
seth(-90)
fd(90)
seth(-95)
fd(80)
seth(180)
fd(80)  # 右腿
penup()  # 左腿和过渡
fd(30)
seth(-90)
fd(30)
seth(0)
circle(30, 90)
pendown()
circle(30, 180)
penup()
circle(30, 90)
seth(90)
fd(30)
seth(180)
fd(30)
pendown()
fd(80)  # 腿
seth(92)
fd(80)
seth(90)
fd(75)
fd(-30)
seth(-135)
fd(30)
right(90)
fd(40)
right(93)
fd(78)
seth(0)
fd(205)
end_fill()
fillcolor("red")  # 项圈的补充
begin_fill()
circle(5, 90)
fd(10)
circle(5, 90)
fd(10)
end_fill()
penup()
seth(50)
fd(70)
seth(40)
fd(16)
right(90)
fd(20)
pendown()
fillcolor("white")  # 手掌
begin_fill()
circle(30)
end_fill()
penup()
seth(-90)
fd(253)
seth(180)
fd(160)
seth(-90)
fd(30)
seth(0)
pendown()
fillcolor("white")
begin_fill()
penup()
circle(31, 90)
pendown()
circle(31, 180)
penup()
circle(31, 90)
end_fill()
seth(90)
fd(30)
seth(0)
fd(24)
pendown()
seth(180)
circle(15, 180)  # 脚
fd(90)
circle(15, 180)
fd(90)
penup()
seth(180)
fd(60)
penup()
seth(0)
pendown()
circle(-15, 180)
fd(80)
circle(-15, 180)
fd(80)
penup()
seth(180)
fd(140)
seth(90)
fd(90)
seth(-45)
pendown()
fillcolor("white")
begin_fill()
circle(30)
end_fill()
penup()
seth(-90)
fd(50)
seth(0)
fd(173)
seth(0)
fillcolor("white")  # 胸
begin_fill()
pendown()
circle(90, 128)
seth(180)
fd(145)
seth(-128)
circle(90, 129)
end_fill()
seth(90)
penup()
fd(35)
seth(0)
pendown()
circle(70, 90)  # 口袋
seth(180)
fd(140)
seth(-90)
circle(70, 90)
penup()
seth(90)
fd(90)
pendown()
seth(0)
fillcolor("#ffd200")  # 铃铛
begin_fill()
circle(20)
end_fill()
seth(90)
pensize(2)
fd(13)
fillcolor("black")
begin_fill()
seth(0)
circle(2)
end_fill()
seth(-90)
fd(13)
seth(0)
penup()
circle(20, 110)
pendown()
seth(170)
fd(20)
seth(190)
fd(20)
penup()
seth(-90)
fd(3.5)
pendown()
seth(10)
fd(20)
seth(-10)
fd(22)

# 大雄部分
pensize(1)
penup()
seth(0)
fd(400)
pendown()
# speed(0)
fillcolor("black")
begin_fill()
seth(30)
circle(100, 60)
fd(20)  # 右脸
seth(50)
circle(50, 150)
seth(70)
fd(4)
seth(50)
fd(4)
fd(-4)
seth(70)
fd(-4)
seth(145)
fd(5)
seth(138)
fd(5)
fd(-5)
seth(145)
fd(-5)
seth(150)
circle(60, 150)
seth(-90)
fd(20)
circle(84, 92)
end_fill()
penup()
seth(90)
fd(110)
seth(0)
fd(50)
fillcolor("#FAFAD2")
begin_fill()
pendown()  # 发际线
seth(85)
fd(20)
seth(160)
fd(20)
seth(165)
fd(20)
seth(170)
fd(10)
seth(175)
fd(20)
seth(180)
fd(10)
seth(185)
fd(20)
seth(190)
fd(20)
seth(195)
fd(10)
seth(200)
fd(14.5)
seth(-85)
fd(30)  # 发际线
seth(-90)
fd(20)
circle(84, 92)
seth(30)
circle(100.5, 60)
fd(30)
end_fill()  # 脸的补全
penup()
seth(-90)
fd(10)
pendown()
fillcolor("#FAFAD2")
begin_fill()
seth(80)
circle(-8, 190)
seth(-90)
fd(5)
seth(-95)
fd(5)
seth(-100)
fd(5)
seth(-105)
fd(5)
seth(-110)
fd(5)
circle(-8, 135)
penup()
seth(90)
fd(15)
seth(0)
fd(3)
pendown()

seth(60)
fd(8)
seth(70)
fd(8)
fd(-8)
seth(70)
circle(-5, 180)
seth(-120)
fd(14)
end_fill()
penup()
seth(180)
fd(142)
seth(90)
fd(23)
pendown()
fillcolor("#FAFAD2")
begin_fill()
seth(100)
circle(8, 180)
seth(-90)
fd(6)
seth(-85)
fd(6)
seth(-80)
fd(6)
circle(8, 140)
end_fill()
seth(100)
fd(20)
circle(5, 210)
fd(7)
penup()
seth(0)
fd(142)
seth(90)
fd(9)
pendown()
seth(180)
fd(18)
seth(90)
fillcolor("white")
begin_fill()
a = 2.3
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a -= 0.05
        lt(3)
        fd(a)
    else:
        a += 0.05
        lt(3)
        fd(a)

penup()
seth(180)
fd(50)
seth(90)
pendown()
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a -= 0.05
        lt(3)
        fd(a)
    else:
        a += 0.05
        lt(3)
        fd(a)
end_fill()
seth(180)
penup()
fd(70)
pendown()
seth(0)
fd(20)
penup()
fd(34)
seth(-90)
fd(2)
pendown()
pensize(6)
circle(4)
penup()
seth(0)
fd(26)
seth(-90)
fd(2.5)
seth(0)
pendown()
circle(4)
pensize(2)
penup()
seth(90)
fd(40)
seth(0)
fd(15)
seth(30)
pendown()
fd(8)
seth(0)
fd(10)
seth(-40)
fd(15)
seth(-50)
fd(7)
seth(-60)
fd(7)
penup()
seth(180)
fd(95)
seth(90)
fd(25)
pendown()
seth(-145)
fd(10)
seth(-135)
fd(5)
seth(-125)
fd(5)
seth(-120)
fd(5)
seth(-115)
fd(5)
seth(-110)
fd(5)
penup()
seth(90)
fd(30)
seth(0)
fd(25)
pendown()
seth(-30)
fd(19)
penup()
pensize(1)
seth(0)
fd(13)
seth(-90)
fd(81)
seth(0)
pendown()
circle(8)
penup()
seth(-90)
fd(20)
seth(180)
fd(10)
seth(160)
pendown()
fd(25)
fd(-25)
seth(-15)
fd(5)
seth(-10)
fd(5)
seth(0)
fd(5)
seth(10)
fd(5)
seth(15)
fd(5)
seth(20)
fd(27)
seth(-90)
penup()
fd(25)
seth(180)
fd(36)
seth(0)
pendown()
fillcolor("white")
begin_fill()
circle(68.5, 75)
seth(-105)
circle(-68.5, 75)
circle(-72.5, 78)
penup()
seth(-90)
fd(100)
seth(0)
fd(133)
seth(90)
fd(85)
end_fill()
fillcolor("#FAFAD2")
begin_fill()
seth(-160)
fd(104)
seth(0)
fd(38)
seth(-90)
fd(7.5)
pendown()
seth(0)
circle(66, 76)
end_fill()
penup()
seth(180)
fd(80)
seth(-90)
fd(33.5)
pendown()
seth(-15)
fd(5)
seth(-10)
fd(5)
seth(0)
fd(5)
seth(10)
fd(5)
seth(15)
fd(5)
seth(20)
fd(27)
penup()
seth(180)
fd(12)
seth(-90)
fd(21)
pendown()
fillcolor("#FAFAD2")
begin_fill()
fd(12)
seth(180)
fd(46)
seth(90)
fd(11)
penup()
seth(-30)
fd(5)
seth(-20)
fd(5)
seth(-10)
fd(5)
seth(0)
fd(5)
pendown()
circle(73, 27)
end_fill()
penup()
seth(-90)
fd(6)
seth(180)
fd(5)
pendown()
fillcolor("white")
begin_fill()
seth(-50)
fd(12)
seth(-100)
fd(30)
seth(135)
fd(40)
seth(-135)
fd(40)
seth(100)
fd(30)
seth(45)
fd(16)
end_fill()
fillcolor("#EEC900")
begin_fill()
fd(-16)
seth(-145)
fd(40)
circle(20, 45)
fd(10)
left(10)
fd(5)
right(10)
fd(10)
left(90)
fd(25)
seth(85)
fd(25)
seth(75)
fd(10)
fd(-10)
seth(85)
fd(-25)
seth(-90)
fd(15)
seth(-85)
fd(18)
seth(0)
fd(95)
circle(6, 180)
seth(90)
fd(30)
seth(95)
fd(35)
fd(-30)
right(90)
fd(25)
left(80)
fd(6)
left(6)
fd(6)
left(12)
fd(20)
circle(20, 60)
fd(20)
end_fill()
penup()
seth(180)
fd(54)
seth(90)
fd(10)
pendown()
fillcolor("#FAFAD2")
begin_fill()
seth(-90)
fd(10)
seth(0)
fd(48)
seth(90)
fd(10)
end_fill()
seth(180)
penup()
fd(24)
pendown()
circle(-160, 13)
seth(-13)
circle(160, 13)
seth(0)
circle(160, 12)
penup()
seth(-90)
fd(12)
seth(180)
fd(3)
pendown()
fillcolor("white")
begin_fill()
seth(-100)
fd(30)
seth(135)
fd(40)
seth(-135)
fd(40)
seth(100)
fd(26)
end_fill()
penup()
seth(0)
fd(20)
seth(90)
fd(2)
pendown()
seth(0)
fd(41)
penup()
seth(0)
fd(40)
seth(-90)
fd(53)
pendown()
fillcolor("#FAFAD2")
begin_fill()
seth(-80)
fd(60)
seth(-30)
fd(5)
seth(-40)
fd(5)
seth(-50)
fd(5)
seth(-60)
fd(5)
seth(-80)
fd(5)
seth(-90)
fd(5)
seth(-95)
fd(5)
seth(-135)
fd(6)
seth(-138)
fd(6)
seth(-143)
fd(6)
circle(-15, 160)
seth(180)
circle(20, 20)
seth(95)
fd(80)
end_fill()
penup()
fd(-90)
seth(0)
fd(20)
pendown()
seth(-70)
fd(10)
fd(-10)
penup()
seth(0)
fd(8)
seth(-70)
pendown()
fd(7)
fd(-7)
penup()
seth(0)
fd(8)
seth(-70)
fd(-10)
pendown()
fd(13)
penup()
seth(180)
fd(165)
seth(90)
fd(82)
seth(-95)
fillcolor("#FAFAD2")
begin_fill()
pendown()
fd(80)
seth(-150)
circle(20, 190)
seth(145)
fd(10)
left(90)
fd(6)
fd(-14)
fd(8)
right(90)
fd(-7)
seth(45)
circle(20, 80)
seth(85)
fd(85)
end_fill()

penup()
seth(-90)
fd(35)
seth(0)
fd(3)
pendown()
fillcolor("#FAFAD2")
begin_fill()
seth(-105)
fd(10)
seth(-87)
fd(70)
seth(-90)
fd(70)
seth(-145)
fd(20)
circle(10, 160)
seth(0)
fd(50)
circle(5, 110)
fd(20)
seth(90)
fd(50)
seth(87)
fd(60)
circle(-6, 175)
fd(60)
seth(-90)
fd(50)
seth(-120)
fd(18)
circle(5, 130)
seth(0)
fd(50)
circle(10, 160)
fd(16)
seth(90)
fd(70)
seth(87)
fd(80)
end_fill()
penup()
seth(90)
fd(1)
fillcolor("#FF3E96")
begin_fill()
pendown()
seth(180)
fd(96)
seth(-105)
fd(10)
seth(-87)
fd(45)
seth(0)
fd(43)
seth(87)
fd(13)
circle(-6, 175)
seth(-90)
fd(15)
seth(0)
fd(40)
end_fill()
penup()
seth(-90)
fd(98)
seth(180)
fd(40)
pendown()
seth(-10)
fd(15)
seth(0)
fd(15)
seth(10)
fd(15)
penup()
seth(180)
fd(62)
pendown()
seth(-170)
fd(15)
seth(180)
fd(15)
seth(-190)
fd(15)
turtle.done()
