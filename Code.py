import pyttsx3
import datetime
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

hour = int(datetime.datetime.now().hour)
if ( hour >= 0 and hour <12 ):
	speak("Good Morning!")

elif ( hour >= 12 and hour < 18 ):
	speak("Good Afternoon!") 

else:
	speak("Good Evening!") 


def number_guess_game():

   speak("Please Enter Your Name")
   name = input("Please Enter your Name : ")
   
   print(name + ' Welcome to Number Guess Game')
   speak(name + 'Welcome to Number Guess Game')
   
   a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
   number = random.choice(a)
   b = "yes"
   round = 1
   while b == "yes":
      
      print("Round 1 Started :")
      speak("Round 1 Started")
      speak("Enter a number from 1 to 20 ")
      guess = int(input('Please Enter Number from 1 to 20\n'))
      nguess = 1
      
      while number != guess :
         round += 1
         print("Round "+ str(round) + " Started :")
         speak("Round "+ str(round) + " Started")
         if guess >20 or guess < 0:
            print("Error")
            speak("Error")
            break
         if guess < number :
            print("Please Enter Higher Number from "+ str(guess))
            speak("Please Enter Higher Number from "+ str(guess))
         if guess > number :
            print("Please Enter Lower Number from " + str(guess))
            speak("Please Enter Lower Number from " + str(guess))
         nguess += 1
         guess = int(input())
      if number == guess :
         print(name + " You Won the Game in "+ str(nguess) + " Guesses")
         speak(name + " You Won the Game in "+str(nguess) + " Guesses")

      speak(name + " Do you want to play again Number Guess Game?")   
      b = input(name + " Do you want to play again Number Guess Game? (yes or no) : ")
   print(name + " Thanks For Playing Number Guess Game")
   speak(name + " Thanks For Playing Number Guess Game")


number_guess_game()
