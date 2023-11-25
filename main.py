from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)

pdf.cell(w=0, h=12, txt="Hi King", align="L", ln=1, border=1)

pdf.set_font(family="Helvetica", style="I", size=12)

pdf.cell(w=0, h=12, txt="Hi Sir", align="R", ln=1, border=1)

pdf.set_font(family="Arial", style="B", size=12)

pdf.cell(w=0, h=12, txt="Hello World", align="C", ln=1, border=1)

pdf.output("output.pdf")