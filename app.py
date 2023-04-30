
from documents.pancard import verify_pancard
from waitress import serve
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app = Flask(__name__)
app = Flask(__name__)


@app.route('/verify-document', methods=['GET'])
@cross_origin()
def update_features():
    args = request.args
    file_link = args.get('file_link')
    status = False
    doc_type = "Others"

    status = verify_pancard(file_link)
    if status:
        doc_type = "Pan Card"

    # code for other documents

    return jsonify({'status': status, 'doc_type': doc_type})


if __name__ == "__main__":
    app.config['CORS_HEADERS'] = 'Content-Type'
    print("Starting server")
    serve(app, host="0.0.0.0", port="8000")
