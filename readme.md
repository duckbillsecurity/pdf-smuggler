## Disclaimer

Scripts are for educational and demonstration purposes only. The author does not endorse or condone the use of this script for any criminal or malicious activities and it should only be used where explicitly allowed with proper permission.

## Introduction

Create PDFs with HTML smuggling attachments that save on opening the document.

## Instructions

1. Create HTML smuggling file using html_smuggle.py.

The mandatory parameters are:

- `smugglefile`: The full file path and name of the file for HTML smuggling.

Note: requires smuggle_template.html file in same location as the script.

2. Create final PDF using pdf-smuggler.py.

The mandatory parameters are:

- `inputpdf`: The full file path of the original PDF document.
- `file`: The full file path of the file to be attached to the PDF document.
- `outpdf`: The full file path of the final created PDF document.
