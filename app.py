import subprocess

text = "बच्चों की रेरणादायक कहानियां"
model_path = "./hi/fastpitch/best_model.pth"
config_path = "./hi/fastpitch/config.json"
speakers_file_path = "./hi/fastpitch/speakers.pth"
vocoder_path = "./hi/hifigan/best_model.pth"
vocoder_config_path = "./hi/hifigan/config.json"
out_path = "output_audio.wav"

command = [
    "tts",
    "--text", text,
    "--model_path", model_path,
    "--config_path", config_path,
    "--speakers_file_path", speakers_file_path,
    "--vocoder_path", vocoder_path,
    "--vocoder_config_path", vocoder_config_path,
    "--out_path", out_path,
    "--speaker_idx", "female"
]

# Run the command
subprocess.run(command)