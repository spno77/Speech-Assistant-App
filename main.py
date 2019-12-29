import speech_recognition as sr  

r = sr.Recognizer()

with sr.Microphone() as source:
	print("Say something: ")
	r.adjust_for_ambient_noise(source)
	audio = r.listen(source,timeout=3,phrase_time_limit=3)
	voice_data = r.recognize_google(audio)
	print(voice_data)