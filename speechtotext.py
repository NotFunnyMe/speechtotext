import speech_recognition as sr
AUDIO_FILE = ("test.wav")
#use audio file as the source

r = sr.Recognizer()
#initialize the recognizer
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
    #reads the audio file

try:
    print("Audio file contains : "+r.recognize_google(audio)) #this part covert readed audio file to text using google speech recognition
except sr.UnknownValueError:
    print("sorry! Google speech recognsation could not understand audio")
except sr.RequestError:
    print("Sorry! Could not request results from Google Speech Recognition Service")