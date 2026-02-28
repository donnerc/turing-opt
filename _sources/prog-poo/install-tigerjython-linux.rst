**************************************
Installation de TigerJython sous Linux
**************************************

Pour installer *TigerJython* (http://jython.tobiaskohn.ch/) sous Linux, entrer
les commandes suivantes dans un terminal

..	code-block:: bash

	# création du dossier pour tigerjython
	mkdir tigerjython && cd tigerjython

	# installation de la JRE (Java Runtime Environment)
	sudo apt-get install default-jre wget

	# aller dans le dossier de tigerjython et télécharger TigerJython
	cd tigerjython && wget http://jython.tobiaskohn.ch/tigerjython.jar


Exécuter tigerjython
=====================

Pour exécuter TigerJython, il suffit d'entrer la commande suivante :

..	code-block:: bash

	# exécution de l'archive Java de TigerJython
	java -jar tigerjython.jar




