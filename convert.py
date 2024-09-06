import fitz  # PyMuPDF
import argparse

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

def main():
    parser = argparse.ArgumentParser(description="Adds text to each page of a PDF document.")

    parser.add_argument('input_pdf', type=str, help='Path to the input PDF file.')
    parser.add_argument('output_pdf', type=str, help='Path to the output PDF file.')
    parser.add_argument('text', type=str, help='Text to add to each page of the PDF.')
    parser.add_argument('--x', type=float, default=None, help='X position for the text (default is 60 percents of the page width).')
    parser.add_argument('--y', type=float, default=None, help='Y position for the text (default is 30 pixels from the bottom of the page).')

    args = parser.parse_args()

    add_text_to_each_page(args.input_pdf, args.output_pdf, args.text, args.x, args.y)

if __name__ == "__main__":
    main()
