import pyaudio
import wave
import pydub
import requests
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "audio.wav"


exit = 0


def SendRequest(fname):
	
	url= "http://192.168.49.2:30007/"
	#files={'files': open(fname,'rb')}
	r=requests.post(url,data=open(fname,'rb'))
	print("request sent")
	return


while not exit:

	ok = 0
	while not ok:
		record = input("Want to record another frame? y/n \n")
		if record == "n":
			print("Quitting")
			sys.exit(0)
		elif record == "y":
			ok = 1
		else:
			print("Please, choose a correct option")
	

	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT,
		        channels=CHANNELS,
		        rate=RATE,
		        input=True,
		        frames_per_buffer=CHUNK)

	print("* recording")

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()
	
	SendRequest(WAVE_OUTPUT_FILENAME)
	
	
	    
	    
