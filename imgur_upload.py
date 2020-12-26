import os
from imgur import authenticate
from datetime import datetime

album = None
image_name = os.listdir("media/")[0]


def upload_image(client, image_name):
    config = {
        "album": album,
        "name": "RanomizationxD",
        "title": "YEEEEEEET",
        "description": "GENERATEDDD{0}".format(datetime.now())
    }

    print("Uploading...")
    image = client.upload_from_path("media/" + image_name, config=config, anon=False)
    print("Done")

    return image


if __name__ == "__main__":
    client = authenticate()
    for i in range(len(os.listdir("media/"))):
        image_name = os.listdir("media/")[i]
        image = upload_image(client, image_name)
        print("Image has been uploaded tp {}".format(image["link"]))
