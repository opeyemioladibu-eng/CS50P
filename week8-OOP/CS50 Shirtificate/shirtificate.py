from fpdf import FPDF


name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

# Title
pdf.set_font("Helvetica", "B", 32)
pdf.cell(0, 30, "CS50 Shirtificate", align="C")

# Shirt image
pdf.image("shirtificate.png", x=15, y=60, w=180)

# Name on shirt
pdf.set_font("Helvetica", "B", 24)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(0, 140)
pdf.cell(210, 10, f"{name} took CS50", align="C")

# Output
pdf.output("shirtificate.pdf")