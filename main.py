from flask import Flask, request, jsonify
from utils import query_openai

# Initialize Flask app
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
  return jsonify('hello'), 200


# Define the endpoint
@app.route('/joke', methods=['GET'])
def joke():
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


# Define the endpoint
@app.route('/primary-care', methods=['GET'])
def primary_care():
  # Get insights description from the query parameter
  population = request.args.get('population')
  if not population:
    return jsonify({"error": "population is required."}), 400

  # Query OpenAI API
  try:
    value_to_population = query_openai(
        f"Act as an innovator like Clay Christensen who understand US healthcare deeply, and reflect on the value that primary care can bring to {population}."
    )
  except Exception as e:
    return jsonify({"error": str(e)}), 500

  # Return the list of possible diagnoses in JSON format
  return jsonify({"primary_care": value_to_population}), 200


# Run the Flask app
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
