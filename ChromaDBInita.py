import chromadb
from sentence_transformers import SentenceTransformer
import pandas as pd

def initchromaDB():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    chroma_client = chromadb.PersistentClient(path="./chroma_db") 
    collection = chroma_client.get_or_create_collection(name="booking_embeddings")
    
    df = pd.read_csv("hotel_bookings.csv")  
    df['booking_text'] = df.apply(lambda row: 
        f"Hotel: {row['hotel']}, Lead Time: {row['lead_time']}, Market Segment: {row['market_segment']}, "
        f"Country: {row['country']}, Total Nights: {row['stays_in_week_nights'] + row['stays_in_weekend_nights']}", axis=1)

    # Define batch size
    batch_size = 1000
    num_rows = len(df)
    
    for i in range(0, num_rows, batch_size):
        batch_df = df.iloc[i:i + batch_size]
        
        ids = [str(idx) for idx in batch_df.index]
        embeddings = [model.encode(text).tolist() for text in batch_df['booking_text']]
        metadatas = [{
            "hotel": row["hotel"], 
            "country": row["country"], 
            "market_segment": row["market_segment"]
        } for _, row in batch_df.iterrows()]
        
        collection.add(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadatas
        )
        print(f"Processed batch {i // batch_size + 1}/{(num_rows - 1) // batch_size + 1}")

    print("Booking data stored as vector embeddings in ChromaDB! ✅")
    return collection
