# aldi_survey

A Python script which fills out Aldi surveys that are printed on the bottom of receipts using [Splinter](https://splinter.readthedocs.io/en/latest/).

Functionality:
- Storing user info in a pickle file for later surveys
- Reading in information from the receipt using OCR with pytesseract
- Automatic conversion from .heic to .png for receipt processing
- Image pre-processing with OpenCV

*Splinter requires ChromeDriver to be installed in /aldi_survey/ directory to work*

`py script.py` to run