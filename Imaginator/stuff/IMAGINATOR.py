from ursina import *
from ursina.prefabs.cursor import Cursor

app = Ursina()






window.fullscreen=True

btnX= 0.2
btnY = 0.075

btnColor= rgb(0,0,0,60)
btnHcolor= rgb(0,0,0,80)



def Fullscreen_T():
	window.fullscreen=True

def Fullscreen_F():
	window.fullscreen=False

def FPS_T():
	window.fps_counter.enabled =True

def FPS_F():
	window.fps_counter.enabled =False

def Graphics_High():
	optGraphicsBTN2.text = 'Nope!!'
	optGraphicsBTN3.text = 'Low'

def Graphics_Low():
	optGraphicsBTN3.text = 'Nope!!'
	optGraphicsBTN2.text = 'High'






def NewGame():
	Message.y=0.41
	baseOptE.position=(0,5)
	optMenuP.position=(0,5)
	shopMenuP.position=(0,5)
	newGameEN.y=-5


def opt():
	newGameEN.x=-0.75
	optMenuP.position=(0,0)
	shopMenuP.position=(2,0)

	optionsGameBTN.scale= (0.26,0.075)
	optionsGameBTN.color=(0,0,0,50)

	shopGameBTN.scale= (0.2,0.075)
	shopGameBTN.color=btnColor

	#content
	baseOptE.position=(0,0)




def shop():
	newGameEN.x=-0.75
	optMenuP.position=(2,0)
	shopMenuP.position=(0,0)

	shopGameBTN.scale= (0.26,0.075)
	shopGameBTN.color=(0,0,0,50)

	optionsGameBTN.scale= (0.2,0.075)
	optionsGameBTN.color=btnColor

	#reset
	baseOptE.position=(2,0)


def quit_():

	newGameEN.x=0
	optMenuP.position=(2,0)
	shopMenuP.position=(2,0)

	optionsGameBTN.scale= (0.2,0.075)
	optionsGameBTN.color=btnColor

	shopGameBTN.scale= (0.2,0.075)
	shopGameBTN.color=btnColor

	baseOptE.position=(2,0)

	optGraphicsBTN3.text = 'Low'
	optGraphicsBTN2.text = 'High'



optMenuP= Entity(position=(2,0),parent=camera.ui)
shopMenuP= Entity(position=(2,0),parent=camera.ui)

UI = Entity(parent=camera.ui)



newGameEN = Entity(parent=camera.ui,position=(0,0))

newGameBTN = Button(parent=UI,x=0,scale=(btnX,btnY),text='New Game',color=btnColor,highlight_color=btnHcolor,highlight_scale=1,pressed_scale=1.07,pressed_color=btnHcolor)
newGameBTN.add_script(SmoothFollow(target=newGameEN,speed=5))
newGameBTN.on_click=NewGame

btnPosY1= newGameBTN.y
optionsGameBTN = Button(parent=UI,scale=(btnX,btnY),text='Options',color=btnColor,highlight_color=btnHcolor,highlight_scale=1,pressed_scale=1.07,pressed_color=btnHcolor,
			   y=0 )
optionsGameBTN.add_script(SmoothFollow(target=newGameBTN,speed=10,offset=[0,-1.55,0.75]))
optionsGameBTN.on_click=opt


btnPosY2= optionsGameBTN.y
shopGameBTN = Button(parent=UI,scale=(btnX,btnY),text='Shop',color=btnColor,highlight_color=btnHcolor,highlight_scale=1,pressed_scale=1.07,pressed_color=btnHcolor,
			   y= 0 )
shopGameBTN.add_script(SmoothFollow(target=optionsGameBTN,speed=10,offset=[0,-1.55,0.75]))
shopGameBTN.on_click=shop


btnPosY3= shopGameBTN.y
quitGameBTN = Button(parent=UI,scale=(0.15,0.07),text='Quit',color=btnColor,highlight_color=rgb(255,0,0,60),highlight_scale=1,pressed_scale=1.07,pressed_color=rgb(255,0,0,100),
			   y=0 )
quitGameBTN.add_script(SmoothFollow(target=shopGameBTN,speed=10,offset=[0,-1.75,0.75]))
quitGameBTN.on_click=quit



optMenu= Button(scale=(1,0.8),z=3,text='Options',text_scale=2,color=rgb(0,0,0,40),highlight_color=rgb(0,0,0,40),x=2,text_origin=(0,0.40),radius=.05)
optMenu.add_script(SmoothFollow(target=optMenuP,speed=6))

