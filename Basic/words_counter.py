
sentence = input("Enter your sentence: ")

words = sentence.split()

print(f"The total words in this sentence are: {len(words)}")
print(f"The total chars in this sentence are: {len(sentence)}")

# exclude spaces

no_spaces =  sentence.replace(' ','')
print(f"The total chars in this sentence without spaces are: {len(no_spaces)}")
