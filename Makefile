format:
	black -t py310 -l 100 .
	isort --atomic -l 100 --trailing-comma --remove-redundant-aliases --multi-line 3 .