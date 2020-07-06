#from pygame import mixer
#import time

#mixer.init()
#alert = mixer.Sound('beep-02.wav')
#time.sleep(5.0)

#alert.play()

from pybeep.pybeep import PyVibrate, PyBeep
PyBeep().beep()
PyBeep.beepn(3)

print("Done")
