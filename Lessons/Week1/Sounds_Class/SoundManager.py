class SoundManager:
    fileNames = ["Deep Logic.wav", "End Game.wav", "Score.wav"]
    
    def __init__(self, s1):
        self.sound1 = s1
    
    def playMainMusic(self):
        self.sound1.play()
