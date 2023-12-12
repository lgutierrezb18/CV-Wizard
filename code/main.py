from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def create_pdf_template(filename, personal_data, professional_profile, academic_background):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    add_personal_data(c, personal_data, height)
    add_professional_profile(c, professional_profile, height)
    add_academic_background(c, academic_background, height)

    c.save()

def add_personal_data(canvas, data, page_height):
    canvas.setFont("Helvetica", 10)
    y_position = page_height - 30
    for key, value in data.items():
        text = f"{key}: {value}"
        canvas.drawString(72, y_position, text)
        y_position -= 20

def add_professional_profile(canvas, profile, page_height):
    start_y_position = page_height - 100
    canvas.setFont("Helvetica-Bold", 12)
    canvas.drawString(72, start_y_position, "Professional Profile")
    canvas.setFont("Helvetica", 10)
    canvas.drawString(72, start_y_position - 20, profile)

def add_academic_background(canvas, academic_data, page_height):
    start_y_position = page_height - 200
    canvas.setFont("Helvetica-Bold", 12)
    canvas.drawString(72, start_y_position, "Academic Background")
    canvas.setFont("Helvetica", 10)
    y_position = start_y_position - 20
    for education in academic_data:
        for key, value in education.items():
            text = f"{key}: {value}"
            canvas.drawString(72, y_position, text)
            y_position -= 20
        y_position -= 10

# Example data
personal_data = {"Name": "John Doe", "Email": "john@example.com", "Location": "New York"}
professional_profile = "Experienced software developer with a passion for developing innovative programs..."
academic_background = [{"Institute": "University A", "Degree": "B.Sc. Computer Science", "Year": "2015-2019"}]

# Create the PDF
create_pdf_template("cv_template.pdf", personal_data, professional_profile, academic_background)
