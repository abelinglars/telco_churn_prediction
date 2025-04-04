import requests

# test imput for api prediction
payload = {
    "total_charges": 0.0,
    "monthly_charges": 1.0,
    "payment_method": 1.0
}


if __name__ == "__main__":

    r = requests.post("http://127.0.0.1:8080/predict",
                      json = payload)

    print(r.text)
