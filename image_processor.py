
from PIL import Image

from bot_reply_manager import BotReplyManager

from config import FRAME_PATH as frame_path
from config import FILE_SAVE_PATH as file_path
from config import PROCESSED_OUTPUT_PATH as output_path

class ImageProcessor:

  def __init__(self, downloaded_path, chat_id, messageId, processor):

    self.downloaded_path = downloaded_path
    self.chat_id = chat_id
    self.processor = processor
    self.messageId = messageId

    self.__process_image()

  def __process_image(self):
 
    base_img = Image.open(file_path + self.downloaded_path)
    frame = Image.open(frame_path)

    width, height = base_img.size

    # This value is used for cropping the photo correctly
    reference_size = height if width >= height else width

    base_img = self.crop_photo(base_img, reference_size)
  
    frame_size = (reference_size, reference_size)
    frame = frame.resize(frame_size)
  
    # Top of the world baby
    position = (0, 0)

    transparent = Image.new('RGBA', (reference_size, reference_size), (0,0,0,0))
    transparent.paste(base_img, position)
    transparent.paste(frame, position, mask=frame)

    transparent.save(output_path + self.downloaded_path + ".PNG")

    self.send_image_to_user()
    
  def crop_photo(self, image, reference_size):

    width, height = image.size

    x_pos = (width - height) / 2 if width >= height else 0
    y_pos = (height - width) / 2 if height >= width else 0

    box_coords = (x_pos, y_pos, x_pos + reference_size, y_pos + reference_size)

    return image.crop(box_coords)
    
  def send_image_to_user(self):

    file_path = output_path + self.downloaded_path + ".PNG"

    reply_manager = BotReplyManager(self.chat_id)

    reply_manager.send_image_with_caption(file_path)

    self.processor.finishJob(self.messageId)