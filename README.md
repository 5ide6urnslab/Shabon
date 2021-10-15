# Shabon
Fabcafe Kyoto主催 COUNTER POINTの「インクルーシブなアソビ」で製作したシャボン玉装置Shabon（シャボン）のレポジトリ。

<img class="photo" src="https://github.com/5ide6urnslab/Shabon/blob/master/resource/inclusive_1.jpg" width="480px" />


https://fabcafe.com/jp/magazine/report/20210929_counter-point-report


## Description
ダイソー製シャボン玉装置BUBBLEを改造して、任天堂Switch Joy-Conで操作するためのシステム「Shabon」となる。raspberry pi zeroとJoy-ConをBlutoothで接続し、シャボン玉装置のDCモーターをトランジスタ「2SC2655L-Y-T9N-K」で制御する。トランジスタは熱を持つため、ヒートシンクを付ける事を推奨(放熱接着剤などでヒートシンクを付けば良い)。このシステムは、「インクルーシブなアソビ」プロジェクトを通して、企画での検証や開発中となります。

<img class="photo" src="https://github.com/5ide6urnslab/Shabon/blob/master/resource/Shabon_bb.jpg" width="480px" />


#### 抵抗（R1）について
抵抗R1はDCモーターの定格負荷時電流から求める。負荷電流は0.7Aのため、トランジスタのコレクターには0.7A以上流れる様にベース電流を調整する必要がある。トランジスタ「2SC2655L-Y-T9N-K」のデータシートに記載されているコレクタ電流と電圧の関係グラフからモーターを4.5vでコレクタ電流0.7Aの場合、ベース電流は6mAとなる(raspi zeroのGPIOは8mA)。R1抵抗は1kΩとなる。

#### 抵抗（R2）について
トランジスタの安定化とベース電流をLOWにした場合に電流をGNDに逃がすため、10kΩとする。（R1 <= R2）

#### 抵抗（RE）について
今回の試作では使用していないが、エミッタ抵抗（エミッタ端子とGND間）を入れることによりトランジスタの温度変化に対する挙動を安定化することができる。

#### 抵抗（RC）について
今回の試作では使用していないが、コレクタ負荷抵抗（モーターとVCC間）として、VCCからの大電流をこの抵抗によって制限することができる。VCCとコレクタ間に負荷抵抗がない場合、トランジスタが壊れる場合がある。入力インピーダンスの1/100でRC抵抗値は決めれば良い。

## Installation
(1) raspi zeroのベース環境を構築する （ベース環境はraspi Desktopで問題ない。起動速度を上げたい場合は、ライト版の環境を推奨）
https://www.raspberrypi.com

(2) 必要なソースコードをダウンロードする  
https://github.com/5ide6urnslab/Shabon

(3) raspi zeroにSSH接続し、（2）でダウンロードした下記ファイルを/usr/loca/bin/にコピーする
・autoConnector.sh
・putonLed.py
・switchJoycon.py
・blinkLed.py

(4)cronにbluetooth接続のための監視周期を追加する
　*/2 * * * * bash /usr/local/bin/autoConnector.sh
 
## Running the Project
操作マニュアルを参照し、Shabonシステムを動作させる。
http://www.irobot.com/About-iRobot/STEM/Create-2/Projects.aspx


## Reference
(1) raspi zero Specifition
https://www.raspberrypi.com

## Copyright
© 2015 All Rights Reserved. iRobot, Roomba and Create are registered trademarks of iRobot Corporation.  
   http://www.irobot.com/About-iRobot/ST...
   
© 2013 Makeblock Co., Ltd. All Rights Reserved.  
   http://www.makeblock.cc

© 2015 All Rights Reserved. Sparkfun is a trademark of Sparkfun Electronics.  
   https://www.sparkfun.com

## License
##### About this manual and image files.
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />Show Kawabata and ミラスタ！つながる ”こうえん” プロジェクト is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

##### About this software. 
Released under the MIT license. http://opensource.org/licenses/mit-license.php

## Credit
Electronics:   [Show Kawabata](http://www.showkawabata.net)  
Planning:      [ミラスタ！つながる ”こうえん” プロジェクト](https://mirasta2020.wixsite.com/inclusive)
Residence:     [Fabcafe Kyoto COUNTER POINT](https://fabcafe.com/jp/labs/kyoto/counterpoint)
Photo:         [Fabcafe Kyoto COUNTER POINT](https://fabcafe.com/jp/labs/kyoto/counterpoint)
