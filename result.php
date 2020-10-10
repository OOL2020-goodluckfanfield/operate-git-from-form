<?php
  echo "<p>取得中。。。" . $_GET["ripo"] ."</p>";
  $fp = fopen("command.data","w");
  fwrite($fp, $_GET["ripo"]);
  fclose($fp);

  echo '<pre>';
  $last_line = system('python out.py');
  $last_line

?>

