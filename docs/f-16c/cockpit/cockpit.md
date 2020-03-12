# コックピット解説

<!-- markdownlint-disable MD033 -->

コックピットは以下の5つの主要なエリアに分けられる.

![dcs0-cockpit_overview](../images/dcs0-cockpit_overview.jpg)

- [Instrument Panel: 計器パネル](#instrument-panel)
- [Left Auxiliary Console: 左補助コンソール](#left-auxiliary-console)
- [Right Auxiliary Console: 右補助コンソール](#rifht-auxiliary-console)
- [Left Console: 左コンソール](#left-console)
- [Right Console: 右コンソール](#right-console)

## Instrument Panel: 計器パネル

![dcs1-instrument_panel](../images/dcs1-instrument_panel.jpg)

### Head-Up Display (HUD): ヘッドアップディスプレイ

<img src="../../images/dcs2-hud.jpg" align="right" hspace="10" width="300">

HUD には攻撃・航法・兵装・照準・着陸に関するシンボルが表示される.
また, 高度・速度・姿勢・方位などの航空機の飛行に必要なシンボルも表示される.

</br>

### AoA Indexer: 迎え角表示器

<img src="../../images/ss0-aoa_indexer.jpg" align="right" hspace="10" width="150">

迎え角 (AoA) 表示器には3つのライトがある.
上のライトが赤く点灯している場合は, AoA 14° 以上でエネルギーを消耗している.
中央の緑色のライトが点灯しているときは, AoA 11° から13° の間で, 最適な AoA を維持するオンスピード状態である.
下のライトが黄色に点灯していれば, AoA は11° 以下となり, エネルギーが蓄積している状態である.
これは同じ計器パネルの AoA ゲージと, ランディングギアを降ろしたときにHUDに表示される AoA ブラケットと連動している.

着陸時には AoA 11° から13° の間を維持する.
この AoA 表示器は, ランディングギアを出していない状態でも点灯する.

### AR Status/NWS Indicator: 空中給油/NWS 指示器

<img src="../../images/ss1-ar_states_nws_indicator.jpg" align="right" hspace="10" width="150">

ノーズホイールステアリングが有効であれば, 中央の NWS ライトが緑色に点灯する.
ラダーペダルを動かすことにより前脚を操作できる.

受油口が開いて空中給油ができるときは, 上の RDY ライトが青く点灯する.
給油ブームが差し込まれると, 中央のライトが緑色に点灯する.
ブームが離れると下のライトが点灯する.

</br>

### Integrated Control Panel (ICP): 統合操作パネル

<img src="../../images/dcs3-icp.jpg" align="right" hspace="10" width="300">

ICP は中央計器パネルの上部に配置されている.
これは CNI と呼ばれる, 通信・航法・識別の要となるシステムである.

これについては別項で説明する.

</br></br>

### Data Entry Display (DED): データ入力表示装置

<img src="../../images/dcs4-ded.jpg" align="right" hspace="10" width="300">

DED は通信・航法・識別 (CNI) とウェポンデリバリーに関する情報を表示する.
DED の操作は ICP を通じて行う.

</br></br>

### RWR Prime Control Panel/Azimuth Display: レーダー警報受信機

<img src="../../images/dcs5-rwr.jpg" align="right" hspace="10" width="300">

ALR-56M は F-16 のレーダー警報受信機である.
自機を中心とした, 360度のレーダー波をスコープに平面表示する.
スコープの左には脅威警報指示灯がある.

</br>

### Eyebrow Light

<img src="../../images/ss2-eyebrow_left.jpg" align="right" hspace="10" width="300">

- **IFF Identification Light (敵味方識別灯)**: これを押すと敵味方識別が行われる, もしくは AWACS に敵味方識別情報を要求する.
- **Fault Acknowledge Light (F-ACK)**: これを押すと, Pilot Fault List Display (PFLD) の障害表示を消すことができる.
- **Master Caution Light (主警告灯)**: このライトは, 機体の故障や特殊な状況が発生した場合に Caution ライトと共に点灯し, 押すことでリセットできる.

### Left and Right Multifunction Display (MFD): 多機能表示装置

<img src="../../images/dcs6-mfd.jpg" align="right" hspace="10" width="300">

MFD は5つずつ, 4つのグループに分かれた20個の Optional Select Button (OSB) が囲むように配置されたフルカラーの CRT スクリーンである.
MFD の角にはディスプレイのゲイン, 輝度, シンボルのコントラスト, 輝度を変更するロッカースイッチがある.

</br></br></br></br>

### Miscellaneous (MISC) Panel

<img src="../../images/dcs7-misc_panel.jpg" align="right" hspace="10" width="150">

- **Autopilot Roll and Pitch Switch (自動操縦ロール/ピッチスイッチ)**: ピッチとロールを自動で制御する2つのスイッチである.ピッチスイッチを ALT HOLD にすると現在の高度を維持し, A/P OFF にするとオフになる. ATT HOLD にすると航空機は現在のピッチとロール姿勢を維持する.

    ロールスイッチを HDG SEL にすると, HSI でバグした方位を維持するように飛行する.
    ATT HOLD にすると現在のロールとピッチ姿勢を維持し, STRNG SEL にすると DED で選択したステアポイントに向かって自動操縦される.
    両方のスイッチは相互に機能する.

- **ADV Mode Switch (ADV モードスイッチ)**: 地形追随レーダーを使った地形回避ボタンである.ブロック 50 バイパーでは機能しない.
- **Master Arm Switch (マスターアームスイッチ)**: 3ポジションスイッチで, OFF の場合は Emergency Jettison (緊急投棄) を除いて兵装の発射が制限される. ARM と SIMULATE の場合, レーダーと兵装管理システム (SMS) は通常通り動作するが, SIMULATE では兵装の発射は行われない. SIM モードでは兵装の発射はなされずに (緊急兵装投棄を除く) シンボルだけが表示され, 主に訓練で使用する.
- **ALT Release Button (予備発射ボタン)**: オルトリリースボタンは, 操縦桿に付いたウェポンリリースボタンが故障したときの予備である.
- **Laser Arm Switch (レーザーアームスイッチ)**: ターゲティングポッドが搭載されている場合, レーザーアームスイッチはレーザーを ARM する.
- **ECM Enable Light (ECM作動灯)**: ECM が送信されている場合, このライトが点灯する.
- **RF Switch (電波スイッチ)**: 航空機からの電波放出を制御する3ポジションスイッチである. SILENT の場合は, レーダー・レーダー高度計・データリンク・TACAN・ECM を含む, 航空機から放出されるすべての電波が遮断される. QUIET モードの場合は, レーダー・データリンク・TACAN を除くすべての電波が遮断される.

### Warning Lights: 警報灯

<img src="../../images/ss3-eyebrow_right.jpg" align="right" hspace="10" width="300">

- **Engine and Engine Fire Warning Lights (エンジン/エンジン火災警報灯)**: 右 Eyebrow に配置されたライトは, すぐさま対処が必要な緊急用のライトである. エンジン警報灯は, RPM と FTIT 計が温度超過・フレームアウト・スタグネーションが起きたことを示したときに点灯する. すなわち, RPM が 60 % 未満もしくは, FTIT が 1000 ℃ 以上のときである. エンジン火災警報灯はエンジンベイでの火災を検知したときに点灯する.
- **Hydraulic and Oil Pressure Warning Light (作動油/滑油圧力警報灯)**: 油圧が 30 秒以上にわたって 10 psi 未満のとき, もしくはAかBの油圧システムのどちらかが 1000 psi を下回ったときに点灯する.
- **FLCS and DBU Warning Lights (FCLS/DBU 警報灯)**: FLCS 警報灯は, FLCS プロセッサー, 電力供給, 入力信号, AOA, もしくはエアデータ入力の故障を検知したときに点灯する. また, 前縁フラップが固定されているときか, BIT が失敗したときにも点灯する. DBU 警報灯は, FLCS デジタルバックアップが有効な場合に点灯する.
- **Takeoff and Landing Configuration Warning Lights (離着陸形態警報灯)**: このライトは, 10,000 フィート以下でランディングギアが降りておらず, 対気速度が 190 ノット以下で, 降下率が 250 フィート毎分以上のときに点灯する. これはランディングギアの警報ホーンと連動している.
- **Canopy and Oxygen Low Waring Lights (キャノピー/酸素残量低下警報灯)**: キャノピーが降りていない, もしくはロックされていないときに点灯する. 酸素残量低下警報灯は酸素システムが5 psi 以下, もしくは BIT が失敗したときに点灯する.

### Engine Instruments: エンジン計器

<img src="../../images/ss4-engine_instruments.jpg" align="right" hspace="10" width="200">

- **Oil Pressure Indicator (滑油油圧計)**: エンジンにはエンジン本体とギアボックスの潤滑に使う油圧システムが内蔵されている. 目盛りは 0 から 100 psi である. 地上でのアイドル時には通常, 15 psi あたりで, ミリタリー以上になると 60 psi を指す.
- **Engine Nozzle Position Indicator (エンジンノズル位置計)**: エンジンノズルは, ノズルとそれに連動して動くダイバージェントノズルの2つの要素から構成される可変ノズルである. ノズルの開閉は4つのアクチュエーターによって行われ, それをパーセンテージで確認できる.
- **Engine RPM Indicator (エンジン回転数計)**: RPM 計はエンジンオルタネーターから得られるエンジン回転数を 1 から 110 ％ の間で表示する.
- **FTIT Indicator (タービンファン内部温度計)**: Fan Turbine Inlet Temperature (FTIT) 計は, タービン内部の平均温度をセルシウス温度で表する. 目盛りは 100 ℃ 刻みで, 200 から 1200 ℃ まである.

### Airspeed and Mach Indicator: 対気速度/マッハ計

<img src="../../images/ss5-airspeed_indicator.jpg" align="right" hspace="10" width="200">

対気速度/マッハ計はピトー管システムの空気圧を表示する.
計器の外側は 80 から 850 ノットまで計測できる対気速度計で, 内側の小窓にはマッハ 0.5 から 2.2 まで測れるマッハ計がある.
赤色の三角は超過禁止速度 (VNE) を示している.

</br>

### Altimeter: 高度計

<img src="../../images/ss6-altimeter.jpg" align="right" hspace="10" width="200">

1,000 フィートから 80,000 フィートまで計測できるサーボ気圧式の高度計である.
電波で計測するモードと, 気圧で計測するモードがある.
気圧モードの場合は PNEU フラッグがゲージに現れる.
右下のノブで高度計規正値を設定できる.
設定した規正値は右下の小窓に示されている.

</br>

### Angle of Attack Indicator: 迎え角 (AoA) 計

<img src="../../images/ss7-aoa_indicator.jpg" align="right" hspace="10" width="150">

AoA 計は HUD の左にある AoA 表示器と同じ内容かつ, -32° から +32° までの範囲を表示する.
テープの色は AoA 表示器と適合している.
中央にあるバーの位置が現在の AoA である.

</br></br></br></br></br>
</br></br>

### Attitude Director Indicator: 姿勢指示器

<img src="../../images/ss8-adi.jpg" align="right" hspace="10" width="200">

ADI は慣性航法装置 (INS) から得られる機体のピッチとロール姿勢を表する.
インジケーターには, 1本の針の幅が 1 秒あたり 1 〜 1.2 度の回転速度に相当する回転速度針と, スリップインジケーターも含まれる.
ピッチトリムノブを使用して, 自機のシンボルに相当する球体を調整できる.

計器着陸装置 (ILS) が有効な場合, ローカライザーとグライドスロープバーが ADI に表示される.

### Vertical Velocity Indicator: 昇降計

<img src="../../images/ss9-vvi.jpg" align="right" hspace="10" width="150">

VVI は機体の上昇率と降下率を 6,000 フィート毎分の範囲で表示する.

</br></br></br></br></br>
</br></br></br></br>

### Horizontal Situation Indicator: 水平姿勢指示器

<img src="../../images/dcs8-hsi.jpg" align="right" hspace="10" width="200">

HSI は自機を中心とした平面図を表示する.
自機シンボルを囲むコンパスは INS によって動くため, 磁北は常にラバーラインで読まれる.
ヘディングセットノブでヘディングインジケーターを, コースノブでコースを設定できる.

</br>

### Fuel Quantity Select Panel: 燃料計表示選択パネル

<img src="../../images/ss10-fuel_qty_panel.jpg" align="right" hspace="10" width="150">

Fuel Quantity Select パネルでは燃料計に何を表示させるか選択できる.

- **TEST**: 両方の針が 2,000 ポンドを指し, トータライザーは 6,000 ポンドを示する. コーションライトパネルには FWD FUEL LOW と AFT FUEL LOW が点灯する.
- **NORM**: AL ポインターが後部左タンクと A-1 胴体タンクの残燃料を, FR ポインターが前部右リザーバータンクと F-1, F-2 タンクの残燃料を示す.
- **RSVR**: AL ポインターと FR ポインターがそれぞれ, 後方と前方のリザーバータンクの燃料を示す.
- **INT WING**: AL ポインターと FR ポインターがそれぞれ, 左右の主翼内タンクの燃料を示す.
- **EXT WING**: AL ポインターと FR ポインターがそれぞれ, 左右の外部燃料タンクの燃料を示す.
- **EXT CTR**: FR ポインターが胴体下の外部燃料タンクの燃料を示す.
- **The External Fuel Transfer**: 外部タンクからの燃料流量を制御できる. NORM の場合はセンターラインタンクから先に消費し, WING FIRST の場合はウィングタンクから消費する.

## Left Auxiliary Console: 左補助コンソール

![dcs9-left_aux_panel](../images/dcs9-left_aux_panel.jpg)

### Miscellaneous Switches and Indicators

<img src="../../images/ss11-gear_panel.jpg" align="right" hspace="10" width="300">

- **EMER STORES JETTISON Button (緊急兵装投棄ボタン)**: すべての燃料タンク, 懸架ラック, 自由落下兵器を投棄する.
- **WHEELS Down Light (降着装置展開灯)**: 主脚と前脚の状態を示し, 緑色の場合はギアが降りてロックされている状態である. ランディングギアが動作中はハンドルが赤く点灯し, ハンドルと対応した位置にあれば, そのライトはオフになる.
- **HOOK Switch (フックスイッチ)**: アレスティング装置がある滑走路で緊急着陸をするためのフックを展開できる. フックは一度展開すると, スイッチからでは完全に格納することができない.
- **ANTI-SKID Switch (アンチスキッドスイッチ)**: アンチスキッドもしくはパーキングブレーキをオンにできる.
- **LANDING TAXI LIGHTS Switch (着陸/滑走灯スイッチ)**: テイクオフ/ランディングライトもしくはタキシーライトをオンにできる.
- **DN LOCK REL Button (ダウンロック解除ボタン)**: 電磁ソレノイドが故障もしくは通電していない場合, スプリング動作ハンドルを機械的にアンロックする. ランディングギアによるすべての電気信号をオーバーライドする. (WoWを解除し, ギアに重量が掛かっていても上げられるようになる)
- **LG Handle (降着装置ハンドル)**: ハンドルを動かすと, 電気スイッチが作動しランディングギアへ格納または展開の信号が送られる. ギアとドアが動作中もしくは正常にロックされていない場合, ハンドル内の警報灯が点灯する. また, この警報灯は, ギアが降りてロックされておらず, 対気速度 190 ノット以下, 高度 10,000 フィート以下, 降下率 250 フィート毎分以上のすべての条件を満たす場合にも点灯する.
- **SPEED BRAKE Position Indicator (スピードブレーキ位置表示器)**: 閉鎖・開放・電源なしの3つのスピードブレーキの状態を示する. スピードブレーキが閉じているときはインジケータは CLOSED を表示し, 開いているときは9つのドットが, 電源が入っていないときはストライプが表示される.
- **STORES CONFIG Switch (兵装形態スイッチ)**: 兵装に応じて CAT I か CAT III に設定する. 通常, CAT I は空対空ロードアウトで, CAT III は翼下に重たい空対地兵装や燃料タンクを装備しているときに使用する. CAT III のとき, FCLS は離陸制限を厳しくするために AOA と onset rate を制限する.
- **HORN SILENCER Button (警告ホーン停止ボタン)**: 対気速度 190 ノット以下, 高度 10,000 フィート以下で, 後縁フラップが作動しランディングギアが正常に降りていないときに鳴るオーディオホーンを停止することができる. 通常はランディングギアの展開を促すための警報であるが, 10,000 フィート MSL 以下でドッグファイトをしている際にも鳴ることがある.
- **GND JETT ENABLE Switch (地上投棄実行スイッチ)**: OFF であれば, 地上にいるとき (WoW: ランディングギアが展開し重量が掛かっている状態) の緊急兵装投棄と, ランディングギアが展開しているときのセレクティブジェティソンと兵装の通常投下を制限する. ENABLE の場合, ギアの展開や WoW に関係なく兵装を投棄または投下できる.これは航空機の兵装システムチェックのメンテナンスのために使用する.
- **BRAKES Channel Switch (ブレーキチャンネルスイッチ)**: チャンネル 1 , 2 のどちらでもペダルブレーキを有効にできるが, 通常はチャンネル 1 のままにしておく.

### CMDS Control Panel: 対抗手段放出装置パネル

<img src="../../images/dcs10-cmds_panel.jpg" align="right" hspace="10" width="300">

対抗手段の操作と表示は, このパネルから行える.
パネルからチャフ/フレアの放出プログラムとジャマーを選択し, HOTAS から実行できる.

</br></br></br>

### HMCS Control Panel: ヘルメット装着式照準システム制御パネル

<img src="../../images/dcs11-hmcs_panel.jpg" align="right" hspace="10" width="300">

ヘルメットバイザーに飛行と兵装照準情報を投影させることができる.
ノブで電源のオンオフ, 輝度を調整できる.

### Threat Warning Aux Control Panel: 脅威警報補助制御パネル

<img src="../../images/dcs12-twa_panel.jpg" align="right" hspace="10" width="150">

RWR の電源と管理の操作を行える.

</br></br></br></br></br>
</br></br>

### ALT GEAR Handle: 予備降着装置ハンドル

<img src="../../images/ss12-alt_gear_handle.jpg" align="right" hspace="10" width="150">

油圧もしくはメインランディングギアハンドルが故障した場合に, 代わりに降着装置を展開させることができる.

</br></br></br></br></br>

## Right Auxiliary Console: 右補助コンソール

![dcs13-right_aux_panel](../images/dcs13-right_aux_panel.jpg)

### Magnetic Compass: 方位磁針

<img src="../../images/ss13-compass.jpg" align="right" hspace="10" width="200">

磁北を基準とした自機の機首方位を示す自己完結型の方位磁針である.

</br></br></br></br>

### Fuel Quantity Indicator: 燃料計

<img src="../../images/ss14-fuel_qty_indicator.jpg" align="right" hspace="10" width="200">

燃料計の小窓には数字で残燃料の合計値が, 2本の針がそれぞれ後部と左, 前部と右のタンクを示す.
2本の針の間隔は燃料の不均衡を表しており, これが広がると針の根本に赤い表示が現れる.
このような場合は, FUEL パネルにある ENG FEED スイッチを使って不均衡を解消する.

</br>

### Hydraulic Pressure Indicators for System A and B: 油圧計

<img src="../../images/ss15-hyd_press_indicator.jpg" align="right" hspace="10" width="200">

油圧システム A と B の油圧を示す.
通常, 2,850 から 3,250 PSI の値を示す.

</br></br></br></br>

### Pilot Fault List Display: パイロット障害リスト表示装置

<img src="../../images/ss16-pfld.jpg" align="right" hspace="10" width="200">

PFLD はフライトコントロールシステム (FLCS) が検知した障害を表示する.
表示される内容には警報レベルと警告レベルがある.
警報レベルは FLCS と連動しており, 警報内容に括弧がつく.
警告レベルではエンジンとアビオニクスなどの FLCS 以外の要素と連動している.
PFLD にアイテムが表示された場合, 対応する Caution ライトと MASTER CAUTION ライトが点灯する.
障害表示をクリアするには F-ACK を押す.

### Caution Light Panel: 警告灯パネル

<img src="../../images/ss17-caution_panel.jpg" align="right" hspace="10" width="300">

Caution ライトパネルには検出された障害と, 対応した複数のライトがある.

</br></br></br></br></br></br>

### EPU Fuel Quantity Indicator: EPU 燃料計

<img src="../../images/ss18-epu_fuel_qty_indicator.jpg" align="right" hspace="10" width="200">

EPU (非常用電源装置) 燃料計は残りのヒドラジンの量をパーセンテージで表示する.
100 % の場合, EPU は約5分から10分間稼働できる.

</br></br>

### CABIN PRESS ALT gauge: コックピット内気圧高度計

<img src="../../images/ss19-cabin_press_alt_gauge.jpg" align="right" hspace="10" width="200">

コックピット内の気圧高度を 0 フィートから 50,000 フィートまで表示する.

</br></br></br>

### Clock: 時計

<img src="../../images/ss20-clock.jpg" align="right" hspace="10" width="200">

最大60分の経過時間を表示できる8日間の手巻き時計である.

</br></br></br></br>

## Left Console: 左コンソール

![dcs14-left_console](../images/dcs14-left_console.jpg)

### Test Switch Panel: テストスイッチパネル

<img src="../../images/ss21-test_swch_panel.jpg" align="right" hspace="10" width="150">

TEST パネルには以下の操作と表示を含む.

- **Fire and Overheat Detection (FIRE & OHEAT DETECT) Test Button (火災/過熱検知テストボタン)**: オーバーヒート検出システムのテストを行う. これを押すと Caution ライトの OVERHEAT と, 右 Eyebrow ライトの ENG FIRE が点灯する. これにより MASTER CAUTION ライトも点灯する.
- **PROBE HEAT Switch(ピトー管加熱スイッチ)**: オンにするとデータプローブを加熱する. TEST に倒すと, テストが良好に完了したあとに Caution ライトの PROBE HEAT が点滅する.
- **On-Board Oxygen Generation System (OBOGS) BIT Switch (機上酸素発生装置テストスイッチ)**: BIT にすると, 右 Eyebrow ライトの OXY LOW が点灯する.
- **Emergency Power Unit / Generator (EPU/GEN) Test Switch (非常用電源装置/発電機テストスイッチ)**: エンジン起動後の EPU のテストができる.
- **MAL & IND LTS Test Button (故障/指示灯テストボタン)**: 警報ライトと警告ライト, 音声メッセージのテストができる.
- **FLCS PWR TEST Switch (FLCS電力テストスイッチ)**: ABCD 4つのフライトコントロールチャンネルライトのテストができる.TEST に倒すと, MAIN PWR スイッチが BATT に設定されたときに FLCS への電力出力を確認する.

### FLT Control Panel: 操縦系統制御パネル

<img src="../../images/ss22-flt_ctrl_panel.jpg" align="right" hspace="10" width="300">

F-16 の操縦系統の手動制御パネルである.
バイパーの FLCS は高度に自動化されているため, 通常は何も設定する必要ない.

- **Digital Buck Up Switch (デジタルバックアップスイッチ)**: FLCS のバックアップソフトウェアを選択する. オンの場合, 右 Eyebrow ライトに DBU ON , HUD に WARNING が表示される.
- **ALT FLAPS Switch (フラップ代替スイッチ)**: 後縁フラップを自動制御ではなく手動で展開させる. 非対称フラップ設定でフラップが故障した場合に使用する.
- **MANUAL TF FLY UP Switch (手動地形追随飛行スイッチ)**: 地形追随レーダー用であるが, ブロック 50 バイパーでは使用しない.
- **LE FLAPS Switch (前縁フラップスイッチ)** : 前縁フラップを手動または自動で制御する. これにより, 前縁フラップを規定通りに動かしたり, 所定の位置に固定することができる. 片方の前縁フラップが故障し, 両方を同じように動作させる必要がある場合は, 手動設定を使用する.
- **FLCS RESET Switch (FLCS リセットスイッチ)**: FLCS の警報とライト, サーボアクチュエーター及び FLCS の電気部分の故障をリセットする.
- **FLCS BIT Switch (FLCS テストスイッチ)**: 地上にいる (WoW) ときに自己診断テスト (BIT) を行う. BIT にすると, 操縦翼面の動作テストが行われる. スイッチは BIT 位置に45秒間保持され, 緑色の RUN ライトが点灯する. 完了するとライトは消灯し, スイッチは中央位置にスナップバックする. BIT 中に問題が発生すると赤色の FAIL ライトが点灯し, PFLD に障害の内容が表示される.

### Manual Trim Panel: 手動トリムパネル

<img src="../../images/ss23-man_trim_panel.jpg" align="right" hspace="10" width="300">

F-16 の自動トリムは優秀なため, 通常の飛行においては設定する必要はないが, 操縦桿のトリムスイッチから操作することができる.

- 左上にはロールトリムインジケーターと操作するホイールがある.
- 右下にはピッチトリムインジケーターと操作するホイールがある.
- 左下にはヨートリムを操作するダイヤルがある.
- Trim Autopilot Disconnect (TRM/ AP DISC) スイッチは, 操縦桿のトリムスイッチが故障した場合に, そのトリムスイッチと自動操縦モードを無効にできる.

### Fuel Control Panel: 燃料制御パネル

<img src="../../images/ss24-fuel_panel.jpg" align="right" hspace="10" width="300">

FUEL パネルで燃料システムの制御ができる.

- **FUEL MASTER Switch (燃料マスタースイッチ)**: ガードされており, 燃料のシャットオフバルブの開閉ができる. 通常はオン位置でガードしておく.
- **TANK INERTING Switch (タンク不活性化スイッチ)**: 不揮発性ハロンガスを燃料タンクに送り込むことで内圧を低下させ, 戦闘ダメージなどの緊急時の火災リスクを低減させる.
- **ENG FEED Knob (エンジン送油ノブ)**: 燃料ポンプをオンまたはオフにすることで, 搭載燃料の重心を中央に保つ. ダイヤルを回すと燃料バランスの調整を手動か自動に変更できる. 燃料の不均衡は燃料計の針の開き具合で確認できる. AFT もしくは FWD にすることで, クロスフィードの燃料タンクポンプを選択できる. これにより燃料の重心位置の手動調整が可能になる. NORM では燃料システムが自動で調整し, OFF では燃料ポンプが止まる.
- **AIR REFUEL Switch (空中給油スイッチ)**: 機体の背部にある空中給油用の扉を開閉できる.

### IFF Control Panel: 敵味方識別装置制御パネル

<img src="../../images/ss25-iff_panel.jpg" align="right" hspace="10" width="300">

通信・航法・識別 (CNI) の機能と IFF の主要な機能のいくつかを制御できる.

</br></br></br>

### EXT Lighting Control Panel: 機外照明制御パネル

<img src="../../images/ss26-ext_light_panel.jpg" align="right" hspace="10" width="300">

航空機に取り付けられているすべての機外灯を制御する.

- **ANTI-COLL Knob (衝突防止灯ノブ)**: OFF ポジションと, 点滅パターンの異なる7つのモード (1, 2, 3, 4, A, B, C) がある.
- **FLASH STEADY Switch (位置灯スイッチ)**: 点滅と点灯が選択できる位置灯のスイッチである.
- **WING/TAIL and FUSELAGE Switch (衝突防止灯スイッチ)**: 翼端灯と胴体の衝突防止灯を制御する, 全灯・消灯・微灯の3ポジションスイッチである.
- **FORM Knob (編隊灯ノブ)**: 編隊灯の輝度を調整する.
- **MASTER COVERT Knob (可視不可視ノブ)**: 外部灯火の可視・不可視の切り替えノブである.不可視 (CONVERT) はナイトビジョン用である.
- **AERIAL REFUELING Knob (空中給油ノブ)**: 夜間に空中給油オペレーターが給油口を視認しやすくするために, 給油口を照らすライトの輝度を調整する.

### EPU Control Panel: 非常用電源装置制御パネル

<img src="../../images/ss27-epu_panel.jpg" align="right" hspace="10" width="150">

EPU は, ヒドラジン駆動の自己完結型ユニットで, 約10~15分間, 緊急用の油圧と電力を供給できる.
主にエンジンが停止した場合に使用し, EPU は油圧および電気システムに電力を供給する.

- **EPU Switch (EPU スイッチ)**: ガード付きで, NORM であれば両方の油圧システムや MAIN/STBY ジェネレーターの両方が喪失するなどの条件を満たした場合に, 自動的に作動する. ON にして手動で作動させることもできる. EPU が稼働してタービンが正常に動作していれば, 緑色の EPU 動作ライトが点灯する.
- **HYDRAZN AIR Light (稼働ソースライト)**: ヒドラジンを使用してタービンを稼働させている場合は HYDRAZN が点灯し, 空気のみで作動している場合は AIR が点灯する.

### ELEC Control Panel: 電力制御パネル

<img src="../../images/ss28-elec_panel.jpg" align="right" hspace="10" width="200">

航空機に必要な電力を制御できる.

- **MAIN PWR Switch (主電源スイッチ)**: 電気システムに接続する主電源を, 外部電源もしくは主発電機から選択できる. BATT はバッテリーをバッテリーバスに接続し, OFF では電源を無効にする. 航空機を始動するときは, まず BATT でテストを行い, その後 MAIN PWR に接続してエンジンを始動する.
- **ELEC CAUTION RESET Button (電気警告リセットボタン)**: 電気システムの Caution ライトを消し, 主発電機と予備発電機を再起動する.
- **MAIN GEN Light (主発電機ライト)**: 外部もしくは主発電機の電源が入っていない場合に点灯する.
- **STBY GEN Light (予備発電機ライト)**: 予備発電機が使用できない場合に点灯する.
- **EPU GEN Light (EPU 発電機ライト)**: EPU は動作しているが, 両方の非常用バスに電力を供給していない場合に点灯する.
- **EPU PMG Light (EPU 磁気発電機ライト)**: EPU は動作しているが, すべての FLCS の末端まで動作させるには PMG からの電力が足りない場合に点灯する.
- **Aircraft Battery Indicator Light (航空機搭載バッテリー指示灯)**: **FAIL** ライトは飛行中でバッテリーが 20 ボルト未満, もしくは地上でバッテリー障害があるときに点灯する. **TO FLCS** ライトが点灯していれば, 飛行中に1つ以上の FLCS ブランチが 25 ボルト未満, もしくは地上でバッテリーの電力が1つ以上の FLCS ブランチに接続されている.**FLCS RLY** は, 1つ以上の FLCS ブランチが 20 ボルト未満か, バッテリーに接続されていない場合に点灯する.

### ECM Control Panel: 電子対抗手段制御パネル

<img src="../../images/ss29-ecm_panel.jpg" align="right" hspace="10" width="300">

ECM 装備が搭載されている場合にECM を制御し, 状態を表示する.

</br>

### AVTR Control Panel: 飛行録画制御パネル

<img src="../../images/ss30-avtr_panel.jpg" align="right" hspace="10" width="300">

Airborne Video Tape Recorder (AVTR) は HUD と MFD, もしくは HMD と MFD 画面の録画ができる.

</br>

### ENG & JET Start Control Panel: エンジンジェット始動制御パネル

<img src="../../images/ss31-eng_jfs_panel.jpg" align="right" hspace="10" width="150">

GE-129 エンジンの始動とその他の制御を行う.

- **JET FUEL START Switch (JSF 始動スイッチ)**: OFF, START1, START2 の3ポジションがある. これらは, 1つまたは2つのジェット燃料始動装置のアキュムレータを使用して油圧始動モーターを駆動させる.JP8 燃料を使う場合は START2 にセットする.
- **JSF RUN Light (JSF 稼働灯)**: JSF 始動 30 秒以内に点灯する.
- **ENG CONT Switch (エンジン制御スイッチ)**: **PRI** (プライマリ) モードと **SEC** (セカンダリ) モードがあるガード付きスイッチである. エンジンのデジタル電子制御に障害が発生しない限り, 通常は PRI にする. 故障が発生した場合は, SEC を選択するか, エンジンが停止後の再起動のために PRI を選択しなおす. SEC ではアフターバーナーが使用できないことに注意する. また, SEC では, Caution パネルの SEC が点灯し, アイドル時の推力が増加する.
- **MAX POWER Switch (最大推力スイッチ)**: GE-129 エンジンでは使用しない.

### UHF Backup Control Panel: UHF 予備無線機制御パネル

<img src="../../images/ss32-uhf_backup_panel.jpg" align="right" hspace="10" width="300">

無線のほとんどの機能は計器パネルの ICP と DED を介して操作するが, バックアップ UHF 無線パネルでも同様に操作できる.
バッテリー電源から使える唯一の無線機なので, エンジン始動前に使用する必要がある.
アクセスドアの右にはチャンネルを設定するノブがある.
A-10Cに精通している人にとっては慣れ親しんだ無線機である.

パネルの中央には周波数を設定するダイヤルと表示窓がある.
下部には, 無線機の電源およびモードを選択する機能ノブ, トーンシグナルボタン, 音量ノブ, そして, マニュアル・プリセット・緊急周波数 (243.0) を選択するモード選択ノブがある.

### Audio 1 Control Panel: 音量制御パネル 1

<img src="../../images/ss33-audio1_panel.jpg" align="right" hspace="10" width="300">

COMM 1 と COMM 2 両方の無線機と, それぞれをスケルチ OFF, スケルチ ON, 緊急周波数にするモードノブがある.
パネルの右側には, 保安音声用の SECURE VOICE ノブ, サイドワインダーのシーカー音量を調節する MSL Tone ノブ, 脅威警報用の THREAT Tone ノブ, (実機では動作しない) TF Tone ノブがある.

### Audio 2 Control Panel: 音量制御パネル 2

<img src="../../images/ss34-audio2_panel.jpg" align="right" hspace="10" width="300">

地上クルーおよび空中給油のブームオペレーターとの会話に用いるインターコム音量を調節する INTERCOM ノブ, 戦術航法装置 (TACAN) のコード再生音量を調節する TACAN ノブ, 計器着陸装置 (ILS) のローカライザー認識シグナルの ILS Power ノブ, そして HOT MIC スイッチがある.

### Manual Pitch Override Switch: ピッチ手動オーバーライドスイッチ

<img src="../../images/ss35-man_pitch_ovrd_swch.jpg" align="right" hspace="10" width="200">

MANUAL PITCH スイッチを OVRD にすると, ディープストール時にスタビライザーの権限を上書きすることにより, 機首をより大きく下げることができる.
これで増速して失速時でも飛行制御が可能になる.
パイロットがシートストラップから逆さまにぶら下がっていてもしっかりと握ることができるように, スイッチの両側にガードがついている.

### Canopy Jettison Handle: キャノピー投棄ハンドル

<img src="../../images/ss36-canopy_jett_handle.jpg" align="right" hspace="10" width="200">

緊急事態に限り使用する.
座席射出ハンドルを引いてもキャノピーが正常に分離せずに射出を妨げている場合に使いる.

</br>

### De-Fog Lever: 防曇レバー

<img src="../../images/ss37-defog_lever.jpg" align="right" hspace="10" width="200">

前後どちらかに動かすと, キャノピーの曇りを取り除くことができる.

## Right Console: 右コンソール

![dcs15-right_console](../images/dcs15-right_console.jpg)

### Sensor Power Control Panel: センサー電源制御パネル

<img src="../../images/ss38-snsr_pwr_panel.jpg" align="right" hspace="10" width="300">

インテーク下にある左右のチンポッド, 火器管制レーダー (FCR) , レーダー高度計の電源を入れることができる.

### HUD Remote Control Panel: HUD 制御パネル

<img src="../../images/ss39-hud_remote_panel.jpg" align="right" hspace="10" width="300">

HUD の表示内容を管理する.

詳細は[HUD](hud.md) を参照．

</br>

### Interior Lighting Control Panel: 機内照明制御パネル

<img src="../../images/ss40-int_light_panel.jpg" align="right" hspace="10" width="300">

コックピット計器の照明を調節できる.
ナイトビジョンゴーグルのために, 照明のほとんどは緑色になっている.
PRIMARY CONSOLES ノブは左右コンソール, PRIMARY INST PNL ノブは計器パネルと補助コンソールパネル用である.
PRIMARY DATA ENTRY DISPLAY ノブは, DED と PFLD の輝度を調節する.

MAL&IND LTS スイッチは, AoA 表示器, AR/NWS 指示器, DED, ECM 制御パネル, 左右 MFD, PFLD, RWR の輝度を全灯か微灯に設定する.

FLOOD CONSOLE ノブは左右コンソールの投光照明を, FLOOD INST PNL ノブは計器パネルの投光照明を調節する.

### Air Cond Control Panel: エアコン制御パネル

<img src="../../images/ss41-air_cond_panel.jpg" align="right" hspace="10" width="300">

コックピット温度とエンジンの抽気設定が行える.
TEMP ノブはシミュレーションでは機能しないが, AIR SOURCE ノブは機能する.
OFF はすべてのエンジン抽気バルブを閉じ, NORM は環境制御システム (ECS) を自動制御にする.
DUMP はコックピットの内圧と外圧を均等にし, RAM は抽気バルブを閉じて内圧を下げる.

### Secure Voice Panel: 秘話装置パネル

<img src="../../images/ss42-secure_vc_panel.jpg" align="right" hspace="10" width="300">

UHF 無線機及び VHF 無線機と組み合わせて使用し, 暗号化通信を可能にする.

</br></br></br></br></br></br></br>

### Voice Message Switch: 音声メッセージスイッチ

<img src="../../images/ss43-vc_msg_swch.jpg" align="right" hspace="10" width="200">

音声メッセージの無効化ができる.

</br></br></br></br>

### Oxygen Panel: 酸素パネル

<img src="../../images/ss44-oxg_panel.jpg" align="right" hspace="10" width="300">

酸素マスクの酸素流量を調節する.
SUPPLY レバーは OFF と ON に加えて, G に対する補助呼吸 (PBG) 設定がある.
Diluter レバーは酸素の割合を通常 (NORM) と 100 % から選択できる.
EMERGENCY レバーは, 非常時のための EMERGENCY, 通常時の NORM, テスト用の TEST MASK がある.
パネル上部には酸素システムの圧力計がある.

### Engine Anti Ice Switch: エンジン防氷スイッチ

<img src="../../images/ss45-ant_sel_panel.jpg" align="right" hspace="10" width="300">

プローブとエンジンを熱して凍結を防ぐ.
ON は手動で有効, AUTO は凍結を検知した場合のみ自動でオンになる.
OFF はシステムを無効にする.

### ANT SEL Panel: アンテナ選択パネル

IFF と UHF 無線機のアンテナを, 上部 (UPPER) アンテナ, 通常 (NORM) , 下部 (LOWER) アンテナのいずれかにする.

### Avionics Power Panel: アビオニクス電源パネル

<img src="../../images/ss46-avio_pwr_panel.jpg" align="right" hspace="10" width="300">

航空機に搭載している電子機器の電源を入れる.

- **MMC**: モジュラーミッションコンピュータの電源を入れる.
- **ST STA**: 兵装ステーションの電源を入れる.
- **MFD**: 左右の多機能表示装置の電源を入れる.
- **UFC**: アップフロントコントロール (ICP と DED) の電源を入れる.
- **MAP**: ブロック 50 バイパーでは使用しない.
- **GPS**: 全地球測位システム (GPS) の電源を入れる.
- **DL**: データリンクの電源を入れる.
- **INS**: ノブには, OFF, 機体の位置を保存しておく STOR HDG, 通常の起動に用いる NORM, INS を実際に用いる NAV, 飛行中にアラインする IN FLT ALIGN, 安定した飛行を続けることで GPS を用いて INS を更新する ATT オプションがある.
- **MIDS**: 多機能情報伝達システムの ON, OFF と, データを抹消する ZERO がある.

### Zeroize Switch: 暗号抹消スイッチ

<img src="../../images/ss47-zero_swch.jpg" align="right" hspace="10" width="200">

緊急時において, 暗号化通信や GPS キーを含むすべての機密情報を抹消する.

</br></br>
