import requests
api_base_url = "https://api.crowdstrike.com/some-endpoint"
auth_token = "YOUR_AUTH_TOKEN"  
yara_rule = {
    "name": "Example YARA Rule",
    "description": "An example YARA rule for detection",
    "platform_name": "Windows",
    "rule": "rule example_rule { strings: $a = \"example_string\" condition: $a }",
}
 
def create_crowdstrike_yara_rule():
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    
    endpoint = f"{api_base_url}/yara/rules"
    
    try:
        response = requests.post(endpoint, json=yara_rule, headers=headers)
        if response.status_code == 201:
            print("YARA rule successfully added to CrowdStrike Falcon.")
        else:
            print(f"Error: Failed to add YARA rule. Status code: {response.status_code}")
            print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
 
if __name__ == "__main__":
    create_crowdstrike_yara_rule()
