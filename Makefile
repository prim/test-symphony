test:
	@test -s m4.md
	@grep -q '^# 春夜$$' m4.md
	@test "$(shell grep -cv '^$$' m4.md)" -eq 9
	@test -s m21.md
	@grep -q '^# 秋声$$' m21.md
	@test "$(shell grep -cv '^$$' m21.md)" -eq 9
