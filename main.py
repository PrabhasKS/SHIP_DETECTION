import streamlit as st
from inference_sdk import InferenceHTTPClient
import tempfile
from PIL import Image, ImageDraw, ImageFont
import io

# Initialize the client with your API URL and API Key
CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="fspbglyeW2LCrT2u4alO"
)

# Streamlit UI
st.title("Object Detection App")
st.write("Upload an image to detect objects.")

# Image uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image using PIL
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Save the uploaded image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())  # Use .getvalue() instead of read()
        tmp_file_path = tmp_file.name

    # Perform inference
    try:
        result = CLIENT.infer(tmp_file_path, model_id="ship-object-detection/1")
        st.write("Inference Result:")
        st.json(result)

        # Check if a ship is detected
        predictions = result.get("predictions", [])
        if predictions:
            # Draw the bounding box on the image
            draw = ImageDraw.Draw(image)
            font = ImageFont.load_default()  # Default font

            for pred in predictions:
                if pred["class"] == "ship":
                    # Extract bounding box coordinates and confidence
                    x, y, width, height = pred["x"], pred["y"], pred["width"], pred["height"]
                    confidence = pred["confidence"]
                    
                    # Scale coordinates (if necessary) based on image size (if needed for your model)
                    img_width, img_height = image.size
                    x1 = int(x * img_width)
                    y1 = int(y * img_height)
                    x2 = int((x + width) * img_width)
                    y2 = int((y + height) * img_height)

                    # Draw the bounding box
                    draw.rectangle([x1, y1, x2, y2], outline="red", width=5)

                    # Add the confidence text
                    confidence_text = f"{confidence * 100:.2f}%"
                    # Place confidence text slightly above the box
                    draw.text((x1, y1 - 10), confidence_text, fill="red", font=font)

            st.write("Ship detected!")
        else:
            st.write("No ship detected.")

        # Show the image with bounding box and confidence
        st.image(image, caption="Processed Image with Bounding Box", use_column_width=True)

    except Exception as e:
        st.error(f"Error occurred during inference: {e}")
