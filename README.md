
# PDF Text Inserter

This Python script allows you to add custom text to every page of a PDF document at specified positions. You can provide the input and output PDF paths, the text to add, and optionally the coordinates for where the text should be placed on each page.

## Requirements

The script requires Python and the following libraries:

- `fitz` (PyMuPDF)
- `argparse`

### Installing Dependencies

To install the required packages, use the following command:

```
pip install pymupdf
```

## Usage

You can run the script with the following command:

```
python convert.py input.pdf output.pdf "Text to add" --x 100 --y 50
```

### Arguments

- `input_pdf`: Path to the input PDF file.
- `output_pdf`: Path to the output PDF file where the modified PDF will be saved.
- `text`: The text to add to each page of the PDF.
- `--x`: (Optional) X coordinate for the text. Default is 60% of the page width.
- `--y`: (Optional) Y coordinate for the text. Default is 30 pixels from the bottom of the page.

### Example

```
python convert.py input.pdf output.pdf "Registration number: 2024/10/12" --x 100 --y 50
```

In this example, the text "Registration number: 2024/10/12" will be added to every page of input.pdf at the position (100, 50) and the result will be saved to output.pdf.

### Help

You can also view the help message by running:

```
python convert.py --help
```

## License

This project is open-source and available under the MIT License.
