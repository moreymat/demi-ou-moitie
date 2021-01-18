import random
from data import (
    numero_rue,
    random_arrete,
    random_year,
    nom_famille,
    random_address,
    random_organisation,
    random_dim,
    random_surface,
    prenom,
    type_rue,
    debut_rue,
    fin_rue,
    societes,
    type_societe,
    arrondissements,
)


def new_text(path_to_save, number_of_documents):
    for i in range(number_of_documents):
        file_name = "addons_%d.txt" % i
        path = path_to_save + file_name
        f = open(path, "w")
        f.write("La O \nSociété O\n")
        f.write(random_organisation(False))
        f.write(
            ", O\nest O\nautorisé(e) O\nà O\noccuper O\nun O\nemplacement O\npublic O\nau O\ndroit O\nde O\nson O\ncommerce O\n"
        )
        f.write(random_address(False))
        f.write(
            "MARSEILLE I-LOC\nen O\nvue O\nd' O\ny O\ninstaller O\n: O\nFace O\nau O\nn° O\n"
        )
        f.write("%d O\n" % numero_rue())
        f.write(
            ": O\nune O\nterrasse O\nsimple O\nsans O\ndélimitation O\nni O\ncouverture O\nni O\nécran O\ndétachée O\ndu O\ncommerce O\nFaçade O\n: O\n"
        )
        f.write(random_dim())
        f.write(" I-SAI\nm I-SAI\nSaillie I-SAI\n/ O\nLargeur I-LRG\n: O\n")
        f.write(random_dim())
        f.write(" I-LRG\nm I-LRG\nSuperficie I-SUP\n: O\n")
        f.write(random_surface())
        f.write(" I-SUP\nm² I-SUP\nFace O\nau O\nau O\nn° O\n")
        f.write("%d O\n" % numero_rue())
        f.write(
            ": O\nune O\nterrasse O\nsimple O\nsans O\ndélimitation O\nni O\ncouverture O\nni O\nécran O\ndétachée O\ndu O\ncommerce O\nFaçade O\n: O\n"
        )
        f.write(random_dim())
        f.write(" I-SAI\nm I-SAI\nSaillie I-SAI\n/ O\nLargeur I-LRG\n: O\n")
        f.write(random_dim())
        f.write(" I-LRG\nm I-LRG\nSuperficie I-SUP\n: O\n")
        f.write(random_surface())
        f.write(" I-SUP\nm² I-SUP\nSuivant O\nplan O\n. O\n")
        f.write(
            "L' O\nexploitation O\nde O\nl' O\nétablissement O\nsusmentionné O\ndoit O\nêtre O\nconforme O\naux O\nnormes O\nsanitaires O\nen O\nvigueur O\n. O\n\n"
        )
        f.write(
            "Toute O\ninfraction O\nen O\nmatière O\nd' O\nhygiène O\nou O\nnon-respect O\ndes O\ndispositions O\nréglementaires O\nconstatés O\nlors O\ndes O\ncontrôles O\nréalisés O\npar O\nles O\nAdministrations O\n"
        )
        f.write(
            "compétentes O\npourra O\nentraîner O\nla O\nrévocation O\nde O\nl' O\nautorisation O\nd' O\noccupation O\ndu O\ndomaine O\npublic O\n. O\n"
        )
        f.write(nom_famille() + " I-PER\n" + prenom() + " I-PER\n")
        f.write("N° I-ART\n")
        f.write(random_arrete())
        f.write("_VDM I-ART\n")  #  2018_00086_VDM I-ART\
        f.write(
            "Arreté O\nOportant O\nautorisation O\nd' O\noccupation O\ndu O\ndomaine O\npublic O\n- O\nTerasses O\n- O\n"
        )
        f.write(random_address(False))
        f.write("- O\n")
        f.write(random_organisation())
        f.write("- O\n")
        f.write("compte I-CMP\n")
        f.write("n° I-CMP\n")
        f.write("%d/0%d I-CMP\n" % (random.randint(10000, 60000), random.randint(1, 9)))
        f.write(". O\n")

        f.write(
            "Vu O\nla O\ndemande O\n%d/%d I-DMD\n"
            % (random.randint(2009, 2021), random.randint(1000, 5000))
        )
        f.write("reçue O\nle O\n")

        f.write(random_year() + " I-DAT\n")
        f.write("présentée O\npar O\n")
        f.write(random_organisation(False))
        f.write(", O\nreprésentée O\npar O\n")
        f.write(nom_famille() + " I-PER\n" + prenom() + " I-PER\n")
        f.write(", O\ndomiciliée O\n")
        f.write(random_address(True))
        f.write("Marseille I-LOC\n")
        f.write(
            "en O\nvue O\nd' O\noccuper O\nun O\nemplacement O\npublic O\nà O\nl' O\nadresse O\nsuivante O\n: O\n"
        )
        f.write(random_address(True))
        f.write("MARSEILLE I-LOC\n")
        f.write(". O\n")
        f.write(nom_famille() + " I-PER\n" + prenom() + " I-PER\n")
        f.close()


validation = "addons_validation/"
train = "addons_train/"

new_text(train, 500)
new_text(validation, 50)
