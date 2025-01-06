#aula_08/pipeline.py

from etl import pipeline_calc_total_sales

def main():
    folder: str = "data"
    output_format: list = ["parquet", "csv"]
    pipeline_calc_total_sales(folder, output_format)

if __name__ == "__main__":
    main()