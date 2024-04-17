import requests

url = "https://api.limewire.com/api/image/generation"

payload = {
  "prompt": "a small Plant growing in the drought ",
  "aspect_ratio": "1:1"
}

headers = {
  "Content-Type": "application/json",
  "X-Api-Version": "v1",
  "Accept": "application/json",
  "Authorization": "Bearer lmwr_sk_0eD6Q1nQyG_TKktiaEJ6sHC653R97yTdCN0IMNvcAhNIuXPB"
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(data)
