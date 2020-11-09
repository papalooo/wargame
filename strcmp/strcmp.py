
# 문제
# if you can bypass the strcmp function, you get the flag.    

# view source 를 눌러 확인한 코드 ㄱ
#  require("../lib.php"); // for auth_code function
# $password = sha1(md5(rand().file_get_contents("/var/lib/dummy_file")).rand());

# if (isset($_GET['view-source'])) {
#     show_source(__FILE__);
#     exit();
# }else if(isset($_POST['password'])){
#     sleep(1); // do not brute force!
#     if (strcmp($_POST['password'], $password) == 0) {
#         echo "Congratulations! Flag is <b>" . auth_code("strcmp") ."</b>";
#         exit();
#     } else {
#         echo "Wrong password..";
#     }
# }

# 14번째 줄을보면 입력된 password 와 비교해서 0을 반환하면 
# FLAG 값을 얻을 수 있는데 
#!strcmp 함수의 취약점인 문자열과 배열을 비교하면 
# 0을 반환하는 것을 이용하여 FLAG 값을 확인할 수 있다.