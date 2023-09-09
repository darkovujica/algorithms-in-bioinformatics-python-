Pattern = input()
Text = input()

def Broj(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            print(i, end=" ")

Broj(Text, Pattern)
