class BotModel:

    def __init__(self, name, version, author, description):
        self.name = name
        self.version = version
        self.author = author
        self.description = description

    def __repr__(self):
        return f"BotModel(name={self.name}, version={self.version}, author={self.author}, description={self.description})"
