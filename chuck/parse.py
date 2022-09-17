list_url = [
#        'https://transcripts.foreverdreaming.org/viewtopic.php?f=178&t=16127&sid=c4a1ce8bcd3678b8f46177326fe24d90',
#        'https://transcripts.foreverdreaming.org/viewtopic.php?f=178&t=16176&sid=d2863a3efe14fe7205b2dca30a12ce4c',
           ]

from urllib.request import urlopen
from bs4 import BeautifulSoup

for url in list_url:
    result = urlopen(url)
    bs = BeautifulSoup(result.read(), "html.parser")

    title = bs.select('h2')[0].text.strip()
    print(title)

    list_p = bs.select('p')
    with open("{0}.md".format(title), "w") as f:
        f.write("# {0}\n\n".format(title))
        print(list_p[0].text.strip())
        for element in list_p[1:-3]:
            s = element.text.strip()
            if s == "":
                continue
            elif s.find("Chuck") != -1 and s.find("Season") != -1 and s.find("Episode") != -1:
                f.write("***\n")
            else:
                f.write("- {0}\n".format(element.text))
        print(list_p[-3].text.strip())
        print(list_p[-2].text.strip())
        print(list_p[-1].text.strip())
