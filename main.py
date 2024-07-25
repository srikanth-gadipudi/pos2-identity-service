from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False)

dt = pd.read_csv("topics .csv")

for index, row in dt.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(x1=10, y1=20, x2=200, y2=20)
    pdf.ln(260)
    pdf.set_font(family='Times', style='B', size=8)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)

    for count in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(270)
        pdf.set_font(family='Times', style='B', size=8)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)

pdf.output(name='test.pdf')