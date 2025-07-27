import streamlit as st
from utils.detect_boxes import detect_colored_boxes
from utils.extract_text import extract_text_from_image
from utils.pattern_rules import match_rule

st.title("VisualStruct AI")

uploaded_file = st.file_uploader("Upload SOP Image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    with open("samples/temp.png", "wb") as f:
        f.write(uploaded_file.read())

    results = detect_colored_boxes("samples/temp.png")

    structured_data = []

    for res in results:
        x, y, w, h = res["coords"]
        box_img = res["image"]
        text = extract_text_from_image(box_img)
        rule = match_rule(res["color"], text)

        structured_data.append({
            "text": text,
            "box_color": res["color"],
            "coords": res["coords"],
            "mapped_rule": rule
        })

    st.json(structured_data)
