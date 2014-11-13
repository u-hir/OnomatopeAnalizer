# coding: utf-8
import urllib2
import lxml.html

# アメーバ検索から上位50件のスニペットを取得する関数
# 引数は単数の文字列(クエリ)、返り値は文字列のリスト(スニペット)
def get_ameba_single(query):
  encoded_query = urllib2.quote(query)
  # ameba検索の検索URLを作成
  ameba_search_url = "http://search.ameba.jp/search.html?q="+encoded_query+"&row=50&profileRow=&target=blog&aid=&author=all&start=0"
  html = urllib2.urlopen(ameba_search_url).read() # html 取得
  root = lxml.html.fromstring(html) # ルート要素
  paragraphs = root.xpath('//p') # p要素をリストとして全て取得

  descriptions = []
  for paragraph in paragraphs:
    css_class = paragraph.get('class')

    # cssのクラスがdescriptionなら
    if css_class != "None" and css_class == "description":
      description_text = lxml.html.tostring(paragraph, method='text', encoding='utf-8') #テキストを文字列型で取得する
      descriptions.append(description_text)
  return descriptions

# アメーバ検索から上位50件のスニペットを取得する関数
# 引数は文字列のリスト(クエリ)、返り値は文字列のリスト(スニペット)
def get_ameba_multi(querys):
  querys_len = len(querys)
  combined_querys = "" # URLに挿入するクエリ文字列を初期化
  for index, query in enumerate(querys):
    encoded_query = urllib2.quote(query)
    combined_querys = combined_querys + encoded_query # クエリ文字列を追加する
    if (index<querys_len-1):
      combined_querys = combined_querys + "+" # クエリ文字列の間に+を入れる
  # ameba検索の検索URLを作成
  ameba_search_url = "http://search.ameba.jp/search.html?q="+combined_querys+"&row=50&profileRow=&target=blog&aid=&author=all&start=0"
  html = urllib2.urlopen(ameba_search_url).read() # html 取得
  root = lxml.html.fromstring(html) # ルート要素
  paragraphs = root.xpath('//p') # p要素をリストとして全て取得

  descriptions = []
  for paragraph in paragraphs:
    css_class = paragraph.get('class')

    # cssのクラスがdescriptionなら
    if css_class != "None" and css_class == "description":
      description_text = lxml.html.tostring(paragraph, method='text', encoding='utf-8') #テキストを文字列型で取得する
      descriptions.append(description_text)
  return descriptions


if (__name__ == '__main__'):
  tests = get_ameba_single('テスト')
  for test in tests:
    print(test)
