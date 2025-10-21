import sys
import os
import base64
import mimetypes
from bs4 import BeautifulSoup
from urllib.parse import unquote

def embed_images_as_base64(html_file_path, md_file_dir):
    print(f"Processing HTML file: {html_file_path}")
    print(f"Using Markdown file directory as base for images: {md_file_dir}")

    if not os.path.exists(html_file_path):
        print(f"Error: HTML file not found at '{html_file_path}'")
        sys.exit(1)
    if not os.path.isdir(md_file_dir):
        print(f"Error: Markdown source directory not found at '{md_file_dir}'")
        sys.exit(1)
        
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'lxml')

        images_found = soup.find_all('img')
        if not images_found:
            print("No <img> tags found.")
            return

        modified = False
        for img_tag in images_found:
            src = img_tag.get('src')

            if not src or src.startswith('http://') or src.startswith('https://') or src.startswith('data:'):
                print(f"Skipping (URL or data URI): {src}")
                continue
            decoded_src = unquote(src)

            image_path = os.path.join(md_file_dir, decoded_src)

            if not os.path.exists(image_path):
                print(f"Warning: Image file not found at {image_path}")
                continue

            try:
                with open(image_path, 'rb') as img_file:
                    encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
                
                mime_type, _ = mimetypes.guess_type(image_path)
                if mime_type is None:
                    mime_type = 'application/octet-stream'
                
                data_uri = f"data:{mime_type};base64,{encoded_string}"
                
                img_tag['src'] = data_uri
                modified = True
                print(f"Successfully embedded image: {decoded_src}")

            except Exception as e:
                print(f"Error processing image {image_path}: {e}")

        if modified:
            with open(html_file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print("HTML file updated successfully.")
        else:
            print("No local images were found to embed.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python embed_images.py <path_to_html_file> <path_to_md_file_dir>")
        print("This script is intended to be called by Typora's export command.")
        sys.exit(1)
        
    html_file = sys.argv[1]
    md_dir = sys.argv[2]
    embed_images_as_base64(html_file, md_dir)