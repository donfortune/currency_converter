API = "XXXXXXXXX"
BASE_URL = "http://api.exchangeratesapi.io/v1/"  # Address to send API request to

from requests import get

endpoint = BASE_URL + "latest?access_key=" + API

# Now you can use the 'endpoint' variable to make the API request
response = get(endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    rates = data.get('rates', {})
    dates = data.get('date', '')
   
    print("Date:", dates)

    # Print out all the countries
    for currency in rates:
        print(currency)
    selected_currency = input('Please select your currency:')
    amount = float(input("How much do you want to convert"))
    against_currency = input("Select your other currency:")
    
    if selected_currency in rates:
        Selected_rate =  rates[selected_currency]
    if against_currency in rates:
        against_rate = rates[against_currency]
    calculated_rate = amount  * (Selected_rate  / against_rate)
    print(f"{amount:.2f} {selected_currency} is equivalent to {calculated_rate} {against_currency}")


else:
    # Handle the error appropriately
    print("Error occurred:", response.text)
