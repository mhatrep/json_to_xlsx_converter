
# 📄 JSON to XLSX Converter with Flattening Levels

This Python script converts all JSON files in the current directory into neatly formatted Excel (`.xlsx`) files.  
It also supports flattening nested JSON structures up to a specified depth, making it ideal for exploring and analyzing complex JSON data in Excel.

---

## ✅ Features

- Converts all `.json` files in the current working directory.
- Supports flattening nested JSON structures to a specified depth using the `--explode-level` option.
- Uses `_` as the default separator between hierarchical keys.
- Outputs `.xlsx` files with the same base filename as the input JSON.
- Handles complex JSON structures gracefully (dictionaries, arrays, nulls).
- Skips invalid or improperly formatted JSON files.

---

## 🚀 How to Run

### 1. Install Required Dependencies

```bash
pip install pandas
```

### 2. Run the Script

#### **Basic Conversion (Full Flattening)**

```bash
python json_to_excel.py
```

- Flattens all levels by default and creates `.xlsx` files in the same directory.

#### **Limit Flattening to a Specific Level**

| Explode Level | Behavior                               |
|----------------|----------------------------------------|
| 0              | No flattening; entire JSON in one column. |
| 1              | Flatten only top-level keys.           |
| 2              | Flatten top 2 levels of keys.          |
| N              | Flatten up to N levels.                |

##### Example: Flatten Only Top-Level Keys

```bash
python json_to_excel.py --explode-level 1
```

##### Example: Flatten Top Two Levels

```bash
python json_to_excel.py --explode-level 2
```

---

## 📚 Example

**Input JSON (`customer.json`):**

```json
{
    "customer": {
        "id": 1,
        "name": "John Doe",
        "contact": {
            "email": "john@example.com",
            "phone": "123-456-7890"
        }
    },
    "order": {
        "id": 1001,
        "amount": 250.75
    }
}
```

### Output at Different Explode Levels:

| Explode Level | Output Columns                                             |
|----------------|-----------------------------------------------------------|
| 0              | Single column containing entire JSON.                     |
| 1              | `customer` (JSON), `order` (JSON)                         |
| 2              | `customer_id`, `customer_name`, `customer_contact` (JSON), `order_id`, `order_amount` |
| 3+             | Fully flattened to individual columns.                    |

---

## 📦 Output Files

- For `customer.json`, an Excel file `customer.xlsx` will be created in the same directory.

---

## 🛠️ Dependencies

- Python 3.x
- pandas

#### Install Dependencies

```bash
pip install pandas
```

---

## 📖 Script Overview

- **flatten_json()**:  
  Flattens JSON objects up to a specified level, preserving deeper structures as JSON strings.

- **process_json_file()**:  
  Loads JSON data, applies flattening, and writes the result to an `.xlsx` file.

- **main()**:  
  Parses arguments and processes all JSON files in the current directory.

---

## 🛡️ Error Handling

- Skips invalid JSON files and displays appropriate messages.
- Unsupported JSON structures will also be reported.

---

## 📢 License

This script is open-source and free to use under the MIT License.
