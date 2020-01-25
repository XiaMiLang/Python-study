#抓取ptt電影版的網頁原始碼(html)


# import urllib.request as req
# url = "https://www.ptt.cc/bbs/movie/index.html"
# request = req.Request(url, headers={
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
# })
# with req.urlopen(request) as response:
#     data = response.read().decode("utf-8")
# print(data)



import urllib.request
url = "https://www.ptt.cc/bbs/movie/index.html"
#建立一個 Request 物件，附加 Request Headers 的資訊
requ = urllib.request.Request(url, headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
})
data = urllib.request.urlopen(requ).read().decode("utf-8")
# print(data)
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="title")
for t in titles:
    if t.a != None:
        print(t.a.string)