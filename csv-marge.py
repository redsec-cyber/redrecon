import pandas as pd
import os

BASE_DIR = "/home/kali/Desktop/RedRecon/Results/"
OUTPUT_FILE = "merged_results.xlsx"

csv_found = False
writer = pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl")
used_sheets = set()

for root, _, files in os.walk(BASE_DIR):
    for file in files:
        if file.lower().endswith(".csv"):
            csv_found = True
            file_path = os.path.join(root, file)
            print(f"[+] Found CSV: {file_path}")

            try:
                # Check if file is empty
                if os.path.getsize(file_path) == 0:
                    print(f"[!] Skipping empty file: {file_path}")
                    continue

                df = pd.read_csv(
                    file_path,
                    sep=None,
                    engine="python",
                    encoding="utf-8-sig",
                    on_bad_lines="skip"
                )

                if df.empty:
                    print(f"[!] No data in: {file_path}")
                    continue

            except Exception as e:
                print(f"[X] Failed to read {file_path}: {e}")
                continue

            # Sheet name = relative path
            sheet = os.path.relpath(file_path, BASE_DIR)
            sheet = sheet.replace(os.sep, "_").replace(".csv", "")[:31]

            # Avoid duplicate sheet names
            base_sheet = sheet
            i = 1
            while sheet in used_sheets:
                sheet = f"{base_sheet[:27]}_{i}"
                i += 1

            used_sheets.add(sheet)

            try:
                df.to_excel(writer, sheet_name=sheet, index=False)
                print(f"[✓] Written to sheet: {sheet}")
            except Exception as e:
                print(f"[X] Excel write failed for {sheet}: {e}")

if not csv_found:
    print("[X] No CSV files found at all!")

writer.close()
print("\n✅ Finished. Check merged_results.xlsx")
