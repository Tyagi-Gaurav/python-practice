from bs4 import BeautifulSoup

with open("website.html", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print (soup.title)
print (soup.title.string)

print (soup.a)

# Get all tags
all_anchor_tags = soup.find_all(name="a")
anchor_tag_text = [tag.text for tag in all_anchor_tags]
anchor_tag_hrefs = [tag.get("href") for tag in all_anchor_tags]
print (all_anchor_tags)
print (anchor_tag_text)
print (anchor_tag_hrefs)

# Find by attribute
tag_with_id = soup.find(name="h1", id="name") # or find_all for many
print(tag_with_id)

# Find by class
section_heading = soup.find(name="h3", class_="heading")
print (section_heading)
print (section_heading.get("class"))

# By CSS Selectors
company_url = soup.select_one(selector="p a") # Or could also say #name (By ID) or .heading
print (company_url)
print (company_url.get("href"))
print (company_url.getText())


# print (soup.prettify())
