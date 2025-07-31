import requests
from bs4 import BeautifulSoup

def get_passage():
    url = "https://ubf.org/daily-breads"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    passage_tag = soup.find("strong", string="Passage")
    if passage_tag:
        return passage_tag.next_sibling.strip()
    return None

def get_bible_text(passage):
    url = f"https://www.biblegateway.com/passage/?search={passage}&version=NIV;CUV"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    text = soup.get_text()
    return text[:1000]  # Short preview for demo

def get_meditation():
    url = "https://ubf.org/daily-breads"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    content_div = soup.find("div", class_="daily-bread-body")
    if content_div:
        return content_div.get_text(strip=True)
    return "未找到默想內容"

def get_daily_bread_content():
    passage = get_passage()
    if not passage:
        return "找不到今日經文"
    bible_text = get_bible_text(passage)
    meditation = get_meditation()
    return f"📖 今日經文 Passage：{passage}\n\n{bible_text}\n\n📝 默想內容：\n{meditation}"