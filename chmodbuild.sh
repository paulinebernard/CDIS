#!/bin/csh
set dirs='*/'
foreach dir ($dirs)
 echo $dir
 cd "${dir}"
 chmod +x build
 cd ..
end