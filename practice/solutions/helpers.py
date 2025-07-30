from __future__ import annotations


def humanbytes(bytes_: int) -> str:  # from https://stackoverflow.com/a/31631711
    """Return the given bytes as a human friendly KB, MB, GB, or TB string."""
    b = float(bytes_)
    kb = float(1024)
    mb = float(kb ** 2) # 1,048,576
    gb = float(kb ** 3) # 1,073,741,824
    tb = float(kb ** 4)  # 1,099,511,627,776

    if b < kb:
        return '{0:.0f} {1}'.format(b, 'Byte' if b == 1 else 'Bytes')
    elif kb <= b < mb:
        return '{0:.2f} KB'.format(b / kb)
    elif mb <= b < gb:
        return '{0:.2f} MB'.format(b / mb)
    elif gb <= b < tb:
        return '{0:.2f} GB'.format(b / gb)
    else:
        return '{0:.2f} TB'.format(b / tb)

if __name__ == "__main__":
    tests = [0, 1, 5, 1024, 500000, 1048576, 50000000, 1073741824, 5000000000, 1099511627776, 5000000000000]

    for t in tests: print(f"{t:,} == {humanbytes(t)}")