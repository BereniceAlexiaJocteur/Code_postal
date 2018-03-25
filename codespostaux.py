import urllib.request
import regex


def get_webpage(n):
    page = urllib.request.urlopen("https://www.codespostaux.com/home/r.php?q="+str(n)+"&Pays=FR").read(10000)
    return str(page)


def get_tags(n):
    titleList = regex.findall("<b>"+str(n)+" </b></td><td valign=\"top\"><b>(.*)</b>", get_webpage(n), overlapped=True)
    return titleList


def get_villes(n):
    for i in get_tags(n):
        nom_brut = i.split('<')[0]
        newstr = nom_brut.replace("\\'", "'")
        print(newstr)


get_villes(74300)
