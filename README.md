# 潮州話詞庫 (teochew-lexicon）

## 簡介

本項目收集潮州話所用字詞，無論是漢字還是白話字寫其。

> 潮州白話字，簡稱 PUJ，是古早來華傳教士根據當時汕頭地區其話語，使用羅馬字構造其潮州話文字系統。

## 進度

- [x] 初步收集漢字 4379個，並整理成 [han_list.txt](han_list.txt) 和 [puj_list.txt](puj_list.txt)。
- [ ] 整理常用詞語。

## 貢獻

1. 修改 [han_list.txt](han_list.txt)後提交 PR。
2. 在 issue 中提出問題或建議。

`han_list.txt` 中詞條格式爲：

```
漢字 PUJ{異體}(例詞)
```

例如：

```
斫 tok4{斲}(~斷)
```

* 注意：所有標點符號均爲西文模式。

## 用途

1. 生成輸入法詞典，作爲拍字之用，見項目 [rime-teochew](https://github.com/hokkien-writing/rime-teochew)。
2. 生成潮州話同音字表，供學習之用，見項目 [teochew-homophone-list](https://github.com/hokkien-writing/teochew-homophone-list)。
