# coding: utf-8

import sys

from gensim.models import word2vec

#data = word2vec.Text8Corpus('data.txt')
#model = word2vec.Word2Vec(data, size=200)
model = word2vec.Word2Vec.load("onomatope.model")

word = sys.argv[1]
u = word.decode('utf-8')
out=model.most_similar(positive=[u])
for x in out:
    print x[0],x[1]
