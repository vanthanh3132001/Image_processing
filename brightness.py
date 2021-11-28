from PIL import Image

def truncate(value):
    if (value < 0):
        return 0
    if (value > 255):
        return 255
    return value

if __name__ == "__main__":
    img = Image.open('img.png')
    pixels = img.load()

    img_new = Image.new(img.mode, img.size)
    pixels_new = img_new.load()
    brightness = 100
    for i in range(img_new.size[0]):
        for j in range(img_new.size[1]):
            r, b, g = pixels[i,j]
            _r = truncate(r + brightness)
            _b = truncate(b + brightness)
            _g = truncate(g + brightness)
            pixels_new[i,j] = (_r, _b, _g, 255)
    # img_new.show()
    images = [img, img_new]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new(img.mode, (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_im.show()