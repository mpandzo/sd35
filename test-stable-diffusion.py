import gradio as gr
from diffusers import StableDiffusion3Pipeline
import torch
import os
import psutil
from dotenv import load_dotenv

SD3_MODEL_CACHE = "./sd3-cache"

load_dotenv()

if not os.getenv("HF_TOKEN"):
    print("Missing HF_TOKEN in .env file, please refer to the README file for setup instructions")
    exit()

os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")

pipe = StableDiffusion3Pipeline.from_pretrained(
    "stabilityai/stable-diffusion-3.5-medium",
    torch_dtype=torch.float16,
    cache_dir=SD3_MODEL_CACHE,
)

# Check available system RAM and enable attention slicing if less than 64 GB
if (available_ram := psutil.virtual_memory().available / (1024**3)) < 64:
    pipe.enable_attention_slicing()

# Automatically infer the device and prioritize "mps" if available
device = (
    "mps"
    if torch.backends.mps.is_available()
    else "cuda" if torch.cuda.is_available() else "cpu"
)
pipe = pipe.to(device)
print(f"Pipeline moved to device: {pipe.device}")

seed = int.from_bytes(os.urandom(2), "big")
print(f"Using seed: {seed}")
generator = torch.Generator(device=device).manual_seed(seed)

def generate_image(prompt):
    with torch.device(device):
        print(f"Current device: {torch.device(device)}")
        image = pipe(
            prompt=prompt,
            height=(height := 512),
            width=(width := 512),
            num_inference_steps=28,
            guidance_scale=7.0,
            num_images_per_prompt=1,
            generator=generator,
            output_type="pil",
            return_dict=True,
            callback_on_step_end_tensor_inputs=["latents"],
        ).images[0]
    return image

iface = gr.Interface(
    fn=generate_image,
    inputs="text", 
    outputs="image", 
    title="Stable Diffusion 3.5",
    description="Enter a prompt to generate an image using Stable Diffusion 3.5."
)

iface.launch()