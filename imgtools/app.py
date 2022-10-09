import gradio as gr
from imgtools.utils import asset_path
from imgtools.modules import grayscale

with gr.Blocks() as app:
    gr.Markdown('\n'.join([
        'Yet another simple image tools collection by memset0. ',
        '[source code](https://github.com/memset0/imgtools)',
    ]))
    with gr.Tabs():
        with gr.TabItem("灰阶图"):
            with gr.Row():
                with gr.Column():
                    gs_input = gr.Image()
                    gs_button = gr.Button("Submit")
                with gr.Column():
                    gs_output = gr.Image()
            gs_button.click(grayscale.to_gray, inputs=gs_input, outputs=gs_output)
            gs_examples = gr.Examples(examples=[[asset_path('example.png')]], inputs=[gs_input])
        with gr.TabItem("灰阶图（单彩）"):
            with gr.Row():
                with gr.Column():
                    gsc_input = gr.Image()
                    gsc_button = gr.Button("Submit")
                with gr.Column():
                    gsc_output = gr.Image()
            gsc_button.click(grayscale.to_rgb, inputs=gsc_input, outputs=gsc_output)
            gsc_examples = gr.Examples(examples=[[asset_path('example.png')]], inputs=[gsc_input])
