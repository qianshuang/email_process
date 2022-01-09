# -*- coding: utf-8 -*-

from common import *

subject_ori = "RE: (External)Billing"
subject = re.sub(r"^RE: ", "", subject_ori)
subject = re.sub(r"^re: ", "", subject)
print("---" + subject)