shopMenu= Button(scale=(1,0.8),z=3,text='..Coming Soon..',color=rgb(0,0,0,40),highlight_color=rgb(0,0,0,40),x=2,text_origin=(0,0.40),radius=.05)
shopMenu.add_script(SmoothFollow(target=shopMenuP,speed=6))



baseOptE = Entity(position=(2,0),z=-1,parent=camera.ui)

# DONE BUTTON
doneBTN = Button(scale=(0.05,0.05),radius=0.35, text='X',z=-1,color=rgb(255,0,0,100),x=2)
doneBTN.on_click = quit_
doneBTN.add_script(SmoothFollow(target=optMenuP,speed=6,offset=[6.5,5.75,-1]))


doneBTN2 = Button(scale=(0.05,0.05),radius=0.35, text='X',z=-1,color=rgb(255,0,0,100),x=2)
doneBTN2.on_click = quit_
doneBTN2.add_script(SmoothFollow(target=shopMenuP,speed=6,offset=[6.5,5.75,-1]))



	#OPTIONS MENU

	#1

optGraphicsBTN = Button(scale=(btnX,btnY),color=rgb(0,0,0,0),text='Graphics',x=2)
optGraphicsBTN.add_script(SmoothFollow(target=baseOptE,speed=6,offset=[-4.75,0.75,0]))


optGraphicsBTN2 = Button(scale=(btnX,btnY),color=rgb(255,255,255,30),text='High',x=2)
optGraphicsBTN2.add_script(SmoothFollow(target=optGraphicsBTN,speed=6,offset=[3.75,0,0]))
optGraphicsBTN2.on_click = Graphics_High

optGraphicsBTN3 = Button(scale=(btnX,btnY),color=rgb(255,255,255,10),text='Low',x=2)
optGraphicsBTN3.add_script(SmoothFollow(target=optGraphicsBTN2,speed=6,offset=[4.75,0,0]))
optGraphicsBTN3.on_click = Graphics_Low


	#2
optFullScreenBTN = Button(scale=(btnX,btnY),color=rgb(0,0,0,0),text='Fullscreen',x=2)
optFullScreenBTN.add_script(SmoothFollow(target=baseOptE,speed=5,offset=[-4.75,-2,0]))


optFSBTN2 = Button(scale=(btnX,btnY),color=rgb(255,255,255,10),text='True',x=2)
optFSBTN2.add_script(SmoothFollow(target=optFullScreenBTN,speed=5,offset=[3.75,0,0]))
optFSBTN2.on_click = Fullscreen_T

optFSBTN3 = Button(scale=(btnX,btnY),color=rgb(255,255,255,30),text='False',x=2)
optFSBTN3.add_script(SmoothFollow(target=optFSBTN2,speed=5,offset=[4.75,0,0]))
optFSBTN3.on_click = Fullscreen_F


	#3
optFpsBTN = Button(scale=(btnX,btnY),color=rgb(0,0,0,0),text='FPS Counter',x=2)
optFpsBTN.add_script(SmoothFollow(target=baseOptE,speed=6,offset=[-4.75,-4.75,0]))


optFPSBTN2 = Button(scale=(btnX,btnY),color=rgb(255,255,255,30),text='True',x=2)
optFPSBTN2.add_script(SmoothFollow(target=optFpsBTN,speed=6,offset=[3.75,0,0]))
optFPSBTN2.on_click = FPS_T

optFPSBTN3 = Button(scale=(btnX,btnY),color=rgb(255,255,255,10),text='False',x=2)
optFPSBTN3.add_script(SmoothFollow(target=optFPSBTN2,speed=6,offset=[4.75,0,0]))
optFPSBTN3.on_click = FPS_F





######## GAME CODE #######

def update():
	global OutputNO
	Result2.text=str(OutputNO)

def Card_1_Clicked():
	global OutputNO
	Card_1.color=rgb(0,70,0,80)
	OutputNO += 1
	print(OutputNO)

	Result1.visible=False
	Result2.visible=False

def Card_2_Clicked():
	global OutputNO
	Card_2.color=rgb(0,70,0,80)
	OutputNO += 2
	print(OutputNO)

	Result1.visible=False
	Result2.visible=False

def Card_4_Clicked():
	global OutputNO
	Card_4.color=rgb(0,70,0,80)
	OutputNO += 4
	print(OutputNO)

	Result1.visible=False
	Result2.visible=False

