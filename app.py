from flask import Flask, request, jsonify

from model.sentiment_analysis import SentimentAnalysis

__author__ = "Wesam Al-Nabki"

app = Flask(__name__)

sentiment_classification_service = SentimentAnalysis()


@app.route('/classify_sentiment', methods=['POST'])
def classify_sentiment():
    if 'text' in request.json:
        text = request.json.get('text', '')
    else:
        text = ''

    response = sentiment_classification_service.predict_sentiment(text=text)
    return jsonify(response)


# run using:
# python -m flask run --host=0.0.0.0 --port=9066
#
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9066, debug=False, use_reloader=False)
