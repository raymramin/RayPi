from pygame import mixer
mixer.init()
alert = mixer.Sound('beep-02.wav')
alert.play()
print("Done")
