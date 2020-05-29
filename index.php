<?php
echo '<a href="launch.php" onclick="return confirm(\'Mohon Tunggu 10 detik setelah klik ini !\')">Backup Now</a><br><a href="data/">Download data</a><br><br>';

echo shell_exec('ls data');
?>
