
import sys
from urllib import request
def fetch_words():
    book=request.urlopen('https://www.gutenberg.org/files/2554/2554-0.txt')
    red=book.read().decode('utf8').split()
    book_words=[]
    for a in red[:30]:
        book_words.append(a)
    book.close()
    return book_words

def print_words(book_words):
    for b in book_words:
        print (b)

def main():
    words=fetch_words()
    print_words(words)

if __name__ == '__main__':
    main()
