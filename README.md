# Coolest Art — Fire Phoenix Over the Ruined City

A fire phoenix breathing flame onto a skyscraper under a dark sky,
ruined buildings smouldering in the foreground — drawn in Japanese
art style, with flowing flame feathers, swirling clouds and a moonlit
night. Burning orange wings against a blackened city, a single bold
silhouette that reads at any size.

## Entry

- `entry.png.b64` — the art as one line of base64 text (decodes to a
  1024x683 JPEG, 276,684 bytes)
- `main.py` — Python 3.13, standard library only; decodes `entry.png.b64`
  to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`),
  byte for byte, so both runs write identical bytes.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
