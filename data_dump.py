import pymongo
import pandas as pd
import json
from sensor.config import mongo_client

DATA_FILE_PATH ="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns : {df.shape}")

    #convert dataframe to jason so we can dump these record in mongo db

    df.reset_index(drop = True ,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

     # insert converted json recored to mongo db
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)



    