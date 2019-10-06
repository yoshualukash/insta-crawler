# DATASET.md
link untuk file data ada di data.txt
## Level 1
### Output Data
- Folder akun instagram yang berisikan:
  -  File .txt tiap post yang berisikan captionnya
  -  File .rar yang didalamnya berisikan file json dari suatu postnya
  -  File ```_comment.json``` yang berisikan file json dari komentar yang ada dari suatu postnya (jika tak ada comment, maka tidak akan ada output ```_comment.json``` 

Beberapa Proses yang ada :
- Untuk akun pustikom_official dengan 119 post, proses memakan waktu sekitar 5 menit, file yang dihasilkan 2,01 mb
- Untuk akun pkkmb_unj2019 dengan 240 post, proses memakan waktu sekitar 9 menit, file yang dihasilkan 1,78 mb
- Untuk akun bemf_mipaunj dengan 1279 post, proses memakan waktu sekitar 40 menit, file yang dihasilkan  5,45 mb

Total dari 6 akun yang di extract sejumlah 10,6 mb data
## Followers & Following
### Output Data
- File .json yang berisikan list followers / following dari suatu akun
