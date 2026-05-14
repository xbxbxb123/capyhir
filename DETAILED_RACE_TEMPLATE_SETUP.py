#!/usr/bin/env python3

import os
from os.path import join

print("==================================================")
print("IT'S RECOMMENDED TO BACKUP YOUR MOD BEFORE CONTINUING.")
print("ENTER A NAME FOR YOUR RACE AND HIT ENTER.")
print("==================================================")
print()

while True:
  raceName = input("NAME:" )
  if len(raceName) < 4:
    print("Please choose a name at least 4 characters in length.")
    continue
  break

print("--------------------------------------------------")
print("THIS COULD TAKE SEVERAL MINUTES DEPENDING ON YOUR SYSTEM.")
print("DO NOT CLOSE THIS WINDOW.")
print("--------------------------------------------------")
print()
print("PLEASE WAIT...")

search = "skadvtest"
extensions = (".patch", ".species", ".animation", ".config", ".structure", ".recipe", ".monstertype", ".monsterpart", ".object", ".frames", ".activeitem", ".npctype", ".statuseffect", ".legs", ".chest", ".head", ".cinematic", ".item", ".tenant")

for root, dirs, files in os.walk(".", topdown=False):
  for name in files:
    path = join(root, name)

    if name.endswith(extensions):
      with open(path, "r") as file:
        data = file.read()
      if search in data:
        with open(path, "w") as file:
          file.write(data.replace(search, raceName))
      print("#", end="")

    if search in name:
      newPath = join(root, name.replace(search, raceName))
      os.rename(path, newPath)
  
  for name in dirs:
    if search in name:
      path = join(root, name)
      newPath = join(root, name.replace(search, raceName))
      os.rename(path, newPath)

print()
print("--------------------------------------------------")
print("THE SETUP HAS SUCCESSFULLY COMPLETED.")
print("You may now close this window by pressing enter.")
print("--------------------------------------------------")
input()
