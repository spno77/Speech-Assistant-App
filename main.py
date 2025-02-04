import speech_recognition as sr  
import webbrowser
import time
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
	with sr.Microphone() as source:
		if ask:
			print(ask)
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source,timeout=3,phrase_time_limit=3)
		voice_data = " "
		try:
			voice_data = r.recognize_google(audio)
		except sr.UnknownValueError:
			print("Sorry, I did not get that")
		except sr.RequestError:
			print("Sorry, my speech service is down")
		return voice_data


def respond(voice_data):
	if 'what is your name' in voice_data:
		print('my name is alexis')
	if 'what time is it' in voice_data:
		print(ctime())
	if 'search' in voice_data:
		search = record_audio('What do you want to search for')
		url = 'https://google.com/search?q=' + search
		webbrowser.get().open(url)
		print('Here is what I found for ' + search)
	if 'find location' in voice_data:
		location = record_audio('What is the location')
		url = 'https://google.com/maps/place/' + location + '/&amp;'
		webbrowser.get().open(url)
		print('Here is the location of ' + location)
	if 'exit' in voice_data:
		exit()


time.sleep(1)
print("How can i help you?")
while 1:
	voice_data = record_audio()
	respond(voice_data)

