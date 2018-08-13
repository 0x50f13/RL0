import pyaudio
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 8
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS,
rate=RATE, input=True,
frames_per_buffer=CHUNK)

def read(**kwargs):
    return stream.read(CHUNK,**kwargs)