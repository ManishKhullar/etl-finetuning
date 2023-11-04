import json
from google.cloud import firestore
import os

db = firestore.Client()

# Fetch all documents from the 'train_data' collection
docs = db.collection('train_data').stream()

# Get the absolute path to the directory where the script is located
script_dir = os.path.dirname(__file__)
# Define the path to the file using the script directory
file_path = os.path.join(script_dir, 'training_data', 'training_data.jsonl')

# Open a file to write the JSONL content
with open(file_path, 'w') as file:
    # Loop through the documents and create JSON objects
    for doc in docs:
        data = doc.to_dict()
        instruction = data.get('instruction', '')
        code = data.get('code', '')

        # Construct the JSON object for the current document
        json_obj = {
            "messages": [
                {"role": "system", "content": "empty"},
                {"role": "user", "content": instruction},
                {"role": "assistant", "content": code}
            ]
        }
        # Convert the JSON object to a string and write it to the file with a newline
        file.write(json.dumps(json_obj) + "\n")
        print(json.dumps(json_obj) + "\n")

