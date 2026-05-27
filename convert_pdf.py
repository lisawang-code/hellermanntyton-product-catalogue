import fitz
import os
import json
import sys

PDF_PATH = r'C:\Users\lisa\Desktop\公司资料\ht_product_catalogue_2025_com.pdf'
OUTPUT_DIR = r'c:\Users\lisa\WorkBuddy\20260414103257\电子目录册英文版\pages'
INDEX_PATH = r'c:\Users\lisa\WorkBuddy\20260414103257\电子目录册英文版\search_index.json'

def convert_pdf_to_images():
    doc = fitz.open(PDF_PATH)
    total = len(doc)
    print(f"Total pages: {total}")

    search_index = []

    for i in range(total):
        page_num = i + 1
        page = doc[i]

        # Render page to image at 200 DPI
        mat = fitz.Matrix(200/72, 200/72)
        pix = page.get_pixmap(matrix=mat)
        img_path = os.path.join(OUTPUT_DIR, f'page_{page_num:03d}.png')
        pix.save(img_path)

        # Extract text for search index
        text = page.get_text()
        # Clean up text
        text = ' '.join(text.split())
        if text.strip():
            search_index.append({
                "page": page_num,
                "text": text[:3000]  # Limit text length
            })

        if page_num % 50 == 0 or page_num == total:
            print(f"Processed {page_num}/{total} pages...")

    doc.close()

    # Save search index
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        json.dump(search_index, f, ensure_ascii=False, indent=2)

    print(f"\nDone! Images saved to {OUTPUT_DIR}")
    print(f"Search index saved to {INDEX_PATH}")
    print(f"Total pages with text: {len(search_index)}")

if __name__ == '__main__':
    convert_pdf_to_images()
