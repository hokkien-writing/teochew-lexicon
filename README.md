# 潮州漢字及白話字（teochew-character）

## 簡介

本項目收集潮州漢字及其白話字，並生成同音字表及潮州話拍字方案詞典文件，以便呾潮州話其儂可學字拍字。

潮州漢字是潮州話中使用到的漢字集。 

潮州白話字，簡稱 PUJ，是古早來華傳教士根據當時汕頭地區的話語使用羅馬字構造的潮州話文字系統。

## 同音字表

* Markdown格式由腳本生成，見 [潮州話同音字表.md](潮州話同音字表.md)。 
* PDF格式採用 Obsidian插件生成，見 [潮州話同音字表.pdf](潮州話同音字表.pdf)。

## 輸入法詞典

本項目生成了兩個文件[teochew.han.dict.yaml](teochew.han.dict.yaml) 和 [teochew.puj.dict.yaml](teochew.puj.dict.yaml) 用作姊妹項目 [rime-teochew](https://github.com/hokkien-writing/rime-teochew) 中的潮州話拍字方案的詞典文件。

如想了解如何在各個平台上使用潮州話拍字方案，請訪問該[項目](https://github.com/hokkien-writing/rime-teochew)。

## 完成度

- [ ] 漢字（4379個）

- [x] PUJ

## 貢獻

修改 [han_list.txt](han_list.txt)，然後運行 `python3 main.py` 即可生成新的同音字表。

歡迎大家提交 PR，或者在 issue 中提出建議。
