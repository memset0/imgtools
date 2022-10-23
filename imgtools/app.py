import gradio as gr
from imgtools.utils import gradio, read_file, asset_path
from imgtools.modules import grayscale, deepen

with gr.Blocks(
        title="mem's imgtools",
        css=read_file(asset_path("style.css")),
) as app:
    error_box = gr.Textbox(label="Error", visible=False)
    gradio.error_box = error_box
    gr.Markdown("\n".join([
        "Yet another simple image tools collection by memset0. ",
        "[source code](https://github.com/memset0/imgtools)",
    ]))
    with gr.Tabs():
        with gr.TabItem("Grayscale"):
            with gr.Row():
                with gr.Column():
                    input_img = gr.Image()
                    submit_button = gr.Button("Submit")
                with gr.Column():
                    output = gr.Image()
            submit_button.click(grayscale.to_gray, inputs=input_img, outputs=output)
            examples = gr.Examples(examples=[[asset_path("example.png")]], inputs=[input_img])
        with gr.TabItem("Grayscale (Colored)"):
            with gr.Row():
                input_r = gr.Textbox(label='R', value=255)
                input_g = gr.Textbox(label='G', value=0)
                input_b = gr.Textbox(label='B', value=0)
            with gr.Row():
                with gr.Column():
                    input_img = gr.Image()
                    submit_button = gr.Button("Submit")
                with gr.Column():
                    output = gr.Image()
            submit_button.click(
                grayscale.to_rgb,
                inputs=[input_img, input_r, input_g, input_b],
                outputs=output,
            )
            examples = gr.Examples(examples=[[asset_path("example.png")]], inputs=[input_img])
        with gr.TabItem('Deepen'):
            with gr.Row():
                input_scale = gr.Slider(label='Scale (%)', minimum=0, maximum=999, value=100)
                input_mode = gr.Radio(['Darker', 'Lighter'], label="Mode", value="Darker")
            with gr.Row():
                with gr.Column():
                    input_img = gr.Image()
                    submit_button = gr.Button("Submit")
                with gr.Column():
                    output = gr.Image()
            submit_button.click(
                deepen.apply,
                inputs=[input_img, input_scale, input_mode],
                outputs=output,
            )
            examples = gr.Examples(examples=[[asset_path("example.png")]], inputs=[input_img])