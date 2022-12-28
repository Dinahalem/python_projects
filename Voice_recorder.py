#This program is Voice Recorder
# the first install two library: pip install sounddevice
#                                pip install scipy
# Then limit frequency and duration for record
# once print Recording, the user starts record for 10 sec

import sounddevice
from scipy.io.wavfile import write   #save record 

fps= 44100   #frequency
duration= 10   # 10 second duration recording
print("Recording...")
recording = sounddevice.rec(int(duration*fps), samplerate=fps, channels= 2)
sounddevice.wait()
print("Done!")
write("output.wav", fps, recording)    # output.wav is name of record file after save



