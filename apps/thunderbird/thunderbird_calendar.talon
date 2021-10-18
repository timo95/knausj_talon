app: thunderbird
# English
title: Calendar - Mozilla Thunderbird
title: /January /
title: /February /
title: /March /
title: /April /
title: /May /
title: /June /
title: /July /
title: /August /
title: /September /
title: /October /
title: /November /
title: /December /
# German (duplicates removed)
title: Kalender - Mozilla Thunderbird
title: /Januar /
title: /Februar /
title: /März /
title: /Mai /
title: /Juni /
title: /Juli /
title: /Oktober /
title: /Dezember /
-
# event/task
event new: key("{user.mod()}-i")
task new: key("{user.mod()}-d")
(task | event) delete: key(delete)
# layout
toggle today: key(f11)
view <number_small>: user.thunderbird_calendar_view(number_small)
view day: user.thunderbird_calendar_view(1)
view week: user.thunderbird_calendar_view(2)
view multi [week]: user.thunderbird_calendar_view(3)
view month: user.thunderbird_calendar_view(4)
