import os
import argparse
from fontTools.ttLib import TTFont


def convert_font(input_path, output_path, flavor):
    font = TTFont(input_path)
    font.flavor = flavor
    font.save(output_path)


def wfc():
    parser = argparse.ArgumentParser(description='フォント ⇄ Web フォント')
    parser.add_argument('input', help='入力フォントへのパス')
    args = parser.parse_args()

    input_path, ext = os.path.splitext(args.input)
    if ext in ['.ttf', '.otf']:
        output_path = f'{input_path}.woff'
        convert_font(args.input, output_path, 'woff')

        output_path = f'{input_path}.woff2'
        convert_font(args.input, output_path, 'woff2')

    elif ext in ['.woff', '.woff2']:
        font = TTFont(args.input)
        if ('CFF ' in font) or ('CFF2' in font):
            output_path = f'{input_path}.otf'
            convert_font(args.input, output_path, None)
        else:
            output_path = f'{input_path}.ttf'
            convert_font(args.input, output_path, None)


def wfc_woff():
    parser = argparse.ArgumentParser(description='WOFF へ変換')
    parser.add_argument('input', help='入力フォントへのパス')
    parser.add_argument('--output', '-o', default='',
                        help='入力フォントへのパス（ デフォルトは拡張子のみ変更 ）')
    args = parser.parse_args()

    if args.output:
        output_path = args.output
    else:
        input_path, ext = os.path.splitext(args.input)
        output_path = f'{input_path}.woff'

    convert_font(args.input, output_path, 'woff')


def wfc_woff2():
    parser = argparse.ArgumentParser(description='WOFF2 へ変換')
    parser.add_argument('input', help='入力フォントへのパス')
    parser.add_argument('--output', '-o', default='',
                        help='入力フォントへのパス（ デフォルトは拡張子のみ変更 ）')
    args = parser.parse_args()

    if args.output:
        output_path = args.output
    else:
        input_path, ext = os.path.splitext(args.input)
        output_path = f'{input_path}.woff2'

    convert_font(args.input, output_path, 'woff2')


def wfc_otf():
    parser = argparse.ArgumentParser(description='OTF へ変換')
    parser.add_argument('input', help='入力フォントへのパス')
    parser.add_argument('--output', '-o', default='',
                        help='入力フォントへのパス（ デフォルトは拡張子のみ変更 ）')
    args = parser.parse_args()

    if args.output:
        output_path = args.output
    else:
        input_path, ext = os.path.splitext(args.input)
        output_path = f'{input_path}.otf'

    convert_font(args.input, output_path, None)


def wfc_ttf():
    parser = argparse.ArgumentParser(description='TTF へ変換')
    parser.add_argument('input', help='入力フォントへのパス')
    parser.add_argument('--output', '-o', default='',
                        help='入力フォントへのパス（ デフォルトは拡張子のみ変更 ）')
    args = parser.parse_args()

    if args.output:
        output_path = args.output
    else:
        input_path, ext = os.path.splitext(args.input)
        output_path = f'{input_path}.ttf'

    convert_font(args.input, output_path, None)
