#finalproject.pyw
#July 29, 2014
#By Emanuel Guerrero
#This program uses graphics to create a graphical interface that enables the user to play a game

from graphics import *

#function definitions
#x1,y1 is the bottom left
#x2,y2 is the top right


def MAINGAME(win):
    #Declare variables
    #int: score = 0
    score = 0
    #str: entName
    Name = ""

    #bool isOver
    isOver = False

    #create and draw Question 1
    question1txt = CreateText(win, "What Planet are the Transformers from?", 5,9, 12, color_rgb(255,255,0), "courier", "bold")
    question1txt.draw(win)
    #create and draw image
    img1 = Image(Point(5,6.5), "transformers.gif")
    img1.draw(win)
    #create and draw Question 1 answers
    q1rect = Rectangle(Point(1,3.5), Point(4,4.5))
    q1rect.setFill(color_rgb(255,255,0))
    q1rect.draw(win)
    q1Atxt = Text(Point(2.5,4), "A)Galvontron")
    q1Atxt.setTextColor("black")
    q1Atxt.draw(win)
    q1rect2 = Rectangle(Point(1,2.5), Point(4,3.5))
    q1rect2.setFill(color_rgb(255,255,0))
    q1rect2.draw(win)
    q1Btxt = Text(Point(2.5,3), "B)Cybertron")
    q1Btxt.setTextColor("black")
    q1Btxt.draw(win)
    q1rect3 = Rectangle(Point(1,1.5), Point(4,2.5))
    q1rect3.setFill(color_rgb(255,255,0))
    q1rect3.draw(win)
    q1Ctxt = Text(Point(2.5,2), "C)Galerfray")
    q1Ctxt.setTextColor("black")
    q1Ctxt.draw(win)
    q1rect4 = Rectangle(Point(1,0.5), Point(4,1.5))
    q1rect4.setFill(color_rgb(255,255,0))
    q1rect4.draw(win)
    q1Dtxt = Text(Point(2.5,1), "D)Hoth")
    q1Dtxt.setTextColor("black")
    q1Dtxt.draw(win)
    #create CORRECT and WRONG Indicators
    q1rect5 = Rectangle(Point(5,3.5), Point(7,4.5))
    q1rect5.setFill(color_rgb(255,255,0))
    q1CORRECT = Text(Point(6,4), "CORRECT")
    q1CORRECT.setTextColor("black")
    q1rect6 = Rectangle(Point(7,3.5), Point(9,4.5))
    q1rect6.setFill(color_rgb(255,255,0))
    q1WRONG = Text(Point(8,4), "WRONG")
    q1WRONG.setTextColor("black")
    #create scorebox
    q1rect7 = Rectangle(Point(5,1.9), Point(7,2.9))
    q1rect7.setFill(color_rgb(255,255,0))
    #create NEXT QUESTION button
    q1rect8 = Rectangle(Point(7.2,1), Point(9.7,2))
    q1rect8.setFill(color_rgb(255,255,0))
    q1NEXT = Text(Point(8.5,1.5), "NEXT QUESTION")
    q1NEXT.setTextColor("black")
    #Determine region for user to click on CORRECT answer
    isOver = False
    p1 = win.getMouse()
    if p1.getX() >= 1   and p1.getY() >= 2.5  and p1.getX() <= 4 and p1.getY() <= 3.5 :
        q1rect5.draw(win)
        q1CORRECT.draw(win)
        score += 100
        q1score = Text(Point(5.8,2.5), score)
        q1score.setTextColor("black")
        q1rect7.draw(win)
        q1score.draw(win)
        q1rect8.draw(win)
        q1NEXT.draw(win)
    else:
        q1rect6.draw(win)
        q1WRONG.draw(win)
        score += 0
        q1score = Text(Point(5.8,2.5), score)
        q1score.setTextColor("black")
        q1rect7.draw(win)
        q1score.draw(win)
        q1rect8.draw(win)
        q1NEXT.draw(win)
    #Determine region for user to click on NEXT QUESTION to continue with game
    p1 = win.getMouse()
    if p1.getX() >= 7.2 and p1.getY() >= 1 and p1.getX() <= 9.7 and p1.getY() <= 2 :
        imgBackground1 = Image(Point(5,5), "blackBackground.gif")
        imgBackground1.draw(win)

    #create and draw Question 2 with same format
    question2txt = CreateText(win, "Who was Spiderman's first villian?", 5,9, 12, color_rgb(255,255,0), "courier", "bold")
    question2txt.draw(win)
    #create and draw image
    img2 = Image(Point(5,6.5), "sinster6spiderman.gif")
    img2.draw(win)
    #create and draw Question 2 answers
    q2rect = Rectangle(Point(1,3.5), Point(4,4.5))
    q2rect.setFill(color_rgb(255,255,0))
    q2rect.draw(win)
    q2Atxt = Text(Point(2.5,4), "A)Green Goblin")
    q2Atxt.setTextColor("black")
    q2Atxt.draw(win)
    q2rect2 = Rectangle(Point(1,2.5), Point(4,3.5))
    q2rect2.setFill(color_rgb(255,255,0))
    q2rect2.draw(win)
    q2Btxt = Text(Point(2.5,3), "B)Doc Ock")
    q2Btxt.setTextColor("black")
    q2Btxt.draw(win)
    q2rect3 = Rectangle(Point(1,1.5), Point(4,2.5))
    q2rect3.setFill(color_rgb(255,255,0))
    q2rect3.draw(win)
    q2Ctxt = Text(Point(2.5,2), "C)Venom")
    q2Ctxt.setTextColor("black")
    q2Ctxt.draw(win)
    q2rect4 = Rectangle(Point(1,0.5), Point(4,1.5))
    q2rect4.setFill(color_rgb(255,255,0))
    q2rect4.draw(win)
    q2Dtxt = Text(Point(2.5,1), "D)Vulture")
    q2Dtxt.setTextColor("black")
    q2Dtxt.draw(win)
    #create CORRECT and WRONG Indicators
    q2rect5 = Rectangle(Point(5,3.5), Point(7,4.5))
    q2rect5.setFill(color_rgb(255,255,0))
    q2CORRECT = Text(Point(6,4), "CORRECT")
    q2CORRECT.setTextColor("black")
    q2rect6 = Rectangle(Point(7,3.5), Point(9,4.5))
    q2rect6.setFill(color_rgb(255,255,0))
    q2WRONG = Text(Point(8,4), "WRONG")
    q2WRONG.setTextColor("black")
    #create scorebox
    q2rect7 = Rectangle(Point(5,1.9), Point(7,2.9))
    q2rect7.setFill(color_rgb(255,255,0))
    #create NEXT QUESTION button
    q2rect8 = Rectangle(Point(7.2,1), Point(9.7,2))
    q2rect8.setFill(color_rgb(255,255,0))
    q2NEXT = Text(Point(8.5,1.5), "NEXT QUESTION")
    q2NEXT.setTextColor("black")
    #Determine region for user to click on CORRECT answer
    isOver = False
    p1 = win.getMouse()
    if p1.getX() >= 1   and p1.getY() >= 3.5  and p1.getX() <= 4 and p1.getY() <= 4.5 :
        q2rect5.draw(win)
        q2CORRECT.draw(win)
        score += 200
        q2score = Text(Point(5.8,2.5), score)
        q2score.setTextColor("black")
        q2rect7.draw(win)
        q2score.draw(win)
        q2rect8.draw(win)
        q2NEXT.draw(win)
    elif p1.getX() >= 1 and p1.getY() >= 2.5  and p1.getX() <= 4 and p1.getY() <= 3.5 or p1.getX() >= 1   and p1.getY() >= 1.5  and p1.getX() <= 4 and p1.getY() <= 2.5 or p1.getX() >= 1   and p1.getY() >= 0.5  and p1.getX() <= 4 and p1.getY() <= 1.5:
        q2rect6.draw(win)
        q2WRONG.draw(win)
        score += 0
        q2score = Text(Point(5.8,2.5), score)
        q2score.setTextColor("black")
        q2rect7.draw(win)
        q2score.draw(win)
        q2rect8.draw(win)
        q2NEXT.draw(win)
    else:
        x = 10
    #Determine region for user to click on NEXT QUESTION to continue with game
    isOver = False
    p1 = win.getMouse()
    if p1.getX() >= 7.2 and p1.getY() >= 1 and p1.getX() <= 9.7 and p1.getY() <= 2 :
        imgBackground2 = Image(Point(5,5), "blackBackground.gif")
        imgBackground2.draw(win)

   #create and draw Question 3 with same format
    question3txt = CreateText(win, "Name that starship", 5,9, 12, color_rgb(255,255,0), "courier", "bold")
    question3txt.draw(win)
    #create and draw image
    img3 = Image(Point(5,6.5), "slave1.gif")
    img3.draw(win)
    #create and draw Question 3 answers
    q3rect = Rectangle(Point(1,3.5), Point(4,4.5))
    q3rect.setFill(color_rgb(255,255,0))
    q3rect.draw(win)
    q3Atxt = Text(Point(2.5,4), "A)The Ark")
    q3Atxt.setTextColor("black")
    q3Atxt.draw(win)
    q3rect2 = Rectangle(Point(1,2.5), Point(4,3.5))
    q3rect2.setFill(color_rgb(255,255,0))
    q3rect2.draw(win)
    q3Btxt = Text(Point(2.5,3), "B)Slave 1")
    q3Btxt.setTextColor("black")
    q3Btxt.draw(win)
    q3rect3 = Rectangle(Point(1,1.5), Point(4,2.5))
    q3rect3.setFill(color_rgb(255,255,0))
    q3rect3.draw(win)
    q3Ctxt = Text(Point(2.5,2), "C)Star Destroyer")
    q3Ctxt.setTextColor("black")
    q3Ctxt.draw(win)
    q3rect4 = Rectangle(Point(1,0.5), Point(4,1.5))
    q3rect4.setFill(color_rgb(255,255,0))
    q3rect4.draw(win)
    q3Dtxt = Text(Point(2.5,1), "D)Millennium Falcon")
    q3Dtxt.setTextColor("black")
    q3Dtxt.draw(win)
    #create CORRECT and WRONG Indicators
    q3rect5 = Rectangle(Point(5,3.5), Point(7,4.5))
    q3rect5.setFill(color_rgb(255,255,0))
    q3CORRECT = Text(Point(6,4), "CORRECT")
    q3CORRECT.setTextColor("black")
    q3rect6 = Rectangle(Point(7,3.5), Point(9,4.5))
    q3rect6.setFill(color_rgb(255,255,0))
    q3WRONG = Text(Point(8,4), "WRONG")
    q3WRONG.setTextColor("black")
    #create scorebox
    q3rect7 = Rectangle(Point(5,1.9), Point(7,2.9))
    q3rect7.setFill(color_rgb(255,255,0))
    #create NEXT QUESTION button
    q3rect8 = Rectangle(Point(7.2,1), Point(9.7,2))
    q3rect8.setFill(color_rgb(255,255,0))
    q3NEXT = Text(Point(8.5,1.5), "NEXT QUESTION")
    q3NEXT.setTextColor("black")
    #Determine region for user to click on CORRECT answer
    isOver = False
    p1 = win.getMouse()
    if p1.getX() >= 1   and p1.getY() >= 2.5  and p1.getX() <= 4 and p1.getY() <= 3.5 :
        q3rect5.draw(win)
        q3CORRECT.draw(win)
        score += 500
        q3score = Text(Point(5.8,2.5), score)
        q3score.setTextColor("black")
        q3rect7.draw(win)
        q3score.draw(win)
        q3rect8.draw(win)
        q3NEXT.draw(win)
    else:
        q3rect6.draw(win)
        q3WRONG.draw(win)
        score += 0
        q3score = Text(Point(5.8,2.5), score)
        q3score.setTextColor("black")
        q3rect7.draw(win)
        q3score.draw(win)
        q3rect8.draw(win)
        q3NEXT.draw(win)
    #Determine region for user to click on NEXT QUESTION to continue with game
    isOver = False
    p1 = win.getMouse()
    if p1.getX() >= 7.2 and p1.getY() >= 1 and p1.getX() <= 9.7 and p1.getY() <= 2 :
        imgBackground3 = Image(Point(5,5), "blackBackground.gif")
        imgBackground3.draw(win)

   #create and draw Question 4 with same format
    question4txt = CreateText(win, "How many times can the Doctor regenerate?", 5,9, 12, color_rgb(255,255,0), "courier", "bold")
    question4txt.draw(win)
    #create and draw image
    img4 = Image(Point(5,6.5), "doctorwho.gif")
    img4.draw(win)
    #create and draw Question 4 answers
    q4rect = Rectangle(Point(1,3.5), Point(4,4.5))
    q4rect.setFill(color_rgb(255,255,0))
    q4rect.draw(win)
    q4Atxt = Text(Point(2.5,4), "A)10")
    q4Atxt.setTextColor("black")
    q4Atxt.draw(win)
    q4rect2 = Rectangle(Point(1,2.5), Point(4,3.5))
    q4rect2.setFill(color_rgb(255,255,0))
    q4rect2.draw(win)
    q4Btxt = Text(Point(2.5,3), "B)4")
    q4Btxt.setTextColor("black")
    q4Btxt.draw(win)
    q4rect3 = Rectangle(Point(1,1.5), Point(4,2.5))
    q4rect3.setFill(color_rgb(255,255,0))
    q4rect3.draw(win)
    q4Ctxt = Text(Point(2.5,2), "C)12")
    q4Ctxt.setTextColor("black")
    q4Ctxt.draw(win)
    q4rect4 = Rectangle(Point(1,0.5), Point(4,1.5))
    q4rect4.setFill(color_rgb(255,255,0))
    q4rect4.draw(win)
    q4Dtxt = Text(Point(2.5,1), "D)infinite")
    q4Dtxt.setTextColor("black")
    q4Dtxt.draw(win)
    #create CORRECT and WRONG Indicators
    q4rect5 = Rectangle(Point(5,3.5), Point(7,4.5))
    q4rect5.setFill(color_rgb(255,255,0))
    q4CORRECT = Text(Point(6,4), "CORRECT")
    q4CORRECT.setTextColor("black")
    q4rect6 = Rectangle(Point(7,3.5), Point(9,4.5))
    q4rect6.setFill(color_rgb(255,255,0))
    q4WRONG = Text(Point(8,4), "WRONG")
    q4WRONG.setTextColor("black")
    #create scorebox
    q4rect7 = Rectangle(Point(5,1.9), Point(7,2.9))
    q4rect7.setFill(color_rgb(255,255,0))
    #create NEXT QUESTION button
    q4rect8 = Rectangle(Point(7.2,1), Point(9.7,2))
    q4rect8.setFill(color_rgb(255,255,0))
    q4NEXT = Text(Point(8.5,1.5), "NEXT QUESTION")
    q4NEXT.setTextColor("black")
    #Determine region for user to click on CORRECT answer
    isOver = False
    p1 = win.getMouse()
    if p1.getX() >= 1   and p1.getY() >= 1.5  and p1.getX() <= 4 and p1.getY() <= 2.5 :
        q4rect5.draw(win)
        q4CORRECT.draw(win)
        score += 1000
        q4score = Text(Point(5.8,2.5), score)
        q4score.setTextColor("black")
        q4rect7.draw(win)
        q4score.draw(win)
        q4rect8.draw(win)
        q4NEXT.draw(win)
    else:
        q4rect6.draw(win)
        q4WRONG.draw(win)
        score += 0
        q4score = Text(Point(5.8,2.5), score)
        q4score.setTextColor("black")
        q4rect7.draw(win)
        q4score.draw(win)
        q4rect8.draw(win)
        q4NEXT.draw(win)
    #Determine region for user to click on NEXT QUESTION to continue with game
    isOver = False
    p1 = win.getMouse()
    if p1.getX() >= 7.2 and p1.getY() >= 1 and p1.getX() <= 9.7 and p1.getY() <= 2 :
        imgBackground4 = Image(Point(5,5), "blackBackground.gif")
        imgBackground4.draw(win)

   #create and draw Question 5 with same format
    question5txt = CreateText(win, "What is this called?", 5,9, 12, color_rgb(255,255,0), "courier", "bold")
    question5txt.draw(win)
    #create and draw image
    img5 = Image(Point(5,6.8), "infinitygauntlet.gif")
    img5.draw(win)
    #create and draw Question 4 answers
    q5rect = Rectangle(Point(1,3.5), Point(4,4.5))
    q5rect.setFill(color_rgb(255,255,0))
    q5rect.draw(win)
    q5Atxt = Text(Point(2.5,4), "A)A Thanos")
    q5Atxt.setTextColor("black")
    q5Atxt.draw(win)
    q5rect2 = Rectangle(Point(1,2.5), Point(4,3.5))
    q5rect2.setFill(color_rgb(255,255,0))
    q5rect2.draw(win)
    q5Btxt = Text(Point(2.5,3), "B)Warhammer")
    q5Btxt.setTextColor("black")
    q5Btxt.draw(win)
    q5rect3 = Rectangle(Point(1,1.5), Point(4,2.5))
    q5rect3.setFill(color_rgb(255,255,0))
    q5rect3.draw(win)
    q5Ctxt = Text(Point(2.5,2), "C)Power Arm")
    q5Ctxt.setTextColor("black")
    q5Ctxt.draw(win)
    q5rect4 = Rectangle(Point(1,0.5), Point(4,1.5))
    q5rect4.setFill(color_rgb(255,255,0))
    q5rect4.draw(win)
    q5Dtxt = Text(Point(2.5,1), "D)infinity gauntlet")
    q5Dtxt.setTextColor("black")
    q5Dtxt.draw(win)
    #create CORRECT and WRONG Indicators
    q5rect5 = Rectangle(Point(5,3.5), Point(7,4.5))
    q5rect5.setFill(color_rgb(255,255,0))
    q5CORRECT = Text(Point(6,4), "CORRECT")
    q5CORRECT.setTextColor("black")
    q5rect6 = Rectangle(Point(7,3.5), Point(9,4.5))
    q5rect6.setFill(color_rgb(255,255,0))
    q5WRONG = Text(Point(8,4), "WRONG")
    q5WRONG.setTextColor("black")
    #create scorebox
    q5rect7 = Rectangle(Point(5,1.9), Point(7,2.9))
    q5rect7.setFill(color_rgb(255,255,0))
    #create NEXT QUESTION button
    q5rect8 = Rectangle(Point(7.2,1), Point(9.7,2))
    q5rect8.setFill(color_rgb(255,255,0))
    q5NEXT = Text(Point(8.5,1.5), "NEXT QUESTION")
    q5NEXT.setTextColor("black")
    #Determine region for user to click on CORRECT answer
    isOver = False
    p1 = win.getMouse()
    if p1.getX() >= 1   and p1.getY() >= 0.5  and p1.getX() <= 4 and p1.getY() <= 1.5 :
        q5rect5.draw(win)
        q5CORRECT.draw(win)
        score += 2000
        q5score = Text(Point(5.8,2.5), score)
        q5score.setTextColor("black")
        q5rect7.draw(win)
        q5score.draw(win)
        q5rect8.draw(win)
        q5NEXT.draw(win)
    else:
        q5rect6.draw(win)
        q5WRONG.draw(win)
        score += 0
        q5score = Text(Point(5.8,2.5), score)
        q5score.setTextColor("black")
        q5rect7.draw(win)
        q5score.draw(win)
        q5rect8.draw(win)
        q5NEXT.draw(win)
    #Determine region for user to click on NEXT QUESTION to continue with game
    isOver = False
    p1 = win.getMouse()
    if p1.getX() >= 7.2 and p1.getY() >= 1 and p1.getX() <= 9.7 and p1.getY() <= 2 :
        imgBackground5 = Image(Point(5,5), "blackBackground.gif")
        imgBackground5.draw(win)

    #Display total score
    txtTotalscore = CreateText(win, "Your score for today is:", 5,9, 12, color_rgb(255,255,0), "courier", "bold")
    txtTotalscore.draw(win)
    txtScore = CreateText(win, score, 5,8.8, 12, color_rgb(255,255,0), "courier", "bold")
    txtScore.draw(win)

    #Determine if user has highscore. If not prompt to play again.
    if score > 1200:
       #create and draw enter name prompt
       txthighscore = CreateText(win, "You Have A Highscore!!!", 5,7.7, 12, color_rgb(255,255,0), "courier", "bold")
       txthighscore.draw(win)
       #insert image
       winnersimg = Image(Point(5,5.7), "mariokart.gif")
       winnersimg.draw(win)
       #create and draw name prompt
       txtName = CreateText(win, "Please enter your name: ", 3,3.5, 12, color_rgb(255,255,0), "courier", "bold")
       txtName.draw(win)
       #create and draw name entry box
       entName = Entry(Point(6.9,3.6), 15)
       entName.setFill(color_rgb(255,255,0))
       #give a default value for entry box
       entName.setText("")
       entName.draw(win)
       
       #create button to enter data
       enterrect = Rectangle(Point(3,2.3), Point(4,2.9))
       enterrect.setFill(color_rgb(255,255,0))
       enterrect.draw(win)
       txtENTER = Text(Point(3.5,2.5), "ENTER")
       txtENTER.setTextColor("black")
       txtENTER.draw(win)
       isOver = False
       p1 = win.getMouse()
       if p1.getX() >= 3 and p1.getY() >= 2.3 and p1.getX() <= 4 and p1.getY() <= 2.9 :
           entName.undraw()
           Name = entName.getText()
           #convert score and entName to strings to write to file
           score = str(score)
           #write the user's name and score to a text file called highscore
           outfile = open("highscore.txt", "a")
           #Write to the file
           #Make sure to end every line with a newline character
           outfile.write("*******HIGHSCORES*******\n\n")
           outfile.write(Name)
           outfile.write("\t")
           outfile.write(score)
           outfile.write("\n")
           #Close the file
           outfile.close()
           #Draw Background to nextscreen
           imgBackground6 = Image(Point(5,5), "blackBackground.gif")
           imgBackground6.draw(win)
    else:
        txtfinish = CreateText(win, "Thats All Folks!!!", 5,5, 12, color_rgb(255,255,0), "courier", "bold")
        txtfinish.draw(win)
        sleep(3)
        imgBackground6 = Image(Point(5,5), "blackBackground.gif")
        imgBackground6.draw(win)

    #Create and draw screen to prompt player to player again.
    txtPlayagain = CreateText(win, "Do you want to play again?", 5,9, 12, color_rgb(255,255,0), "courier", "bold")
    txtPlayagain.draw(win)
    promptimg = Image(Point(5,5), "bowsersymbol.gif")
    promptimg.draw(win)
    Yesrect = Rectangle(Point(2,2), Point(3,3))
    Yesrect.setFill(color_rgb(255,255,0))
    Yesrect.draw(win)
    YES = Text(Point(2.5,2.5), "YES")
    YES.setTextColor("black")
    YES.draw(win)
    Norect = Rectangle(Point(7,2), Point(8,3))
    Norect.setFill(color_rgb(255,255,0))
    Norect.draw(win)
    NO = Text(Point(7.5,2.5), "NO")
    NO.setTextColor("black")
    NO.draw(win)

    #Determine region for user to play again or to go to mainmenu
    isOver = False
    p1 = win.getMouse()
    if p1.getX() >= 2 and p1.getY() >= 2 and p1.getX() <= 3 and p1.getY() <= 3 :
        imgBackground7 = Image(Point(5,5), "blackBackground.gif")
        imgBackground7.draw(win)
        MAINGAME(win)
    else:
        imgBackground7 = Image(Point(5,5), "blackBackground.gif")
        imgBackground7.draw(win)
        mainmenu(win)
