# BEE2041 Empirical Project: The 2008 Financial Crisis

## Research Question
How did the 2008 financial crisis affect stock market volatility and recovery across major global markets?

## Author
Noelia Vladareanu — University of Exeter (nvn303@exeter.ac.uk)

## Project Structure

    BEE2041-financial-crisis/
    ├── data/               # Raw and scraped data files
    ├── notebooks/          # Main blog post (blog.ipynb)
    ├── scripts/            # Data collection and scraping scripts
    ├── output/             # Generated plots and figures
    ├── requirements.txt    # Python dependencies
    └── README.md

## How to Replicate

### 1. Clone the repository
    git clone https://github.com/NoeliaVladareanu/BEE2041-financial-crisis.git
    cd BEE2041-financial-crisis

### 2. Install dependencies
    pip3 install -r requirements.txt

### 3. Download the stock market data
    cd scripts
    python3 download_data.py

### 4. Scrape the crisis events data
    python3 scrape_bank_failures.py
    cd ..

### 5. Run the notebook
Open `notebooks/blog.ipynb` in VS Code and run all cells.

## Data Sources
- **S&P 500, FTSE 100, Euro Stoxx 50, Nikkei 225, VIX** — Yahoo Finance via yfinance
- **Crisis Events** — Federal Reserve History scraped via BeautifulSoup

## Requirements
- Python 3.12+
- pandas, numpy, matplotlib, seaborn
- yfinance, requests, beautifulsoup4
- jupyter, ipykernel
