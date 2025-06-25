import requests
from requests.auth import HTTPBasicAuth

# 🔐 Replace these with your actual credentials
EXOTEL_SID = "unitedinstituteoftechnology1"
EXOTEL_TOKEN = "d59df1fe5c4fd580d78a3a56d91ca81f85c328245de379fc"
FROM_NUMBER = "01139589394"  # Your Exotel virtual number (usually begins with 011)
TO_NUMBER = "7068378758"     # Recipient's number (your number)

# 🧠 Emergency message to be spoken on call
message = """
Hello, this is an emergency AI assistant from AmbuBuddy.
A patient is bleeding and unconscious near Najarapur.
Please send an ambulance as fast as possible.
"""

# 🔊 Create a dynamic IVR XML file (called .xml or .twiml file)
ivr_url = f"https://my.exotel.com/{EXOTEL_SID}/exoml/start_voice.xml"
ivr_payload = f"""
<Response>
  <Say>{message}</Say>
</Response>
"""

# 🔧 Make the call using Exotel's Voice API
response = requests.post(
    f"https://api.exotel.com/v1/Accounts/{EXOTEL_SID}/Calls/connect",
    auth=HTTPBasicAuth(EXOTEL_SID, EXOTEL_TOKEN),
    data={
        'From': FROM_NUMBER,
        'To': TO_NUMBER,
        'CallerId': FROM_NUMBER,
        'Url': ivr_url,
        'CallType': 'trans'  # transactional call
    }
)

# ✅ Output the result
if response.status_code == 200:
    print("📞 Emergency call successfully triggered!")
else:
    print("❌ Failed to initiate call.")
    print("Response:", response.status_code, response.text)
