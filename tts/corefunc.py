import torch
from scipy.io.wavfile import write
from uuid import uuid4
import os

def generate_tts(text):
    APPDIR='tts/'
    language = 'en'
    model_id = 'v3_en'
    device = torch.device('cpu')
    local_file = APPDIR+'model.pt'
    sample_rate = 48000
    speaker = 'random'

    if not os.path.isfile(local_file):
        torch.hub.download_url_to_file(f'https://models.silero.ai/models/tts/{language}/{model_id}.pt',
                                    local_file)  

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")

    model.to(device)  # gpu or cpu

    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate)

    audioID=uuid4()
    audioPath=f'static/tts/audio-{audioID}.wav'
    write(APPDIR+audioPath,sample_rate,audio.numpy())

    return audioPath
