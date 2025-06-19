from fpdf import FPDF
name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=24)
pdf.cell(0, 10, "CS50 Shirtificate", align="C")

pdf.image("shirtificate.png", x=(pdf.w - 200)/2, y=25, w=200)

pdf.set_y(70)
pdf.cell(0, 10, name, align="C")

pdf.output("shirtificate.pdf")
