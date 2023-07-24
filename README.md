# UI Bulk Save Tool
This is a simple Python script with a graphical user interface (GUI) that allows users to perform bulk data save operations. The script interacts with two APIs, first to obtain an access token from [YOUR_AUTHORIZE_REQUEST_URL], and then uses that token to make POST requests to [YOUR_AUTHORIZE_REQUEST_URL]. Users can input their credentials, main ID, sub ID, and other necessary parameters through the GUI. The script reads user IDs from a text file and iterates through each user, performing bulk save operations for each sub ID. The script provides real-time feedback on successful saves and displays error messages if any save operations fail.

How to Use:
1. Enter your login credentials and main ID.
2. Click the '+' button to dynamically add multiple sub IDs.
3. Enter the desired IsActiveFlag value.
4. Click "Dosya Seç" to select the text file containing user IDs.
5. Click "Başlat" to start the bulk save process.
6. The script will show success and error messages for each user save.

Note: Replace [YOUR_AUTHORIZE_REQUEST_URL] with the appropriate URLs for token acquisition and data save APIs.

Author: [Alperen Kuru]
