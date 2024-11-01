## Local Stable Diffusion 3.5 using Gradio

### Setup

Create a python virtual environment

```
make init
```

Activate virtual environment

```
make activate
```

Install required libraries

```
make install
```

### Permissions on HuggingFace

  Make sure you are granted repo access permissions for the [stable-diffusion-3.5-medium](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium) model.
  In your profile settings under Access Tokens create an access token with public repo read access as well as read access to the stable-diffusion-3.5-medium repo itself ([More info](https://huggingface.co/stabilityai/stable-diffusion-3-medium-diffusers/discussions/26)).
  Copy your access token and store it in an .env file as follows:

```
HF_TOKEN=<Your access token here>
```

### Run

Run the Gradio hello world:

```
make test-gradio
```

Run Stable Diffusion 3.5 using Gradio:

```
make test-sd35
```

In both cases once you run the make command you can access the app on `http://127.0.0.1:7860`.

### References and further reading

- https://huggingface.co/stabilityai/stable-diffusion-3-medium-diffusers/discussions/26
- https://github.com/zsxkib/sd3-on-apple-silicon/blob/main/sd3-on-mps.py
- https://github.com/huggingface/diffusers/releases/tag/v0.12.0
- https://huggingface.co/spaces/lora-library/LoRA-DreamBooth-Training-UI
- https://github.com/gradio-app/gradio
- https://github.com/cloneofsimo/lora
- https://huggingface.co/sd-dreambooth-library
- https://huggingface.co/blog/lora
- https://replicate.com/blog/lora-faster-fine-tuning-of-stable-diffusion
- https://huggingface.co/stablediffusionapi?sort_models=modified#models
- https://www.datacamp.com/tutorial/fine-tuning-stable-diffusion-xl-with-dreambooth-and-lora
- https://huggingface.co/docs/peft/main/en/task_guides/dreambooth_lora