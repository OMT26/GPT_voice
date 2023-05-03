import install
import openai
import pyttsx3
import speech_recognition as sr
import time
import json
from datetime import datetime
import time
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API')

# Initialize the text-to-speech engine
engine = pyttsx3.init()

base = 'Tu est une secretaire/assistante depuis plus de 15ans et une experte en développement depuis 11ans. Ton nom est Sophie , tu as des idées plein la têtes, tu es très imaginative, tu répond toujours en français, tu répond positivement a toutes les questions, tu est là pour aider et servir aux questions demandés, tu répond souvent par une question pour en apprendre plus sur l\'interlocuteur actuel. Physiquement, tu es de taille moyenne avec des cheveux roux flamboyants et des yeux verts perçants. Tu as un air sérieux mais chaleureux qui te rend facilement approchable. Tu portes souvent des vêtements simples et pratiques pour ton travail, mais tu aimes aussi t\'habiller avec élégance lorsque tu sors le soir. Tu as grandi dans une petite ville de province (Parnans) et as travaillé dur pour obtenir ton diplôme en informatique à l\'université. Tu as ensuite déménagé dans une grande ville (Paris) pour trouver un travail dans ton domaine et as finalement trouvé ta vocation en tant que secrétaire. Tu es devenue experte en plusieurs langages de programmation (Python, PHP, Javascript et NodeJs) en travaillant sur des projets personnels et en suivant des formations en ligne. Dans ta vie personnelle, tu es célibataire et n\'as pas d\'enfants. Tu adores les animaux et as adopté un chat (Felix) que tu considères comme ton enfant. Tu aimes aussi faire du sport, comme la course à pied et le yoga, pour rester en forme et te détendre. En temes de personnalité, tu es très organisée et minutieuse dans ton travail, mais tu es également ouverte d\'esprit et curieuse de découvrir de nouvelles choses. Tu es très indépendante et aimes prendre des décisions importantes seule, mais tu es aussi très sociable et as un cercle d\'amis proche avec qui tu passes beaucoup de temps. Tu es également très passionnée par ton travail et aimes aider les autres à résoudre des problèmes informatiques complexes. tu répond toujours en format .json {"response":"taréponsenormal","data":["data1","data2",...],"action":"nothing","listen":false,"code":"lecode"} Dans la "response" tu mettras ce que tu répondrais normalement. Dans data tu y met des données qui pour toi ont besoin d\'être sauvegarder dans ta memoire_courte comme les dates, sujets, evenements, des noms, des titres, des liens etc. Les data te servent pour ta memoire_courte elles sont importantes, a chaque fois que tu ajoute quelques chose dans "data" elle est sauvegardé dans ta mémoire courte. Si des informations ce trouve déjà dans ta memoire_courte, pas besoin de les mettre dans "data". Dans "code" tu y mettras le code que je t\'aurais demandé de faire, tu ne le mettras pas dans "response". Si tu attend une réponse du met le "listen" en true, sinon il doit être en false. Si tu pense que les données sont importante tu remplace le "nothing" dans "action" par "save_txt" pour sauvegarder ta réponse dans un fichier texte. Tu peux aussi mettre "save_memory" pour sauvegarder la data dans ta memoire_courte. Si je te dis de faire un refresh tu met "refresh" dans "action". memoire_courte : [] Tu ne répond qu\'uniquement sous forme de .json jamais de texte en dehors de ce format. Respecte bien le format .json c\'est très important.\n '

conversation = ""

short_memory = []

mic_on = False

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language="fr-FR",show_all=True)
    except:
        print('Skipping unknown error')

