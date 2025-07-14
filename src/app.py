# Import required modules
from flask import Flask, jsonify
import requests

# Initialize Flask app 
app = Flask(__name__)

# Route to get public gists for a given GitHub username
@app.route('/<user>',methods=['GET'])

def get_user_gists(user):
     headers = {
      "Accept": "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28",
     }

     # Generate the GitHub API URL
     url=f"https://api.github.com/users/{user}/gists"

     # Make the GET request to GitHub API
     response = requests.get(url, headers=headers)

     # Handle the response based on status code 
     if response.status_code == 200:
          gists = response.json()
          if not gists:
               return jsonify({"message": "No public gists exist for this user."}), response.status_code
          return jsonify(gists), response.status_code

     elif response.status_code == 404:
          return jsonify({"error": "GitHub user not found"}), response.status_code

     elif response.status_code == 403:
          return jsonify({"error": "Access Forbidden – you may have exceeded GitHub's rate limit"}), response.status_code
          
     else:
          return jsonify({"error": f"Unexpected error from GitHub (status code: {response.status_code})"}), response.status_code





