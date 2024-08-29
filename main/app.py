from flask import Flask, render_template, request, redirect, url_for
import os
import datetime
import subprocess

app = Flask(__name__) 
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return 'Image uploaded successfully'  
        
    return render_template('upload_image.html')

@app.route('/upload_video', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return 'Video uploaded successfully'
    return render_template('upload_video.html')

def create_upload_folder():
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

create_upload_folder()  # Ensure UPLOAD_FOLDER exists

@app.route('/upload_text', methods=['GET', 'POST'])
def upload_text():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        # If user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return 'Text file uploaded successfully'

    subprocess.run(['python', 'text.py', UPLOAD_FOLDER])
    
    return render_template('upload_text.html')
    
@app.route('/upload_url', methods=['GET', 'POST'])
def upload_url():
    if request.method == 'POST':
        url = request.form['url']
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = f'url_{timestamp}.txt'
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(file_path, 'w') as file:
            file.write(url) 
    subprocess.run(['python3', 'text.py', UPLOAD_FOLDER])

    return render_template('upload_url.html')

@app.route('/upload_pdf', methods=['GET', 'POST'])
def upload_pdf():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return 'PDF uploaded successfully' 
    subprocess.run(['python3', 'text.py', UPLOAD_FOLDER])
    return render_template('upload_pdf.html')

if __name__ == '__main__':
    app.run(debug=True)
