import fitz  # PyMuPDF
import argparse
import os

def add_text_to_each_page(input_pdf, output_pdf, text, x, y):
    pdf_document = fitz.open(input_pdf)
    font = fitz.Font("tiro")  # this is the font file
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        page.insert_font(fontname="F0", fontbuffer=font.buffer)
        page_width = page.rect.width
        page_height = page.rect.height
        # If x or y are not provided, use default values
        xition = x if x is not None else page_width * 0.6
        yition = y if y is not None else page_height - 30
        page.insert_text((xition, yition), text, fontsize=14, fontname="F0", color=(0, 0, 1))
    pdf_document.save(output_pdf)
    pdf_document.close()

def add_image_to_pdf(input_pdf, output_pdf, image_path, x, y, width=None, height=None, page_numbers=None):
    """
    Add an image to specified pages of a PDF file at given coordinates.

    Args:
        input_pdf (str): Path to input PDF file
        output_pdf (str): Path to output PDF file
        image_path (str): Path to image file
        x (float): X coordinate for image placement
        y (float): Y coordinate for image placement
        width (float, optional): Desired width of the image. If None, original size is used
        height (float, optional): Desired height of the image. If None, original size is used
        page_numbers (list, optional): List of page numbers to add image to. If None, adds to all pages
    """
    # Check if image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    # Open the PDF
    pdf_document = fitz.open(input_pdf)

    # Determine which pages to modify
    if page_numbers is None:
        page_numbers = range(len(pdf_document))
    else:
        # Convert 1-based page numbers to 0-based indices
        page_numbers = [i-1 for i in page_numbers if 0 < i <= len(pdf_document)]

    for page_num in page_numbers:
        page = pdf_document[page_num]

        # Insert the image
        image_rectangle = fitz.Rect(x, y, x + (width or 100), y + (height or 100))
        page.insert_image(image_rectangle, filename=image_path)

    # Save and close the PDF
    pdf_document.save(output_pdf)
    pdf_document.close()

def main():
    parser = argparse.ArgumentParser(description="Modify PDF documents by adding text or images.")
    parser.add_argument('input_pdf', type=str, help='Path to the input PDF file.')
    parser.add_argument('output_pdf', type=str, help='Path to the output PDF file.')

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Text command
    text_parser = subparsers.add_parser('text', help='Add text to PDF')
    text_parser.add_argument('text', type=str, help='Text to add to each page of the PDF.')
    text_parser.add_argument('--x', type=float, default=None,
                            help='X position for the text (default is 60 percents of the page width).')
    text_parser.add_argument('--y', type=float, default=None,
                            help='Y position for the text (default is 30 pixels from the bottom of the page).')

    # Image command
    image_parser = subparsers.add_parser('image', help='Add image to PDF')
    image_parser.add_argument('image_path', type=str, help='Path to the image file.')
    image_parser.add_argument('--x', type=float, required=True, help='X position for the image.')
    image_parser.add_argument('--y', type=float, required=True, help='Y position for the image.')
    image_parser.add_argument('--width', type=float, help='Width of the image in points.')
    image_parser.add_argument('--height', type=float, help='Height of the image in points.')
    image_parser.add_argument('--pages', type=int, nargs='+',
                             help='Page numbers to add image to (default is all pages).')

    args = parser.parse_args()

    if args.command == 'text':
        add_text_to_each_page(args.input_pdf, args.output_pdf, args.text, args.x, args.y)
    elif args.command == 'image':
        add_image_to_pdf(args.input_pdf, args.output_pdf, args.image_path,
                        args.x, args.y, args.width, args.height, args.pages)

if __name__ == "__main__":
    main()
