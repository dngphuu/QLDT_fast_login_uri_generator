import requests
import json
import base64
import urllib.parse
import os
from dotenv import load_dotenv
import sys
import traceback
import pyperclip

load_dotenv()

def get_fast_login_link(username, password):
    login_api_url = "https://qldt.ptit.edu.vn/api/auth/login"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9,vi;q=0.8",
        "content-type": "text/plain",
        "idpc": "0",
        "origin": "https://qldt.ptit.edu.vn",
        "referer": "https://qldt.ptit.edu.vn/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "ua": "MFg0D3N5UTrDk3JVVjEOd3JbOMKrFzEmK3ILDSFE",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
    }
    payload = {
        'username': username,
        'password': password,
        'grant_type': 'password'
    }
    response = requests.post(login_api_url, headers=headers, data=payload)

    if response.status_code == 200:
        try:
            response_json = response.json()
            curr_user_data_json_string = json.dumps(response_json)
            base64_encoded_curr_user = base64.b64encode(curr_user_data_json_string.encode('utf-8')).decode('utf-8')
            url_encoded_curr_user = urllib.parse.quote(base64_encoded_curr_user)
            base_url = "https://qldt.ptit.edu.vn/public/#/home"
            fast_login_url = f"{base_url}?CurrUser={url_encoded_curr_user}"
            return fast_login_url
        except json.JSONDecodeError:
            print("Error: Could not parse JSON response.")
            print("Response Text:", response.text)
            return None
    else:
        print(f"Login request failed with status code: {response.status_code}")
        print("Response Text:", response.text)
        return None

if __name__ == "__main__":
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        
        print(f"Current directory: {os.getcwd()}")
        print("Loading environment variables...")
        
        load_dotenv(verbose=True)
        
        username = os.environ.get("USERNAME")  # Changed back to USERNAME
        password = os.environ.get("PASSWORD")
        output_file = os.path.join(script_dir, "fast_login_link.txt")

        print(f"Username found: {'Yes' if username else 'No'}")
        print(f"Password found: {'Yes' if password else 'No'}")

        if not username or not password:
            print("Error: USERNAME or PASSWORD not found in environment variables")
            sys.exit(1)

        fast_login_link = get_fast_login_link(username, password)

        if fast_login_link:
            print("\nGenerated Fast Login Link:")
            print(fast_login_link)
            # Copy to clipboard
            pyperclip.copy(fast_login_link)
            print("Link has been copied to clipboard!")
            try:
                with open(output_file, "w", encoding='utf-8') as f:
                    f.write(fast_login_link)
                print(f"\nLink saved to: {output_file}")
            except Exception as e:
                print(f"Error writing to file: {e}")
                traceback.print_exc()
                sys.exit(1)
        else:
            print("Failed to generate fast login link")
            sys.exit(1)

    except Exception as e:
        print(f"Unexpected error: {e}")
        traceback.print_exc()
        sys.exit(1)