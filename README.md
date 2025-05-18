# 📄 JSON to XLSX Converter with Flattening Levels

This script converts all JSON files in the current directory into nicely formatted Excel (`.xlsx`) files.  
It supports flattening nested JSON structures up to a specified depth, using `_` as the hierarchy separator.

---

## ✅ Features

- Converts all `.json` files in the current directory.
- Flattens nested JSON structures based on the specified explode level.
- Outputs `.xlsx` files with the same base filename as the input JSON.
- Handles complex nested structures, including dictionaries and arrays.
- Gracefully skips invalid or unsupported JSON formats.

---

## 🚀 How to Run

### Basic Conversion (Full Flattening)

```bash
python json_to_excel.py
