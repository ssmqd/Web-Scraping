import requests, bs4, os

def main():
    search_field = input('Write topic to search: ')
    n_images = input('Write number of images you want to download: ')

    # Make directory for images
    os.makedirs('images', exist_ok=True)

    # Create and check the connection
    res = requests.get('https://imgur.com/search?q=' + search_field)
    res.raise_for_status()

    # Get images elements by their id 
    bspage = bs4.BeautifulSoup(res.text, 'html.parser')
    images = bspage.select('a[class=image-list-link] > img')

    # Iterate throught images to download selected value
    numOpen = min(int(n_images), len(images))
    for i in range(numOpen):
        imageurl = 'https:' + images[i].get('src')
        res = requests.get(imageurl)
        writefile = open(os.path.join('images', os.path.basename(imageurl)), 'wb')

        # Write images by chunks 
        for j in res.iter_content(100000):
            writefile.write(j)
            print('chunk injested')

main()
