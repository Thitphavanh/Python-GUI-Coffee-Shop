# bill.py

from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from datetime import datetime



# -----------------START-----------------
# Set font size
pdfmetrics.registerFont(TTFont('F1','tahomabd.ttf'))
pdfmetrics.registerFont(TTFont('F2','tahoma.ttf'))

c = canvas.Canvas('bill.pdf')
c.setPageSize((80 * mm, 150 * mm))

# Hello text
c.setFont('F1',10)
c.drawString(10 * mm, 140 * mm, 'Hello Text')
c.drawString(10 * mm, 30 * mm, 'Example')
c.drawCentredString(40 * mm, 50 * mm, 'Center')
c.drawRightString(70 * mm, 80 * mm, '5')
c.drawRightString(70 * mm, 85 * mm, '600')
c.drawRightString(70 * mm, 90 * mm, '700')
c.drawRightString(70 * mm, 95 * mm, '8000')


c.showPage()
c.save()