import requests
from lxml import etree
import lxml.html
import csv

def parse(url):
    api = requests.get(url)
    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath('Код с сайта, что нужно вытащить')
    text_translate = tree.xpath('Код с сайта, что нужно вытащить')
    for i in range(len(text_original)):
        print(text_original[i], text_translate[i])

def main():
    parse("https://www.amalgama-lab.com/songs/t/tones_and_i/dance_monkey.html")

if __name__ == "__main__":
    main()
