# bill.py

from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from datetime import datetime
import win32print
import win32api


# -----------------START-----------------
# Set font size
pdfmetrics.registerFont(TTFont('F1', 'tahomabd.ttf'))
pdfmetrics.registerFont(TTFont('F2', 'tahoma.ttf'))
pdfmetrics.registerFont(TTFont('F3', 'impact.ttf'))

c = canvas.Canvas('bill.pdf')
c.setPageSize((80 * mm, 150 * mm))

# HEADER
c.setFont('F1', 10)
c.drawCentredString(40 * mm, 140 * mm, 'Receipt/Tax')

c.setFont('F1', 15)
c.drawCentredString(40 * mm, 130 * mm, 'Phenomenal Inc.')

company = ['Address : 11 Street, Oudomvilay, Kaisone, Savannakhet',
           'Cell : 020 9252 4334',
           'WhatsApp : +856 20 9252 4334',
           'Facebook : Phenomenal Inc.']

c.setFont('F2', 8)
for i, cm in enumerate(company):
    c.drawCentredString(40 * mm, (120 - (i * 3)) * mm, cm)

products = [['croissant', 1, 120, 120],
            ['pancake', 2, 25000, 50000],
            ['latte', 3, 20000, 60000],
            ['cheese-cake', 4, 25000, 100000]]

for i, pd in enumerate(products):
    c.drawString(10 * mm, (100 - (i * 4)) * mm, pd[0])
    c.drawRightString(35 * mm, (100 - (i * 4)) * mm, str(pd[1]))
    c.drawRightString(50 * mm, (100 - (i * 4)) * mm, str(pd[2]))
    c.drawRightString(70 * mm, (100 - (i * 4)) * mm, str(pd[3]))

c.showPage()
c.save()


# -----------------PRINT PDF-----------------
current_printer = win32print.GetDefaultPrinter()
win32api.ShellExecute(0,'print','bill.pdf', None, '.',0)
win32print.SetDefaultPrinter(current_printer)


'''
# Hello text example
c.setFont('F1', 10)
c.drawString(10 * mm, 140 * mm, 'Hello Text')

c.setFont('F2', 10)
c.drawString(10 * mm, 30 * mm, 'Example')
c.drawCentredString(40 * mm, 50 * mm, 'Center')


c.setFont('F3', 10)
c.drawRightString(70 * mm, 80 * mm, '5')
c.drawRightString(70 * mm, 85 * mm, '600')
c.drawRightString(70 * mm, 90 * mm, '700')
c.drawRightString(70 * mm, 95 * mm, '8000')

x1, y1, x2, y2 = [10 * mm, 100 * mm, 70 * mm, 100 * mm]
ml = [[10 * mm, 100 * mm, 70 * mm, 100 * mm],[10 * mm, 120 * mm, 70 * mm, 120 * mm]]
c.line(x1, y1, x2, y2)
c.lines(ml)
'''
