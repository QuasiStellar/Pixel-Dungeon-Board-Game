from PIL import Image
import json
import Card
import Text

WIDTH = 63
HEIGHT = 94


def main():

    try:
        bg = Image.open("assets/background.png")
        borders = Image.open("assets/sprite_borders.png")
        types = Image.open("assets/types.png")
        types_borders = Image.open("assets/types_borders.png")
        enemy = Image.open("assets/enemy.png")
    except FileNotFoundError:
        print("File not found")
        return

    with open("cards.json", "r") as read_file:
        data = json.load(read_file)

# BANNER
    banner = Image.new('RGBA', (WIDTH * 20 * 4, HEIGHT * 5 * 4), (0, 0, 0, 0))
    x, y = 0, 0
# BANNER

    for card_data in data["cards"]:
        card = Card.Card(card_data["name"],
                         card_data["power"],
                         card_data["description"],
                         card_data["card_type"],
                         card_data["is_enemy"],
                         card_data["chapter"])
        card_image = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))

        card_bg = bg.crop((card.chapter * 64, 0, (card.chapter + 1) * 64, 96))
        card_image.paste(card_bg)

        card_border = borders.crop((card.chapter * 32, 0, (card.chapter + 1) * 32, 32))
        card_image.alpha_composite(card_border, (WIDTH // 2 - 15, WIDTH // 2 - 15))

        try:
            icon = Image.open("assets/icons/" + card.name + ".png")
        except FileNotFoundError:
            print("File " + card.name + ".png not found")
            icon = Image.open("assets/icons/FileNotFound.png")
        card_image.alpha_composite(icon, (WIDTH // 2 - 8, WIDTH // 2 - 8))

        card_type_borders = types_borders.crop((0, card.chapter * 18, 17, (card.chapter + 1) * 18))
        card_image.alpha_composite(card_type_borders, (2, HEIGHT - 24))

        card_type = types.crop((Card.types[card.card_type] * 14, 0, (Card.types[card.card_type] + 1) * 14, 16))
        card_image.alpha_composite(card_type, (2, HEIGHT - 22))

        if card.is_enemy:
            card_image.alpha_composite(enemy, (WIDTH - 20, HEIGHT - 20))

        card_image = card_image.resize((WIDTH * 4, HEIGHT * 4), resample=0)

        Text.draw_name(card_image, card.name, WIDTH * 4, HEIGHT * 4)

        Text.draw_desc(card_image, card.description, WIDTH * 4, HEIGHT * 4)

        if card.power:
            Text.draw_power(card_image, card.power, WIDTH * 4)

        card_image.save("cards/" + Card.chapters[card.chapter] + "/" + card.name + ".png")

# BANNER
        banner.alpha_composite(card_image, (x * WIDTH * 4, y * HEIGHT * 4))
        x += 1
        if x == 20:
            y += 1
            x = 0
    banner.save("banner.png")
# BANNER


if __name__ == '__main__':
    main()
