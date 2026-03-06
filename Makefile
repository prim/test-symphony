test:
	@test -s m4.md
	@grep -q '^# 春夜$$' m4.md
	@test "$(shell grep -cv '^$$' m4.md)" -eq 9
	@test -s m11.md
	@grep -q '^# 秋信$$' m11.md
	@test "$(shell grep -cv '^$$' m11.md)" -eq 9
