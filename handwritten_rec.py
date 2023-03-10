from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests

# load image from the IAM database
img = '/home/basha/LCA/Passport/test.jpeg'
image = Image.open(img).convert("RGB")

processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')
pixel_values = processor(images=image, return_tensors="pt").pixel_values

generated_ids = model.generate(pixel_values)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
print(generated_text)


# load image from the IAM database

# processor = TrOCRProcessor.from_pretrained('microsoft/trocr-small-handwritten')
# model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-small-handwritten')
# pixel_values = processor(images=image, return_tensors="pt").pixel_values
#
# generated_ids = model.generate(pixel_values)
# generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
# print(generated_text)