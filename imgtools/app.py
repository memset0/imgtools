import cv2
import gradio
from imgtools.utils import assetpath


def to_black(image):
    output = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return output


interface = gradio.Interface(
    fn=to_black,
    inputs='image',
    outputs='image',
    examples=[[assetpath('example.png')]],
)

interface.launch()