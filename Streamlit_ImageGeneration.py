import streamlit as st
import requests
import time

def generate_image(prompt, aspect_ratio):
    url = "https://api.limewire.com/api/image/generation"
    payload = {
        "prompt": prompt,
        "aspect_ratio": aspect_ratio
    }
    headers = {
        "Content-Type": "application/json",
        "X-Api-Version": "v1",
        "Accept": "application/json",
        "Authorization": "Bearer lmwr_sk_0eD6Q1nQyG_TKktiaEJ6sHC653R97yTdCN0IMNvcAhNIuXPB"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        data = response.json()
        return data
    except requests.exceptions.HTTPError as e:
        st.error(f"Failed to generate image: {e}")
        return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    st.title("Image Generation")

    # Input fields for user to enter prompt and aspect ratio
    prompt = st.text_input("Enter prompt", "a small Plant growing in the drought")
    aspect_ratio = st.selectbox("Select aspect ratio", ["1:1", "16:9", "4:3", "3:2"])

    # Generate image button
    if st.button("Generate Image"):
        with st.spinner("Generating image..."):
            # Sleep for a few seconds to simulate processing time
            time.sleep(5)
            # Call the function to generate the image
            data = generate_image(prompt, aspect_ratio)

            
            if data and "data" in data and len(data["data"]) > 0:
                image_url = data["data"][0]["asset_url"]
                st.image(image_url, caption="Generated Image", use_column_width=True)
            else:
                st.error("Failed to generate image. Please try again.")

if __name__ == "__main__":
    main()
