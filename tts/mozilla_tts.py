import subprocess


def mozilla_tts(outfile, infile):
    with open(infile, newline='\n') as infile:
        for index, line in enumerate(infile.readlines()):
            subprocess.run(['tts',
                            '--text', line,
                            '--model_name', 'tts_models/en/ljspeech/tacotron2-DDC',
                            '--vocoder_name', 'vocoder_models/en/ek1/wavegrad',
                            '--out_path', outfile + f'/{index}.wav'])
