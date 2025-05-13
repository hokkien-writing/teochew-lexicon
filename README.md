# 潮州話詞庫 (teochew-lexicon）

## 簡介

本項目收集潮州話所用字詞，無論是漢字還是白話字寫其。

> 潮州白話字，簡稱 PUJ，是古早來華傳教士根據當時汕頭地區其話語，使用羅馬字構造其潮州話文字系統。


## 相輔

### 字表

修改 [character.csv](character.csv) 後提交 PR。


### 詞庫

修改 [phrase.csv](phrase.csv) 後提交 PR。

### 對話

修改 [conversation.csv](conversation.csv) 後提交 PR。

#### 分級

爲便利詞條使用，本倉庫按照詞語其常用程度佮組詞能力，將詞語分：

- 常用程度四個等級：
  - 0 特別常用
  - 1 常用
  - 2 毋常用
  - 3 特別毋常用
- 組詞能力三個等級：
  - 0 特別強
  - 1 強
  - 2 毋強

計共十二個等級：

| 等級          | 常用程度   | 組詞能力 |
| ------------- | ---------- | -------- |
| k00           | 特別常用   | 特別強   |
| k01           | 特別常用   | 強       |
| k02           | 特別常用   | 毋強     |
| k10           | 常用       | 特別強   |
| k11           | 常用       | 強       |
| **k12(默認)** | 常用       | 毋強     |
| k20           | 毋常用     | 特別強   |
| k21           | 毋常用     | 強       |
| k22           | 毋常用     | 毋強     |
| k30           | 特別毋常用 | 特別強   |
| k31           | 特別毋常用 | 強       |
| k32           | 特別毋常用 | 毋強     |

> 除非設置，否則默認都是 k12，即常用、毋強。

應當注意，此十二個等級其分別目前是相當粗糙佮主觀其，只能作爲參考。


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
