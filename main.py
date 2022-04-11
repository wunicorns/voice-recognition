import numpy as np
import sounddevice as sd

duration = 3  # seconds


def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata
    volume_norm = np.linalg.norm(indata) * 10
    #print("|" * int(volume_norm))

    print (volume_norm)


def voice_recognition():

    while True:

        with sd.RawStream(channels=2, dtype='int24', callback=callback):
            sd.sleep(int(duration * 1000))


if __name__ == '__main__':

    print(sd.query_devices())

    voice_recognition()

