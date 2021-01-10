from flask_restful import Resource
from notion.client import NotionClient

client = NotionClient(token_v2="d0228534fa14ec9e53c78d360aa85c8ec633ddedb18b6cd7ea60cfc6b9d9e09d59f1d4be60aabf1ec14f2f453580faf9ef90ecdc12ec98ccef22f308581983e46f2193a402940edea12e886261c0")
page = client.get_block("https://www.notion.so/ACP-American-Corporate-Partners-ccc5b8d3be294ac0a8df87e601c1cddc")
cv = client.get_collection_view("https://www.notion.so/2b0f3719ede9425dadee305fba74b3a7?v=d465bcdf86624c1cb2589fe978a0c3f8")
pages = []

def get_title(page):
  return page.get('title')

class Todo(Resource):
  def get(self, id):
    pages.clear()
    for row in cv.collection.get_rows():
      if id in row.category:
        temp = {
          'title': row.title,
          'website': row.website,
          'description': row.description,
          'logo': row.logo
          }
        pages.append(temp)
    pages.sort(key=get_title)
    return pages, 200

