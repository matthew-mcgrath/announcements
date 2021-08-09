 #!/usr/bin/env python

import time
import life

baby = life.create()

due_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1639288801))

parents = ["My wife", "I"]

try:
    for b in baby:
        print("Baby McGrath #2 is due on " + due_date + "!  " + parents[0] + " and " + parents[1] + " are quite excited.  Cheers!")
except Exception as e:
    print(e)        
