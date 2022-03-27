import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Start")
    audio = r.listen(source)
    print("Done")

data = r.recognize_google(audio)

print(data)
