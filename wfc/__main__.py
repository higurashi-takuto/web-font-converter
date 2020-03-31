import os
import argparse
from fontTools.ttLib import TTFont


def convert_font(input_path, output_path, flavor):
    '''
    フォントの形式を選択して出力する。
    '''
    font = TTFont(input_path)
    font.flavor = flavor
    font.save(output_path)


def wfc():
    '''
    入力がフォントの場合は WOFF / WOFF2 を出力する。
    入力が Web フォントの場合は内容に応じて OTF / TTF を出力する。
    それぞれ出力は拡張子のみを変えたパスに行う。
    '''
    # 引数処理
    parser = argparse.ArgumentParser(description='フォント ⇄ Web フォント')
    parser.add_argument('input', help='入力フォントへのパス')
    args = parser.parse_args()

    input_path, ext = os.path.splitext(args.input)

    # 入力がフォントの場合
    if ext in ['.ttf', '.otf']:
        output_path = f'{input_path}.woff'
        convert_font(args.input, output_path, 'woff')

        output_path = f'{input_path}.woff2'
        convert_font(args.input, output_path, 'woff2')

    # 入力が Web フォントの場合
    elif ext in ['.woff', '.woff2']:
        font = TTFont(args.input)
        if ('CFF ' in font) or ('CFF2' in font):
            output_path = f'{input_path}.otf'
            convert_font(args.input, output_path, None)
        else:
            output_path = f'{input_path}.ttf'
            convert_font(args.input, output_path, None)


def wfc_woff():
    '''
    入力フォントを WOFF に変換し出力する。
    '''
    # 引数処理
    parser = argparse.ArgumentParser(description='WOFF へ変換')
    parser.add_argument('input', help='入力フォントへのパス')
    parser.add_argument('--output', '-o', default='',
                        help='入力フォントへのパス（ デフォルトは拡張子のみ変更 ）')
    args = parser.parse_args()

    # Web フォントの出力
    if args.output:
        output_path = args.output
    else:
        input_path, ext = os.path.splitext(args.input)
        output_path = f'{input_path}.woff'

    convert_font(args.input, output_path, 'woff')


def wfc_woff2():
    '''
    入力フォントを WOFF2 に変換し出力する。
    '''
    # 引数処理
    parser = argparse.ArgumentParser(description='WOFF2 へ変換')
    parser.add_argument('input', help='入力フォントへのパス')
    parser.add_argument('--output', '-o', default='',
                        help='入力フォントへのパス（ デフォルトは拡張子のみ変更 ）')
    args = parser.parse_args()

    # Web フォントの出力
    if args.output:
        output_path = args.output
    else:
        input_path, ext = os.path.splitext(args.input)
        output_path = f'{input_path}.woff2'

    convert_font(args.input, output_path, 'woff2')


def wfc_otf():
    '''
    入力フォントを OTF に変換し出力する。
    現在、中身は TTF と同じ処理で拡張子のみが異なる。
    '''
    # 引数処理
    parser = argparse.ArgumentParser(description='OTF へ変換')
    parser.add_argument('input', help='入力フォントへのパス')
    parser.add_argument('--output', '-o', default='',
                        help='入力フォントへのパス（ デフォルトは拡張子のみ変更 ）')
    args = parser.parse_args()

    # フォントの出力
    if args.output:
        output_path = args.output
    else:
        input_path, ext = os.path.splitext(args.input)
        output_path = f'{input_path}.otf'

    convert_font(args.input, output_path, None)


def wfc_ttf():
    '''
    入力フォントを TTF に変換し出力する。
    現在、中身は OTF と同じ処理で拡張子のみが異なる。
    '''
    # 引数処理
    parser = argparse.ArgumentParser(description='TTF へ変換')
    parser.add_argument('input', help='入力フォントへのパス')
    parser.add_argument('--output', '-o', default='',
                        help='入力フォントへのパス（ デフォルトは拡張子のみ変更 ）')
    args = parser.parse_args()

    # フォントの出力
    if args.output:
        output_path = args.output
    else:
        input_path, ext = os.path.splitext(args.input)
        output_path = f'{input_path}.ttf'

    convert_font(args.input, output_path, None)
