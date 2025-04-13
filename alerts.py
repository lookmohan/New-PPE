import pygame
from gtts import gTTS
import tempfile
import time
import os

# Initialize pygame mixer
pygame.mixer.init()

def play_alert(message):
    """
    Convert text to speech and play it as an audio alert
    
    Args:
        message: Text message to be spoken
    """
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            temp_path = f.name
        
        tts = gTTS(text=message, lang='en', slow=False)
        tts.save(temp_path)
        time.sleep(0.5)
        
        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
    except Exception as e:
        print(f"Audio error: {e}")
    finally:
        try:
            if temp_path and os.path.exists(temp_path):
                os.remove(temp_path)
        except:
            pass