from notion.client import NotionClient

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
client = NotionClient(token_v2="7918c45b97adf9dcec7a32a015be86024d4f2447772c2e92fa71718e6b0f86faa692c3caabdfa9b75e01ff7b127968c3f9a8c94f709715d0c640f2f0a3f965f0eda362e33f0b20a63cc9044eb362")

# Replace this URL with the URL of the page you want to edit
page = client.get_block("https://www.notion.so/ACP-American-Corporate-Partners-ccc5b8d3be294ac0a8df87e601c1cddc")

print("Page Info: ", page.logo)

# Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
# page.title = "The title has now changed, and has *live-updated* in the browser!"