print("**************************************************************************************************************************************************")
#title
intro = "   'KBC':Kaun Banega Crorepati(KBC)   "
intro01 = "    Aapka 'HOT SEAT' pe 'SAWAGAT' hai , chaliye 'GAME' shuru karte hai   "
intro02 = "    Please ENTER UR GOOD NAME   "

#rules & DLGs
dlg01 = "is 'GAME' ko khelne ke 'NIYAM' apke 'COMPUTER SCREEN' par ye rahe"
dlg02 = "aapko dene honge kuch '16' 'SAWAALO' ke sahi 'UTTAR'"
dlg03 = "to, 'KYA AAP TAYAR HAI'"
dlg04 = "agar 'HAA!'to 'ENTER'dabaye"
dlg05 = "aapke 'COMPUTER SCREEN' par pesh hai diye gae sawaalo ki sahi 'RAKAM'"
dlg06 = "aur, sabse 'JAROORI' baat to batana ham bhool hi gae"
dlg07 = "aapke paas hongi kuch lifelines"
dlg08 = "'50-50','EXPERT ADVICE'"
dlg09 = "jo aap 'SAHI TIME' aane par 'ISTEMAAL' kar skte hai"
dlg10 = "apko kya lagta aap  yha se kitni RAKAM le jaenge??"
dlg11 = "ham to yahi 'DUA' karte hai ki aap yahase"
dlg12 = "to jaroor hi lekar jae"
dlg13 = "to chaliye shuru karte hai"

#ques & money
rule01 = "Q1=1,000\nQ2=2,000\nQ3=3,000\nQ4=5,000"
rule02 = "Q5=10,000\nQ6=20,000\nQ7=40,000\nQ8=80,000"
rule03 = "Q9=1,60,000\nQ10=3,20,000\nQ11=6,40,000\nQ12=12,50,000"
rule04 = "Q13=25,00,000\nQ14=50,00,000\nQ15=1,00,00,000\nQ16=5,00,00,000"

#----------------------------------------PRINTING-----------------------------------------#

print("{0:$>60}{1:$<24}\n\n{2:≈>75}{3:≈<9}\n\n{4:◊>55}{5:◊<29}".format(intro,"",intro01,"",intro02,""))
name = input()
print("{0}!!{1}\n{2}\n{3}".format("Hello",name,"Nice To Meet You","Myself:Amitabh Bacchan"))
print("{0}\n{1}\n{2}\n{3}".format(dlg01,dlg02,dlg03,dlg04))
opinion = input()

print("{0}\n{1}\n{2}\n{3}\n{4}\n\n{5}".format(dlg05,rule01,rule02,rule03,rule04,dlg10))
money = input()
print("{0} {1} {2}\n{3},{4}".format(dlg11,money,dlg12,dlg13,intro))

input("please press 'ENTER' to start")

#---------------------------------------GAME----STARTS--------------------------------------#

print("to '1 SAWAAL',poore'1,000'ke liye,apke saamne yeh raha\n")
print("WHO IS THE ANCHOR OF BIG-BOSS IN LATEST SEASON?")
print("opt1)SALMAN KHAN                             opt2)AMITABH BACHAN")
print("opt3)SANJAYDUTT                              opt4)FARAH KHAN")

Answer = input("enter your Answer: ").strip().upper()

if Answer == "1" or Answer == "a":
    print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "EXPERT ADVICE":
    print("being BIG-BOSS an 'indian telivision series'")
    print("so the anchor of it would also be an indian actor or actoress.")
    print("but here all the option given to u are also of indian actors")
    print("by the way coming to ques,my opiion goes with option 1")
    print("because amitabh bachan is anchoring KBC")
    print("also sanjay dutt and farah khan, no doubt has been anchor of bigboss in previous years")
    
    Answer = input("Now Please enter your Answer").strip().upper()
    
    if Answer == "1" or Answer =="a":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "50-50":
        print("opt1)SALMAN KHAN        opt2)")
        print("opt3)SANJAY DUTT        opt3)")
        
        Answer = input("Now please enter your Answerwer")

        if Answer == "1" or Answer =="a":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "50-50":
    print("opt1)SALMAN KHAN        opt2)")
    print("opt3)SANJAY DUTT        opt4)")
    
    Answer = input("Now please enter your Answerwer")

    if Answer == "1" or Answer =="a":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
        
    elif Answer == "EXPERT ADVICE":
        print("being BIG-BOSS an 'indian telivision series'")
        print("so the anchor of it would also be an indian actor or actoress.")
        print("but here all the option given to u are also of indian actors")
        print("by the way coming to ques,my opiion goes with option 1")
        print("because amitabh bachan is anchoring KBC")
        print("also sanjay dutt and farah khan, no doubt has been anchor of bigboss in previous years")

        if Answer == "1" or Answer =="a":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
        
