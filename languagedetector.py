#coded by Bisno Das

from langdetect import detect

text = input(" Enter Any Text In Any Language ==> ")
print(" Your Language is :",detect(text))