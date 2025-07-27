visualstruct-ai/
├── app.py                          # Streamlit UI
├── utils/
│   ├── detect_boxes.py             # Detects colored boxes & values
│   ├── extract_text.py             # Extracts text using OCR
│   ├── extract_tables.py           # Detects table structure
│   ├── extract_colors.py           # Maps background colors
│   ├── pattern_rules.py            # Stores common visual patterns/rules
│   └── visual_parser.py            # Main parser combining everything
├── samples/
│   └── sample_sop_form.png         # Complex sample image (yours)
├── output/
│   ├── structured_output.json
│   └── extracted_fields/
├── requirements.txt
└── README.md
