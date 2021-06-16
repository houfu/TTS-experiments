import click


@click.command()
@click.option('--solution', '-s', type=click.Choice(['google', 'mozillaTTS']), default='google', help='Solution to try')
@click.option('--outfile', '-o', type=click.Path(exists=True, file_okay=False, writable=True),
              help='Directory to output_g file')
@click.argument('infile')
def main(solution, outfile, infile):
    if solution == 'google':
        from tts.google_cloud import google
        google(outfile, infile)
    elif solution == 'mozillaTTS':
        from tts.mozilla_tts import mozilla_tts
        mozilla_tts(outfile, infile)


if __name__ == '__main__':
    main()
