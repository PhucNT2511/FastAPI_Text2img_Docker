from fastapi import FastAPI
from pydantic import BaseModel
from diffusers import StableDiffusionPipeline
from fastapi.responses import StreamingResponse
from io import BytesIO
import torch

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
).to(device)

@app.post("/txt2img")
def txt2img(p: Prompt):
    image = pipe(p.prompt).images[0]
    buf = BytesIO()
    image.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")
