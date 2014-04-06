# getLimbaughSpeeches.py
# Searches through the archives for Rush Limbaugh speeches,
# and stores them in the specified folder
# Dan Scarafoni, J. Hassler Thurston
# HackNY Fall 2014 Hackathon
# April 5-6, 2014

import datetime, urllib
from bs4 import BeautifulSoup, element

def get_limbaugh_speeches(folder, num_days):
    # search through the archives starting from the day before
    # (they don't update their website that often),
    # and going back until num_days
    yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
    date_list = get_datestrings(yesterday, num_days)
    prependurl = 'http://www.rushlimbaugh.com/daily/'
    # get the URLs to parse
    url_list = [prependurl + day for day in date_list]
    # parse the webpages
    for url in url_list:
        get_speeches(folder, url)


# returns a list of dates (as strings) starting from the given date, going back num_days
# from http://stackoverflow.com/questions/993358/creating-a-range-of-dates-in-python
def get_datestrings(date, num_days):
    ls = [ date - datetime.timedelta(days=x) for x in range(0,num_days) ]
    return [str(day.year)+'/'+str(day.month).rjust(2,'0')+'/'+str(day.day).rjust(2,'0') for day in ls]



# archives the speeches from Rush Limbaugh's site for a given day
def get_speeches(folder, url):
    # get HTML from webpage
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    # from http://stackoverflow.com/questions/6803034/using-beautifulsoup-to-extract-anchor-tag-values
    # get all anchors
    for a in soup.find_all('a'):
        if a.contents[0] == 'Read More' or a.contents[0] == 'Read Transcript':
            # get all the transcripts from that day
            get_transcript(folder, 'http://www.rushlimbaugh.com' + a['href'])


# gets a specific transcript of a Rush Limbaugh speech
def get_transcript(folder, url):
    # get HTML from webpage
    print url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    # from http://stackoverflow.com/questions/13556567/parsing-meta-tag-with-beautiful-soup-and-python
    text2 = soup.find_all('section',{'itemprop':'articleBody'})
    if len(text2) == 0:
        print 0
        return
    else:
        # from http://stackoverflow.com/questions/19678546/convert-resultset-to-string-and-place-in-list
        all_paragraphs = text2[0].find_all('p')
        all_text = [p.contents[0] for p in all_paragraphs if type(p.contents[0]) == element.NavigableString]
        transcript_text = "".join(all_text)
        # get rid of non-ascii characters
        # from http://stackoverflow.com/questions/2743070/removing-non-ascii-characters-from-a-string-using-python-django
        ascii_text = (c for c in transcript_text if 0 < ord(c) < 127)
        # write transcript text to file
        filename = folder + str(url.strip('http://www.rushlimbaugh.com/daily/')).translate(None, '/') + '.txt'
        print filename
        f = open(filename, 'w')
        f.write('Rush Limbaugh\n')
        f.write("".join(ascii_text))
        f.close()






