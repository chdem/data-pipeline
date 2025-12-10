import time
from src.postgres.queries import *

def main():
    while True:
        print("Running...")
        print(get_users_db(None))
        time.sleep(10)
  
if __name__=="__main__":
    main()