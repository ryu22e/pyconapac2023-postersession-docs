# どんな工夫をしてきたか
## 開催回ごとに担当コアスタッフがサポート
Python Boot Campでは開催が決まると現地スタッフをサポートする担当コアスタッフが必ず一人付きます。
現地スタッフはイベントの準備や開催時に困ったことがあればいつでもSlackで相談できます。

## 必要なタスクはすべてマニュアル化
現地スタッフが行うタスクは以下のマニュアルとしてまとめられています。

<https://pycamp.pycon.jp/organize/index.html>

また、タスク管理にはJIRAを採用していて、いつまでに何をすればいいか明示しています。

```{figure} our_approach/JIRA.*
:name: JIRAの画面
:alt: JIRAの画面
:align: center

JIRAの画面
```

## Slack botで諸々を自動化
イベント準備に関する諸々のタスクをSlack botで自動化しています。

### JIRAタスクを作成
JIRAタスクは毎回必要なタスクが決まっていますが、数が多くて手動で作るのは手間がかかるので、
Slack botですべて作成してくれるようになっています。

```{figure} our_approach/slack-bot-1.*
:name: Slack bot経由でJIRAタスクを作成
:alt: Slack bot経由でJIRAタスクを作成
:align: center

Slack bot経由でJIRAタスクを作成
```

### イベント用のロゴを作成
イベント用のロゴの作成もSlack botで作れます。

```{figure} our_approach/slack-bot-2.*
:name: Slack bot経由でイベント用のロゴを作成
:alt: Slack bot経由でイベント用のロゴを作成
:align: center

Slack bot経由でイベント用のロゴを作成
```

コマンドを実行すると、以下のように開催地域名を埋め込んだロゴを作成してくれます。

```{figure} our_approach/event-logo-sample.*
:name: 作成されたイベント用のロゴ
:alt: 作成されたイベント用のロゴ
:align: center

作成されたイベント用のロゴ
```

## コミュニケーションはSlackとZoomでオンラインで行う
Python Boot Campの関係者はそれぞれ別の都道府県に在住している場合が多いので、コミュニケーションは基本的にオンライン上で行います。

非同期で行えるコミュニケーションはSlack、
事前ミーティングや開催後の振り返りミーティングなど関係者が一度に集まる必要があるミーティングはZoomを使います。

## コロナ禍でも活動を止めない工夫
2019年12月ごろに始まったコロナ禍は世界中のコミュニティの活動に大きな影響を与えました。
Python Boot Campもその例に漏れず、2019〜2021年の開催回数を見ると、コロナ禍でほぼ開催が止まっている状況がわかります。

* 2019年: 10回
* 2020年: 1回
* 2021年: 1回

表に見える活動が止まってしまうことでコミュニティの存在感が薄れてしまうことを私たちは心配していました。
そこで、私たちはオンラインでできる範囲の活動をやっていこうと考え、以下について取り組んできました。

### 過去回の現地スタッフにインタビュー
Python Boot Campを開催した人たちがコミュニティ活動を楽しんでいる様子を知ってもらいたいという意図で、
過去回の現地スタッフにオンラインでインタビューを行いました。
近況について話してもらった内容を[PyCon JP Blog](https://pyconjp.blogspot.com/)に公開しています。

```{list-table} 記事一覧
:widths: 10 15 30
:header-rows: 1

 * - 地域名
   - コミュニティ名
   - 記事URL
 * - 山梨
   - shingen.py
   - [Python Boot Campその後 ― Shingen.py](https://pyconjp.blogspot.com/2020/12/after-pycamp-shingen-py.html)
 * - 香川
   - UDONPy
   - [Python Boot Campその後 ― UDONPy](https://pyconjp.blogspot.com/2020/12/after-pycamp-udonpy.html)
 * - 神奈川
   - Shonan.py
   - [Python Boot Campその後 ― Shonan.py](https://pyconjp.blogspot.com/2020/11/after-pycamp-shonan-py.html.html)
 * - 広島
   - すごい広島 IT初心者の会

     （旧: すごい広島 with Python）
   - [Python Boot Campその後 ― すごい広島 with Python](https://pyconjp.blogspot.com/2020/09/after-pycamp-sugoi-hiroshima-with-python.html)
 * - 岡山
   - 岡山Python勉強会
   - [Python Boot Campその後 ― 岡山Python勉強会](https://pyconjp.blogspot.com/2020/08/after-pycamp-okayama-python-benkyokai.html)
 * - 岐阜
   - 飛騨高山Pythonの会
   - [Python Boot Campその後 ― 飛騨高山Pythonの会](https://pyconjp.blogspot.com/2020/06/after-pycamp-hidatakayama-python-kai.html)
```

### Python Boot Camp オンライン相談会を開催
Python Boot Campに興味があるがコロナ禍のため開催をためらっている人のために、オンラインでPython Boot Campについて知ってもらう機会を提供しようと考えました。
[オープンソースカンファレンス](https://www.ospn.jp/)でコアスタッフや過去回の現地スタッフが登壇し、イベントの魅力についてアピールしました。

登壇の様子は以下YouTubeで動画が公開されています。

<iframe width="560" height="315" src="https://www.youtube.com/embed/EynlaLXxjd8?si=4CvZpiCv_ngR8TgH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/uFBKKSIdTz8?si=KsaJszG91wXUXg9c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## オリジナルグッズの作成

### ステッカー
Python Boot Campの参加者、TAには、イベントに参加した証としてPython Boot Campステッカーを渡しています。

```{figure} our_approach/pycamp-sticker.*
:name: Python Boot Campステッカー
:alt: Python Boot Campステッカー
:align: center

Python Boot Campステッカー
```

### Tシャツ
Python Boot Campの開催をサポートしてくれた現地スタッフ、TA、講師に感謝の意を込めてオリジナルTシャツをプレゼントしています。
TA、現地スタッフは2回以上参加してくれた人のみが対象です。

PyCon JP開催時には今までの開催に関わった人たちが同じTシャツを来て集まって、同窓会のように盛り上がっています。
おそらく今日もこのTシャツを着ている人がいるはずです！

```{figure} our_approach/pycamp-t-shirt.*
:name: Python Boot CampTシャツ
:alt: Python Boot CampTシャツ
:align: center

Python Boot CampTシャツ
```
