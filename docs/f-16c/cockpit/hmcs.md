# HMCS

ヘルメット装着式照準システム (HMCS) は、フライトヘルメットのバイザーに機体と兵装の情報を常に表示させる追加の改修キットです。
ヘルメットマウンッテドディスプレイ (HMD) とも称されます。

また、センサーや搭載兵器をヘルメットの視点に合わせてスレーブ (追従) させることができます。
これは、AIM-9X ハイオフボアサイト短距離ミサイルと組み合わせると絶大な効果を発揮します。
ヘルメットは、センサーと搭載兵器を最大 80° のオフボアサイト (非砲口照準) までスレーブできます。

HMD の電源は、左補助コンソールの HMD 制御ノブから入れます。
**OFF** 位置にあるノブを **INC** (増加) へ時計回りに回すと、HMD が起動します。
続けて INC に回し続けると、HMD の輝度が増加します。

<img src="../../images/dcs11-hmcs_panel.jpg" align="left" hspace="10" width="400">

<img src="../../images/dcs_procedure55.jpg" hspace="10" width="150">

HMD のシンボルは右目のみで見えます。
VR を使用したときに違和感があれば、DCS: World オプションの F-16C Special Tab から変更できます。

![dcs61-hmcs_eye](../images/dcs61-hmcs_eye.jpg)

HMCS を用いたウェポンデリバリーは以下の項で扱います。

- AIM-9M/X HMCS ミサイルボアサイト運用
- AIM-9M/X HMCS レーダーボアサイト運用

## Non-Designated Mode: 非指定モード

HMCS の基本機能は Non-Designated モードで投影されます。
HMD のシンボルのほとんどは HUD と似ているため、HUD の延長として扱われます。
以下のシンボルはすべての HMCS モードにおいて機能します。

![dcs62-hmcs_symbols](../images/dcs62-hmcs_symbols.png)

- **Acceleration (G 加速度)**: 現在の G 表示
- **Airspeed (速度)**: HUD の速度表示の写し
- **Master Arm Status (マスターアームの状態)**: マスターアームスイッチの位置が OFF、ARM、SIM のいずれかで表されます
- **Master Mode (マスターモード)**: 現在のマスターモード
- **Bearing/Range to Bullseye (ブルズアイまでの方位/距離)**: 自機からブルズアイまでの方位と距離
- **Altitude (高度)**: HUD の気圧高度表示の写し
- **Dynamic Aiming Cross (ダイナミック照準クロス)**: HMD が空対空モードのとき、照準クロスのには HMD の視角に応じた3通りの位置があります
    - HMD の見通し線が水平線より低い場合、エイミングクロスは HMD の中央に表示されます
    - HMD の見通し線が水平線より 0~30° 高い場合、エイミングクロスは HMD の速度表示と高度表示の中間に表示されます
    - HMD の見通し線が水平線より 30° 以上高い場合、エイミングクロスは HMD の方位表示に重ねて表示されます
- **Distance to Steerpoint/Steerpoint Number (ステアポイントまでの距離/番号)**: 選択中のステアポイントと距離 (海里)
- **Helmet heading (ヘルメット方位)**: ヘルメットが向いている方位の数字表示
