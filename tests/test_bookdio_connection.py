# from scrapers.base_scraper import BaseScraper


# scraper = BaseScraper()

# try:

#     url = "https://www.bookdio.org/all-books"

#     html = scraper.fetch_page(url)

#     print("Successfully fetched Bookdio!")

#     print("\nHTML Length:")
#     print(len(html))

#     print("\nFirst 1000 characters:\n")
#     print(html[:1000])

# finally:

#     scraper.close()

    ##output
#      python -m tests.test_bookdio_connection
# Successfully fetched Bookdio!

# HTML Length:
# 1692242

# First 1000 characters:

# <!DOCTYPE html>
# <html lang="en">
# <head>
  
#   <meta charset='utf-8'>
#   <meta name="viewport" content="width=device-width, initial-scale=1" id="wixDesktopViewport" />
#   <meta http-equiv="X-UA-Compatible" content="IE=edge">
#   <meta name="generator" content="Wix.com Website Builder"/>

#   <link rel="icon" sizes="192x192" href="https://static.wixstatic.com/media/ef8af1_06866286c2314317b1353beae89ac942%7Emv2.png/v1/fill/w_192%2Ch_192%2Clg_1%2Cusm_0.66_1.00_0.01/ef8af1_06866286c2314317b1353beae89ac942%7Emv2.png" type="image/png"/>
#   <link rel="shortcut icon" href="https://static.wixstatic.com/media/ef8af1_06866286c2314317b1353beae89ac942%7Emv2.png/v1/fill/w_32%2Ch_32%2Clg_1%2Cusm_0.66_1.00_0.01/ef8af1_06866286c2314317b1353beae89ac942%7Emv2.png" type="image/png"/>
#   <link rel="apple-touch-icon" href="https://static.wixstatic.com/media/ef8af1_06866286c2314317b1353beae89ac942%7Emv2.png/v1/fill/w_180%2Ch_180%2Clg_1%2Cusm_0.66_1.00_0.01/ef8af1_06866286c2314317b1353beae89ac942%7Emv2.png" type="image



from scrapers.base_scraper import BaseScraper


scraper = BaseScraper()

try:

    url = "https://www.bookdio.org/all-books"

    html = scraper.fetch_page(url)

    print("Successfully fetched Bookdio!")

    print("\nHTML Length:")
    print(len(html))

    # Search for useful keywords
    keywords = [
        "title",
        "author",
        "rating",
        "book",
        "category"
    ]

    for keyword in keywords:

        print(f"\nSearching for: {keyword}")

        index = html.lower().find(keyword.lower())

        if index != -1:

            print("Found!")

            start = max(0, index - 300)
            end = min(len(html), index + 700)

            print(html[start:end])

        else:
            print("Not found.")

finally:

    scraper.close()
