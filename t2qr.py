import base64
import json
import qrcode
import matplotlib.pyplot as plt
import csv
import os
import sys


def generate_base64url_hash(data_items, base_url="https://tooltechgeek.github.io/nodb_table/"):
    # 1. Convert data to JSON string
    json_bytes = json.dumps(data_items).encode("utf-8")

    # 2. Encode bytes to Base64URL string (urlsafe_b64encode handles '-' and '_')
    base64url_bytes = base64.urlsafe_b64encode(json_bytes)

    # 3. Strip padding '=' characters per Base64URL specs
    base64url_str = base64url_bytes.decode("utf-8").rstrip("=")

    # 4. Generate URL with hash fragment instead of query parameter
    full_url = f"{base_url}#data={base64url_str}"
    return base64url_str, full_url


def sanitize_filename(name):
    """Remove or replace characters that are invalid in filenames."""
    invalid_chars = r'\/:*?"<>|'
    for ch in invalid_chars:
        name = name.replace(ch, "_")
    return name.strip()


def generate_qr_from_csv(csv_path, output_dir="qr_output"):
    """
    Read a CSV file and generate one QR code image per row.

    CSV requirements:
      - One column must be named 'id' — its value becomes the image title
        and is used in the output filename.
      - All other columns are encoded as {name, value} pairs in the QR data.
    """

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        # Validate that 'id' column exists
        if "id" not in reader.fieldnames:
            raise ValueError("CSV file must contain a column named 'id'.")

        # Collect non-id column names
        data_columns = [col for col in reader.fieldnames if col != "id"]

        for row_num, row in enumerate(reader, start=1):
            row_id = row["id"].strip()

            if not row_id:
                print(f"  [Warning] Row {row_num} has an empty 'id' — skipping.")
                continue

            # Build the table_data list (excluding the 'id' column)
            table_data = [
                {"name": col, "value": row[col]}
                for col in data_columns
            ]

            encoded_str, generated_url = generate_base64url_hash(table_data)

            print(f"\n--- Row {row_num}: {row_id} ---")
            print(f"  Base64URL : {encoded_str}")
            print(f"  URL       : {generated_url}")

            # Generate QR code
            img = qrcode.make(
                generated_url,
                error_correction=qrcode.constants.ERROR_CORRECT_L
            )

            # Build output filename from the id value
            safe_id = sanitize_filename(row_id)
            out_path = os.path.join(output_dir, f"{safe_id}-QR.png")

            # Plot and save with title
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.imshow(img, cmap="gray")
            ax.set_title(row_id, fontsize=12, pad=12)
            ax.axis("off")

            plt.savefig(out_path, bbox_inches="tight", pad_inches=0.1, dpi=300)
            plt.close()

            print(f"  Saved     : {out_path}")

    print(f"\nDone. QR codes saved to '{output_dir}/'.")


if __name__ == "__main__":
    # Default CSV path; override via command-line argument if provided
    # Usage: python t2qrcsv.py [path/to/file.csv] [output_dir]
    csv_file = sys.argv[1] if len(sys.argv) > 1 else "equipment.csv"
    out_dir  = sys.argv[2] if len(sys.argv) > 2 else "qr_output"

    generate_qr_from_csv(csv_file, out_dir)
