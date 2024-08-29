import ollama

ollama.pull('gemma:2b') 

text = """In the image, there is a man who appears to be in a state of distress or frustration. His hands are clasped together over his head, and he seems to be either shouting or gesturing emphatically. He's wearing a dark suit, which suggests a formal or professional setting. The background shows a typical urban environment with buildings and a street scene, indicating that this is likely taking place in a city center.
The man's facial expression and body language convey a sense of anger, disappointment, or intense emotional distress. He may be reacting to some unexpected news or a challenging situation, possibly related to work or personal matters given his attire. 
It's important to note that the image captures a single moment in time, so it's impossible to know the full context or background of what's causing his reaction. However, his expression and posture suggest he is experiencing some sort of negative emotion."""

modelfile4 = '''
FROM gemma:2b
SYSTEM You are given an input text describing an image. Your task is to classify the text according to the IAB 3 Taxonomy. Provide a very brief explanation of why the classification was chosen, ensuring the explanation is concise and relevant.
'''
ollama.create(model='iab', modelfile=modelfile4) 

response_iab = ollama.generate(model='iab',prompt=text)  

print("The IAB Analysis is as follows : \n",response_iab["response"])