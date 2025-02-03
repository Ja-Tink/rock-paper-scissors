from PIL import Image, ImageTk

scissors_path = "images/scissors.JPG"
paper_path = "images/paper.JPG"
rock_path = "images/rock.JPG"
idle_path = "images/idle.JPG"

#turns filename into formatted photo
def make_formatted_photo(path):
    image = Image.open(path)
    image = image.resize((200, 200))
    photo = ImageTk.PhotoImage(image)

    return photo

#functions to get a tk photo object for each of my images
def get_idle():
    return make_formatted_photo(idle_path)
def get_rock():
    return make_formatted_photo(rock_path)
def get_paper():
    return make_formatted_photo(paper_path)
def get_scissors():
    return make_formatted_photo(scissors_path)
#slightly different for the active image- it requires a rotation
def get_active_image():
    image = Image.open(idle_path)
    image = image.resize((200, 200))
    image = image.rotate(270)
    photo = ImageTk.PhotoImage(image)
    return photo