
# 문제
# What kind of this Database?
# you have to find correlation between user name and database.

# 풀이 
# username 에 닉네임을 치고 들어가 글을 작성해보면
# sql문이 다 막혀있습니다. 그래서 username에서 
# 여러가지 이름을 넣어보았는데 
# admin 을 입력했을 땐 dont access with 'admin'
# 이라는 경고창이 떠서 admin 에 무언가 있다고 생각했습니다.
# / 를 넣었을 때 오류를 출력합니다.

# 오류 ┐
#  Fatal error: Uncaught exception 'Exception' with message 'Unable to open database: unable to open database file' in /var/www/html/db_is_really_good/sqlite3.php:7 Stack trace: #0 /var/www/html/db_is_really_good/sqlite3.php(7): SQLite3->open('./db/wkrm_/.db') #1 /var/www/html/db_is_really_good/memo.php(14): MyDB->__construct('./db/wkrm_/.db') #2 {main} thrown in /var/www/html/db_is_really_good/sqlite3.php on line 7
# /db/wkrm_/.db 이 부분에서 
# wkrm_ 뒤부분에 username 이 들어가야 하는데
# username 으로 / 를 넣어서 경로 인식에 문제가 생겨
# 오류를 출력한 것 같습니다.
# 그래서 /db/wkrm_admin.db 로 접근해보니
# db 파일이 다운로드 되었습니다.
# 해당 db의 데이터를 읽어보면 php 주소가 적혀있는데
# 그 주소를가서 flag 값을 확인할 수 있습니다.