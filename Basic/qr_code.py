import requests


data = input("Enter your text or number: ")
filename = input("Enter filename e.g qrcode.png: ")

size = input("Enter size (e.g., 200x200): ") or "200x200"

url = f"https://api.qrserver.com/v1/create-qr-code/?data={data}&size={size}"

response = requests.get(url)

if response.status_code ==  200 : 
    with open(filename,'wb') as file:
     file.write(response.content)
     print(f"QR code saved as {filename}")
else:
    print("Failed to generate QR code")