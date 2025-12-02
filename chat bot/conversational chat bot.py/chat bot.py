print("HELLO,NOMOSKAR")
print("I AM A  AI BASED CHATBOT,I AM READY TO HEP YOU")
import datetime
import time
name=input("sir/madam, write  your  name:")
hour= datetime.datetime.now().hour
if 5<= hour<=11:
   print("good morning",name)
elif 12<= hour<= 6:
   print("good evening",name)
else:
   print("good  night",name)


memory={
    "hello":"hi",
    "how are you?":"I am fine",
    "what are you doing?" :"I am busy to update my self",
    "what is ai" : "Artificial intelligence, is the capability of computer systems to perform tasks that typically require human intelligence, such as learning, reasoning, problem-solving, and decision-making."
}

def botresponse(userquestion):
    userquestion =userquestion.lower()
    for eachkeys in memory:
        if userquestion in eachkeys:
            return memory[eachkeys]
        
    return "Anwser not available in my  dicsanary ,I am try to learn new  things "
while True:

  userinput=input("please ask your question")
  reply=botresponse(userinput)
  print("bot  response:",reply)

  if "bye" in userinput.lower():
    break