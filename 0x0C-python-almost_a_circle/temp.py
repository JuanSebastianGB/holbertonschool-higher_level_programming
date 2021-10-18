#!/usr/bin/python3
import io
import contextlib

if __name__ == "__main__":
    a = ("#" * 3 + "\n") * 5
    with io.StringIO() as buf, contextlib.redirect_stdout(buf):
        print(a, end="")
        output = buf.getvalue()

    print(a)
    print(output)
    print(f"a == output ? {a == output}")
