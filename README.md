# Contextual Targetting with LLM

This project demonstrates contextual targeting using large language models (LLMs) to analyze both text and image data. The application features a frontend interface where users can select the data type (text or image) and upload files for analysis. Using Google's **Gemma model** for text data and the **LLava 7B model** for image data, the project provides a RESTful API with a Flask backend. The models are prompt-engineered for optimal performance, and can be further customized in the `text.py` and `image.py` files.

## Overview

Contextual targetting analyzes data by understanding its context, whether in text or image form. This project categorizes and analyzes both text and image data, providing targeted insights. The **Gemma model** handles text files, analyzing sentiment, emotion, categorization, and more, while the **LLava 7B model** extracts contextual insights from image data. Prompt engineering is applied to optimize the models’ responses.

## Features

- **Frontend Interface**: Users can select the data type (text or image) and upload files for analysis.
- **Text Analysis**: Sentiment analysis, emotion detection, and categorization using the Gemma model.
- **Image Analysis**: Contextual insights from images using the LLava 7B model.
- **API Integration**: RESTful API with Flask to interact with the models.
- **Customizable Models**: Models are prompt-engineered and can be customized within `text.py` and `image.py`.

## Setup
- **Clone the Repository**:
   ```bash
   git clone https://github.com/origin459/contextual_targeting_llm.git
   cd Contextual_Targeting_with_LLM
   ```
- **Install Dependencies**:
  ```bash
   pip install -r requirements.txt 
  ```
  -**Run the Application**:
  ```bash
  python main/app.py
  ```
Now the Flask server and the frontend should be up and running locally.

### Frontend Interface

After running the application, open [http://127.0.0.1:5000](http://127.0.0.1:5000) in a browser. 
1. **Select Data Type**: Choose between "Text" or "Image" for the type of data you want to analyze.
2. **Upload File**: Upload the relevant file for analysis.
3. **Submit**: Once submitted, the application will send a request to either `image.py` or `text.py` based on the data type, where the appropriate LLM model will analyze the data.

### Customizing the Models

- **Gemma Model**: Customizations for the output target from the text data can be made in `text.py` through simple prompt engineering.
- **LLava 7B Model**: Customizations for the output target from the image data can be made in `image.py` through simple prompt engineering.

 ### Use Cases

1. **Sentiment and Emotion Analysis**: Analyze customer feedback to gauge sentiment and emotions.
2. **Content Moderation**: Filter inappropriate content in user-generated text and images.
3. **Ad Targeting**: Tailor ads based on contextual insights from text and image data.
4. **Product Categorization**: Automatically categorize products based on image or text descriptions.
   
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
