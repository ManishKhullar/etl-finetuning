### Fine-tuning LLM model

![alt text](ETL-openai.jpeg "Title")

- Create a project or select existing
- Enable App Engine and Firestore API's
- Create Firestore database
- Run `pip install -r requirements. txt`
- Run `gcloud app create`
- Run `gcloud app deploy`

For ETL use `python transform/transform_to_jsonl.py`

Or create .env file in root dir with env var `GCLOUD_PROJECT=YOUR_PROJECT_ID` and use jupyter notebook at `transform/transform_to_json.ipynb`

## TODO

- Train the model at OpenAI API with custom data
- Build the full pipeline on the cloud

\*maybe some instructions are missing
