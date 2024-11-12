# PDF Modifier

This Python script allows you to modify PDF documents by:
1. Adding custom text to PDF pages at specified positions
2. Inserting images into PDF pages at specified coordinates

## Requirements

The script requires Python and the following libraries:

- `fitz` (PyMuPDF)
- `argparse`

### Installing Dependencies

To install the required packages, use the following command:

```bash
pip install pymupdf
```

## Usage

The script supports two main commands: `text` and `image`.

### Adding Text

To add text to a PDF:

```bash
python convert.py input.pdf output.pdf text "Text to add" --x 100 --y 50
```

#### Text Command Arguments

- `input_pdf`: Path to the input PDF file
- `output_pdf`: Path to the output PDF file where the modified PDF will be saved
- `text`: The text to add to each page of the PDF
- `--x`: (Optional) X coordinate for the text. Default is 60% of the page width
- `--y`: (Optional) Y coordinate for the text. Default is 30 pixels from the bottom of the page

#### Text Example

```bash
python convert.py input.pdf output.pdf text "Registration number: 2024/10/12" --x 100 --y 50
```

### Adding Images

To add an image to a PDF:

```bash
python convert.py input.pdf output.pdf image path/to/image.jpg --x 100 --y 100 --width 200 --height 150 --pages 1 2 3
```

#### Image Command Arguments

- `input_pdf`: Path to the input PDF file
- `output_pdf`: Path to the output PDF file
- `image_path`: Path to the image file to insert
- `--x`: (Required) X coordinate for the image placement
- `--y`: (Required) Y coordinate for the image placement
- `--width`: (Optional) Desired width of the image in points
- `--height`: (Optional) Desired height of the image in points
- `--pages`: (Optional) List of page numbers to add the image to. If not specified, adds to all pages

#### Image Example

```bash
# Add image to specific pages with custom dimensions
python convert.py input.pdf output.pdf image logo.png --x 50 --y 50 --width 100 --height 100 --pages 1 2 3

# Add image to all pages using default dimensions
python convert.py input.pdf output.pdf image watermark.png --x 200 --y 300
```

### Help

You can view the help message for each command:

```bash
# General help
python convert.py --help

# Text command help
python convert.py input.pdf output.pdf text --help

# Image command help
python convert.py input.pdf output.pdf image --help
```

## Coordinate System

The PDF coordinate system starts from the bottom-left corner of the page:
- X coordinates increase from left to right
- Y coordinates increase from bottom to top
- Units are in points (1/72 of an inch)

## Examples

1. Adding a watermark text to all pages:
```bash
python convert.py input.pdf output.pdf text "CONFIDENTIAL" --x 300 --y 400
```

2. Adding a logo to the first three pages:
```bash
python convert.py input.pdf output.pdf image company_logo.png --x 50 --y 750 --width 200 --height 100 --pages 1 2 3
```

3. Adding a small image to all pages:
```bash
python convert.py input.pdf output.pdf image stamp.png --x 500 --y 20 --width 50 --height 50
```

## License

This project is open-source and available under the MIT License.
