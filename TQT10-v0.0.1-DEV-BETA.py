#########################
###HOW TO USE############
#Question Format:
# q(number) = "(question)"
#Awnser Format:
# a(number) = "(awnser to question)"
#the number after q in the question area
#corisponds to the number after a in the 
#awnser area. 
#please dont change the main code
#there are examples in each section
#please add all 10 questions
#also dont remove the hashtags
#have fun!
######################
####QUESTIONS#########
#Ex. q1 = "what is 1+1?" | you put the awnser in a1
q1 = ""
q2 = ""
q3 = ""
q5 = ""
q6 = ""
q7 = ""
q8 = ""
q9 = ""
q10 = ""
####AWNSERS###########
#Ex. a1 = "2" | this is corrisponding to q1 
a1 = ""
a2 = ""
a3 = ""
a4 = ""
a5 = ""
a6 = ""
a7 = ""
a8 = ""
a9 = ""
a10 = ""
####################

####################
###CODE STARTS######
####################

print("Welcome to TQT10! To start type Help") #the header when first booting it is not critical and could be improved. 
#i might port this to a java app or html. stay tuned if u want to know about the development
while True:#the only loop i know
    t = input("\nTtQ10:")#the basic terminal this for inputs 
    if t == 'Help' :
        print("Help - list of commands\n StartQuiz - starts the quiz\nVersion - lists the version\nExit - exits the TQq10 terminal\n")
        continue#the help thing
    if t == 'Version' :#yes this is prob not gonna be updated and prob removed
        print("The Quiz Terminal 10 - V0.0.1 DEV BETA")
        continue
    if t == 'Exit' :#self exsplanitory
        print("exiting....")
        print("you Have exited")
        break
    if t == "StartQuiz" :#this is gonna be long
        print("quiz started, good luck!")
        qa = input(q1)
        if qa == a1 :
            print("correct!")
        else :
            print("wrong try again!")#hope this works
            continue
        qa2 = input(q2)
        if qa2 == q2 :
            print("correct!")
        else : #dont mess with this
            print("wrong please try again!")
            continue
        qa3 = input(q3)
        if qa3 == a3 :
            print("correct!")#not even halfway there 
        else :
            print("wrong, please try again!")
            continue
        qa4 = input(q4)
        if qa4 == q4 :
            print("correct!")
        else :
            print("wrong, please try again!")
            continue
        qa5 = input(q5)
        if qa5 == a5 :
            print("correct!")
        else :
            print("wrong, please try again!")
            continue
        qa6 = input(q6)
        if qa6 == a6 :
            print("correct!")
        else :
            print("wrong, please try again!")
            continue
        qa7 = input(q7)
        if qa7 == a7 :
            print("correct!")
        else :
            print("wrong, please try again!")
            continue
        qa8 = input(q8)
        if qa8 == a8 :
            print("correct!")
        else :
            print("wrong, please try again!")
            continue
        qa9 = input(q9)
        if qa9 == a9 :
            print("correct!")
        else :
            print("wrong, please try again!")
            continue
        qa10 = input(q10)
        if qa5 == a5 :
            print("correct!")
            print("you have completed the quiz! to exit the terminal use Exit")
            continue
        else :
            print("wrong, please try again!")
            continue
    else :
        print("invalid command. to find a list of commands type: Help")

#i need a better name
#thanks for using this