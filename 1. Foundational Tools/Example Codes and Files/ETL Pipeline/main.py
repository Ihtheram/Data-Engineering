from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def run_etl_pipeline():
    # Extract
    raw = extract_data()

    # Transform
    processed = transform_data(data)

    # Load
    load_data(processed)

if __name__ == "__main__":
    run_etl_pipeline()