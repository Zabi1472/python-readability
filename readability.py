import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize

#getting text from user
Text = str(input("Enter your text here to check readability level: "))

#counting number of alphabets
count_of_alphabets=0
for i in Text:
    if(i.isalpha()):
        count_of_alphabets=count_of_alphabets + 1

#counting number of words
count_of_words = len(Text.split())

#counting number of sentences
sentences = sent_tokenize(Text)
count_of_sentences = len(sentences)

#calculating L & S
L = count_of_alphabets / count_of_words * 100
S = count_of_sentences / count_of_words * 100


#Coleman-Liau Index
Index = 0.0588 * (L) - 0.296 * (S) - 15.8

#Printing Output
if Index <1:
    print("Before Grade 1")
elif Index >=16:
    print("Grade 16+")
else:
    print("Grade ", round(Index))
