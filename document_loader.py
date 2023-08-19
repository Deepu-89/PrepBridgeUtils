def documentLoader(file):
    # to  get file extention
    import os

    name, extension = os.path.splitext(file)
    # for bytes streamlit
    from io import StringIO

    if extension == "pdf":
        pass
