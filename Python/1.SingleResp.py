class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}:{text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # the below functionality might be used by other objects as well.
    # As persistence is sth employed by various obhjects we cannot have them all in every class
    """
    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def low_from_web(self, uri):
        pass
    """


class PersistenceManager:
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today!")
j.add_entry("I ate a bug")
print(f"Journal entires: \n{j}")

file = r"journal.txt"
PersistenceManager.save_to_file(j, file)
with open(file) as fh:
    print(fh.read())