def Card_8_Clicked():
	global OutputNO
	Card_8.color=rgb(0,70,0,80)
	OutputNO += 8
	print(OutputNO)

	Result1.visible=False
	Result2.visible=False

def Card_16_Clicked():
	global OutputNO
	Card_16.color=rgb(0,70,0,80)
	OutputNO += 16
	print(OutputNO)

	Result1.visible=False
	Result2.visible=False

def Card_32_Clicked():
	global OutputNO
	Card_32.color=rgb(0,70,0,80)
	OutputNO += 32
	print(OutputNO)

	Result1.visible=False
	Result2.visible=False

def reset_cards():
	global OutputNO
	OutputNO = 0
	Card_1.color=rgb(0,0,0,40)
	Card_2.color=rgb(0,0,0,40)
	Card_4.color=rgb(0,0,0,40)
	Card_8.color=rgb(0,0,0,40)
	Card_16.color=rgb(0,0,0,40)
	Card_32.color=rgb(0,0,0,40)
	print(OutputNO)
	Result1.visible=False
	Result2.visible=False

def compilee():
	global OutputNO
	Message.y=-5
	Result1.visible=True
	Result2.visible=True
	Result2.text=OutputNO

	if OutputNO == 0:
		Result1.text='....Well you selected NOTHING so....'



OutputNO = 0
## CARDS

Card_1= Button(icon='Cards/1.png',scale=(0.3,0.4),z=100,radius=.5 )#x=-0.4,y=0.15
Card_2= Button(icon='Cards/2.png',scale=(0.3,0.4),z=100,radius=.5 )#, x = 0,y=0.15
Card_4= Button(icon='Cards/4.png',scale=(0.3,0.4),z=100,radius=.5 )#,x= 0.4,y=0.15

Card_8= Button(icon='Cards/8.png',scale=(0.3,0.4),z=100,radius=.5 )#,x=-0.4,y=-0.26
Card_16=Button(icon='Cards/16.png',scale=(0.3,0.4),z=100,radius=.5)#, x = 0,y=-0.26
Card_32=Button(icon='Cards/32.png',scale=(0.3,0.4),z=100,radius=.5)#,x= 0.4,y=-0.26


## TEXT MESSAGE
Message= Button(scale=(1.2,0.1),z=100,text='....Imagine a number BETWEEN 1-63....Pick all cards which contains the number you Imagined....',color=rgb(0,0,0,80),radius=.5 ,x=0,y=-5)
Result1= Button(scale=(1.2,0.1),z=100,visible=False,text='....I flew into your Imagination and found that you chose the number....',color=rgb(0,0,0,100),radius=.5 ,x=0,y=0.21)
Result2= Button(scale=(0.15,0.1),z=100,visible=False,text=str(OutputNO),color=rgb(0,0,0,80),text_color=color.azure,radius=.4 ,x=0,y=0.05)



## CARDS SCRIPT
Card_1.add_script(SmoothFollow(target=Message,speed=4,  offset=[-8,-5.3,0]))
Card_2.add_script(SmoothFollow(target=Message,speed=5,  offset=[00,-5.3,0]))
Card_4.add_script(SmoothFollow(target=Message,speed=4,  offset=[ 8,-5.3,0]))
Card_8.add_script(SmoothFollow( target=Message,speed=3,offset=[-8,-13.7,0]))
Card_16.add_script(SmoothFollow(target=Message,speed=4,offset=[00,-13.7,0]))
Card_32.add_script(SmoothFollow(target=Message,speed=3,offset=[ 8,-13.7,0]))

## CARDS.ON_CLICK
Card_1.on_click= Card_1_Clicked
Card_2.on_click= Card_2_Clicked
Card_4.on_click= Card_4_Clicked
Card_8.on_click= Card_8_Clicked
Card_16.on_click=Card_16_Clicked
Card_32.on_click=Card_32_Clicked

### UTILITY BUTTONS

rstBTN = Button(scale=(0.15,0.1),radius=0.15, text='Reset',z=100,color=rgb(255,0,0,100))
rstBTN.on_click = reset_cards
rstBTN.add_script(SmoothFollow(target=Message,speed=2,offset=[-14,-14.5,0])) 


compileBTN = Button(scale=(0.15,0.1),radius=0.15, text='Done!',z=100,color=rgb(0,200,0,100))
compileBTN.on_click = compilee
compileBTN.add_script(SmoothFollow(target=Message,speed=2,offset=[14,-14.5,0])) 


app.run()