else:
    print("no")
    exit()
input("press enter!!")

#-------------------------------------------------------------------------------------------#
print("to '2 SAWAAL',poore'2,000'ke liye,apke saamne yeh raha\n")
print("IF A DIE IS THROWN AND 2 APPEARS,WHAT WILL BE THE NUMBER NON OPPOSITE FACE?")
print("opt1)1                                        opt2)3")
print("opt3)4                                        opt4)5")

Answer = input("enter yr Answer: ").strip().upper()

if Answer == "4" or Answer == "d":
    print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "EXPERT ADVICE":
    print("very simple!!,but a little tricky")
    print("i m sayig it tricky,becoz a little trick is used to solve this problem")
    print("trick is that")
    print("the sum of no. appearing on one face and no. appearing on its opposite face ")
    print("will always be equall to '7' ")
    print("thus,i will prefer you to go with option 4 i.e. '5'")
    
    Answer = input("Now Please enter your Answer").strip().upper()
    
    if Answer == "4" or Answer =="d":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "50-50":
        print("opt1)1        opt2)" )
        print("opt3)         opt4)5")
        Answer = input("Now Please enter your Answer")

        if Answer == "4" or Answer =="d":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "50-50":
    print("opt1)1        opt2)" )
    print("opt3)         opt4)5")
    
    Answer = input("Now Please enter your Answer")

    if Answer == "4" or Answer =="d":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
        
    elif Answer == "EXPERT ADVICE":
        print("very simple!!,but a little tricky")
        print("i m sayig it tricky,becoz a little trick is used to solve this problem")
        print("trick is that")
        print("the sum of no. appearing on one face and no. appearing on its opposite face ")
        print("will always be equall to '7' ")
        print("thus,i will prefer you to go with option 4 i.e. '5'")
    
        if Answer == "4" or Answer =="d":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
        
else:
    print("no")
    exit()
input("press enter!!")    
#-------------------------------------------------------------------------------------------#
print("to '3 SAWAAL',poore'3,000'ke liye,apke saamne yeh raha\n")
print("WHEN CHEVERLET WAS DISCONTINUED IN INDIA?")
print("opt1)2015                                        opt2)2016")
print("opt3)2017                                        opt4)2018")

Answer = input("enter yr Answer: ").strip().upper()

if Answer == "4" or Answer == "d":
    print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "EXPERT ADVICE":
    print("due to some sale issues 'CHEVERLET' discontinued in '2017' for not reaching their target")

    Answer = input("Now Please enter your Answer").strip().upper()
    
    if Answer == "3" or Answer =="c":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "50-50":
        print("opt1)             opt2)"    )
        print("opt3)2017         opt4)2018")
        
        Answer = input("Now Please enter your Answer")

        if Answer == "3" or Answer =="c":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "50-50":
    print("opt1)             opt2)"    )
    print("opt3)2017         opt4)2018")
    
    Answer = input("Now Please enter your Answer")

    if Answer == "3" or Answer =="c":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "EXPERT ADVICE":
        print("due to some sale issues 'CHEVERLET' discontinued in '2017' for not reaching their target")

        if Answer == "3" or Answer =="c":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '4 SAWAAL',poore'5,000'ke liye, apke saamne yeh raha\n")
