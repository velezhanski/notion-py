from notion.client import NotionClient

client = NotionClient(token_v2="7918c45b97adf9dcec7a32a015be86024d4f2447772c2e92fa71718e6b0f86faa692c3caabdfa9b75e01ff7b127968c3f9a8c94f709715d0c640f2f0a3f965f0eda362e33f0b20a63cc9044eb362")
# page = client.get_block("https://www.notion.so/Bob-Woodruff-Foundation-3a2384b9bfe54f628dad29fef09a7a5e")

# print(page.parent.children[0])


# Access a database using the URL of the database page or the inline block
cv = client.get_collection_view("https://www.notion.so/2b0f3719ede9425dadee305fba74b3a7?v=d465bcdf86624c1cb2589fe978a0c3f8")

# List all the records with "Bob" in them
for row in cv.collection.get_rows():
  if 'Housing' in row.category:
    print("The title is '{}'".format(row.title))