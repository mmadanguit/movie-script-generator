"""
Mini Project 3: Text Mining and Analysis

@author: mmadanguit
"""

def get_scripts():
    """ Return a list of all movie titles in the scripts folder
    """
    cwd = os.getcwd()
    filepath = os.path.join(cwd,'scripts')
    titles = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            titles.append(file)
    return titles

def format_script(title):
    """ Returns script with header, end line, and page numbers removed

        title: script file name
    """
    filepath = os.path.join(os.getcwd(),'scripts',title)
    file = open(filepath, 'r')
    text = file.read()
    start = text.find('EXT')
    end = text.find('THE END')
    page_numbers = ['%s' % i for i in range(0,10)]
    for number in page_numbers:
        text = text[start:end].replace(number,'')
    return text.split()

def create_dictionary():
    """ Returns a dictionary that maps prefixes to a nested dictionary containing
        suffixes and their number of occurrences (all based on the language
        used in every movie script)
    """
    titles = get_scripts()
    d = dict()
    for title in titles:
        text = format_script(title)
        for i in range(len(text)-1):
            suffixes = d.get(text[i],dict())
            suffixes[text[i+1]] = suffixes.get(text[i+1],0)+1
            d[text[i]] = suffixes
    return d

def sort_dictionary():
    """ Returns a dictionary that maps prefixes to common suffixes (based on the
        language used in every movie script)
    """
    d = create_dictionary()
    for key, value in d.items():
        common_suffixes = []
        suffixes_sorted = sorted(value.items(), key=lambda item:item[1], reverse=True)
        for word, freq in suffixes_sorted:
            common_suffixes.append(word)
        d[key] = common_suffixes[:10]
    return d

def markov_analysis(num_words):
    """ Returns a script generated using Markov Analysis

        title: movie title stirng
        num_words: number of words in generated script
    """
    d = sort_dictionary()
    starter = random.choice(['EXT.','INT.'])
    text = [starter]
    i = 0
    for i in range(num_words-1):
        suffix = random.choice(d[text[i]])
        text.append(suffix)
        i += 1
    return ' '.join(text)

if __name__ == "__main__":
    import os
    import random

    print(markov_analysis(500))
