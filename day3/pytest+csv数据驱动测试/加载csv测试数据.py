import csv
from pathlib import Path

data_dir = Path(__file__).parent.parent/"data"  #数据存放目录

def red_csv(filename):
    path = data_dir / filename
    
    
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        
        for i  in reader:
            print(i)
            
            

if __name__ == '__main__':
    red_csv("ddt_test_login.csv")