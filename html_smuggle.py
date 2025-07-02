import base64
import os
import sys

def create_smuggled_html(smuggle_file):
    # Read the content of the file
    with open(smuggle_file, 'rb') as file:
        file_content = file.read()

    # Base64 encode the file content
    base64_content = base64.b64encode(file_content).decode('utf-8')

    # Remove the file extension from the filename
    filename_without_extension = os.path.splitext(smuggle_file)[0]

    # Read the template HTML file
    with open('smuggle_template.html', 'r') as template_file:
        template_content = template_file.read()

    # Replace the placeholders with the appropriate values
    final_content = template_content.replace('INSERT BASE64 HERE', base64_content)
    final_content = final_content.replace('INSERT NAME OF FILE HERE', os.path.basename(smuggle_file))

    # Write the modified content to the new HTML file
    output_file = filename_without_extension + '.html'
    with open(output_file, 'w') as output:
        output.write(final_content)

    print(f'Success! Smuggled HTML file "{output_file}" has been created.')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python smuggle.py <smuggle_file>')
        sys.exit(1)

    smuggle_file = sys.argv[1]
    create_smuggled_html(smuggle_file)


