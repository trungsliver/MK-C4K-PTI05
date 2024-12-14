from oop import AnimeItem
import json, os

# Khởi tạo đối tượng
anime1 = AnimeItem(1, 'One Piece', '01/01/2001')

# Viết đối tượng vào file
    # Cách 1: file được lưu cùng thư mục với file py
        # with open(): dùng để mở, và sẽ tự động đóng khi thực hiện xong
        # 'anime.json': tên file, nếu chưa có sẽ tự động tạo
with open('Lessons/Lesson3/anime.json', 'w') as file:
    json.dump(anime1.__dict__, file)

    # Cách 2: tùy chọn nơi lưu 
directory = r'D:\MindX\Python App\PTI\PTI05\Lessons\Lesson3'
filename = 'anime2.json'
file_path = os.path.join(directory, filename)
        # Kiểm tra và tạo thư mục nếu cần
if not os.path.exists(directory):
    os.makedirs(directory, exist_ok=True)
        # Ghi nội dung vào file
with open(file_path, 'w') as outFile:
    outFile.write(str(anime1.__dict__))

# Đọc dữ liệu từ file đã viết
with open('Lessons/Lesson3/anime.json', 'r') as file:
    data = json.load(file)
    loaded_data = AnimeItem(data['id'],
                            data['title'],
                            data['release_date'])
print(loaded_data.title)

# Trả về thư mục hiện tại
print(os.getcwd())  

# Đọc nhiều đối tượng từ file vào danh sách đối tượng
with open("Lessons/Lesson3/anime_list.json", "r") as file:
    anime_data = json.load(file)

# Danh sách anime
anime_item_list = list()
for data in anime_data:
    anime = AnimeItem(id = data['id'],
                      title=data['title'],
                      release_date=data['release_date'])
    anime_item_list.append(anime)

# In ra để kiểm tra
for anime in anime_item_list:
    # print(anime.title, anime.release_date)
    print(f'[{anime.title}] - {anime.release_date}')