from fastapi import FastAPI
from search import get_top_articles, get_article_schema 

app = FastAPI()

@app.get("/get_top_articles/")
async def get_top_articles_handler(keyword: str):
    try:
        urls = get_top_articles(keyword)  # Call get_top_articles correctly
        return {"urls": urls}
    except ValueError as e:
        return {"error": str(e)}


@app.get("/get_article_schema/")
async def get_article_schema_handler(url: str):
    try:
        schema = get_article_schema(url)
        return {"schema": schema}
    except ValueError as e:
        return {"error": str(e)}
