test:
	@python3 -m unittest discover -s tests -p 'test_*.py'
	@test -s m4.md
	@grep -q '^# 春夜$$' m4.md
	@test "$(shell grep -cv '^$$' m4.md)" -eq 9
