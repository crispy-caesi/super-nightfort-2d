from PIL import Image

def extract_sprites(input_file, output_folder):
    try:
        # Öffne das Spritesheet
        spritesheet = Image.open(input_file)

        # Bestimme die Breite und Höhe des Spritesheets
        sheet_width, sheet_height = spritesheet.size

        # Definiere die Größe der einzelnen Sprites
        sprite_size = 32

        # Extrahiere die einzelnen Sprites
        sprite_count = 0
        for y in range(0, sheet_height, sprite_size):
            for x in range(0, sheet_width, sprite_size):
                # Definiere den Bereich des aktuellen Sprites
                box = (x, y, x + sprite_size, y + sprite_size)
                sprite = spritesheet.crop(box)

                # Speichere das extrahierte Sprite als PNG-Datei
                sprite.save(f"{output_folder}/sprite_{sprite_count}.png")
                sprite_count += 1

        print(f"{sprite_count} sprites wurden extrahiert und gespeichert.")
    except Exception as e:
        print("Fehler beim Extrahieren der Sprites:", e)

if __name__ == "__main__":
<<<<<<< HEAD
    input_file = "sprites/blocks/snowland_spritesheet.png"
    output_folder = "sprites/blocks/snowland/"
=======
    input_file = "sprites/blocks/spritesheets/desert_spritesheet.png"
    output_folder = "sprites/blocks/spritesheets/desert/"
>>>>>>> main
    
    extract_sprites(input_file, output_folder)
