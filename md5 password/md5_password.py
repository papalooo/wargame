
# 문제
# md5('value', true);

# 코드
# <?php
#  if (isset($_GET['view-source'])) {
#   show_source(__FILE__);
#   exit();
#  }

#  if(isset($_POST['ps'])){
#   sleep(1);
#   mysql_connect("localhost","md5_password","md5_password_pz");
#   mysql_select_db("md5_password");
#   mysql_query("set names utf8");

#   include "../lib.php"; // include for auth_code function.
#   $key=auth_code("md5 password");
#   $ps = mysql_real_escape_string($_POST['ps']);
#   $row=@mysql_fetch_array(mysql_query("select * from admin_password where password='".md5($ps,true)."'"));
#   if(isset($row[0])){
#    echo "hello admin!"."<br />";
#    echo "Password : ".$key;
#   }else{
#    echo "wrong..";
#   }
#  }
# ?>

# 20번째 줄을 보면 sqli 를 방어하고있다.
# 21번째 줄을 보면 $ps 변수의 값을 md5 로
# 해시하고, 그 값이 admin_password 테이블에
# 존재하면 $row 변수에 저장합니다.
# 21번째 줄에 있는 sql문을 보면
"select * from admin_password where password='".md5($ps,true)."'"
# 인자 값으로 or 을 줄 수 있다면 True 를 반환하기 때문에
# md5 해시를 했을때 'or' 이 포함되는 문자열을 찾아서
# password에 입력하면 FLAG 값을 확인할 수 있습니다.
# 해당 문자열 : 129581926211651571912466741651878684928 