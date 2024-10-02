import speech_recognition as sr
r = sr.Recognizer()
import pyttsx3
engine = pyttsx3.init() 

with sr.Microphone() as source:                  #with igual a con....
    print("Hable: ")
    audio = r.listen(source)
    try:                                                 # Dice proba a hacer algo y atrapa el eror, 
        text = r.recognize_google(audio, language= 'es-ES')
        print(F"Digiste: {text}")
    except sr.UnknownValueError:                        #La documentación me dice el error que sale
        print("Lo siento, no he podido entender lo que has dicho.")
    except sr.RequestError:
        print("Lo siento, he habido un problema al intentar comunicarme con el servidor de Google.")

que_queres_que_diga =  text
engine.say(que_queres_que_diga)




engine.runAndWait() #siempre va al final de todo para que hable