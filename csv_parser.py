def _parse_csv_line(line: str) -> list[str]:
    fields: list[str] = []
    current: list[str] = []
    in_quotes = False
    quoted_field = False
    after_quote = False
    index = 0

    while index < len(line):
        char = line[index]

        if in_quotes:
            if char == '"':
                next_index = index + 1
                if next_index < len(line) and line[next_index] == '"':
                    current.append('"')
                    index += 1
                else:
                    in_quotes = False
                    after_quote = True
                    quoted_field = True
            else:
                current.append(char)
        elif after_quote:
            if char == ',':
                fields.append(''.join(current))
                current = []
                quoted_field = False
                after_quote = False
            elif char in (' ', '\t'):
                pass
            else:
                raise ValueError('Invalid CSV format: unexpected character after closing quote')
        else:
            if char == ',':
                value = ''.join(current)
                fields.append(value if quoted_field else value.strip())
                current = []
                quoted_field = False
            elif char == '"':
                if ''.join(current).strip():
                    raise ValueError('Invalid CSV format: unexpected quote in unquoted field')
                current = []
                in_quotes = True
            else:
                current.append(char)

        index += 1

    if in_quotes:
        raise ValueError('Invalid CSV format: unterminated quoted field')

    value = ''.join(current)
    fields.append(value if quoted_field else value.strip())
    return fields


def parse_csv(text: str) -> list[dict[str, str]]:
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    lines = text.splitlines()
    if not lines:
        return []

    header_line_number = None
    headers: list[str] | None = None

    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue

        header_line_number = line_number
        headers = _parse_csv_line(line)
        break

    if headers is None:
        return []

    records: list[dict[str, str]] = []

    for line_number, line in enumerate(lines[header_line_number:], start=header_line_number + 1):
        if not line.strip():
            continue

        values = _parse_csv_line(line)
        if len(values) != len(headers):
            raise ValueError(
                f'Line {line_number}: expected {len(headers)} fields, got {len(values)}'
            )

        records.append(dict(zip(headers, values)))

    return records
