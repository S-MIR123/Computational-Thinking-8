###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
q1 = codesters.Square(100, 100, 200, 'black')
q2 = codesters.Square(-100, 100, 200, 'red')
q3 = codesters.Square(-100, -100, 200, 'black')
q4 = codesters.Square(100, -100, 200, 'red')
stage.set_background("winter")
s1 = mySprite = codesters.Sprite("basketball.png", -100, 100)
s2 = mySprite2 = codesters.Sprite("cardinal", 105, 100)
s1.set_size(0.3)
s3 = mySprite = codesters.Sprite("cat.png", -100, -100)
s3.set_size(0.5)
s4 = mySprite = codesters.Sprite("music.png", 100, -100)
s4.set_size(0.5)
message1 = codesters.Text("This is Samir Abduro", 0, 220, "red")
message2 = codesters.Text("Dont let success get to your head and ", 0, -215, "black")
message3 = codesters.Text("dont let failure get to your heart.", 0, -230, "black")
