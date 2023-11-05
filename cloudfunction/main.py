from google.cloud import firestore
from google.cloud import storage
import tempfile
import json

def export_to_storage(request):
    try:
        # Initialize Firestore client
        db = firestore.Client()

        # Initialize Cloud Storage client
        storage_client = storage.Client()
        # Replace 'fine-tuning-training-data' with your Cloud Storage bucket name
        bucket = storage_client.bucket('fine-tuning-training-data')

        # Use a temporary file to avoid local filesystem constraints of Cloud Functions
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.jsonl') as temp_file:
            # Fetch documents from the 'train_data' collection
            docs = db.collection('train_data').stream()

            # Write JSONL content to temporary file
            for doc in docs:
                data = doc.to_dict()
                instruction = data.get('instruction', '')
                code = data.get('code', '')
                json_obj = {
                    "messages": [
                        {"role": "system", "content": "empty"},
                        {"role": "user", "content": instruction},
                        {"role": "assistant", "content": code}
                    ]
                }
                temp_file.write(json.dumps(json_obj) + "\n")

            # Upload the temporary file to Cloud Storage
            # Replace 'training_data.jsonl' with your preferred blob name
            blob = bucket.blob('training_data.jsonl')
            temp_file.seek(0)  # Rewind the file before reading to upload
            blob.upload_from_file(temp_file)

        # After the loop, return a success message
        return f"Data exported to {blob.public_url}", 200
    except Exception as e:
        # If an error occurs, return the error message with a 500 status code
        return str(e), 500
