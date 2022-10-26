class InMemoryUploadedFile(UploadedFile):
    """
    A file uploaded into memory (i.e. stream-to-memory).
    """
    def __init__(self, file, field_name, name, content_type, size, charset, content_type_extra=None):
        super(InMemoryUploadedFile, self).__init__(file, name, content_type, size, charset, content_type_extra)
        self.field_name = field_name

    def open(self, mode=None):
        self.file.seek(0)

    def chunks(self, chunk_size=None):
        self.file.seek(0)
        yield self.read()

    def multiple_chunks(self, chunk_size=None):
        # Since it's in memory, we'll never have multiple chunks.
        return False

def compress_img(image_to_compress, basewidth=650):
    """
    param image_to_compress: Image to be compressed
    param basewidth: Basewidth of the image
    """
    import sys, traceback
    from PIL import Image
    from io import BytesIO
    try:
        img = Image.open(image_to_compress)
        width = (basewidth / float(img.size[0]))
        height = int((float(img.size[1]) * float(width)))
        comp_img = img.resize((basewidth, height), Image.ANTIALIAS).convert('RGB')
        out_io = BytesIO()
        # The compressed image is stored in InMemoryUploadedFile which is then saved to BytesIO
        comp_img.save(out_io, format='JPEG', quality=85)
        in_memory_compressed_img = InMemoryUploadedFile(
            out_io, 'ImageField',
            image_to_compress.name,
            'image/jpeg',
            sys.getsizeof(out_io),
            None
        )
        return in_memory_compressed_img
    except Exception as e:
        print(e, traceback.format_exce())
