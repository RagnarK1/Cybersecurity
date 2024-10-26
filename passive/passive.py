import os
import json
import click
import requests
from bs4 import BeautifulSoup

# API keys
ip_api_key = "5a6700e6ac0c0281f765beb9553826d4"
username_api_key = "d29f5f8152msh40a6bdc4d45793fp1085a7jsn0a3bde1f6198"

# Function to search for full name
def fullname_search(full_name):
    url = f"https://www.whitepages.be/Search/Person/?what={full_name}"
    
    # Send HTTP GET request to the URL
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract detail page URL from "More Info" button
        more_info_button = soup.find('a', {'class': 'btn wg-btn wg-btn--blue', 'data-ta': 'MoreInfoClick'})
        if more_info_button and 'href' in more_info_button.attrs:
            detail_url = "https://www.whitepages.be" + more_info_button['href']
            detail_response = requests.get(detail_url)
            if detail_response.status_code == 200:
                detail_soup = BeautifulSoup(detail_response.content, 'html.parser')
                # Extract name
                name_element = detail_soup.find('h1', class_='wg-detail-title').find('span')
                name = name_element.get_text(strip=True) if name_element else 'Name not found'
                # Extract address
                address_element = detail_soup.find('span', class_='wg-address')
                address = address_element.get_text(strip=True) if address_element else 'Address not found'
                # Extract phone number
                phone_element = detail_soup.find('span', class_='wg-label')
                phone = phone_element.get_text(strip=True) if phone_element else 'Phone not found'
                # Return the extracted information along with the full name
                return {'Name': name, 'Address': address, 'Phone': phone}
            else:
                print(f"Error: Failed to fetch detail page URL ({detail_response.status_code})")
                return None
        else:
            print("Error: 'More Info' button not found")
            return None
    else:
        print(f"Error: Failed to fetch URL ({response.status_code})")
        return None

# Function to lookup IP address
def ip_lookup(ip_address, api_key):
    # Check if the IP address is localhost or in the local network
    if ip_address.startswith('127.') or ip_address == 'localhost':
        print("Local IP address. No location information available.")
        return None
    
    # Construct the API endpoint URL
    api_endpoint = "https://api.whatismyip.com/ip-address-lookup.php"
    
    # Set up parameters for the API request
    params = {
        "key": api_key,
        "input": ip_address,
        "output": "json"
    }
    
    # Send a GET request to the API endpoint
    response = requests.get(api_endpoint, params=params)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        try:
            # Try to parse the JSON response
            result = response.json()
            # Check if the response contains the expected key
            if "ip_address_lookup" in result:
                # Extract IP address information
                lookup_result = result["ip_address_lookup"]
                if lookup_result:
                    ip_info = lookup_result[0]
                    country = ip_info.get("country", "Unknown")
                    region = ip_info.get("region", "Unknown")
                    city = ip_info.get("city", "Unknown")
                    postalcode = ip_info.get("postalcode", "Unknown")
                    isp = ip_info.get("isp", "Unknown")
                    latitude = ip_info.get("latitude", "Unknown")
                    longitude = ip_info.get("longitude", "Unknown")
                    # Return the IP address information as a dictionary
                    return {
                        "Country": country,
                        "Region": region,
                        "City": city,
                        "Postal Code": postalcode,
                        "ISP": isp,
                        "Latitude": latitude,
                        "Longitude": longitude
                    }
                else:
                    # If no IP address information found
                    print("No IP address information found.")
                    return None
            else:
                # If the response format is invalid
                print("Invalid response format.")
                return None
        except json.decoder.JSONDecodeError:
            # If there's an error decoding the JSON response
            print("Error decoding JSON response. No information available.")
            return None
    else:
        # If there's an API error (status code other than 200)
        print(f"API error: {response.status_code}")
        return None

def username_search(username):
    # Define the URL and headers for the API request
    url = "https://username-hunter-api.p.rapidapi.com/hunt/username"
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": username_api_key,
        "X-RapidAPI-Host": "username-hunter-api.p.rapidapi.com"
    }
    
    # List of social media platforms to check
    platforms = ["facebook", "github", "instagram", "linkedin", "skype", "snapchat", "threads", "tiktok", "twitter", "youtube"]
    
    # Initialize a dictionary to store results for each platform
    result = {platform.capitalize(): "no" for platform in platforms}
    
    # Iterate through each platform
    for platform in platforms:
        # Set up parameters for the API request
        params = {"platforms": platform}
        payload = {"username": username}
        
        # Send a POST request to the API endpoint
        response = requests.post(url, json=payload, headers=headers, params=params)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json().get('data', [])
            # Check if the username is available on the current platform
            if any(item['available'] for item in data):
                result[platform.capitalize()] = "yes"
        else:
            # Print an error message if there's an API error
            print(f"API error for {platform}: {response.status_code}")

    # Return the dictionary containing availability status for each platform
    return result

# Command line interface
@click.command()                                                        
@click.option('-fn', '--full-name', help='Search with full name')
@click.option('-ip', '--ip-address', help='Search with IP address')
@click.option('-u', '--username', help='Search with username')
def passive(full_name, ip_address, username):
    # Check which option is provided and call the corresponding function
    if full_name:
        result = fullname_search(full_name)
        # Check if the result is not None
        if result:
            save_result(result, "result.txt")
        else:
            # Print a message if no results are found
            print("No results found. Unable to create result.txt.")
    elif ip_address:
        result = ip_lookup(ip_address, ip_api_key)
        # Check if the result is not None
        if result:
            save_result(result, "result.txt")
        else:
            # Print a message if no results are found
            print("No results found. Unable to create result.txt.")
    elif username:
        result = username_search(username)
        # Check if the result is not None
        if result:
            save_result(result, "result.txt")
        else:
            # Print a message if no results are found
            print("No results found. Unable to create result.txt.")
    else:
        # Print a message if no valid option is provided
        click.echo("Please provide a valid option. Use --help for assistance.")

# Function to save result to a file
def save_result(result, filename):
    # Check if the result is None
    if result is None:
        print("No results found.")
    else:
        index = 1
        # Check if the file already exists and append an index if needed
        while os.path.exists(filename):
            filename = f"result{index}.txt"
            index += 1
        
        # Write the result to the file
        with open(filename, 'w') as file:
            for key, value in result.items():
                file.write(f"{key}: {value}\n")
        # Print a message indicating where the results were saved
        print(f"Results saved to {filename}")

if __name__ == '__main__':
    # Call the passive function when the script is executed
    passive()
