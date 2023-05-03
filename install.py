import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install('openai')
install('pyttsx3')
install('SpeechRecognition')
install('PyAudio')