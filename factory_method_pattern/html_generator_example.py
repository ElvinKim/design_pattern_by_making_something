import abc


class Tag(abc.ABC):

    def __init__(self):
        self._open = None
        self._main = None
        self._close = None

    @abc.abstractmethod
    def open(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass

    def make_html(self, filename):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(self._open + self._main + self._close)

    def __str__(self):
        return self._open + self._main + self._close


class UlTag(Tag):

    def open(self):
        self._open = "<ul>\n"

    def close(self):
        self._close = "</ul>"

    def create_main(self, text_list):
        self._main = ""

        for text in text_list:
            self._main += "\t<li>{}</li>\n".format(text)


class TableTag(Tag):
    def open(self):
        self._open = "<table>\n"

    def close(self):
        self._close = "</table>"

    def create_main(self, text_list):
        self._main = ""

        for text in text_list:
            self._main += "\t<tr>\n\t\t<td>{}</td>\n\t</tr>\n".format(text)


class Factory(abc.ABC):

    @abc.abstractmethod
    def set_tag_open(self, tag):
        pass

    @abc.abstractmethod
    def set_tag_main(self, tag, text_list):
        pass

    @abc.abstractmethod
    def set_tag_close(self, tag):
        pass

    @abc.abstractmethod
    def create_tag(self):
        pass

    def create(self, text_list):
        tag = self.create_tag()

        self.set_tag_open(tag)
        self.set_tag_main(tag, text_list)
        self.set_tag_close(tag)

        return tag


class UlFactory(Factory):

    def set_tag_open(self, tag):
        tag.open()

    def set_tag_close(self, tag):
        tag.close()

    def set_tag_main(self, tag, text_list):
        tag.create_main(text_list)

    def create_tag(self):
        return UlTag()


class TableFactory(Factory):

    def set_tag_open(self, tag):
        tag.open()

    def set_tag_close(self, tag):
        tag.close()

    def set_tag_main(self, tag, text_list):
        tag.create_main(text_list)

    def create_tag(self):
        return TableTag()


if __name__ == "__main__":
    data_list = ["apple", "banana", "carrot", "durian"]

    ul_factory = UlFactory()
    ul_tag = ul_factory.create(data_list)
    print(ul_tag)
    ul_tag.make_html("ul.html")

    table_factory = TableFactory()
    table_tag = table_factory.create(data_list)
    print(table_tag)
    table_tag.make_html("table.html")


