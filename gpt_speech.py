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

openai.api_key = os.getenv('OPENAI_API')

engine = pyttsx3.init()

CHARACTER_PROMPT = os.getenv('CHARACTER_PROMPT')
RULES = os.getenv('RULES_PROMPT')
MEMORY = os.getenv('MEMORY')
SPEECH_LANGAGE = os.getenv('SPEECH_LANGAGE')

conversation = ""

short_memory = []

mic_on = False

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language=SPEECH_LANGAGE,show_all=True)
    except:
        print('Skipping unknown error')

def generate_response(prompt):
    global conversation
    global short_memory
    conversation += "\n"+prompt+"\n"
    memory = json.dumps(short_memory)
    base = CHARACTER_PROMPT + RULES
    if MEMORY == True:
        base += 'memoire_courte : '+memory
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