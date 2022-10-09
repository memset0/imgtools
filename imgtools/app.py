import gradio as gr
from imgtools.utils import read_file, asset_path
from imgtools.modules import grayscale

with gr.Blocks(
        title="mem's imgtools",
        css=read_file(asset_path("style.css")),
) as app:
    gr.Markdown("\n".join([
        "Yet another simple image tools collection by memset0. ",
        "[source code](https://github.com/memset0/imgtools)",
    ]))
    with gr.Tabs():
        with gr.TabItem("灰阶图"):
            with gr.Row():
                with gr.Column():
                    input_image = gr.Image()
                    submit_button = gr.Button("Submit")
                with gr.Column():
                    output = gr.Image()
            submit_button.click(grayscale.to_gray, inputs=input_image, outputs=output)
            examples = gr.Examples(examples=[[asset_path("example.png")]], inputs=[input_image])
        with gr.TabItem("灰阶图（单彩）"):
            with gr.Row():
                input_r = gr.Textbox(label='R', value=255)
                input_g = gr.Textbox(label='G', value=0)
                input_b = gr.Textbox(label='B', value=0)
            with gr.Row():
                with gr.Column():
                    input_image = gr.Image()
                    submit_button = gr.Button("Submit")
                with gr.Column():
                    output = gr.Image()
            submit_button.click(
                grayscale.to_rgb,
                inputs=[input_image, input_r, input_g, input_b],
                outputs=output,
            )
            examples = gr.Examples(examples=[[asset_path("example.png")]], inputs=[input_image])
