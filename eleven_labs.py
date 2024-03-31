from elevenlabs import save
import os
from elevenlabs.client import ElevenLabs
import wave
import soundfile
from pydub import AudioSegment



# try:
#   set_api_key(os.getenv('ELEVENLABS_API_KEY'))
# except TypeError:
#   exit("Ooops! You forgot to set ELEVENLABS_API_KEY in your environment!")

client = ElevenLabs(
api_key=str(os.getenv('ELEVENLABS_API_KEY')), # Defaults to ELEVEN_API_KEY
)

#exit(" forgot to set ELEVENLABS_API_KEY in your environment!")

class ElevenLabsManager:

    #Returns audio bytes from eleven labs
    def text_to_audio(self, input_text, voice="Sarah", save_as_wave=True, subdirectory=""):
        audio_saved = client.generate(
            text=input_text,
            voice=voice,
            model="eleven_monolingual_v1"
        )
        save(audio_saved,"test.wav")

        file_path = "test.wav"

        # Read and rewrite the file with soundfile
        data, samplerate_s = soundfile.read(file_path)
        soundfile.write(file_path, data, samplerate_s)

        # Now try to open the file with wave
        with wave.open(file_path) as file:
            print('File opened!')

        with open ("test.wav", "rb") as f:
           audio_bytes = f.read()
        
        # data, sample_rate = soundfile.read('test.wav')
        with wave.open("test.wav", 'rb') as wf:
           sample_rate = wf.getframerate()
        
        return audio_bytes, sample_rate
