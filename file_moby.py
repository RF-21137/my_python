punct = str.maketrans("", "", "!.,:;-?") 
with open("moby.txt") as infile, open("moby_clean.txt", "w") as outfile: 
    for line in infile: 
# приводим к нижнему регистру 
        cleaned_line = line.lower() 
# удаляем знаки 
        cleaned_line = cleaned_line.translate(punct) 
# делим на слова 
        words = cleaned_line.split() 
        cleaned_words = "\n".join(words) + "\n" 
# записываем в файл 
        outfile.write(cleaned_words)
