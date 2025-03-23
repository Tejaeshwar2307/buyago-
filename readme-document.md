# Hotel Booking Analysis System

A comprehensive web application for analyzing hotel booking data using Flask, ChromaDB for vector embeddings, and data visualization.

## Overview

This project provides a data analysis system for hotel booking data with two main features:
- Interactive analytics dashboard with data visualizations
- Natural language query interface to ask questions about booking data

## Project Structure

```
hotel-booking-analysis/
├── app.py                  # Main Flask application
├── ChromaDBInita.py        # ChromaDB initialization and embedding generation
├── Cleaning.py             # Data cleaning utilities
├── hotel_bookings.csv      # Dataset (not included in repo)
├── chroma_db/              # Directory for ChromaDB persistent storage
├── templates/
│   ├── Dashboard.html      # Analytics dashboard template
│   └── Ask.html            # Query interface template
├── static/                 # CSS, JS, images (not shown in provided files)
└── README.md               # This file
```

## Requirements

- Python 3.7+
- Flask
- ChromaDB
- Sentence Transformers
- Pandas
- NumPy
- Matplotlib/Plotly (for visualizations)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Tejaeshwar2307/buyago-
   cd hotel-booking-analysis
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install flask chromadb sentence-transformers pandas numpy matplotlib plotly
   ```

4. Download the hotel_bookings.csv dataset (not included in repo)
   - Place it in the project root directory

## Usage

1. Start the Flask application:
   ```
   python app.py
   ```

2. Access the application in your web browser:
   - Dashboard: http://localhost:8088/analytics
   - Query Interface: http://localhost:8088/ask

## Features

### Analytics Dashboard

The analytics dashboard provides visualizations of the hotel booking data, including:
- Geographical distribution of bookings (world map)
- Booking lead time distribution
- Monthly cancellation rates
- Revenue trends over time

### Natural Language Query Interface

The query interface allows users to ask questions about the hotel booking data using natural language. The system:
1. Converts the query to a vector embedding
2. Finds the most relevant data points in the ChromaDB vector database
3. Returns the results to the user

Example queries:
- "What countries have the most bookings?"
- "What is the average lead time for bookings?"
- "Which market segment has the highest cancellation rate?"

## Data Cleaning

The system performs the following data cleaning operations:
- Removes the 'company' column
- Fills missing 'agent' values with 0
- Removes rows with missing 'country' values
- Fills missing 'children' values with 0

## Vector Database

The system uses ChromaDB to store vector embeddings of booking data, which enables:
- Efficient semantic search for natural language queries
- Fast retrieval of relevant booking information
- Persistent storage of embeddings for quick startup

## Development

### Extending the Dashboard

To add new visualizations to the dashboard:
1. Create the visualization in your preferred library (Matplotlib, Plotly, etc.)
2. Add the visualization to the Dashboard.html template
3. If needed, add new routes in app.py to provide data for the visualization

### Improving the Query System

To enhance the query system:
1. Modify the embedding generation in ChromaDBInita.py to include more booking attributes
2. Update the query processing in the /getanswer route in app.py
3. Consider implementing a more sophisticated answer generation system using an LLM
