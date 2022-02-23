from bs4 import BeautifulSoup

html_str = """
<html>
<body>
    <ul>
        <li>인공지능</li>
        <li>Big Data</li>
        <li>로봇</li>
    <ul>
    <ul class='item'>
        <li>파이썬</li>
        <li>자바</li>
        <li>자바스크립트</li>
    </ul>
        
</body>
</html>
"""

soup = BeautifulSoup(html_str, "html.parser")
#print(soup)
#ul = soup.find("ul")
# 선택자로 찾기 - 딕셔너리 형태
ul = soup.find("ul", attrs={'class':'item'})
print(ul)
print(ul.text)