#######################################################################################################################################################    

def CreateText(win, text, x, y, size, color, font, style):
    tempText = Text(Point(x,y), text)
    tempText.setSize(size)
    tempText.setTextColor(color)
    tempText.setFace(font)
    tempText.setStyle(style)
    return tempText

#######################################################################################################################################################

def mainmenu(win):
    #bool isOver
    isOver = False
    
   #create and draw title
    txtTitle = CreateText(win, "WHO WANTS TO BE A MILLIONARE", 5,9, 14, color_rgb(255,255,0), "courier", "bold")
    txtTitle.draw(win)

    #create and draw Title image
    imgTitle = Image(Point(5,6), "goldbar.gif")
    imgTitle.draw(win)

    

    #create and draw the CLICK HERE TO PLAY "button" Rectangle and text
    rect2Button = Rectangle(Point(1,2), Point(3,3))
    rect2Button.setFill(color_rgb(255,255,0))
    rect2Button.draw(win)
    clickButton = Text(Point(2,2.8), "CLICK HERE")
    clickButton.setTextColor("black")
    clickButton.draw(win)
    click2Button = Text(Point(2,2.2), "TO PLAY")
    click2Button.setTextColor("black")
    click2Button.draw(win)

    #create and draw the QUIT "button" Rectangle and text
    rect3Button = Rectangle(Point(7,2), Point(9,3))
    rect3Button.setFill(color_rgb(255,255,0))
    rect3Button.draw(win)
    QuitButton = Text(Point(8,2.5), "QUIT")
    QuitButton.setTextColor("black")
    QuitButton.draw(win)

    while isOver == False:
        p1 = win.getMouse()
        if p1.getX() >= 1 and p1.getY() >= 2  and p1.getX() <= 3 and p1.getY() <= 3 :
            imgBackground = Image(Point(5,5), "blackBackground.gif")
            imgBackground.draw(win)
            #This begins the main game
            MAINGAME(win)
        elif p1.getX() >= 7 and p1.getY() >= 2  and p1.getX() <= 9 and p1.getY() <= 3 :
            #This closes the game
            win.close()

            isOver=True
##########################################################################################################################################################            
 
    

def main():

    #create a window
    win = GraphWin("Who Wants To Be A Millionare", 600, 600)

    #set coordinates
    win.setCoords(0,0,10,10)

    #create and set background color
    win.setBackground("black")

    #This begins the game
    mainmenu(win)

    
    

    
