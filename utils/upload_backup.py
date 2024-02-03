import os
import sys

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()

SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_API_SERVICE_ACCOUNT_FILE")
PARENT_FOLDER_ID = os.getenv("GOOGLE_API_PARENT_FOLDER_ID")
SCOPES = ["https://www.googleapis.com/auth/drive"]


def authenticate():
    """Authenticate and return authenticated service account credentials.
    Returns:
      Credentials, the authorized credentials.
    """
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return credentials


def upload_file(file_path):
    """Upload a backup zip file to a google drive folder.
    Returns : Id of the uploaded zip.
    """
    try:
        creds = authenticate()
        service = build("drive", "v3", credentials=creds)
        file_name = os.path.basename(file_path)

        file_metadata = {"name": file_name, "parents": [PARENT_FOLDER_ID]}

        print(f"Uploading: {file_name}")
        file = (
            service.files().create(body=file_metadata, media_body=file_path).execute()
        )

        print(f'File ID: {file.get("id")}')

    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None

    return file.get("id")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 upload_backup.py <backup_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    upload_file(file_path)
