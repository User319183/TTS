import gtts #import text to speech
from playsound import playsound #let the computer play sounds
import os #import the operating system to remove files







entername = gtts.gTTS(f"Hello there! Please enter your name in the console so we can get started.") #tell the text to speech to start up and say this
entername.save("entername.mp3") #save the files as their audio so the computer can play it
playsound("entername.mp3") #play the audio that has `.mp3`


entername = str(input(""))

name = entername

entername = gtts.gTTS(f"Hi {name} !") #tell the text to speech to start up and say this
entername.save("entername.mp3") #save the files as their audio so the computer can play it
playsound("entername.mp3") #play the audio that has `.mp3`

os.remove("entername.mp3") #remove the files so they don't add space




saypythonproject = gtts.gTTS("This is a fun Python project that the owner has created that uses text and converts it to speech!") #tell the text to speech to say this
saypythonproject.save("saypythonproject.mp3") #save the files as their audio so the computer can play it
playsound("saypythonproject.mp3") #play the audio that has `.mp3`

os.remove("saypythonproject.mp3") #remove the files so they don't add space

saysathvikwebsite = gtts.gTTS("Like what you're hearing? View my other projects where you get links for everything else I have created at https://sathvik dot website") #tell the text to speech to say my website
saysathvikwebsite.save("saysathvikwebsite.mp3") #save the files as their audio so the computer can play it
playsound("saysathvikwebsite.mp3") #play the audio that has `.mp3`

os.remove("saysathvikwebsite.mp3") #remove the files so they don't add space


bye = gtts.gTTS("Time to vanish. Bye! I hope you enjoyed.") #Say bye!
bye.save("bye.mp3") #save the files as their audio so the computer can play it
playsound("bye.mp3") #play the audio that has `.mp3`

os.remove("bye.mp3") #remove the files so they don't add space


print("Files have been removed! Text to speech has ended.") #say files have been removed