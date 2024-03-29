import inspect
import StellaTree
import uuid

TreeDefinition = {
    "@StellaTreeTest": {
        "@N'th": {
            "@Character": {
                StellaTree.MakeRegExp(r"[A-z]*"): {
                    StellaTree.MakeRegExp(r"[A-z]*"): {
                        "uuid": lambda x: uuid.uuid4().urn,
                        "name": StellaTree.MakeRegExp(r".*")
                    }
                }
            },
            "@World": {
                "Sanctuary": None,
                "Solphessia": None,
                "Earth+108": None,
                "Orga": None,
                "Vulcan": None,
                "Ganner": None
            }
        }
    }
}

stellaTree = StellaTree.StellaTree(TreeDefinition, rootDirectory="./")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Merrys&Alcott")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Lulu&Alcott")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Rin&Natsume")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Albert&Alcott")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Eve&Alcott")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Alice&Libris")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Crea&Fury")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Lur&Heart")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Natasha&Lord")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Jake&Alcott")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Lord&limus")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Ruka&Chiffon")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Gream&Chiffon")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Ilith&Lectore")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Maria&Organa")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Dag&Oldly")
stellaTree.BakeNode("@StellaTreeTest@N'th@Character&Malth&Lectore")

stellaTree.BakeNode("@StellaTreeTest@N'th@World")

data = {
    "uuid": uuid.uuid4().urn,
    "name": "Eve.Alcott"
}
stellaTree.Glue(
    "@StellaTreeTest@N'th@Character&Eve&Alcott",
    data,
    extend=r"""
        def SayHello():
            print("Hello, I'm %s" % R["name"])
    """)
stellaTree.Glue(
    "@StellaTreeTest@N'th@Character&Albert&Alcott",
    {
        "uuid": uuid.uuid4().urn,
        "name": "Albert.Alcott"
    },
    extend=r"""
        def SayHello():
            print("Hello, I'm %s" % R["name"])
    """)


def F(P):
    print(f"Hello, {P}.")


stellaTree.Glue(
    "@StellaTreeTest@N'th@World",
    "If not defined any function in Tree. Could set any data.",
    extend=inspect.getsource(F))

loadData = stellaTree.LoadDataLib("@StellaTreeTest@N'th@Character&Eve&Alcott;")

print("@StellaTreeTest@N'th@Character&Eve&Alcott; is... ")
print("path:", stellaTree.GeneratePath(
    "@StellaTreeTest@N'th@Character&Eve&Alcott/__init__.py"))
print("data:", loadData.R)
print("Call Function: SayHello()")
loadData.SayHello()
print("")

print("@StellaTreeTest@N'th@World; Call Function: F(\"Stella\")")
stellaTree.LoadDataFIO("@StellaTreeTest@N'th@World;")["F"]("Stella")
print("")


print("Find Gulued data with '@StellaTreeTest@N'th@Character&/**&A/**/t;'")
print(stellaTree.Find("@StellaTreeTest@N'th@Character&/**&A/**/t;"))
print("")
print("Find Gulued data with '/**&Eve/**;'")
print(stellaTree.Find("/**&Eve/**;"))
print("")

print("If you wanna remove Tree, just remove directories '@StellaTreeTest/**/'")
