# -*- coding: utf-8 -*-
import sys

import yaml
import speech_recognition as sr

from GreyMatter.SenseCells.tts import tts

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

#Functioning variables
name = profile_data['name']

tts('Welcome ' + name + ', systems now ready to run. How can I help you?')

def main():
	#obtain audio from the microphone
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Say something!")
		audio = r.listen(source)


	#recognize speech using WIT.AI
	WIT_AI_KEY = "YVRDNX5MC5L6DJRZYU44MOIUWS56JDRW"

	#WIT_AI_KEY = "3HJYXBPG6BZ3KFZG3KQHIOGAYD5OLWXK"

	try:
		speech_text = r.recognize_wit(audio, key=WIT_AI_KEY)
		print("Jarvis thinks you said '" + speech_text + "'")
	except sr.UnknownValueError:
			print("Jarvis could not understand audio")
	except sr.RequestError as e:
			print("Could not request results from Wit.ai service; {0}".format(e))

	tts(speech_text)
main()