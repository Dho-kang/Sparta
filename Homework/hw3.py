import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

rank = 0
for song in songs:

    title = song.select_one('td.info > a.title.ellipsis')
    artist = song.select_one('td.info > a.artist.ellipsis')
    rank += 1
    print(rank, title.text.strip()+' ,', artist.text)


#
#  질문 1  지니페이지 음원순위에서 표시되는 랭킹도 스크래핑하려고 개발자도구 copy selctor를 이용하여 표시해봤더니,
# 숫자 밑에 순위변동 내용도 표시됩니다. 어떻게 분리할 있나요?
# #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#
#  질문 2
#   1)  title = song.select_one('td.info > a.title.ellipsis')
#      위 부분을 print(title.text) 실행해보면 여백이 발생합니다.
#   개발자 도구를 이용해서 해당부분을 보면, 공백이 있는 것으로 보이는데,  공백이 입력된 것이 맞다면
#   이건 디자인적 고려에서 공백을 삽입한 건가요?
#
#  2) 또 이 부분에  "" 와 ==$0 이 보이는데, 실제 화면에는 표시되지 않고 " "내의 텍스트만 표시되는데,
#  같은 텍스트 영역내에 있는 저것들이 왜 표시 안되는건가요? 공백 표시의문법으로 이해하면 되나요?
#




