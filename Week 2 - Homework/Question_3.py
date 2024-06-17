# Question 3 - This code only work while running in Google Colab.

def word_counting(file_path):
    with open(file_path, 'r') as file:
        document = file.read()
        document = document.lower()

    words = document.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Note:  Delete first # in link before run code in Google Colab.


#!gdown https://drive.google.com/uc?id = 1IBScGdW2xlNsc9v5zSAya548kNgiOrko
file_path = '/content/P1_data.txt'
word_counting(file_path)
