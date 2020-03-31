# Web Font Converter

フォント（ OTF / TTF ）と Web フォント（ WOFF / WOFF2 ）の相互変換コマンドです。

## インストール
```shell
$ pip install git+https://github.com/higurashi-takuto/web-font-converter.git
```

## コマンド説明
### wfc
- 入力がフォントの場合は WOFF / WOFF2 を出力する。
- 入力が Web フォントの場合は内容に応じて OTF / TTF を出力する。
- それぞれ出力は拡張子のみを変えたパスに行う。

```shell
usage: wfc [-h] input

フォント ⇄ Web フォント

positional arguments:
  input       入力フォントへのパス

optional arguments:
  -h, --help  show this help message and exit
```

### wfc-woff
- 入力フォントを WOFF に変換し出力する。

```shell
usage: wfc-woff [-h] [--output OUTPUT] input

WOFF へ変換

positional arguments:
  input                 入力フォントへのパス

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        入力フォントへのパス（ デフォルトは拡張子のみ変更 ）
```

### wfc-woff2
- 入力フォントを WOFF2 に変換し出力する。

```shell
usage: wfc-woff2 [-h] [--output OUTPUT] input

WOFF2 へ変換

positional arguments:
  input                 入力フォントへのパス

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        入力フォントへのパス（ デフォルトは拡張子のみ変更 ）
```

### wfc-otf
- 入力フォントを OTF に変換し出力する。

```shell
usage: wfc-otf [-h] [--output OUTPUT] input

OTF へ変換

positional arguments:
  input                 入力フォントへのパス

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        入力フォントへのパス（ デフォルトは拡張子のみ変更 ）
```

### wfc-ttf
- 入力フォントを TTF に変換し出力する。

```shell
usage: wfc-ttf [-h] [--output OUTPUT] input

TTF へ変換

positional arguments:
  input                 入力フォントへのパス

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        入力フォントへのパス（ デフォルトは拡張子のみ変更 ）
```
