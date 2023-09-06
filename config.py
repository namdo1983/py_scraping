from pathlib import Path


CURDIR = Path(__file__).resolve().parent
print(CURDIR)


class TikiData:
    REPORT_CSV = "products.csv"
    URL_APPLE_PRODUCT = "https://tiki.vn/dien-thoai-may-tinh-bang/c1789?brand=17827"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    HEADERS_CSV = ["Name", "Price", "Sold Out", "Discount Price"]
