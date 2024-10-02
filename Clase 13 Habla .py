import pyttsx3
engine = pyttsx3.init() 


que_queres_que_diga =  input("Escribe que queres que diga: ")
engine.say(que_queres_que_diga)

rate = engine.getProperty('rate') #para cambiarle la velocidad
print(f"la velocidad actual es: {rate}")
engine.setProperty('rate', 500)
engine.say(que_queres_que_diga)
engine.setProperty('rate', 50)
engine.say(que_queres_que_diga) #say es prepararlo para que lo diga



voces = engine.getProperty('voices') #para cambiarle la voz
#print(voces[1]) #!muentra la voz pero no es la correcta
for voz in voces:
    print(f"{voz.name} ({voz.languages})")
engine.setProperty('voice', voces [1].id)
engine.say(que_queres_que_diga)    

engine.runAndWait() #siempre va al final de todo para que hable
