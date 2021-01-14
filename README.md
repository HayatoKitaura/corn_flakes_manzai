# 某コーンフレークネタが出来るROSパッケージ

## 目的

講義内で学んだROS、ライセンスに関する知識をROSパッケージの製作を通して確認する。

## 概要

boke.pyでボケるとtukkomi.pyがツッコんでくれるROSパッケージです。
某コーンフレークに関するネタでボケてみるとうまくツッコんでくれます。

## 動作環境

- Ubuntu 18.04
- Raspberry Pi 4 Model B

## インストール
以下のコマンドでインストール

ワークスペースへ移動
```
cd ~/catkin_ws/src
```
リポジトリをクローン
```
git clone https://github.com/HayatoKitaura/corn_flakes.git
cd ~/catkin_ws
```
make
```
catkin_make
```
パーミッション設定
```
cd ~/catkin_ws/src/corn_flakes/scripts
chmod +x boke.py
chmod +x tukkomi.py
```

## 実行
タブを複製してそれぞれ実行
```
roscore
rosrun corn_flakes boke.py
rosrun corn_flakes tukkomi.py
```

## ボケ方
「おかん」というワードから始め、コーンフレークに関するボケをするとつっこんでくれます。

それ以外のボケをするとシンプルなつっこみが返ってきます。

「ありがとうございました」で終了。

## デモ動画

[デモ動画](https://youtu.be/wB3zewX6SKg)
