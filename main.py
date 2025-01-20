import PyPDF2
import argparse
from pprint import pprint

def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text


def parse_text(body): 
    tokens = body.split(' ')
    start_token = 'Highlighted:'
    start_comment_token = "| Comment Text:"
    page_token  ='Page'

    

    response = []
    buffer = "" 
    start = False 
    stop = False
    
    for i in range(len(tokens)):
        token = tokens[i]

        if start:
            buffer += token  + ' '

        if token == page_token:
            start = False

        if token in start_token:
            start = not start 
            if buffer:
                response.append(buffer)
                buffer = ''


    return response




    

if __name__ == '__main__':
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Extract text from a PDF file.')
    parser.add_argument('pdf_file', help='Path to the PDF file')
    args = parser.parse_args()

    # Extract text from the provided PDF file
    extracted_text = extract_text_from_pdf(args.pdf_file)
    parsed_text = parse_text(extracted_text)
    for p in parsed_text:
        print(p)

