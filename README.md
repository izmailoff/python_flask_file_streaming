# python_flask_file_streaming
Example of streaming files for upload/download and both (proxy) in Python Flask.

For more detailed explanation see my post: http://izmailoff.github.io/web/flask-file-streaming.

# Quick Start
Clone this repo:

    git clone git@github.com:izmailoff/python_flask_file_streaming.git

Navigate to the project:

    cd python_flask_file_streaming

Create a virtual environment. One option is:

    python3.6 -m venv env

Activate the environment:

    source env/bin/activate

Install all dependencies (flask, requests):

    pip install -r requirements.txt

Edit this line:

    resp = requests.post('http://destination_host/upload_api', files={'file': request.stream})

in `streaming.py` to set correct upload host, and optionally adjust other parameters of the `post` request. See the comments in the code for more details.

Start the application:

    python streaming.py

Upload a file to one of the APIs. For example:

    curl -F "file=@any_file_binary_or_text.ext" http://127.0.0.1:5000/proxy

Profit.
