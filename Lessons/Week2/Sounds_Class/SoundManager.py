class SoundManager:
    def __init__(self):
        self.sounds = {}
    
    def addSound(self, key, sound):
        self.sounds[key] = sound
        
    def playSound(self, key):
        if key in self.sounds:
            self.sounds[key].play()
    
    def playMainMusic(self, isLoop = False):
        self.sounds["mainMusic"].rewind()
        if isLoop:
            self.sounds["mainMusic"].loop()
        else:
            self.sounds["mainMusic"].play()
            
    def playEndMusic(self, isLoop = False):
        self.sounds["endMusic"].rewind()
        if isLoop:
            self.sounds["endMusic"].loop()
        else:
            self.sounds["endMusic"].play()
    
    def playScore(self):
        self.sounds["score"].rewind()
        self.sounds["score"].play()
    
    def stopMainMusic(self):
        self.sounds["mainMusic"].pause()
    
    def stopEndMusic(self):
        self.sounds["endMusic"].pause()
        
    
    
