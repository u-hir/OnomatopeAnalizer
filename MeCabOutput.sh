#!/bin/sh

for file in sentences/*; do
    mecab -Owakati $file -u userdic.dic >> data.txt
    echo "ok"
done
