import ollama
import sys 
import os 

# Define the path to your image  
ollama.pull('llava:7b') 

if __name__ == '__main__':
    # Check if the correct number of arguments are passed
    if len(sys.argv) < 2:
        print("Usage: python3 text.py <UPLOAD_FOLDER>")
        sys.exit(1)
    
    UPLOAD_FOLDER = sys.argv[1]  # Get the folder path from command line argument 

OUTPUT_FOLDER = "output/" 
for filename in os.listdir(UPLOAD_FOLDER):
    if filename.endswith('.jpg') or filename.endswith('png'):
        image_path = os.path.join(UPLOAD_FOLDER, filename)
    # Prepare the message to send to the LLaVA model
    message = {
        'role': 'user',
        'content': 'Analyze this image and describe the emotions being displayed by the subjects in the image, as well as the context that may be contributing to these emotions.',
        'images': [image_path]
    }

    # Use the ollama.chat function to send the image and retrieve the description
    response = ollama.chat(
        model="llava:7b",  # Specify the desired LLaVA model size
        messages=[message]
    )
    text = response['message']['content']
    # Print the model's description of the image
    print("The image description is: \n",text)  
    ollama.pull('gemma:2b') 
    print("Starting the text analysis")
    modelfile='''
    FROM gemma:2b
    SYSTEM You are given an input and your job is to choose whether the input classifies as Positive or Neutral or Negative. Give a 20 word explanation on your classification.
    ''' 

    modelfile2='''
    FROM gemma:2b
    SYSTEM You are given an input and your job is to choose whether the input classifies as either Romance or Humor or Compassion Rage or Valor or Disgust or Fear or Wonder or Peace. Give a 20 word explanation on your classification.
    ''' 
    modelfile3='''
    FROM gemma:2b
    SYSTEM You are given an input and your job is to classify the input as G (General) for general audience and R (Restricted) (18+) Which is for adult audience. Give a 20 word explanation on your classification.
    ''' 
    modelfile4='''
    FROM gemma:2b
    SYSTEM You are given an input and your job is to classify this according to the IAB tier 1 categorization standards  which include categories like 'Arts & Entertainment', 'Automotive', 'Business', 'Careers', 'Education', etc. Give a reallt small explanation on why the classification was chosen.
    ''' 
    ollama.create(model='sentiment', modelfile=modelfile)
    ollama.create(model='emotion', modelfile=modelfile2)
    ollama.create(model='age', modelfile=modelfile3)
    ollama.create(model='iab', modelfile=modelfile4)


    response = ollama.generate(model='sentiment',prompt=text) 
    response_emotion = ollama.generate(model='emotion',prompt=text) 
    response_age = ollama.generate(model='age',prompt=text) 
    response_iab = ollama.generate(model='iab',prompt=text) 

    analysis_result = response+response_emotion+response_age+response_iab 

    # Write analysis result to output file
    output_file_path = os.path.join(OUTPUT_FOLDER, f'{os.path.splitext(filename)[0]}_analysis.txt')
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(analysis_result) 