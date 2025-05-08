from pathlib import Path

from elasticsearch import Elasticsearch

from langchain_elasticsearch import ElasticsearchStore
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.retrievers import ElasticSearchBM25Retriever
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.suchef_bot.settings import Settings


settings = Settings()

BASE_DIR = Path(__file__).resolve().parent.parent

FILE_PATH = BASE_DIR / "documents" / "База_знаний.txt"


with open(FILE_PATH, encoding="utf-8") as file:
    text = file.read()

print(f"Количество символов: {len(text)}")


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=20,
    length_function=len,
)

chunks = text_splitter.create_documents([text])

N = 5

print(f"Всего чанков: {len(chunks)}")
print(f"Первые {N} чанков:")
print(chunks[:N])

embeddings = HuggingFaceEmbeddings(
    model_name=settings.embeddings.MODEL_NAME,
    model_kwargs={"device": "cpu"},
    encode_kwargs={'normalize_embeddings': False},
)


elastic_client = Elasticsearch(
    hosts=settings.elasticsearch.elasticsearch_url,
    basic_auth=(settings.elasticsearch.ELASTIC_USER, settings.elasticsearch.ELASTIC_PASSWORD)
)

indices = elastic_client.cat.indices(h='index').split()

try:
    for index in indices:
        print(f"Удаление индекса: {index}")
        elastic_client.indices.delete(index=index, ignore=[400, 404])
    print("Все индексы удалены")
except Exception as e:
    print(e)
    print("Нет индексов")


elastic_store = ElasticsearchStore(
    es_url=settings.elasticsearch.elasticsearch_url,
    index_name="suchef-vectors",
    embedding=embeddings,
    es_user=settings.elasticsearch.ELASTIC_USER,
    es_password=settings.elasticsearch.ELASTIC_PASSWORD,
)

elastic_store.add_documents(documents=chunks)
print("Документы добавлены в векторное  хранилище.")

bm25_retriever = ElasticSearchBM25Retriever(
    client=elastic_client,
    index_name="suchef-docs",
)

bm25_retriever.add_texts([document.page_content for document in chunks])
print("Документы добавлены в индекс BM25.")