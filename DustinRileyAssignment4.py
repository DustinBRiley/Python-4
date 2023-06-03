# INF360 - Programming in Python
# Dustin Riley
# Assignment 4
# (1/1 point) - Initial comments*

from pathlib import Path
import re

foundCount = 0
theCount = 0
foundTemp = 0
theTemp = 0
newStory = ""

textFile = open(Path('./story.txt'))
story = textFile.readlines()    # (2/2 points) - Read the file story.txt and store the lines as a variable called story.You must use relative paths, assume the story.txt file is in the same folder as your script.
for line in story:
    re.findall("Sherlock Holmes", line) # (5/5 points) - Write a regular expression that will find all occurances of the phrase,  "Sherlock Holmes".
    line, foundCount = re.subn("Sherlock Holmes", "Dustin Riley", line)   # (5/5 points) - Using the substitue method, replace all occurances of "Sherlock Holmes" with your name, storing the count of these occurances as a variable called foundCount.
    foundTemp += foundCount
    re.findall("the", line) # (2/2 points) - Write a regular expression that will find all occurances of the phrase, "the".
    theCount = len(re.findall("the", line))  # (3/3 points) - Create a variable called theCount, that stores the total number of occurances of the phrase "the".
    theTemp += theCount
    newStory += line
foundCount = foundTemp
theCount = theTemp
print(f"Sherlock Holmes, Dustin Riley, {foundCount}")  # (3/3 points) - Print to the user, the original name, the replacement name, and the total number of occurances using a print command with a formatted string literal using a string that starts with f".
print(f"{theCount}") # (3/3 points) - Print to the user the a string that tells the user the total number of occurances of "the" using a print command with a formatted string literal using a string that starts with f".
open(Path('./new_story.txt'), "x").write(newStory)    # (1/1 points) - Save the story out to a new file called new_story.txt.
textFile.close()
