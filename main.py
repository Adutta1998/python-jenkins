import requests
import pandas as pd

def main():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    ndf = df.groupby("userId")["completed"].sum().reset_index()
    ndf.columns = ["userId", "completed_tasks"]
    print(ndf)



if __name__ == "__main__":
    main()