print("WHICH OF THESE NO. IS NORMALLY REQUIRED IN ONLINE MONEY TRAnswerACTION? ")
print("opt1)CVV                                        opt2)AADHAR")
print("opt3)PAN                                        opt4)PNR")

Answer = input("enter yr Answer: ").strip().upper()

if Answer == "1" or Answer == "A":
    print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "EXPERT ADVICE":
    print("we all kNow,while only money trAnswerferring")
    print("we take use 'CREDIT CARDS'or'DEBIT CARDS'")
    print("so the no. written on back of these cards are always required")
    print("that no. is call 'CVV'")

    Answer = input("Now Please enter your Answer").strip().upper()
    
    if Answer == "1" or Answer == "a":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "50-50":
        print("opt1)CVV         opt2)AADHAR")
        print("opt3)            opt4)")
        
        Answer = input("Now Please enter your Answer")

        if Answer == "1" or Answer =="a":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "50-50":
    print("opt1)CVV         opt2)AADHAR")
    print("opt3)            opt4)")
    
    Answer = input("Now Please enter your Answer")

    if Answer == "1" or Answer == "a":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "EXPERT ADVICE":
        print("we all kNow,while only money trAnswerferring")
        print("we take use 'CREDIT CARDS'or'DEBIT CARDS'")
        print("so the no. written on back of these cards are always required")
        print("that no. is call 'CVV'")


        if Answer == "1" or Answer == "a":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
else:
    print("no")
    exit()
input("press enter!!")    
#-------------------------------------------------------------------------------------------#
print("to '5 SAWAAL',poore'10,000'ke liye, apke saamne yeh raha\n")
print("WHIC OF THESE COME IN DIFFERENT SIZES NAMELY 'MINI,MICRO,NANO'")
print("opt1)PLAYING CARDS                                      opt2)MEMORY CARD")
print("opt3)CREDIT CARD                                        opt4)SIM CARD")

Answer = input("enter yr Answer: ").strip().upper()

if Answer == "4" or Answer == "d":
    print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "EXPERT ADVICE":
    print("only 'SIM CARD' is the option which come in different sizes")

    Answer = input("Now Please enter your Answer").strip().upper()
    
    if Answer == "4" or Answer == "d":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "50-50":
        print("opt1)         opt2)MEMORY CARD")
        print("opt3)         opt4)SIM CARD")
        
        Answer = input("Now Please enter your Answer")

        if Answer == "4" or Answer =="d":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "50-50":
    print("opt1)         opt2)MEMORY CARD")
    print("opt3)         opt4)SIM CARD")
    
    Answer = input("Now Please enter your Answer")

    if Answer == "4" or Answer =="d":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "EXPERT ADVICE":
        print("only 'SIM CARD' is the option which come in different sizes")

        if Answer == "4" or Answer =="d":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
else:
    print("no")
    exit()
input("press enter!!")    
#-------------------------------------------------------------------------------------------#
print("to '6 SAWAAL',poore'20,000'ke liye, apke saamne yeh raha\n")
print("'BAHUBALI'festival is related to which religion? ")
print("opt1)ISLAM                                          opt2)BUDDHISM")
print("opt3)JAINISM                                        opt4)HINDUISM")

Answer = input("enter yr Answer: ").strip().upper()

if Answer == "3" or Answer == "c":
    print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "EXPERT ADVICE":
    print("actually,i m not so sure about this")
    print("i m confuse between jainism and hinduism")
    print("as i hv read somewhere about them")

    Answer = input("Now Please enter your Answer").strip().upper()
    
    if Answer == "3" or Answer == "c":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "50-50":
        print("opt1)                opt2)BUDDHISM")
        print("opt3)JAINISM         opt4)")
        
        Answer = input("Now Please enter your Answer")

        if Answer == "3" or Answer =="c":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "50-50":
    print("opt1)                opt2)BUDDHISM")
    print("opt3)JAINISM         opt4)")
    
    Answer = input("Now Please enter your Answer")

    if Answer == "3" or Answer =="c":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "EXPERT ADVICE":
        print("actually,i m not so sure about this")
        print("i m confuse between jainism and hinduism")
        print("as i hv read somewhere about them")

        if Answer == "3" or Answer =="c":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '7 SAWAAL',poore'40,000'ke liye, apke saamne yeh raha\n")
