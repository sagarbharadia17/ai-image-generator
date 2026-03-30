import streamlit as st
import replicate
from PIL import Image
import requests
from io import BytesIO

# Set your API key
replicate_client = replicate.Client(api_token = "YOUR_API_KEY")

# Title
st.title("🎨 AI High Quality Image Generator")

# Prompt
prompt = st.text_input("Enter your prompt (the model doesn’t understand negative prompts like “no text” or “no extra fingers”):")

# Generate button
if st.button("Generate Image"):
    with st.spinner("Generating..."):
        output = replicate_client.run(
            "black-forest-labs/flux-2-pro",
            input={
                "prompt": prompt,
                "width": 1024,
                "height": 1024,
                "num_outputs": 1
            }
        )

        image_url = output
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))

        st.image(img, caption="Generated Image", use_container_width=True)

        # Convert image to bytes
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # Download button
        st.download_button(
            label="Download Image",
            data=byte_im,
            file_name="ai_image.png",
            mime="image/png"
        )
