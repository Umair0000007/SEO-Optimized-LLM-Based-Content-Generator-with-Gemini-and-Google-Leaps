import streamlit as st
import requests
from model import load_model

# Define FastAPI endpoint URL
FASTAPI_URL = "http://localhost:8000"

def get_top_articles(keyword):
    url = f"{FASTAPI_URL}/get_top_articles/?keyword={keyword}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("urls", [])
    else:
        return []

def get_article_schema(url):
    schema_url = f"{FASTAPI_URL}/get_article_schema/?url={url}"
    response = requests.get(schema_url)
    if response.status_code == 200:
        data = response.json()
        return data.get("schema", {})
    else:
        return {}

def main():
    st.title("Article Schema Fetcher")

    # Initialize session state for URLs and article_structure
    if 'urls' not in st.session_state:
        st.session_state.urls = []

    if 'article_structure' not in st.session_state:
        st.session_state.article_structure = []

    st.subheader("Step 1 - Write Keyword")
    keyword = st.text_input("Enter a keyword", "situational awareness")
    fetch_button = st.button("Fetch Top Articles")

    if fetch_button:
        st.session_state.urls = get_top_articles(keyword)
        st.write("URL Fetching Completed.")
        st.write(st.session_state.urls)
    
    st.subheader("Step 2 - Fetch Blog Structures")
    structure_button = st.button("Fetch Schema")
    if structure_button:
        st.session_state.article_structure = []
        for url in st.session_state.urls:
            structure = get_article_schema(url)
            if structure:
                st.session_state.article_structure.append(structure)
        st.write(st.session_state.article_structure)

    st.subheader("Step 3 - Preprocess")
    preprocess_button = st.button("Preprocess Data")

    all_titles = []
    all_head1 = []
    all_head2 = []
    all_head3 = []

    if preprocess_button:
        for article in st.session_state.article_structure:
            if 'headings' in article:
                all_head1.extend(article['headings'].get('H1', []))
                all_head2.extend(article['headings'].get('H2', []))
                all_head3.extend(article['headings'].get('H3', []))
            all_titles.append(article.get('title', ''))

        st.write("Preprocessing Completed.")
        st.write("Titles:", all_titles)
        st.write("H1 Headings:", all_head1)
        st.write("H2 Headings:", all_head2)
        st.write("H3 Headings:", all_head3)

    # Flatten the list using a list comprehension
    head1_list = [item for sublist in all_head1 for item in sublist]
    # Join the flattened list into a comma-separated string
    head1 = ', '.join(head1_list)

    # Flatten the list using a list comprehension
    head2_list = [item for sublist in all_head2 for item in sublist]
    # Join the flattened list into a comma-separated string
    head2 = ', '.join(head2_list)

    # Flatten the list using a list comprehension
    title_list = [item for sublist in all_titles for item in sublist]
    # Join the flattened list into a comma-separated string
    title_is = ', '.join(title_list)

    

    # st.subheader("Step 4 - Schema Generation")
    # schema_button = st.button("Generate Article Structure")
    # if schema_button:
    #    schema = load_model(title_is, head1, head2)
    #   st.write("Schema:", schema)

if __name__ == "__main__":
    main()
