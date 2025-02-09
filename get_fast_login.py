import requests
import json
import base64
import urllib.parse
import os
from dotenv import load_dotenv

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
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/132.0.0.0"
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
    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")
    output_file = "fast_login_link.txt" # Define output file name

    if not username or not password:
        print("Error: Please set USERNAME and PASSWORD in your .env file.")
    else:
        fast_login_link = get_fast_login_link(username, password)

        if fast_login_link:
            print("Generated Fast Login Link:")
            print(fast_login_link)
            # Remove automatic browser opening:
            # webbrowser.open(fast_login_link)

            # Write the link to the output file
            try:
                with open(output_file, "w") as f:
                    f.write(fast_login_link)
                print(f"Fast login link saved to: {output_file}")
            except Exception as e:
                print(f"Error writing to file {output_file}: {e}")

        else:
            print("Failed to generate fast login link.")