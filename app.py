from flask import Flask, render_template, request, jsonify
from ChromaDBInita import initchromaDB
from Cleaning import cleanData
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("hotel_bookings.csv")
df = cleanData(df)

print("Data Cleaning Done! ✅")
print("Initialising ChromaDB...")

# chromaDB initialisation
collection = initchromaDB()
print("ChromaDB Initialised! ✅")


@app.route("/")
def home_page():
    return "Welcome!\nPlease go to /analytics → for analytics reports.\n/ask → Answers booking-related questions"

@app.route("/analytics", methods=["GET"])
def analyticsReport():
    try:
        return render_template("Dashboard.html"), 200 
    except Exception as e:
        print("AnalyticsReport Error:", str(e))
        return "Internal Server Error", 500  # Return proper HTTP response

@app.route("/ask", methods=["GET"])
def askPage():
    try:
        return render_template("Ask.html"), 200
    except Exception as e:
        print("AskPage Error:", str(e))
        return "Internal Server Error", 500 



@app.route("/getanswer", methods=["POST"])
def asnwerQuestion():
    try:
        data = request.json
        query = data.get("query")
        query_embedding = model.encode(query).tolist()
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=5  
        )

        return jsonify( { "query" : query , "answer" : results } ), 200
    except Exception as e:
        print("AskPage Error:", str(e))
        return "Internal Server Error", 500 



if __name__ == "__main__":
    app.run(host="localhost", port=8088, debug=True)
