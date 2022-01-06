app: fictionpress
-
show front: user.browser_go_path("")
show category fiction: user.browser_go_path("fiction/")
show category poetry: user.browser_go_path("poetry/")
show genre {user.fictionpress_genre_fiction}: user.browser_go_path("fiction/{fictionpress_genre_fiction}")
