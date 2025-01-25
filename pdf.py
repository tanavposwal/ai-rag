import os
from llama_index import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers import PDFReader


def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )

    return index


pdf_path = os.path.join("data", "India.pdf")
india_pdf = PDFReader().load_data(file=pdf_path)
india_index = get_index(india_pdf, "india")
india_engine = india_index.as_query_engine()

pdf_path = os.path.join("data", "Deforestation.pdf")
deforestation_pdf = PDFReader().load_data(file=pdf_path)
deforestation_index = get_index(deforestation_pdf, "deforestation")
deforestation_engine = deforestation_index.as_query_engine()
