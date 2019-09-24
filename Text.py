from PIL import ImageFont, ImageDraw
import textwrap


def draw_name(card_image, name, card_width, card_height):
    draw = ImageDraw.Draw(card_image)
    font = ImageFont.truetype("assets/pixelfont.ttf", 25)
    lines = textwrap.wrap(name, width=15)
    if len(lines) == 1:
        width, height = draw.textsize(name)
        x = (card_width - width * 1.8) / 2
        y = card_height / 18
        draw_with_outline(draw, name, x, y, font, 3)
    else:
        width, height = draw.textsize(lines[0])
        x = (card_width - width * 1.7) / 2
        y = card_height / 36
        draw_with_outline(draw, lines[0], x, y, font, 3)
        width, height = draw.textsize(lines[1])
        x = (card_width - width * 1.9) / 2
        y = card_height / 10
        draw_with_outline(draw, lines[1], x, y, font, 3)


def draw_desc(card_image, desc, card_width, card_height):
    draw = ImageDraw.Draw(card_image)
    font = ImageFont.truetype("assets/pixelfont.ttf", 15)
    y = card_height / 2
    lines = textwrap.wrap(desc, width=30)
    for line in lines:
        width, height = draw.textsize(line)
        x = (card_width - width) / 2
        y += 2 * height
        draw_with_outline(draw, line, x, y, font, 2)


def draw_power(card_image, power, card_width):
    draw = ImageDraw.Draw(card_image)
    font = ImageFont.truetype("assets/pixelfont.ttf", 25)
    x = card_width / 2 + card_width / 10
    y = card_width / 2 + card_width / 13
    draw_with_outline(draw, ":" + str(power), x, y, font, 3)


def draw_with_outline(draw, text, x, y, font, thickness):
    fillcolor = "white"
    outline_color = "black"
    draw.text((x - thickness, y - thickness), text, font=font, fill=outline_color)
    draw.text((x + thickness, y - thickness), text, font=font, fill=outline_color)
    draw.text((x - thickness, y + thickness), text, font=font, fill=outline_color)
    draw.text((x + thickness, y + thickness), text, font=font, fill=outline_color)
    draw.text((x - thickness, y), text, font=font, fill=outline_color)
    draw.text((x + thickness, y), text, font=font, fill=outline_color)
    draw.text((x, y - thickness), text, font=font, fill=outline_color)
    draw.text((x, y + thickness), text, font=font, fill=outline_color)
    draw.text((x, y), text, font=font, fill=fillcolor)