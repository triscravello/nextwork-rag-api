import chromadb

client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection("docs")

# Clear existing documents
existing_ids = collection.get()["ids"]
if existing_ids:
    collection.delete(ids=existing_ids)

with open("k8s.txt", "r") as f:
    text = f.read()

collection.add(documents=[text], ids=["k8s"])

print("Embedding stored in Chroma")
