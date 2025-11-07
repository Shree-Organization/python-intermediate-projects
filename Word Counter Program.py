# Word Counter Program

def word_counter(filename):
    word_dict = {}
    
    # file reading
    with open(filename, "r") as file:
        text = file.read().lower()  # all in  lower case
    
    # word split 
    words = text.split()
    
    for word in words:
        word = word.strip(",.!?")  # punctuation remove
        word_dict[word] = word_dict.get(word, 0) + 1
    
    return word_dict


# Use
filename = "data.txt"
result = word_counter(filename)

print("Word Frequency:")
for word, count in result.items():
    print(f"{word}: {count}")