print("WHICH PLANET HAS MOST ROCKY SURFACE")
print("opt1)JUPITER                                        opt2)MARS")
print("opt3)SATURN                                         opt4)NEPTUNE")

Answer = input("enter yr Answer: ").strip().upper()

if Answer == "2" or Answer == "b":
    print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "EXPERT ADVICE":
    print("all the other planets except 'MARS' are gassy and stormy planets")

    Answer = input("Now Please enter your Answer").strip().upper()
    
    if Answer == "2" or Answer == "b":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "50-50":
        print("opt1)JUPITER         opt2)MARS")
        print("opt3)                opt4)")
        
        Answer = input("Now Please enter your Answer")

        if Answer == "2" or Answer =="b":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "50-50":
    print("opt1)JUPITER         opt2)MARS")
    print("opt3)                opt4)")
    
    Answer = input("Now Please enter your Answer")

    if Answer == "2" or Answer =="b":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "EXPERT ADVICE":
        print("all the other planets except 'MARS' are gassy and stormy planets")

        if Answer == "2" or Answer =="b":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '8 SAWAAL',poore'80,000'ke liye, apke saamne yeh raha\n")
print("WHICH OF THESE IS THE WORLDS BIGGEST ISLAND?")
print("opt1)GREENLAND                                      opt2)ANDEMAN & NICOBAR ISLAND")
print("opt3)ICELAND                                        opt4)LAKSDWEEP ISLAND")

Answer = input("enter yr Answer: ").strip().upper()

if Answer == "1" or Answer == "a":
    print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "EXPERT ADVICE":
    print(" perfectly! go with opt1)greenland")

    Answer = input("Now Please enter your Answer").strip().upper()
    
    if Answer == "1" or Answer == "a":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "50-50":
        print("opt1)GREENLAND         opt2)")
        print("opt3)ICELAND           opt4)")
        
        Answer = input("Now Please enter your Answer")

        if Answer == "1" or Answer =="a":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "50-50":
    print("opt1)GREENLAND         opt2)")
    print("opt3)ICELAND           opt4)")
    
    Answer = input("Now Please enter your Answer")

    if Answer == "1" or Answer =="a":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "EXPERT ADVICE":
        print("perfectly! go with opt1)greenland")

        if Answer == "1" or Answer =="a":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '9 SAWAAL',poore'1,60,000'ke liye, apke saamne yeh raha\n")
print("WHICH AMONG THESE IS THE MOST RICHEST SPORT")
print("opt1)HOCKEY                                      opt2)BASEBALL")
print("opt3)GOLF                                        opt4)BASKETBALL")

Answer = input("enter yr Answer: ").strip().upper()

if Answer == "3" or Answer == "c":
    print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "EXPERT ADVICE":
    print("golf, its obvious !!")

    Answer = input("Now Please enter your Answer").strip().upper()
    
    if Answer == "3" or Answer == "c":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "50-50":
        print("opt1)             opt2)BASEBALL")
        print("opt3)GOLF         opt4)")
        
        Answer = input("Now Please enter your Answer")

        if Answer == "3" or Answer =="c":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "50-50":
    print("opt1)             opt2)BASEBALL")
    print("opt3)GOLF         opt4)")
    
    Answer = input("Now Please enter your Answer")

    if Answer == "3" or Answer =="c":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "EXPERT ADVICE":
        print("golf, its obvious!!")

        if Answer == "3" or Answer =="c":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '10 SAWAAL',poore'3,20,000'ke liye, apke saamne yeh raha\n")
print("THERE WERE HOW MANY CHIMNEYS ON TITANIC ROOF IN ACTUAL")
print("opt1)2                                        opt2)3")
print("opt3)4                                        opt4)5")

Answer = input("enter yr Answer: ").strip().upper()

