# insta-crawler
Instagram Crawler 
### Kelompok:
- Fachry Muhammad - 1313617019
- Yoshua Lukas  - 1313617021

### Program dibawah menggunakan dokumentasi :
[instaloader](https://instaloader.github.io/)

### Pre-requisite:
install package python dari instaloader ```pip install instaloader```

### Level 1
1. Open terminal pada folder ```\instaloader```
2. Jalankan pada terminal, kode berikut ```instaloader.py ig_username --no-pictures --no-videos --comments```
    - ```ig_username``` = masukkan username IG yang ingin diextract datanya.
    - ```--no-pictures``` = program tidak mengambil data foto dari instagram user
    - ```--no-videos``` = program tidak mengambil data video dari instagram user
    - ```--comments``` = program juga mengambil data komentar dari tiap post instagram user
3. Output berupa folder yang berisi file text & .json dari tiap post instagram user.

### List Instagram User Followers & Following
Syarat -> harus dilakukan login user untuk mendapatkan list followers serta list following
#### Followers
1. Buka file ```followers.py```
2. Edit dalam file ```followers.py``` pada bagian :
    - ```username =``` -> isi username instagram pemakai program
    - ```password =``` -> isi password instagram pemakai program
    - ```instagram_target =``` -> isi instagram yang ingin diextract data list followers nya
3. Jalankan program python tersebut ```python followers.py``` pada terminal
4. Output berupa file json dari list followers tersebut -> ```list_followers_username.json```
#### Following
1. Buka file ```following.py```
2. Edit dalam file ```following.py``` pada bagian :
    - ```username =``` -> isi username instagram pemakai program
    - ```password =``` -> isi password instagram pemakai program
    - ```instagram_target =``` -> isi instagram yang ingin diextract data list following nya
3. Jalankan program python tersebut ```python following.py``` pada terminal
4. Output berupa file json dari list followers tersebut -> ```list_following_username.json```




