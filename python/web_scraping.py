# Import the client libraries

import requests
from bs4 import BeautifulSoup
import re

# Select the web page, and fetch a response.

url = "https://www.npr.org/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Now, we use soup to find all elements with the "<a>" tag

links = soup.find_all("a") 

# Notice that using the get method for href returns several section labels

for link in links:
    print("Link:", link.get("href"), "Text:", link.string)

# We will now filter the list to include only items that contain the text 'tiny-desk'
# a video series of live concerts hosted by NPR Music.

tiny_desk_urls = []

for i in range(len(links)):
    text = links[i].get("href")

    if text is None:
        pass

    else:
        # The period and plus indicates regex should be greedy, and capture
        # all characters before and after. You may need to use more complex
        # logic depending on your needs.
        link = re.search('.+tiny-desk.+', links[i].get("href"))

        if link is None:
            pass

        else:
            tiny_desk_urls.append(link[0])

print('There are', len(tiny_desk_urls), "tiny desk links.")

# And now lets see what URLs we captured.

for i in tiny_desk_urls:
    print(i)

# Thank you for reading, I hope this helps!

# Check out the Beautiful Soup documentation for more ways to handle the data.
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# For more guidance on Regex, you can find capture patterns here:
# https://www.w3schools.com/python/python_regex.asp
