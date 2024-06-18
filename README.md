# Web-Scrapping-Analysis
### Project Description and Guide

This project involves web scraping data from various university websites, processing the text to find nouns, adjectives, and verbs, and then visualizing this information through graphs and bar charts. It uses Python for web scraping, natural language processing, and data visualization.

### File Description

1. **main.py**
   - This script performs the following tasks:
     - Scrapes data from university websites using BeautifulSoup.
     - Processes the text to find and categorize nouns, adjectives, and verbs using SpaCy.
     - Visualizes the processed data using Matplotlib and NetworkX.
     - Removes unwanted corpus and plots graphs for noun connections within the scraped data.

### Project Structure

- **main.py**: The main script containing the entire functionality.
- **fast_parsed_data.txt**: Parsed data from FAST university.
- **GK_parsed_data.txt**: Parsed data from GIKI university.
- **GCU_parsed_data.txt**: Parsed data from GCU university.

### Installation and Setup Guide

#### Prerequisites

- Python 3.x
- Required Python libraries: lxml, BeautifulSoup, urllib, spacy, matplotlib, numpy, nltk, networkx, pandas, scipy

#### Steps to Run

1. **Clone or Download the Project**
   
   Ensure you have all the project files, including the `main.py` script.

2. **Install Required Libraries**

   Install the required libraries using pip:

   ```sh
   pip install lxml beautifulsoup4 urllib3 spacy matplotlib numpy nltk networkx pandas scipy
   ```

3. **Download SpaCy Model**

   Download the SpaCy language model required for natural language processing:

   ```sh
   python -m spacy download en_core_web_sm
   ```

4. **Run the Script**

   Execute the `main.py` script:

   ```sh
   python main.py
   ```

### Example Execution Output

1. **Scraping Data**

   The script will scrape data from the specified university websites and store the parsed text in respective files (e.g., `fast_parsed_data.txt`).

2. **Processing Text**

   It will process the text to extract and categorize nouns, adjectives, and verbs, and then remove duplicates.

3. **Visualizing Data**

   - Bar charts showing the count of nouns, adjectives, and verbs for each university.
   - Graphs showing the connections between nouns for each university.
   - Displaying total edges for each graph, representing the complexity of noun connections.

4. **Example Console Output**

   ```
   Total Edges of Graph for FAST: 123
   Total Edges of Graph for GCU: 98
   Total Edges of Graph for GIKI: 110
   ```

### Visualization

The script generates several visual outputs:
- Bar charts for noun, adjective, and verb counts.
- Network graphs for noun connections within each university's text data.
- Plots are displayed using Matplotlib.

### Notes

- The script processes and visualizes the data interactively. Ensure that you run it in an environment that supports GUI-based visualization (e.g., local machine or Jupyter Notebook).
- The script might take some time to execute depending on the network speed and the size of the scraped data.

This guide should help understand, set up, run, and visualize the data processed by the script effectively. For any issues or further details, refer to the comments and documentation within the Python code.
