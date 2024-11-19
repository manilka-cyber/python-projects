total = 0

for count in range (2,21,2):

    total = total + count

    print
'''
from pathlib import Path

# Create a folder and nested folders
folder_path = Path("C:\\Users\\rlnag\\OneDrive\\Desktop\\python-projects")
folder_path.mkdir(parents=True, exist_ok=True)

print(f"Folder structure '{folder_path}' created successfully.")
'''
'''
import cv2
import numpy as np

# Load the image
image_path = "WhatsApp Image 2024-11-16 at 12.10.37_551ab944.jpg"  # Replace with your image path
image = cv2.imread(image_path)

# Define a sharpening kernel
sharpening_kernel = np.array([[-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]])

# Apply the sharpening filter
sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

# Display the sharpened image
cv2.imshow("Sharpened Image", sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
'''
import cv2

# Load the noisy image
image = cv2.imread("WhatsApp Image 2024-11-16 at 12.10.37_551ab944.jpg")

# Apply Non-Local Means Denoising
denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

# Display the denoised image
cv2.imshow("Denoised Image", denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
'''
from PIL import Image

# Open an image
image = Image.open("WhatsApp Image 2024-11-16 at 12.10.37_551ab944.jpg")  # Replace with your image path

# Save the image
image.save("saved_image.png")  # You can specify different formats (e.g., .png, .jpg)

'''
'''
import cv2

# Read the noisy image
noisy_image = cv2.imread("WhatsApp Image 2024-11-16 at 12.10.37_551ab944.jpg")  # Replace with your noisy image path

# Apply denoising
denoised_image = cv2.fastNlMeansDenoisingColored(noisy_image, None, 10, 10, 7, 21)

# Save the denoised image
cv2.imwrite("denoised_image.jpg", denoised_image)  # Replace with your desired file name and format
'''
'''
import numpy as np
from skimage import restoration, io

# Read the blurred image
image = io.imread("WhatsApp Image 2024-11-16 at 12.10.37_551ab944.jpg")

# Apply deconvolution (example with a Gaussian kernel)
deconvolved = restoration.unsupervised_wiener(image, psf=np.ones((5, 5)))[0]

# Save and display the result
io.imsave("deblurred_image.jpg", deconvolved)

'''


