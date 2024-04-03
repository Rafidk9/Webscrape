import requests
from bs4 import BeautifulSoup
import re

def scrape_instagram_profiles(keywords):
    base_url = "https://www.instagram.com/explore/tags/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    
    for keyword in keywords:
        url = base_url + keyword
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print("ok")
            soup = BeautifulSoup(response.text, 'html.parser')
            profile_links = soup.find_all('a', href=True)
            
            for link in profile_links:
                profile_url = link['href']
                if '/p/' in profile_url:
                    continue  # Skip posts
                profile_response = requests.get(f"https://www.instagram.com{profile_url}", headers=headers)
                
                if profile_response.status_code == 200:
                    print("ok")
                    profile_soup = BeautifulSoup(profile_response.text, 'html.parser')
                    
                    # Extract profile details
                    username_tag = profile_soup.find("h2", class_="BrX75")
                    bio_tag = profile_soup.find("div", class_="-vDIg")
                    
                    if username_tag and bio_tag:
                        username = username_tag.get_text(strip=True)
                        bio = bio_tag.get_text(strip=True)
                        
                        # Check if bio contains an email address
                        email = re.findall(r'[\w\.-]+@[\w\.-]+', bio)
                        email = email[0] if email else "Not provided"
                        
                        print("Username:", username)
                        print("Bio:", bio)
                        print("Email:", email)
                        print()
                    else:
                        print("Error: Unable to extract profile details for URL:", profile_url)
                else:
                    print("Error: Unable to access profile URL:", profile_url)
        else:
            print("Error: Unable to access hashtag page.")

# Example keywords: ['football', 'messi', 'ronaldo', 'neymar']
scrape_instagram_profiles(['football', 'messi', 'ronaldo', 'neymar'])