if Answer == "2" or Answer == "b":
    print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "EXPERT ADVICE":
    print("actually i film 'TITAIC', there are shown 4 chimneys")
    print("but in actuall there were 3")

    Answer = input("Now Please enter your Answer").strip().upper()
    
    if Answer == "2" or Answer == "b":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "50-50":
        print("opt1)          opt2)3")
        print("opt3)4         opt4)")
        
        Answer = input("Now Please enter your Answer")

        if Answer == "2" or Answer =="b":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "50-50":
    print("opt1)         opt2)3")
    print("opt3)4         opt4)")
    
    Answer = input("Now Please enter your Answer")

    if Answer == "2" or Answer =="b":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "EXPERT ADVICE":
        print("actually i film 'TITAIC', there are shown 4 chimneys")
        print("but in actuall there were 3")


        if Answer == "2" or Answer =="b":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '11 SAWAAL',poore'6,40,000'ke liye, apke saamne yeh raha\n")
print("IN WHICH YEAR JIO OVERTAKES AIRTEL")
print("opt1)BEGIN,2018                              opt2)MID,2018")
print("opt3)END,2018                                opt4)BEGIN,2019")

Answer = input("enter yr Answer: ").strip().upper()

if Answer == "4" or Answer == "d":
    print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "EXPERT ADVICE":
    print("JIO OVERTAKES AIRTEL to become most subscribed simcard company")
    print("but i m confuse between opt3) & opt4)")
    print("sorry,u should go for 50-50")

    Answer = input("Now Please enter your Answer").strip().upper()
    
    if Answer == "4" or Answer == "d":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "50-50":
        print("opt1)         opt2)MID,2018")
        print("opt3)         opt4)BEGIN,2019")
        
        Answer = input("Now Please enter your Answer")

        if Answer == "4" or Answer =="d":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "50-50":
    print("opt1)         opt2)MID,2018")
    print("opt3)         opt4)BEGIN,2019")
    
    Answer = input("Now Please enter your Answer")

    if Answer == "4" or Answer =="d":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "EXPERT ADVICE":
        print("JIO OVERTAKES AIRTEL to become most subscribed simcard company")
        print("but i m confuse between opt3) & opt4)")
        print("sorry,u should go for 50-50")

        if Answer == "4" or Answer =="d":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '12 SAWAAL',poore'12,50,000'ke liye, apke saamne yeh raha\n")
print("THERE ARE HOW MANY NUMBERS from 0-100 IN WHICH 'a' OCCUR?")
print("opt1)0                                        opt2)2")
print("opt3)20                                        opt4)75")

Answer = input("enter yr Answer: ").strip().upper()

if Answer == "1" or Answer == "a":
    print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "EXPERT ADVICE":
    print("the 1st no. to present with a is 'thousand'")

    Answer = input("Now Please enter your Answer").strip().upper()
    
    if Answer == "1" or Answer == "a":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "50-50":
        print("opt1)0         opt2)2")
        print("opt3)          opt4)")
        
        Answer = input("Now Please enter your Answer")

        if Answer == "1" or Answer =="a":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "50-50":
    print("opt1)0         opt2)2")
    print("opt3)          opt4)")
    
    Answer = input("Now Please enter your Answer")

    if Answer == "1" or Answer =="a":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "EXPERT ADVICE":
        print("the 1st no. to present with a is 'thousand'")

        if Answer == "1" or Answer =="a":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '13 SAWAAL',poore'25,00,000'ke liye, apke saamne yeh raha\n")
print("IN WHICH SERIES OF 'FAST&FURIOUS' DOES JOHNY WALKER DIED")
print("opt1)5                                        opt2)6")
print("opt3)8                                        opt4)7")

Answer = input("enter yr Answer: ").strip().upper()

if Answer == "4" or Answer == "d":
    print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "EXPERT ADVICE":
    print("'JOHNY WALKER'died in 7th series due to a car accident on set")

    Answer = input("Now Please enter your Answer").strip().upper()
    
    if Answer == "4" or Answer == "d":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "50-50":
        print("opt1)5         opt2)")
        print("opt3)          opt4)7")
        
        Answer = input("Now Please enter your Answer")

        if Answer == "4" or Answer =="d":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "50-50":
    print("opt1)5         opt2)")
    print("opt3)          opt4)7")
    
    Answer = input("Now Please enter your Answer")

    if Answer == "4" or Answer =="d":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "EXPERT ADVICE":
        print("'JOHNY WALKER'died in 7th series due to a car accident on set")

        if Answer == "4" or Answer =="d":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '14 SAWAAL',poore'50,00,000'ke liye, apke saamne yeh raha\n")
