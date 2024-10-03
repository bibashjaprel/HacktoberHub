import markdown
import argparse
def convert_md_to_html(md_file_path, output_file_path):
    """
    Convert a Markdown file to an HTML file.

    Parameters:
    md_file_path (str): The path to the input Markdown file.
    output_file_path (str): The path where the output HTML file will be saved.

    The function reads the Markdown content from the specified file, converts it to HTML,
    and writes the resulting HTML to the output file with Bootstrap styling.
    """
    with open(md_file_path, 'r') as md_file:
        md_content = md_file.read()
        html_content = markdown.markdown(md_content)
        html_output = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Markdown to HTML Script</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container mt-5">
            <div class="content">
                {html_content}
            </div>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>
    """    
    with open(output_file_path, 'w') as output_file:
        output_file.write(html_output)
    print(f"Converted {md_file_path} to {output_file_path}")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Markdown file to HTML.')
    parser.add_argument('md_file_path', type=str, help='Path to the input Markdown file')
    parser.add_argument('output_file_path', type=str, help='Path to the output HTML file')
    args = parser.parse_args()
    convert_md_to_html(args.md_file_path, args.output_file_path)