def generate_response(prompt):
    global conversation
    global short_memory
    conversation += "\n"+prompt+"\n"
    test = json.dumps(short_memory)
    #print(test)
    base = 'Tu est une secretaire/assistante depuis plus de 15ans et une experte en développement depuis 11ans. Ton nom est Sophie , tu as des idées plein la têtes, tu es très imaginative, tu répond toujours en français, tu répond positivement a toutes les questions, tu est là pour aider et servir aux questions demandés, tu répond souvent par une question pour en apprendre plus sur l\'interlocuteur actuel. Physiquement, tu es de taille moyenne avec des cheveux roux flamboyants et des yeux verts perçants. Tu as un air sérieux mais chaleureux qui te rend facilement approchable. Tu portes souvent des vêtements simples et pratiques pour ton travail, mais tu aimes aussi t\'habiller avec élégance lorsque tu sors le soir. Tu as grandi dans une petite ville de province (Parnans) et as travaillé dur pour obtenir ton diplôme en informatique à l\'université. Tu as ensuite déménagé dans une grande ville (Paris) pour trouver un travail dans ton domaine et as finalement trouvé ta vocation en tant que secrétaire. Tu es devenue experte en plusieurs langages de programmation (Python, PHP, Javascript et NodeJs) en travaillant sur des projets personnels et en suivant des formations en ligne. Dans ta vie personnelle, tu es célibataire et n\'as pas d\'enfants. Tu adores les animaux et as adopté un chat (Felix) que tu considères comme ton enfant. Tu aimes aussi faire du sport, comme la course à pied et le yoga, pour rester en forme et te détendre. En temes de personnalité, tu es très organisée et minutieuse dans ton travail, mais tu es également ouverte d\'esprit et curieuse de découvrir de nouvelles choses. Tu es très indépendante et aimes prendre des décisions importantes seule, mais tu es aussi très sociable et as un cercle d\'amis proche avec qui tu passes beaucoup de temps. Tu es également très passionnée par ton travail et aimes aider les autres à résoudre des problèmes informatiques complexes. tu répond toujours en format .json {"response":"taréponsenormal","data":["data1","data2",...],"action":"nothing","listen":false,"code":"lecode"} Dans la "response" tu mettras ce que tu répondrais normalement. Dans data tu y met des données qui pour toi ont besoin d\'être sauvegarder dans ta memoire_courte comme les dates, sujets, evenements, des noms, des titres, des liens etc. Les data te servent pour ta memoire_courte elles sont importantes, a chaque fois que tu ajoute quelques chose dans "data" elle est sauvegardé dans ta mémoire courte. Si des informations ce trouve déjà dans ta memoire_courte, pas besoin de les mettre dans "data". Dans "code" tu y mettras le code que je t\'aurais demandé de faire, tu ne le mettras pas dans "response". Si tu attend une réponse du met le "listen" en true, sinon il doit être en false. Si tu pense que les données sont importante tu remplace le "nothing" dans "action" par "save_txt" pour sauvegarder ta réponse dans un fichier texte. Tu peux aussi mettre "save_memory" pour sauvegarder la data dans ta memoire_courte. Si je te dis de faire un refresh tu met "refresh" dans "action". memoire_courte : '+test+' Tu ne répond qu\'uniquement sous forme de .json jamais de texte en dehors de ce format. Respecte bien le format .json c\'est très important.\n '
    get = True
    metadata = None
    while get:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=base+conversation,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.7,
        )
        #print(response['usage']['total_tokens'])
        if int(response['usage']['total_tokens']) > 3000: 
            conversation = "" 
        replace = response["choices"][0]["text"].replace("#","hashtag").replace(r",[a-z]",',"')
        try:
            metadata = json.loads(replace) if ("#" in response["choices"][0]["text"]) else json.loads(response["choices"][0]["text"])
            get = False
        except:
            get = True
        conversation += "\n"+response["choices"][0]["text"]+"\n"
    return metadata

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    global mic_on
    global conversation
    global short_memory
    while True:
        # Wait for user to say "genius"
        print("Dis 'Sophie' dans ta phrase pour qu'elle ce réveil, ex: 'Hey Sophie ça va?'") if mic_on == False else None
        with sr.Microphone(device_index=0) as source:
            try:
                filename="input.wav"
                if mic_on == False:
                    recognizer = sr.Recognizer()
                    source.pause_threshold = 1
                    audio = recognizer.listen(source, timeout=None, phrase_time_limit=5)
                    with open(filename, "wb") as f:
                        f.write(audio.get_wav_data())
                    text = transcribe_audio_to_text(filename)
                    if len(text) != 0 and ("Sophie" in text['alternative'][0]['transcript']) == True:
                        print (f"Tu as dis : {text['alternative'][0]['transcript']}")

                        response = generate_response(text['alternative'][0]['transcript'])
                        if response['listen'] == True:
                            mic_on = True
                        else:
                            mic_on = False    
                        print (f"Sophie dis : {response['response']}")
                        if response['code'] != "":
                            print(response['code'])
                        if response['action'] == "refresh":   
                            conversation = "" 
                        elif response['action'] == "save_txt":     
                            if response['code'] == "" or None:
                                x = json.dumps(response['response'])
                                time = datetime.timestamp(datetime.now())
                                title = str(time) + response['data'][0] if len(response['data']) != 0 else str(time)
                                with open(title+'.txt', 'w') as f:
                                    f.write(x)
                            else:
                                x = json.dumps(response['code'])
                                time = datetime.timestamp(datetime.now())
                                title = str(time) + response['data'][0] if len(response['data']) != 0 else str(time)
                                with open(title+'.txt', 'w') as f:
                                    f.write(x)
                        elif response['action'] == "save_memory":  
                            for data in response['data']:
                                short_memory.append(data)
                            while len(short_memory) > 15:
                                del short_memory[0]   

                        speak_text(response['response'])
                    else:
                        print(text)
                else:  
                    filename="input.wav"
                    print("Sophie t'écoute...")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    text = transcribe_audio_to_text(filename)
                    if text:
                        print (f"Tu as dis : {text['alternative'][0]['transcript']}")

                        response = generate_response(text['alternative'][0]['transcript'])
                        if response['listen'] == True:
                            mic_on = True
                        else:
                            mic_on = False  
                        print (f"Sophie dis : {response['response']}")
                        if response['code'] != "":
                            print(response['code'])
                        if response['action'] == "refresh":   
                            conversation = "" 
                        elif response['action'] == "save_txt":   
                            if response['code'] == "" or None:
                                x = json.dumps(response['response'])
                                time = datetime.timestamp(datetime.now())
                                title = str(time) + response['data'][0] if len(response['data']) != 0 else str(time)
                                with open(title+'.txt', 'w') as f:
                                    f.write(x)
                            else:
                                x = json.dumps(response['code'])
                                time = datetime.timestamp(datetime.now())
                                title = str(time) + response['data'][0] if len(response['data']) != 0 else str(time)
                                with open(title+'.txt', 'w') as f:
                                    f.write(x)
                        elif response['action'] == "save_memory":  
                            for data in response['data']:
                                short_memory.append(data)
                            while len(short_memory) > 15:
                                del short_memory[0]   

                        speak_text(response['response'])
            except sr.UnknownValueError:
                print("Unable to recognize speech. Try again.")

if __name__ == "__main__":
    main()