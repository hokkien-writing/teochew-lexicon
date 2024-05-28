# 潮州話詞庫 (teochew-lexicon）

## 簡介

本項目收集潮州話所用字詞，無論是漢字還是白話字寫其。

> 潮州白話字，簡稱 PUJ，是古早來華傳教士根據當時汕頭地區其話語，使用羅馬字構造其潮州話文字系統。

## 進度

- [x] 初步收集漢字 4379個，並整理成 [han_list.txt](character/han_list.txt) 和 [puj_list.txt](character/puj_list.txt)。
- [ ] 整理常用詞語（進行中）。

## 相輔

### 字表

字表維護於 `character` 文件夾裏，按下底格式修改 [character/han_list.txt](character/han_list.txt) 後提交 PR。

格式爲：

```
漢字 PUJ{異體}(例詞)
```

例如：

```
斫 tok4{斲}(~斷)
```

* 注意：所有標點符號均爲西文模式。

### 詞庫

`classification` 文件夾中存放各類詞語，以 `{分類}.txt` 爲文件名，其內容按下底格式編寫：

```
{普通話}, {潮州話漢字}, {潮州話白話字}, {分級}, {引用簡寫}, {示例}
```

比如`124_動物-蟲.txt`中有：

```
書蟲, 册魚, Chheh-hṳ̂, L2, 汕頭話讀本, 本老冊內底有～
```

#### 分級

爲便利詞條使用，本倉庫按照詞語其常用程度，將詞語分爲三個等級：

* L0：非常常用。
* L1：一般常用。
* L2：毋常用。

應當注意，此三個等級其分別目前是相當粗糙佮主觀其，只能作爲參考。

#### 分類

分類由兩個部分合成，分別是：

* 分類碼：唯一標識該分類其碼，由3位數組成，前2位爲大類，後1位表示小類。例如：`124` 表示大類是 `12`，小類是`4`。
* 分類名。

此陣有入門、天地、時日等等分類，具體見 [classification](classification/) 目錄。

#### 引用

| 引用                                                         | 簡寫      |
| ------------------------------------------------------------ |---------|
| 明朝嘉靖丙寅年（四十五年、1566）刊本《重刊五色潮泉插科增入詩詞北曲勾欄荔鏡記戲文全集》 | 荔鏡記     |
| 明末,《重補摘錦潮調金花女一卷明末刊本-卷一》                 | 蘇六娘     |
| 1841, William Dean([美]璘为仁, 憐為仁).《First Lessons in the Tie-chiw Dialect(潮州話初級教程)》 | 潮州話初級教程 |
| 1883, Adele Marion Fielde([美]A.M.菲爾德, 斐姑娘).《A pronouncing and defining dictionary of the Swatow dialect, arranged according to syllables and tones(汕頭方言音義字典)》 | 斐姑娘字典   |
| 1883, Josiah Goddard([美]高德, 哥達德).《A Chinese and English vocabulary, in the Tie-chiu dialect(漢英潮州方言字典) | 高德字典    |
| 1883, Rudolf Lechler([德]黎力基), Samuel Wells Williams([美]衛三畏), William Duffus([英]卓威廉).《English-Chinese Vocabulary of the Vernacular Or Spoken Language of Swatow(英漢汕頭方言口語詞典)》 | 卓威廉詞典   |
| 1886, Lim Hiong Seng([新加坡]林雄成).《Handbook of the Swatow Vernacular(汕頭話讀本)》 | 汕頭話讀本   |
| 1992, 李新魁, 林伦伦.《潮汕方言词考释》                      | 考釋      |
| 1993, 林伦伦.《潮汕方言熟语辞典》                            | 熟語辭典    |


## 應用

1. 生成輸入法詞典，作爲拍字之用，見項目 [rime-teochew](https://github.com/hokkien-writing/rime-teochew)。
2. 生成《潮州話同音字表》，供學習之用，見項目 [teochew-homophone-list](https://github.com/hokkien-writing/teochew-homophone-list)。
3. 生成《潮州話怎呢呾》，普通話對照潮州話，見項目 [teochew-mandarin](https://github.com/hokkien-writing/teochew-mandarin)。
