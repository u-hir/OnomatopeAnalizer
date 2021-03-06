# coding: utf-8
import urllib2
import lxml.html

# アメーバ検索から上位300のスニペットを取得する関数
# 引数は文字列(クエリオノマトペ)、返り値は文字列のリスト(スニペット)
def get_ameba(query):
  encoded_query = urllib2.quote(query) #クエリをURLの%xxに置換
  # ameba検索の検索URLを作成
  ameba_search_url = "http://search.ameba.jp/search.html?q="+query+"&row=300&profileRow=&target=blog&aid=&author=all&start=0"
  html = urllib2.urlopen(ameba_search_url).read() # html 取得
  root = lxml.html.fromstring(html) # ルート要素
  paragraphs = root.xpath('//p') # p要素をリストとして全て取得

  descriptions = []
  for paragraph in paragraphs:
    css_class = paragraph.get('class')

    # cssのクラスがdescriptionなら
    if css_class != "None" and css_class == "description":
      description_text = lxml.html.tostring(paragraph, method='text', encoding='utf-8') #テキストを文字列型で取得する
      description_text = description_text.replace('\n', '')
      description_text = description_text.replace('\r', '')
      descriptions.append(description_text)
  return descriptions

if (__name__ == '__main__'):
  tests = get_ameba('取得')
  print "----------------------------------------------------"
  for test in tests:
    print(test)
