import os
import uuid
import cloudinary
import cloudinary.uploader
import cloudinary.api
from werkzeug.utils import secure_filename

# Cloudinary is automatically configured if CLOUDINARY_URL is present in the environment variables

def upload_image(file_object, folder="ma_tours"):
    """
    Uploads an image file object to Cloudinary.
    Returns the secure URL of the uploaded image.
    """
    if not file_object or not file_object.filename:
        return None
        
    try:
        # Create a unique filename without the extension
        filename_without_ext = os.path.splitext(secure_filename(file_object.filename))[0]
        unique_id = str(uuid.uuid4())[:8]
        public_id = f"{filename_without_ext}_{unique_id}"
        
        # Upload to Cloudinary
        result = cloudinary.uploader.upload(
            file_object,
            folder=folder,
            public_id=public_id,
            resource_type="image"
        )
        return result.get('secure_url')
    except Exception as e:
        print(f"Error uploading to Cloudinary: {e}")
        return None
