from pathlib import Path
import base64
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded_img = base64.b64encode(img_bytes).decode()

    # Convert images to base64
    image1_base64 = encoded_img

    # Define HTML and CSS for image tabs
    html = f"""
        <a>
            <img src='data:image/jpg;base64,{image1_base64}' style='width: 100px; height: 100px;'>
        </a>
    """
    return html

