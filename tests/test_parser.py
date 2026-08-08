from scrapers.parser import HTMLParser


html = """
<html>
    <head>
        <title>Dell XPS 13</title>
    </head>

    <body>

        <h1 class="product-name">
            Dell XPS 13
        </h1>

        <span class="price">
            ₹129999
        </span>

        <img
            class="product-image"
            src="xps13.jpg"
        >

    </body>
</html>
"""


parser = HTMLParser(html)

print("Title:", parser.get_title())

print(
    "Product:",
    parser.find_text(".product-name")
)

print(
    "Price:",
    parser.find_text(".price")
)

print(
    "Image:",
    parser.find_attribute(
        ".product-image",
        "src"
    )
)

print("Page text:", parser.get_text())