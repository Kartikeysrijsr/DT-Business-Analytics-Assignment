import pandas as pd

def filter_federer_companies(raw_data_path):
    """
    Automated script to pre-filter companies based on Federer ICP criteria.
    """
    # Load raw data from Screener/Zauba
    df = pd.read_csv(raw_data_path)
    
    # Rule 1: Revenue must be between 50Cr and 500Cr
    revenue_filter = (df['Sales'] >= 50) & (df['Sales'] <= 500)
    
    # Rule 2: Strictly Physical Manufacturing
    excluded_sectors = ['IT - Software', 'Banks', 'Finance', 'Trading', 'BPO']
    sector_filter = ~df['Industry'].isin(excluded_sectors)
    
    # Apply filters
    qualified_companies = df[revenue_filter & sector_filter]
    
    print(f"Total pure manufacturers found: {len(qualified_companies)}")
    return qualified_companies

# Note: This is a sample pipeline. In a real-world scenario, 
# this output would be fed into an LLM API for tech-founder verification.
