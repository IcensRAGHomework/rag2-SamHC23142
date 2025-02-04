from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)
q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"

def hw02_1(q1_pdf):
    loader = PyPDFLoader(file_path = q1_pdf)
    docs = []
    docs_lazy = loader.lazy_load()

    for doc in docs_lazy:
        docs.append(doc)
    
    text_splitter = CharacterTextSplitter(
        # separator="\n\n",
        # chunk_size=100,
        chunk_overlap=0,
        #length_function=len,
        #is_separator_regex=False,
    )
    
    texts = text_splitter.split_documents(docs)

    return(texts[-1])
    
def hw02_2(q2_pdf):
    loader = PyPDFLoader(file_path = q2_pdf)
    docs = []
    docs_lazy = loader.lazy_load()

    for doc in docs_lazy:
        docs.append(doc)
    
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n第", "\n   第"],
        chunk_size=5,
        chunk_overlap=0,
        # length_function=len
    )
    texts = text_splitter.split_documents(docs)    
    
    #############Varify#####################
    # page_chunk_counts = []

    # for i, doc in enumerate(docs):
        # chunks = text_splitter.split_text(doc.page_content)
        # page_chunk_counts.append(len(chunks))
        # print(f"Page {i + 1} has {len(chunks)} chunks.")
        # if(i == 7):
            # for j, chunk in enumerate(chunks):
                # print(f"Chunk {j + 1} of Page {i + 1}: {chunk}")
    # print(sum(page_chunk_counts))
    
    return len(texts)
