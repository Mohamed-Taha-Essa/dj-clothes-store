from PIL import Image
import os

def resize_image(input_path, output_path, new_width, new_height):
    """
    Resize an image located at `input_path` and save the resized image to `output_path`.
    
    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the resized image.
        new_width (int): New width of the resized image.
        new_height (int): New height of the resized image.
    """
    try:
        # Open the input image
        with Image.open(input_path) as img:
            # Resize the image
            resized_img = img.resize((new_width, new_height))
            # Save the resized image to the output path
            resized_img.save(output_path)
            print(f"Image resized successfully and saved at: {output_path}")
    except Exception as e:
        print(f"Error resizing image: {e}")

def batch_resize_images(input_dir, output_dir, new_width, new_height):
    """
    Batch resize all images in the input directory and save resized images to the output directory.
    
    Args:
        input_dir (str): Directory containing input images.
        output_dir (str): Directory to save resized images.
        new_width (int): New width of the resized images.
        new_height (int): New height of the resized images.
    """
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # List all files in the input directory
    image_files = [f for f in os.listdir(input_dir) if f.endswith((".jpg", ".jpeg", ".png"))]
    
    # Resize each image file
    for filename in image_files:
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        resize_image(input_path, output_path, new_width, new_height)

def main():
    # Current directory (where the script is located)
    current_dir = os.getcwd()
    
    # Input directory (current directory)
    input_dir = current_dir
    
    # Output directory for resized images
    output_dir = os.path.join(current_dir, "resized_images")
    
    # New dimensions for the resized images
    new_width = 2000
    new_height = 1080
    
    # Batch resize images
    batch_resize_images(input_dir, output_dir, new_width, new_height)

if __name__ == "__main__":
    main()
