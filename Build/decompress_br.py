import brotli
import os

# Bestanden in huidige map
input_files = [
    "WebsiteGame.data.br",
    "WebsiteGame.framework.js.br",
    "WebsiteGame.wasm.br"
]

for file in input_files:
    if os.path.exists(file):
        with open(file, "rb") as f_in:
            compressed_data = f_in.read()
            decompressed_data = brotli.decompress(compressed_data)

        output_file = file.replace(".br", "")
        with open(output_file, "wb") as f_out:
            f_out.write(decompressed_data)
        print(f"✅ Gedecomprimeerd: {output_file}")
    else:
        print(f"⚠️ Bestand niet gevonden: {file}")
