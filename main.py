import os

def get_current_selection():
    selection = os.popen("xsel -o").read()

    # selections of more than three words will be ignored to spare linguee
    # unnecessary traffic and avoid accidental uploads of user data
    if len(selection.split()) > 3: return

    return selection


import requests
from bs4 import BeautifulSoup

def translate(query, language1="english", language2="german"):
    # if you want to translate from or to a different language either change the
    # default parameters in this function or pass sufficient alternatives in the
    # main part of this programm, when this function is called
    url = "https://www.linguee.com/%s-%s/search?query=%s" % (language1, language2, query)

    html = requests.get(url).text
    parsed_html = BeautifulSoup(html, features='html5lib')
    lemmata = parsed_html.find_all("div", { "class": "lemma featured" })
    if not lemmata: return

    result = ""
    for lemma in lemmata:
        result += "\n"

        wordtype = lemma.find("span", { "class": "tag_wordtype" })
        if wordtype: # lemmata _do not_ require a wordtype!
            result += "<b>%s</b>\n" % wordtype.text.upper()

        translations = lemma.find_all("a", { "class": "dictLink featured" })
        for t in translations:
            result += "• %s\n" % t.text

    return result.rstrip()


import notify2
import sys

if __name__ == '__main__':
    if not notify2.init("lingue-to-notification"):
        sys.exit(1)

    query = get_current_selection()
    if not query:
        sys.exit(1)

    translation = translate(query)
    if not translation:
        sys.exit(1)

    n = notify2.Notification(query, translation)

    n.timeout = 5000 # miliseconds 

    if not n.show():
        sys.exit(1)
