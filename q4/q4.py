import sys
import math

l = int(input())
h = int(input())
t = input()
letter_locations = []
for letter in t:
    offset = 0
    if 64 < ord(letter) < 91:
        offset = 65
    elif 96 < ord(letter) < 123:
        offset = 97
    start = (ord(letter) - offset) * l
    end = (ord(letter) - (offset - 1)) * l
    if offset == 0:
        start = 26 * l 
        end = 27 * l
    while start < end:
        letter_locations.append(start)
        start += 1
end_str = ""
for i in range(h):
    row = input()
    for i in letter_locations:
        end_str += row[i]
    end_str += "\n"
print(end_str)
