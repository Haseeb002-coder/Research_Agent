from markdown_pdf import MarkdownPdf, Section
from src.report_compiler import report

# Read Markdown from a file or string


# Create a MarkdownPdf object
def save_pdf():
    pdf = MarkdownPdf()

    # Add the Markdown content as a section
    pdf.add_section(Section(report["report"]))

    # Save the PDF to a file
    pdf.save("output.pdf")