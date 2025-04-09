import requests

if __name__ == '__main__':
    # URL of the Hugging Face Space endpoint
    url = "https://amirkiarafiei-github-hf-sync.hf.space/"

    # Send a GET request and print the response
    response = requests.get(url)
    print(response.text)