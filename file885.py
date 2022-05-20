def files2():
    files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']
    myset = set(c.lower() for c in files if c.lower().endswith('png'))
    print(*sorted(myset))
