from flask import Flask, request, jsonify
from utils import query_openai

# Initialize Flask app
app = Flask(__name__)


# Define the endpoint
@app.route('/make-me-laugh', methods=['GET'])
def diagnose():
  # Get the symptoms description from the query parameter
  topic = request.args.get('topic')
  if not topic:
    return jsonify({"error": "Topic is required."}), 400

  # Query OpenAI API
  try:
    joke = query_openai(
        f"Act as an AI version of Dr Glaucomflecken. Tell a short, witty, satirical joke on the topic of {topic} for a clinical audience. Be creative."
    )
  except Exception as e:
    return jsonify({"error": str(e)}), 500

  # Return the list of possible diagnoses in JSON format
  return jsonify({"joke": joke}), 200


# Run the Flask app
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
