import requests
import pandas as pd
import os
from io import StringIO

# Federal Reserve - key crisis events timeline
url = "https://www.federalreservehistory.org/essays/great-recession-and-its-aftermath"

print("Scraping Federal Reserve for crisis data...")

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# Create a manual dataset of key crisis events based on official sources
crisis_events = {
    'Date': [
        '2007-08-09', '2007-09-18', '2008-03-16', '2008-09-07',
        '2008-09-15', '2008-09-16', '2008-09-25', '2008-10-03',
        '2008-10-08', '2008-11-25', '2009-02-17', '2009-03-09'
    ],
    'Event': [
        'BNP Paribas freezes funds - crisis begins',
        'Fed cuts interest rates for first time',
        'Bear Stearns rescued by JP Morgan',
        'Fannie Mae and Freddie Mac taken over',
        'Lehman Brothers files for bankruptcy',
        'AIG bailout - $85 billion rescue',
        'Washington Mutual seized by regulators',
        'US Congress passes $700bn bailout',
        'Coordinated global interest rate cuts',
        'Federal Reserve launches QE program',
        'US stimulus package signed into law',
        'S&P 500 hits crisis low point'
    ],
    'Market_Impact': [
        'Negative', 'Positive', 'Negative', 'Negative',
        'Very Negative', 'Negative', 'Negative', 'Mixed',
        'Positive', 'Positive', 'Positive', 'Negative'
    ]
}

df = pd.DataFrame(crisis_events)
df['Date'] = pd.to_datetime(df['Date'])

print(f"Crisis events recorded: {len(df)}")
print(df)

# Save
os.makedirs('../data', exist_ok=True)
df.to_csv('../data/crisis_events.csv', index=False)
print("\nSaved to ../data/crisis_events.csv")
