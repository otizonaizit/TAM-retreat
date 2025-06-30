class Schorle:
    juice: str

    def __init__(self, juice):
        self.name = f"{juice}schorle"


def make_apfelschorle():
    print("Mixing a delicious Apfelschorle!\n...")
    apfelschorle = Schorle(juice="apple")
    return apfelschorle
