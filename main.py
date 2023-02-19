import textwrap
import requests
from PIL import Image, ImageFont, ImageDraw
from icrawler.builtin import GoogleImageCrawler
import random

PHILOSOPHERS = [
    'Plato - The Republic',
    'Aristotle - Nicomachean Ethics',
    'René Descartes - Meditations on First Philosophy',
    'Immanuel Kant - Critique of Pure Reason',
    'Friedrich Nietzsche - Thus Spoke Zarathustra',
    'Søren Kierkegaard - Fear and Trembling',
    'Jean-Jacques Rousseau - The Social Contract',
    'David Hume - A Treatise of Human Nature',
    'John Stuart Mill - On Liberty',
    'Thomas Aquinas - Summa Theologica',
    'Friedrich Hegel - Phenomenology of Spirit',
    'Ludwig Wittgenstein - Tractatus Logico-Philosophicus',
    'Baruch Spinoza - Ethics',
    'Martin Heidegger - Being and Time',
    'Gottfried Wilhelm Leibniz - Monadology',
    'Jean-Paul Sartre - Being and Nothingness',
    'Thomas Hobbes - Leviathan',
    'Arthur Schopenhauer - The World as Will and Representation',
    'Moses Maimonides - Guide for the Perplexed',
    'George Berkeley - A Treatise Concerning the Principles of Human Knowledge',
    'Epicurus - Letters and Principal Doctrines',
    'Blaise Pascal - Pensées',
    'Confucius - Analects',
    'Plutarch - Parallel Lives',
    'Friedrich Schiller - On the Aesthetic Education of Man',
    'Seneca - Letters from a Stoic',
    'Montesquieu - The Spirit of the Laws',
    'William James - The Varieties of Religious Experience',
    'Ralph Waldo Emerson - Self-Reliance',
    'Hannah Arendt - The Human Condition',
    'Michel Foucault - Discipline and Punish',
    'John Dewey - Democracy and Education',
    'Erasmus - The Praise of Folly',
    'Simone de Beauvoir - The Second Sex',
    'Averroes - The Incoherence of the Incoherence',
    'Karl Popper - The Open Society and Its Enemies',
    'Jacques Derrida - Of Grammatology',
    'Jacques Lacan - Écrits',
    'Giambattista Vico - The New Science',
    'G.W.F. Hegel - The Philosophy of History',
    'Charles Sanders Peirce - Collected Papers',
    'Socrates - Apology',
    'Gottlob Frege - Begriffsschrift',
    'Augustine of Hippo - Confessions',
    'John Locke - An Essay Concerning Human Understanding',
    'Wilhelm Dilthey - Introduction to the Human Sciences',
    'William of Ockham - Summa Logicae',
    'Maurice Merleau-Ponty - Phenomenology of Perception'
]

FONT_COLOR = "#000000"  # this is black
STROKE_COLOR = "#ffffff"  # white
FONT_SIZE = 32

IMAGE_HEIGHT = 800
IMAGE_WIDTH = 800

if __name__ == '__main__':

    api_url = "https://api.kanye.rest"
    response = requests.get(api_url)
    # get kanye quote and surround in quotation marks
    quote = '"' + response.json()['quote'] + '"'

    #get random philosopher
    philosopher = PHILOSOPHERS[random.randint(0, len(PHILOSOPHERS) - 1)].split(" - ")
    name = philosopher[0]
    work = philosopher[1]
    # get photo of philosopher
    google_Crawler = GoogleImageCrawler(storage={'root_dir': r'.'})
    google_Crawler.crawl(keyword='photo of ' + name, max_num=1, overwrite=True)

    # get the photo
    image = Image.open("000001.jpg")
    # resize to the same size everytime
    image = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT))

    font = ImageFont.truetype("timesbd.ttf", FONT_SIZE)  # change font size to fit image
    name_text = " - " + name + ","
    work_text = '    "' + work + '"'
    image_editable = ImageDraw.Draw(image)

    # set x and y coord to write text from bottom up
    x = 0
    y = IMAGE_HEIGHT - FONT_SIZE
    # offset to write text higher each time text is written
    offset = FONT_SIZE
    # write work
    image_editable.text((x, y - offset), work_text, font=font, fill="#000000",
                        stroke_width=1, stroke_fill="#ffffff")
    # write philosopher
    offset += FONT_SIZE
    image_editable.text((x, y - offset), name_text, font=font, fill="#000000",
                        stroke_width=1, stroke_fill="#ffffff")
    offset += FONT_SIZE
    # split quotes that are too long
    lines = textwrap.wrap(quote, width=40)
    # print each line of the quote
    for line in lines[::-1]:
        image_editable.text((x, y - offset), line, font=font, fill="#000000",
                            stroke_width=1, stroke_fill="#ffffff")
        offset += FONT_SIZE

    # save image
    image.show()
    image.save("result.jpg")
