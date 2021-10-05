
#импорт библиотек
import pygame as pg
import numpy as np



#блок описания функций

#функция рисования сегмента облака
def oblako(x,y, square,co):
	'''
	Функция рисует сегмент облака
	f - плоскость на которой будет нарисован объект
	x - координаты объекта рисования в плоскости по оси X
	y - координаты объекта рисования в плоскости по оси Y
	co - цвет сегмента облака
	'''
	pg.draw.circle(square, co, (x,y), 15, 0)
	pg.draw.circle(square, bl, (x,y), 15, 1)
#функция сбора сегментов облако в одно облако
def clouds(f,x,y,a,b,co):
	'''
	Функция рисует облако
	f - плоскость на которой будет нарисован объект
	x - координаты объекта рисования в плоскости по оси X
	y - координаты объекта рисования в плоскости по оси Y
	a - масштаб облака в плоскости по оси X
	b - масштаб облака в плоскости по оси Y
	co - цвет облака
	'''
	kusok_neba = pg.Surface((200,100),pg.SRCALPHA)

	for i in range(2):
		oblako(10 + 20 * (i + 1),15,kusok_neba,co)
		oblako(-5 + 20 * (i + 1),30,kusok_neba,co)

	oblako(-5 + 20 * 3,30,kusok_neba,co)
	oblako(10 + 20 * 3,15,kusok_neba,co)
	oblako(-5 + 20 * 4,30,kusok_neba,co)
	kusok_neba = pg.transform.smoothscale(kusok_neba, (int(200 * a), int(100 * b)))
	f.blit(kusok_neba, (x,y))

#функция рисования солнца
def sun(f,x,y,a,b,cs):
	'''
	Функция рисует солнцо
	f - плоскость на которой будет нарисован объект
	x - координаты объекта рисования в плоскости по оси X
	y - координаты объекта рисования в плоскости по оси Y
	a - масштаб солнца в плоскости по оси X
	b - масштаб солнца в плоскости по оси Y
	cs - цвет солнца
	'''
	solnce = pg.Surface((120,120),pg.SRCALPHA)
	pg.draw.circle(solnce, cs, (60, 60), 50, 0)
	for i in range(60):
		pg.draw.polygon(solnce, cs, [(int(60 + 60 * np.cos(np.pi / 24 * i)),int(60 - 60 * np.sin(np.pi / 24 * i))),
											  (int(60 + 50 * np.cos(np.pi / 24 * i + np.pi / 48)),int(60 - 50 * np.sin(np.pi / 24 * i + np.pi / 48))),
											  (int(60 + 50 * np.cos(np.pi / 24 * i - np.pi / 48)),int(60 - 50 * np.sin(np.pi / 24 * i - np.pi / 48)))])

	solnce = pg.transform.smoothscale(solnce, (int(120 * a), int(120 * b)))
	f.blit(solnce,(x,y))

#функция рисования фона с песком и волнами
def fon(f,cp,cw,cn):
	'''
	Функция рисует фон
	f - плоскость на которой будет нарисован объект
	cp - цвет песка
	cw - цвет воды
	cn - цвет неба
	'''
	pg.draw.rect(f, cn, (0,0,600,180), 0)
	pg.draw.rect(f, cw, (0,180,600,100), 0)
	pg.draw.rect(f, cp, (0,280,600,120), 0)
	for i in range(5):
		pg.draw.circle(f, cp, (30 + 120 * i,320), 50)
		pg.draw.circle(f, cw, (90 + 120 * i,240), 50)

#функция рисования зонта
def umbrella(f,x,y,a,b,cz):
	'''
	Функция рисует зонт
	f - плоскость на которой будет нарисован объект
	x - координаты объекта рисования в плоскости по оси X
	y - координаты объекта рисования в плоскости по оси Y
	a - масштаб зонта в плоскости по оси X
	b - масштаб зонта в плоскости по оси Y
	cz - цвет зонта
	'''
	zont = pg.Surface((125,125),pg.SRCALPHA)
	pg.draw.polygon(zont, cz, [(60,0), (65,0), (125,30), (0,30)], 0)
	pg.draw.rect(zont, cz, (60, 0, 5, 125))

	for i in range(4):
		pg.draw.line(zont, bl, (60,0), (0 + 15 * i,30), 1)

	for i in range(4):
		pg.draw.line(zont, bl, (65,0), (65 + 15 * (i + 1),30), 1)

	zont = pg.transform.smoothscale(zont, (int(125 * a), int(125 * b)))
	f.blit(zont, (x,y))

#функция рисования корабля
def best_ship(f,x,y,a,b,ck,cp,ce):
	'''
	Функция рисует корабль
	f - плоскость на которой будет нарисован объект
	x - координаты объекта рисования в плоскости по оси X
	y - координаты объекта рисования в плоскости по оси Y
	a - масштаб корабля в плоскости по оси X
	b - масштаб корабля в плоскости по оси Y
	ck - цвет корабля
	cp - цвет паруса
	ce - цвет иллюминатора
	'''
	ship = pg.Surface((300,200),pg.SRCALPHA)
	pg.draw.circle(ship, ck, (30,130), 30, 0)
	pg.draw.rect(ship, (0,0,0,0), (0,100, 60, 30))
	pg.draw.rect(ship, ck, (30,130, 150, 30))
	pg.draw.polygon(ship, ck, [(180,130), (180, 159), (250,130)], 0)
	pg.draw.line(ship, bl, (30,130), (30, 160))
	pg.draw.line(ship, bl, (180,130), (180, 160))
	pg.draw.circle(ship, ce, (195,142), 9, 0)
	pg.draw.circle(ship, bl, (195,142), 9, 3)
	pg.draw.rect(ship, bl, (90, 30, 5, 100), 0)
	pg.draw.polygon(ship, (190,216,153), [(95,30), (110,80), (95,130), (155,80)])
	pg.draw.polygon(ship, bl, [(95,30), (110,80), (95,130), (155,80)], 1)
	pg.draw.line(ship, bl, (110,80), (155, 80), 1)
	ship = pg.transform.smoothscale(ship, (int(300 * a), int(200 * b)))
	f.blit(ship, (x,y))
	
#блок инициализации параметров для отрисовки
pg.init()
FPS = 30
screen = pg.display.set_mode((600, 400), pg.SRCALPHA)
TargetSuf = pg.Surface((600,400), pg.SRCALPHA)

bl = (0,0,0)
wh = (255,255,255)

#блок вызова функций для прорисовки
fon(TargetSuf,(238,246,12,255),(68,35,223,255),(161,245,255,255))
clouds(TargetSuf,100,40,1,1,wh)
clouds(TargetSuf,220,20,1.7,1.7,wh)
clouds(TargetSuf,40,100,1.7,1,wh)
sun(TargetSuf,470,30,1,1, (255,255,0))
umbrella(TargetSuf,30,250,1,1,(244,81,81,200))
umbrella(TargetSuf,180,270,0.4,0.7,(244,81,81,200))
best_ship(TargetSuf,300,80,1,1,(186,80,5,255),(222,213,153,255),(255,255,255,255))
best_ship(TargetSuf,150,130,0.5,0.5,(186,80,5,255),(222,213,153,255),(255,255,255,255))
#сбор всего и вся
screen.blit(TargetSuf,(0,0))
#фигня
pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()