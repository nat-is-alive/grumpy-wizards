import re
import urllib.request

def poison(s, n):
    s = urllib.request.urlopen("http://localhost:8080/poison?string=" + s + "&num=" + str(n)).read().decode("utf-8")
    return s

def potion(str):
    return re.sub( '[^A-Za-z0-9]+', '', str). lower()

while True:
    string_input = input("Enter a string: ")
    number_input = int(input("Enter a number: "))

    poisoned_string = poison(string_input, number_input)

    print("Poisoned String: " + poisoned_string)
    print ("Restored String: " + potion(poisoned_string))