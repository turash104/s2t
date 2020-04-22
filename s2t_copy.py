import speech_recognition as sr
r = sr.Recognizer()



# generate a list of all audio cards/microphones
mic_list = sr.Microphone.list_microphone_names()

# the following loop aims to set the device ID of the mic that
# we specifically want to use to avoid ambiguity.
for i, microphone_name in enumerate(mic_list):
    print(i)
    print(microphone_name)

harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    print("started")
    audio = r.record(source)
    text = r.recognize_google(audio)
    print(text)
    print("done")

mic = sr.Microphone()
print(mic)
mic = sr.Microphone(device_index=0)
print(mic)
print(mic_list)

with mic as source:

    # wait for a second to let the recognizer adjust the
    # energy threshold based on the surrounding noise level
    #r.adjust_for_ambient_noise(source, duration = 1)
    r.adjust_for_ambient_noise(source)
    r.energy_threshold = 30
    print("Say Something")

    # listens for the user's input
    audio = r.listen(source, timeout=5)
    print("heard...")