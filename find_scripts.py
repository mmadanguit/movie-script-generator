
"""
Mini Project 3: Text Mining and Analysis

@author: mmadanguit
"""

def genre_html(genre):
    """ Returns the portion of HTML code from IMSdb.com containing the movie titles

        genre: movie genre string
    """
    genre = genre
    link = 'https://www.imsdb.com/genre/%s' % genre
    html = str(BeautifulSoup(requests.get(link).text, 'lxml'))

    start = html.find('<h1>Romance Movie Scripts</h1>')
    end = html[start:].find('</td>')
    return html[start:start+end]

def list_titles(genre):
    """ Returns a list of all the movie titles in a specified genre from IMSdb.com

        genre: movie genre string
    """
    text = genre_html(genre)
    num_titles = text.count('title=')

    titles = []
    for i in range(num_titles):
        start = text.find('title=')
        end = text[start+7:].find('">')
        title = text[start+7:start+end]
        titles.append(title)
        text = text[start+7:]

    return titles

def title_html(title):
    """ Returns the portion of HTML code from IMSdb.com containing the script

        title: movie title string
    """
    title = title.replace(' ', '-')
    link = 'https://www.imsdb.com/scripts/%s.html' % title
    html = str(BeautifulSoup(requests.get(link).text, 'lxml'))

    start = html.find('<pre>')
    end = html[start:].find('</pre')
    return html[start:start+end]

def save_script(title):
    """ Formats and saves the script to a file titled {Title}.txt.

        title: movie title string
    """
    script = title_html(title)
    script = script.replace('</b>','')
    script = script.replace('<b>','\n')

    cwd = os.getcwd()
    filepath = os.path.join(cwd,'scripts','%s.txt' % title)
    file = open(filepath, 'w')
    file.write(script)
    file.close()

def save_all_scripts(genre):
    """ Formats and saves all the scripts to a folder titled 'scripts'

        genre: movie genre string
    """
    if os.path.exists('scripts'):
        pass
    else:
        os.mkdir('scripts')

    titles = list_titles(genre)
    for title in titles:
        save_script(title)

if __name__ == "__main__":
    import os
    from bs4 import BeautifulSoup
    import requests

    save_all_scripts('Romance')
