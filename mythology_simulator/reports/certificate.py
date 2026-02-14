# ===============================
# Certificate Generator
# ===============================

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime


def generate_certificate(user_name, character, average_positivity, file_path):
    """
    Generates a PDF certificate.

    user_name: str
    character: str
    average_positivity: float
    file_path: str (where to save PDF)
    """

    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 120, "Certificate of Character Assessment")

    # Body text
    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, height - 180, "This certifies that")

    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 210, user_name)

    c.setFont("Helvetica", 12)
    c.drawCentredString(
        width / 2,
        height - 250,
        "has completed the Mythology Decision Simulator"
    )

    c.drawCentredString(
        width / 2,
        height - 280,
        f"and most closely aligns with the character: {character}"
    )

    c.drawCentredString(
        width / 2,
        height - 310,
        f"Overall Positivity Score: {average_positivity}%"
    )

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    date_str = datetime.now().strftime("%d %B %Y")
    c.drawString(50, 50, f"Issue Date: {date_str}")
    c.drawRightString(width - 50, 50, "Mythology Decision Simulator")

    c.showPage()
    c.save()
