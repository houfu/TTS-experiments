import click
from google.cloud import texttospeech


def google(outfile, infile):
    client = texttospeech.TextToSpeechClient()

    with open(infile, newline='\n') as infile:
        for index, line in enumerate(infile.readlines()):
            # Set the text input to be synthesized
            synthesis_input = texttospeech.SynthesisInput(text=line)

            # Build the voice request, select the language code ("en-US") and the ssml
            # voice gender ("neutral")
            voice = texttospeech.VoiceSelectionParams(language_code="en-US",
                                                      ssml_gender=texttospeech.SsmlVoiceGender.MALE)

            # Select the type of audio file you want returned
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.LINEAR16
            )

            # Perform the text-to-speech request on the text input with the selected
            # voice parameters and audio file type
            response = client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )

            # The response's audio_content is binary.
            with open(outfile + f'/{index}.wav', "wb") as out:
                # Write the response to the output_g file.
                out.write(response.audio_content)
                click.echo(f'Audio file {index} saved to output directory.')