print("WHAT WAS THE FIRST PROGRAME BUILT BY BILL GATES")
print("opt1)TIC-TAC-TOE                                        opt2)CALCULATOR")
print("opt3)CROSSWORD                                          opt4)CLOCK")

Answer = input("enter yr Answer: ").strip().upper()

if Answer == "1" or Answer == "a":
    print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "EXPERT ADVICE":
    print("sorry sir!!! NO IDEA")

    Answer = input("Now Please enter your Answer").strip().upper()
    
    if Answer == "1" or Answer == "a":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "50-50":
        print("opt1)TIC-TAC-TOE         opt2)")
        print("opt3)                    opt4)CLOCK")
        
        Answer = input("Now Please enter your Answer")

        if Answer == "1" or Answer =="a":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "50-50":
    print("opt1)TIC-TAC-TOE         opt2)")
    print("opt3)                    opt4)CLOCK")
    
    Answer = input("Now Please enter your Answer")

    if Answer == "1" or Answer =="a":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "EXPERT ADVICE":
        print("sorry sir!!! no idea")

        if Answer == "1" or Answer =="a":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '15 SAWAAL',poore'1,00,00,000'ke liye, apke saamne yeh raha\n")
print("THERE WERE HOW MANY 'USTAAD'S' IN THE FILM 'SANJU'")
print("opt1)2                                        opt2)3")
print("opt3)4                                        opt4)5")

Answer = input("enter yr Answer: ").strip().upper()

if Answer == "2" or Answer == "b":
    print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "EXPERT ADVICE":
    print("acc. to me , there were 3 ustaads which were actually termed for songs")

    Answer = input("Now Please enter your Answer").strip().upper()
    
    if Answer == "2" or Answer == "b":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "50-50":
        print("opt1)         opt2)3")
        print("opt3)         opt4)5")
        
        Answer = input("Now Please enter your Answer")

        if Answer == "2" or Answer =="b":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "50-50":
    print("opt1)         opt2)3")
    print("opt3)         opt4)5")
    
    Answer = input("Now Please enter your Answer")

    if Answer == "2" or Answer =="b":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "EXPERT ADVICE":
        print("acc. to me , there were 3 ustaads which were actually termed for songs")

        if Answer == "2" or Answer =="b":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
else:
    print("no")
    exit()
input("press enter!!")
#-------------------------------------------------------------------------------------------#
print("to '16 SAWAAL',poore'5,00,00,000'ke liye, apke saamne yeh raha\n")
print("WHICH IS THE LONGEST RIVER IN THE WORLD?")
print("opt1)NILE                                        opt2)YAMUNA")
print("opt3)GANGA                                       opt4)AMAZON")

Answer = input("enter yr Answer: ").strip().upper()

if Answer == "4" or Answer == "d":
    print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "EXPERT ADVICE":
    print("confused between nile & amazon")

    Answer = input("Now Please enter your Answer").strip().upper()
    
    if Answer == "4" or Answer == "d":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "50-50":
        print("opt1)NILE         opt2)")
        print("opt3)             opt4)AMAZON")
        
        Answer = input("Now Please enter your Answer")

        if Answer == "4" or Answer =="d":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
    
elif Answer == "50-50":
    print("opt1)NILE         opt2)")
    print("opt3)             opt4)AMAZON")
    
    Answer = input("Now Please enter your Answer")

    if Answer == "4" or Answer =="d":
        print("Yes!! Aapka Jawaab Bilkul sahi hai!!")

    elif Answer == "EXPERT ADVICE":
        print("confused between nile & amazon")

        if Answer == "4" or Answer =="d":
            print("Yes!! Aapka Jawaab Bilkul sahi hai!!")
else:
    print("no")
exit()
