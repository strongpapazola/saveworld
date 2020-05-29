<?php
shell_exec('echo \'{"kode":"1"}\' > transit');
echo 'mohon tunggu !';
sleep('10');
header('Location: index.php');
?>
