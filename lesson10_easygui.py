import easygui as g
import sys
while 1:
    g.msgbox('welcome to the  minigame')
    strMsg='what do you want to know in the future'
    strTitle='fortune teller'
    strChoice=['Life','Money','Family','Disaster']
    choice=g.choicebox(strMsg,strTitle,strChoice)
    g.msgbox('Your choice is:'+str(choice),'result')

    strMsg='Do you want reload the game'
    title='reload game'

    if g.ccbox(strMsg,title):
        pass
    else:
        sys.exit(0)



