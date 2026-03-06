test:
	@test -s m4.md
	@grep -q '^# 春夜$$' m4.md
	@test "$(shell grep -cv '^$$' m4.md)" -eq 9
	@test -s m12.md
	@grep -q '^# 冬夜$$' m12.md
	@test "$(shell grep -cv '^$$' m12.md)" -eq 9
