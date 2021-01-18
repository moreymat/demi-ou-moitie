# Méthodologie

## Développement collaboratif

Nous travaillerons tous sur le même dépôt <https://github.com/moreymat/demi-ou-moitie> en créant des branches pour le développement de chaque fonctionnalité.
Ce fonctionnement correspond au modèle de dépôt partagé [(Shared Repository Model)](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/about-collaborative-development-models).

Sur cet entrepôt partagé, nous suivrons le [GitHub Flow](https://guides.github.com/introduction/flow/).
Je vous invite également à lire la [documentation plus détaillée sur chaque étape](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/github-flow).

## Environnement conda

Je vous conseille de travailler dans un environnement virtuel conda, où vous pourrez installer toutes les bibliothèques nécessaires à ce projet et leurs dépendances.
J'ai créé un fichier `environment.yml` pour automatiser ce processus, il vous suffit donc, pour créer un environnement conda nommé `demi-ou-moitie` et contenant quelques dépendances de base, de faire :

```sh
conda env create -f environment.yml
```

Au début de chaque session de travail, vous aurez besoin d'activer cet environnement conda:

```sh
conda activate demi-ou-moitie
```

À la fin de chaque session, vous pouvez le désactiver :

```sh
conda deactivate
```

Ce tutoriel couvre les bases de l'utilisation des environnements conda en 20 minutes environ : <https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html> .

## Conventions

Afin d'harmoniser la mise en page du code et de minimiser les différences de style, tout votre code devra être formaté par le formatteur automatique `black`: <https://black.readthedocs.io/en/stable/>
Les éditeurs de code et environnements de développement intégrés, comme PyCharm ou Visual Studio Code, peuvent être configurés pour formatter automatiquement votre code (voir par exemple <https://code.visualstudio.com/docs/python/editing>).

Je vous demande de documenter votre code, mais également si possible d'ajouter des indications de typage : <https://docs.python.org/3.8/library/typing.html> .
Les indications de typage permettent de facililter le travail collaboratif et d'automatiser l'APIfication (<https://fastapi.tiangolo.com/>) ou la vérification des arguments (<https://pydantic-docs.helpmanual.io/>).

## Outils recommandés

Vous pouvez utiliser vos éditeurs de développement préférés.
Si vous n'en avez pas ou que vous êtes ouverts au changement, je vous recommande Visual Studio Code qui offre une expérience utilisateur très agréable et riche pour Python :
<https://code.visualstudio.com/docs/python/python-tutorial>
<https://code.visualstudio.com/docs/languages/python>
