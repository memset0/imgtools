import gradio as gr
from imgtools.utils import asset_path
from imgtools.modules import grayscale

with gr.Blocks() as app:
    gr.Markdown("Flip text or image files using this demo.")
    with gr.Tabs():
        with gr.TabItem("灰阶图"):
            with gr.Row():
                gs_input = gr.Image()
                gs_output = gr.Image()
            gs_button = gr.Button("Submit")
            gs_button.click(grayscale.to_gray, inputs=gs_input, outputs=gs_output)
        with gr.TabItem("灰阶图（单彩色）"):
            with gr.Row():
                gsc_input = gr.Image()
                gsc_output = gr.Image()
            gsc_button = gr.Button("Submit")
            gsc_button.click(grayscale.to_rgb, inputs=gsc_input, outputs=gsc_output)