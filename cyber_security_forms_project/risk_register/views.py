from django.shortcuts import render, redirect
from .models import Risk
from .forms import RiskForm
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

def index(request):
    if request.method == 'POST':
        form = RiskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('risk_register:index')  # Redirect after POST
    else:
        form = RiskForm()

    risks = Risk.objects.all()
    return render(request, 'risk_register/index.html', {'form': form, 'risks': risks})


def risk_delete(request, id):
    risk = Risk.objects.get(id=id)
    risk.delete()
    return redirect('risk_register:index')  # updated redirect
def export_risks_to_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=letter)

    risks = Risk.objects.all()
    y = 750
    for risk in risks:
        p.drawString(50, y, f"Risk ID: {risk.id}, Description: {risk.description}, Date Raised: {risk.date_raised}")
        y -= 50

    # Close the PDF object cleanly, and end writing process.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    return FileResponse(BytesIO(pdf), as_attachment=True, filename='risks.pdf')