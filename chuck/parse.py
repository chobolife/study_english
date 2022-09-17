list_url_t = [
    16127, 16176, 16177, 16178, 16179, 16180, 16181, 16182, 16183, 16184, 16185, 16186, 16187,
#    16188, 16189, 16190, 16191, 16192, 16193, 16194, 16195, 16196, 16197, 16198, 16199, 16200, 16201, 16202, 16203, 16204, 16205, 16206, 16207, 16208, 16209,
#    16210, 16211, 16212, 16213, 16214, 16215, 16216, 16217, 16218, 16219, 16220, 16221, 16222, 16223, 16224, 16225, 16226, 16227, 16228,
#    16229, 16230, 16231, 16232, 16233, 16234, 16235, 16236, 16237, 16238, 16239, 16240, 16241, 16242, 16243, 16244, 16245, 16246, 16247, 16248, 16249, 16250, 16251, 16252,
#    16253, 16254, 16255, 16256, 16257, 16258, 16259 ,16260, 16261, 16262, 16263, 16264 ,16265
             ]

from urllib.request import urlopen
from bs4 import BeautifulSoup

for t in list_url_t:
    url = 'https://transcripts.foreverdreaming.org/viewtopic.php?&t={0}'.format(t)
    print(url)

    result = urlopen(url)
    bs = BeautifulSoup(result.read(), "html.parser")

    title = bs.select('h2')[0].text.strip()
    print(title)

    list_p = bs.select('p')
    with open("{0}.md".format(title[3:]), "w") as f:
        f.write("# {0}\n\n".format(title[8:]))
        print(list_p[0].text.strip())
        for element in list_p[1:-3]:
            s = element.text.strip()
            if s == "":
                continue
            elif s.find("Chuck") != -1 and s.find("Season") != -1 and s.find("Episode") != -1:
                print(s)
                f.write("***\n")
            else:
                s = s.replace('*', '\*')
                f.write("- {0}\n".format(s))
        print(list_p[-3].text.strip())
        print(list_p[-2].text.strip())
        print(list_p[-1].text.strip())
        print()
