import subprocess

# virtualenv -p python3 $HOME/tmp/deepspeech-venv/
subprocess.run(['virtualenv', '-p', 'python3', '$HOME/tmp/deepspeech-venv/'])

# source $HOME/tmp/deepspeech-venv/bin/activate
subprocess.run(['source', '$HOME/tmp/deepspeech-venv/bin/activate'], shell=True)

# pip install deepspeech
subprocess.run(['pip', 'install', 'deepspeech'])

# pip install deepspeech-gpu
subprocess.run(['pip', 'install', 'deepspeech-gpu'])

# ffmpeg -i audio/recording.wav -vn -ar 16000 -ac 1 audio/audio.wav
subprocess.run(['ffmpeg', '-i', 'audio/audio.wav', '-vn', '-ar', '16000', '-ac', '1', 'audio/audio16.wav'])

# deepspeech --model deepspeech-0.9.3-models.pbmm --scorer deepspeech-0.9.3-models.scorer --audio audio/test-audio.wav
process = subprocess.Popen(['deepspeech', '--model', 'deepspeech-0.9.3-models.pbmm', '--scorer', 'deepspeech-0.9.3-models.scorer', '--audio', 'audio/test-audio.wav'], stdout=subprocess.PIPE)
output, _ = process.communicate()
with open('transcript.txt', 'w') as f:
    f.write(output.decode())