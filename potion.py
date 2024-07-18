import re
import urllib.request

def poison(s, n):
    s = urllib.request.urlopen("http://localhost:8080/poison?string=" + s + "&num=" + str(n)).read().decode("utf-8")
    return s

def potion(str):
    return re.sub( '[^A-Za-z0-9]+', '', str). lower()

poisoned_string = poison("string", 3)

print("Poisoned String: " + poisoned_string)
print ("Restored String: " + potion(poisoned_string))

poisoned_string = poison("malwareus", 2)
print("Poisoned String: " + poisoned_string)
print ("Restored String: " + potion(poisoned_string))