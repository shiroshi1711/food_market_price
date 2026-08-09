import pandas as pd

def  clean_data(data):
    rows = []

    for item in data:
        rows.append({
            "variant_id": item["variant_id"],
            "variant_name": item["variant_nama"],
            "unit": item["satuan_display"],
            "date": item["tanggal"],
            "region": "National",
            "price": item["harga"]
        })

        for region in item.get("region", []):
            rows.append({
                "variant_id": item["variant_id"],
                "variant_name": item["variant_nama"],
                "unit": item["satuan_display"],
                "date": item["tanggal"],
                "region": region["region"],
                "price": region["harga"]
            })

    return pd.DataFrame(rows)