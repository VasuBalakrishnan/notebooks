import os
from urllib import request
import bs4
import pandas as pd

class Scraper:
    
    def scrape(self, page):
        
        req = request.Request(page, headers={'User-Agent': 'Mozilla/5.0'})
        source = request.urlopen(req).read()
        return source
    
    def parse(self, source):
        return None
    
    def load(self, **kwargs):
        refresh = kwargs.get('refresh', False)
        saveToCsv = kwargs.get('saveToCsv', True)
        if refresh or not os.path.exists(self.csv_path):
            source = self.scrape(self.page)
            df = self.parse(source)
            if not df.empty:
                if saveToCsv:
                    df.to_csv(self.csv_path, index=False)
                return df
            
        if os.path.exists(self.csv_path):
            return pd.read_csv(self.csv_path)