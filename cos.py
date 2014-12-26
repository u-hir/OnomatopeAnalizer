#!/usr/bin/env python
import numpy as np
import scipy.spatial.distance
 
if __name__ == '__main__':
    x = np.array([1, 1, 1, 1, 1])
    y = np.array([1, 0, 1, 0, 1])
    z = np.array([0, 1, 0, 0, 0])
 
    print 1 - scipy.spatial.distance.cosine(x, y)
    print 1 - scipy.spatial.distance.cosine(x, z)

a = {"a":1, "b":2}
b = {"a":3, "c":4}

for w in set(a+b):#和を出して被りを消す
    if w :
        print w

#それぞれの数字を出して新しいリストを作る
#対応する単語は別のリストにしても良い
#上のベクトル計算に食わして、類似度判定
