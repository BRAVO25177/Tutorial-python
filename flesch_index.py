string = "In 1949, Rudolf Flesch published The Art of Readable Writing, in which he proposed a measure of text readability known as the Flesch Index . This index is based on the average number of syllables per word and the average number of words per sentence in a piece of text . Index scores usually range from 0 to 100, and they indicate readable prose for the following grade levels:"
sentences=0
syllables=0
for i in string:
    if i in ".!?;:":
        sentences += 1
x=list(string.split())
words=len(x)
vowels=['a', 'e', 'i', 'o', 'u']
for word in x:
    if len(word)<=3:
        syllables+=1
        continue
    l1 = ''
    for letter in word.lower():
        if letter.isalpha():
            if l1 and l1 in vowels and letter in vowels:
                syllables += 1
            l1 = letter
    if word.lower().endswith(("es", "ed")) :
        syllables -= 1
    if word.lower().endswith("e") and not word.lower().endswith("le"):
        syllables -= 1
    syllables = max(1, syllables)
F = 835.206 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
print("No.of sentences:", sentences)
print("No.of syllables:", syllables)
print("No of words:", words)
print("Flesch Index:", F)
if 0<=F<= 30:
    print("College")
elif 50<= F<= 60:
    print("High School")
elif 90<= F<= 100:
    print("Fourth Grade")
G = 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59
print('Grade level:', G)
