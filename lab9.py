####################################
# Ryan Dorrity, Nathan Warren-Acord
# lab 9
# 11/15/2018
####################################




# Saves a sound file
def saveSound(sound, name):
  writeSoundTo(sound, "C:\\Users\\rdorr\\OneDrive\\Documents\\GitHub\\lab-8\\output\\" + name)
  
# returns a sound file
def getS():
  s = pickAFile()
  sd = makeSound(s)
  return sd
  
# Increases volume of sound file
def increaseVolume(sound, x):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * x)
   explore(sound)
      
# Decreases sound of file
def decreaseVolume(sound, x):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value / x)
   explore(sound)
      
# Changes volume of sound file      
def changeVolume(sound, factor):
   if factor < 0:
     decreaseVolume(sound, abs(factor))
   else:
     increaseVolume(sound, factor)
     

def maxSample(sound):
  temp = 0
  for sample in getSamples(sound):
    temp = max(temp, getSampleValue(sample))
  print temp
  return temp
  
  
  
#def maxVolume(sound):
  
  
  
def goToEleven(sound):
  temp = maxSample(sound)
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > 0:
      setSampleValue(sample, temp)
    elif value < 0:
      setSampleValue(sample, -temp)
  explore(sound)  