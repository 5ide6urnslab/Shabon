# Shabon
Fabcafe Kyoto主催 COUNTER POINTの「インクルーシブなアソビ」で製作したシャボン玉装置Shabon（シャボン）のレポジトリ。<br>
[COUNTER POINT第5期「インクルーシブなアソビ」活動報告](https://fabcafe.com/jp/magazine/report/20210929_counter-point-report)

![image](/resource/inclusive_1.jpg)


## Description
ダイソー製シャボン玉装置BUBBLEを改造して、任天堂Switch Joy-Conで操作するためのシステム「Shabon」となる。raspberry pi zeroとJoy-ConをBlutoothで接続し、シャボン玉装置のDCモーターをトランジスタ「2SC2655L-Y-T9N-K」で制御する。このシステムは、「インクルーシブなアソビ」プロジェクトを通して、開発と検証中。

![image2](/resource/Shabon_bb.jpg)

##### トランジスタについて
トランジスタは熱を持つため、ヒートシンクを付ける事を推奨(放熱接着剤などでヒートシンクを付ければ良い)。<br>
https://akizukidenshi.com/catalog/g/gI-08746/

##### 単三電池について
改造前のシャボン玉装置は単三電池3本で動作する。この単三電池3本をモーター制御用の電源とする。raspi zeroから電力供給する事も可能であるが、Bluetoothと併せてモーターを動作させるとモーターが数回しか動かない。電流不足になるため、外部電源でモーターを動作させることを推奨（モーターは単三電池2本でも動作可能）。

##### 抵抗（R1）について
抵抗R1はDCモーターの定格負荷時電流から求める。負荷電流は0.7Aのため、トランジスタのコレクターには0.7A以上流れる様にベース電流を調整する必要がある。トランジスタ「2SC2655L-Y-T9N-K」のデータシートに記載されているコレクタ電流と電圧の関係グラフからモーターを4.5vでコレクタ電流0.7Aの場合、ベース電流は6mAとなる(raspi zeroのGPIOは8mA)。R1抵抗は1kΩとなる。

##### 抵抗（R2）について
トランジスタの安定化とベース電流をLOWにした場合に電流をGNDに逃がすため、10kΩとする。（R1 <= R2）

##### 抵抗（RE）について
今回の試作では使用していないが、エミッタ抵抗（エミッタ端子とGND間）を入れることによりトランジスタの温度変化に対する挙動を安定化することができる。

##### 抵抗（RC）について
今回の試作では使用していないが、コレクタ負荷抵抗（モーターとVCC間）として、VCCからの大電流をこの抵抗によって制限することができる。VCCとコレクタ間に負荷抵抗がないと、トランジスタが壊れる場合がある。入力インピーダンスの1/100でRC抵抗値は決めれば良い。


## Installation
(1) raspi zeroのベース環境を構築する<br>
https://www.raspberrypi.com

※ベース環境はraspi Desktopで問題ない。起動速度を上げたい場合は、ライト版の環境を推奨。<br>

(2) 必要なソースコードをダウンロードする  
https://github.com/5ide6urnslab/Shabon

(3) raspi zeroにSSH接続し、2)でダウンロードした下記ファイルを/usr/loca/bin/にコピーする<br>
&ensp;・autoConnector.sh<br>
&ensp;・putonLed.py<br>
&ensp;・switchJoycon.py<br>
&ensp;・blinkLed.py<br>

(4)Joy-ConのBluetoothデバイスIDをBluezで取得する<br>
&ensp; bluetoothctl<br>
&ensp; scan on<br>

(5)autoConnector.shのBluetoothデバイスID（device変数）を追加する<br>
&ensp; device="BluetoothデバイスID"

(6)cronにbluetooth接続のための監視周期を追加する<br>
　*/2 * * * * bash /usr/local/bin/autoConnector.sh
 
(7)cronを開始する<br>
　/etc/init.d/cron start
 

## Running the Project
操作マニュアルを参照し、Shabonシステムを動作させる。<br>
https://github.com/5ide6urnslab/Shabon/blob/master/manual/20211008_Shabon-Manual.pdf


## Reference
(1) raspi zero Specifition <br>
https://www.raspberrypi.com

## Copyright
© All Rights Reserved. 自動回転シャボン玉メーカーBUBLLE is a trademark of Daiso.  
© All Rights Reserved. Astro E1 is a trademark of ANKER.  
© All Rights Reserved. Switch Joycon is a trademark of Nintendo.  
© All Rights Reserved. Bluetooth is a trademark of Bluetooth SIG.
   
## Credit
Electronics:   [Show Kawabata](http://www.showkawabata.net)  <br>
Planning:      [ミラスタ！つながる ”こうえん” プロジェクト](https://mirasta2020.wixsite.com/inclusive)<br>
Residence:     [Fabcafe Kyoto COUNTER POINT](https://fabcafe.com/jp/labs/kyoto/counterpoint)<br>
Photo:         [Fabcafe Kyoto COUNTER POINT](https://fabcafe.com/jp/labs/kyoto/counterpoint)<br>
