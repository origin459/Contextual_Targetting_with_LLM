import ollama
import os 
import sys  
import PyPDF2

# Ensure the model is pulled
ollama.pull('gemma:2b') 
print("Starting the llama model")

if __name__ == '__main__':
    # Check if the correct number of arguments are passed
    if len(sys.argv) < 2:
        print("Usage: python3 text.py <UPLOAD_FOLDER>")
        sys.exit(1)
    
    UPLOAD_FOLDER = sys.argv[1]  # Get the folder path from command line argument 
    OUTPUT_FOLDER = "output/"
    
    # Ensure OUTPUT_FOLDER exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Define the system prompts for each model
    modelfile = '''
    FROM gemma:2b
    SYSTEM You are given an input and your job is to choose whether the input classifies as Positive or Neutral or Negative. Give a 20 word explanation on your classification.
    ''' 
    modelfile2 = '''
    FROM gemma:2b
    SYSTEM You are given an input and your job is to choose whether the input classifies as Romance or Humor or Compassion or Rage or Valor or Disgust or Fear or Wonder or Peace. Give a 20 word explanation on your classification.
    ''' 
    modelfile3 = '''
    FROM gemma:2b
    SYSTEM You are given an input and your job is to choose whether the input classifies as G (General) or R (Restricted) (18+). Give a 20 word explanation on your classification.
    ''' 
    modelfile4 = '''
    FROM gemma:2b
    SYSTEM You are given an input and your job is to classify this according to the IAB tier 1 categorization standards. Give a 20 word explanation on your classification.
    '''

    # Create models once
    ollama.create(model='sentiment', modelfile=modelfile)
    ollama.create(model='emotion', modelfile=modelfile2)
    ollama.create(model='age', modelfile=modelfile3)
    ollama.create(model='iab', modelfile=modelfile4)

    for filename in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        
        if filename.endswith('.txt') and 'url' not in filename.lower():
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read().strip()

        elif filename.endswith('.pdf'):
            # Process .pdf files
            text = ""
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                for page_num in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(page_num)
                    text += page.extract_text()
        
        else:
            continue  # Skip unsupported files

        # Run the models on the text
        response = ollama.generate(model='sentiment', prompt=text) 
        response_emotion = ollama.generate(model='emotion', prompt=text) 
        response_age = ollama.generate(model='age', prompt=text) 
        response_iab = ollama.generate(model='iab', prompt=text) 
        analysis_result = response + response_emotion + response_age + response_iab

        # Write analysis result to output file
        output_file_path = os.path.join(OUTPUT_FOLDER, f'{os.path.splitext(filename)[0]}_analysis.txt')
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(analysis_result)