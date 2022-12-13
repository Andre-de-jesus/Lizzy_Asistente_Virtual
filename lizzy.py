import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser 
import os

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa():
    try:
        with sr.Microphone() as source:
            print('ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            while 'ana' in comando:
                comando = comando.replace('ana', ' ')
                print(comando)
                maquina.say(comando)
                maquina.rundAndWait()
                
    except:
        print('Não entendi, pode repetir')
        
    return comando
   
def voz_do_usuario():
    comando = executa()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'o que é' in comando:
        procurar = comando.replace('o que é', ' ')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque', ' ')
        resultado = webbrowser.open('www.youtube.com' + musica)
        maquina.say('tocando musica')
        maquina.runAndWait()
                
    elif 'executar' in comando:
      executar = os.startfile(comando + '.exe')
      maquina.say = ('executando {} programa'.format(comando))
      maquina.runAndWait()

    elif 'web' in comando: 
      web = comando
      resultado = webbrowser.open('https://www.{}.com'.format(web))
      maquina.say('abrindo o site...')
      maquina.runAndWait()
voz_do_usuario()

