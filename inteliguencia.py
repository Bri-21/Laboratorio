#API:  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
import pyttsx3
engine = pyttsx3.init()
import speech_recognition as sr #as es para que me lo muestre así
r = sr.Recognizer()
presta_atencion = primo

from groq import Groq 


while True:
   #Abre el microfono para hacer preguntas
    while presta_atencion:
        with sr.Microphone() as source:                  #with igual a con....
            print("Hable: ")
            audio = r.listen(source)

            #Ajusta el nivel de ruido de ambiente para obtener mejores resultados
            r.adjust_for_ambient_noise(source)

            #Escucha el audio de micro por 10 segundos
            audio = r.listen(source, timeout=10, phrase_time_limit=5)

        try:                           # Dice proba a hacer algo y atrapa el eror, 
            #Usa el reconocimiento de Google con el audio
            text = r.recognize_google(audio, language= 'es-ES').capitalize()
            print(F"Digiste: {text}")
        except sr.UnknownValueError:                        #La documentación me dice el error que sale
            print("Lo siento, no he podido entender lo que has dicho.")
        except sr.RequestError:
            print("Lo siento, he habido un problema al intentar comunicarme con el servidor de Google.")
            
        if text == "Basta":
            exit("GRACIAS POR USAR NUESTRA APP")
            #break #False #!cualquier opción esta bien

        usuario = Groq(   #es un objeto pq tiene metodo y propidades pq tiene . y un metodo
        api_key= "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",
        )

        interaccion_chat = usuario.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": (text),
                }
            ],
            model="llama3-8b-8192", #el modelo se puede cambiar pq es al que le preguntamos
        )
        respuenta = interaccion_chat.choices[0].message.content
        engine.say(respuenta)
        engine.runAndWait() #siempre va al final de todo para que hable
        print(interaccion_chat.choices[0].message.content)

        