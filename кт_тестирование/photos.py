
import requests
import json

url = "https://jsonplaceholder.typicode.com/photos"

response = requests.get(url, timeout=30)

response.raise_for_status()

photos = response.json()

selected_photos = [
    photo for photo in photos
    if 100 <= photo["id"] <= 800
]

for photo in selected_photos:
    print(json.dumps(photo, indent=4, ensure_ascii=False))

with open("photos.json", "w", encoding="utf-8") as file:
    json.dump(
        selected_photos,
        file,
        indent=4,
        ensure_ascii=False
    )

print("Данные сохранены в photos.json")
print(f"Количество фотографий: {len(selected_photos)}")
