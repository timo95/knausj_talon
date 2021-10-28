app: fictionpress
-
go front: user.browser_go_path("")
(go | browse) category fiction: user.browser_go_path("fiction/")
(go | browse) category poetry: user.browser_go_path("poetry/")
(go | browse) genre {user.fictionpress_genre_fiction}: user.browser_go_path("fiction/{fictionpress_genre_fiction}")
