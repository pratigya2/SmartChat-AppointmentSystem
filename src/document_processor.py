# src/document_processor.py

import os
import pickle
import logging
from langchain_community.document_loaders import PyPDFLoader, PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

class DocumentProcessor:
    def __init__(self, model_name="sentence-transformers/all-mpnet-base-v2", device='cpu'):
        self.model_name = model_name
        self.device = device
        self.embedding = HuggingFaceEmbeddings(
            model_name=self.model_name,
            model_kwargs={'device': self.device},
            encode_kwargs={'normalize_embeddings': False}
        )
    
    def process_documents(self, pdf_path, persist_directory):
        try:
            loader = PyPDFLoader(pdf_path)
            docs = loader.load()
        except ImportError as e:
            try:
                loader = PDFPlumberLoader(pdf_path)
                docs = loader.load()
            except Exception as ex:
                raise ex
        except Exception as e:
            raise e
        
        if not docs:
            raise ValueError("Document loading failed.")
        
        # Split documents
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
    
        # Create and persist vectorstore
        try:
            vectorstore = Chroma.from_documents(
                documents=splits,
                embedding=self.embedding,
                persist_directory=persist_directory
            )
        except Exception as e:
            raise e
    
        # Save processed documents
        try:
            processed_docs_path = os.path.join(persist_directory, 'processed_docs.pkl')
            with open(processed_docs_path, 'wb') as f:
                pickle.dump(splits, f)
        except Exception as e:
            raise e
    
        return vectorstore, splits
    
    def load_stored_data(self, persist_directory):
        try:
            embedding = HuggingFaceEmbeddings(
                model_name=self.model_name,
                model_kwargs={'device': self.device},
                encode_kwargs={'normalize_embeddings': False}
            )
            vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embedding)
        except Exception as e:
            raise e
    
        try:
            with open(os.path.join(persist_directory, 'processed_docs.pkl'), 'rb') as f:
                splits = pickle.load(f)
        except FileNotFoundError:
            raise
        except Exception as e:                  
            raise e
    
        return vectorstore, splits
