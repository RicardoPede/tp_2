import pandas as pd
from sqlalchemy import create_engine


def main():
    engine = create_engine('mysql+mysqlconnector://root:@localhost/mi-base-de-datos')
    df = pd.read_csv('data_base/localidades.csv')
    df.to_sql('localidades', engine, if_exists='replace', index=False)
