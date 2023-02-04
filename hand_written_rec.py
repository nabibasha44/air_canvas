from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import pytesseract


# def detect_hand_written(img):
#     image = Image.open(img).convert("RGB")
#
#     processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
#     model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')
#     pixel_values = processor(images=image, return_tensors="pt").pixel_values
#     generated_ids = model.generate(pixel_values)
#     generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
#     return generated_text


def detect_hand_written(img):
    image = Image.open(img).convert("RGB")
    result = pytesseract.image_to_string(image)
    return result