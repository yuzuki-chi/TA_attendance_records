def insert_text_output_pdfrw(pdf_file_path, insert_text):
    """
    既存のPDFファイルに文字を挿入し、別名で出力します
    :param pdf_file_path:       既存のPDFファイルパス
    :param insert_text:         挿入するテキスト
    :return:
    """
    from pdfrw import PdfReader
    from pdfrw.buildxobj import pagexobj
    from pdfrw.toreportlab import makerl
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    from reportlab.pdfbase import pdfmetrics
    from reportlab.lib.units import mm

    # 出力名
    output_name = "output.pdf"
    # PDF新規作成
    cc = canvas.Canvas(output_name)

    # フォントの設定
    # font_name = "HeiseiKakuGo-W5"
    # pdfmetrics.registerFont(UnicodeCIDFont(font_name))
    # cc.setFont(font_name, 16)

    # 既存ページ読み込み
    page = PdfReader(pdf_file_path, decompress=False).pages
    # 1ページ目をオブジェクトに
    pp = pagexobj(page[0])
    cc.doForm(makerl(cc, pp))

    # 挿入位置(mm指定)
    target_x, target_y = 10*mm, 10*mm
    # 文字列挿入
    cc.drawString(target_x, target_y, insert_text)
    cc.showPage()
    # 保存
    cc.save()