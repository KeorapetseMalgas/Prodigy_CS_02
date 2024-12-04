from PIL import Image
import numpy as np

class ImageEncryptionTool:
    def __init__(self, key=42):
        """Initialize with a simple encryption key."""
        self.key = key
    
    def encrypt(self, input_path, output_path):
        """Encrypt the image by manipulating pixel values."""
        image = Image.open(input_path)
        pixel_array = np.array(image)
        
        encrypted_array = (pixel_array + self.key) % 256
        

        encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
        encrypted_image.save(output_path)
        print(f"Image encrypted and saved to {output_path}")
    
    def decrypt(self, input_path, output_path):
        """Decrypt the image by reversing the encryption operation."""
        image = Image.open(input_path)
        pixel_array = np.array(image)
        

        decrypted_array = (pixel_array - self.key) % 256
        
        
        decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
        decrypted_image.save(output_path)
        print(f"Image decrypted and saved to {output_path}")


if __name__ == "__main__":
    tool = ImageEncryptionTool(key=50)  
    tool.encrypt("original_image.png", "encrypted_image.png")
    tool.decrypt("encrypted_image.png", "decrypted_image.png")
