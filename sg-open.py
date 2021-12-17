import webbrowser
import random
url="https://www.sg-siken.com/kakomon/"
url_year=[28,29,30,31,1]
url_serson=int(1)
mon = [1,2,3]
if url_serson==1:
    url_serson=str('haru')
else:
    url_serson=str('aki')
url_year=random.choice(url_year)
mon=random.choice(mon)
url_year='%02d' % url_year
mon='%02d' % mon
if url_year=='01':
    url_serson='aki'
elif url_year=='31':
    url_serson='haru'
result=url + url_year + "_" + url_serson + "/pm" + mon + ".html"
webbrowser.open(result)