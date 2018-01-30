from flask import Flask
from flask import Response
from flask import stream_with_context
import requests
from flask import request

app = Flask(__name__)


# Upload file as stream to a file.
@app.route("/upload", methods=["POST"])
def upload():
    with open("/tmp/output_file", "bw") as f:
        chunk_size = 4096
        while True:
            chunk = request.stream.read(chunk_size)
            if len(chunk) == 0:
                return
            f.write(chunk)


# Download from provided URL.
@app.route('/<path:url>')
def download(url):
    req = requests.get(url, stream=True)
    return Response(stream_with_context(req.iter_content()), content_type=req.headers['content-type'])


# Proxy uploaded files as stream to another web API without saving them to disk or holding them in memory.
# This example uses multipart form data upload for both this API and destination API.
#
# Test this endpoint with:
# curl -F "file=@some_binary_file.pdf" http://127.0.0.1:5000/proxy
@app.route("/proxy", methods=["POST"])
def proxy():
    # use data=... or files=..., etc in the call below - this affects the way data is POSTed: form-encoded for `data`,
    # multipart encoding for `files`. See the code/docs for more details here:
    # https://github.com/requests/requests/blob/master/requests/api.py#L16
    resp = requests.post('http://destination_host/upload_api', files={'file': request.stream})
    return resp.text, resp.status_code


if __name__ == '__main__':
    app.run()
