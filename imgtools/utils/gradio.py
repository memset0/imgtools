import cv2
import gradio as gr
from .fs import asset_path
# from ..app import error_box

img404 = cv2.cvtColor(cv2.imread(asset_path("404.png")), cv2.COLOR_RGB2BGR)

error_box = None
def send_error(message="unnamed error"):
    if error_box is None:
        raise Exception('Error box is not declared.')
    return {error_box: gr.update(value=message, visible=True)}