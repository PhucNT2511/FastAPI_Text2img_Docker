from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from diffusers import StableDiffusionPipeline
from fastapi.responses import StreamingResponse
from io import BytesIO
import torch
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class Prompt(BaseModel):
    prompt: str
    negative_prompt: str | None = None  # optional
    guidance_scale: float = 7.5
    num_inference_steps: int = 50


# Detect device
device = "cuda" if torch.cuda.is_available() else "cpu"
logger.info(f"Using device: {device}")

try:
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16 if device == "cuda" else torch.float32
    ).to(device)
    pipe.enable_attention_slicing()  # Giảm VRAM tiêu thụ
except Exception as e:
    logger.exception("Failed to load the Stable Diffusion pipeline.")
    pipe = None

@app.post("/txt2img")
def txt2img(p: Prompt):
    if pipe is None:
        raise HTTPException(status_code=500, detail="Model not available.")

    prompt = p.prompt.strip()
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt must not be empty.")

    try:
        image = pipe(
            prompt=prompt,
            negative_prompt=p.negative_prompt,
            guidance_scale=p.guidance_scale,
            num_inference_steps=p.num_inference_steps
        ).images[0]

    except Exception as e:
        logger.exception("Image generation failed.")
        raise HTTPException(status_code=500, detail="Failed to generate image.")

    try:
        buf = BytesIO()
        image.save(buf, format="PNG")
        buf.seek(0)
        return StreamingResponse(buf, media_type="image/png")
    except Exception as e:
        logger.exception("Failed to convert image to response.")
        raise HTTPException(status_code=500, detail="Image conversion failed.")
