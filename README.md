# S3_GameJam
Dans le cadre du BUT2 à l'IUT2 voici une game jam dans notre seconde année.

Pour lancer l'application il faut taper dans une console python3 [NAME_PYTHON_FILE]

THE INFO STUDENT est un jeu d'arcade montrant la vie d’un étudiant à l’IUT2.
Cet étudiant devra alterner entre 3 mini-jeux pour améliorer son score.

Mais attention de garder un œil sur la jauge de sommeil et de sociabilité, car si une d’entre elles arrive à zéro, c’est game over ! Il faut aussi faire les travaux demandés dans le temps imparti. Au bout de 3 travaux non rendus, c’est aussi game over !



Le personnage se déplace grâce aux flèches directionnelles. Lancez une interaction en vous collant à l’ordinateur de l’IUT, du lit, ou de vous amis qui discutent.

Les travaux se réalisent en travaillant sur l’ordinateur de l’IUT. Il faut appuyer sur la touche qui s’affiche le plus vite possible, mais gare à ne pas se tromper ou le jeu vous punira !

Le sommeil peut se récupérer en allant dormir. Utilisez la barre d'espace pour faire avancer la barre et tentez de la faire rester dans la zone pour raugmenter votre jauge de sommeil !

La sociabilité descend lorsque vous travaillez. Allez donc régulièrement discuter avec vos amis vous sociabiliser. Appuyez sur la barre d'espace au bon moment pour raugmenter votre jauge de sociabilité.



Vous pouvez personnaliser la difficulté du jeu en modifiant les paramètres du jeu ! Pour cela, ajouter à votre commande de lancement du jeu des arguments sous la forme : [NOM_PARAMÈTRE]=[VALEUR]

Choisissez votre difficulté avec les paramètres :

tasksDifficulty: modifie la difficulté du jeu sur l’ordinateur de l’IUT ainsi que des travaux. Valeur comprise entre 1 et 4.

gamesDifficulty: modifie la difficulté des 2 autres mini-jeux. Valeur comprise entre 1 et 4.

globalDifficulty: modifie la difficulté des deux paramètres précédents. Valeur comprise entre 1 et 4.

Bien que fortement déconseillé, vous pouvez aussi modifier chaque paramètre du jeu de la même manière. Modifiez ces paramètres à vos risques et périls.

playerSpeed: vitesse du joueur. Valeur par défaut 0,45.

socialBarSpeed: vitesse à laquelle la jauge de sociabilité réduit. Valeur par défaut 0,0015.

sleepBarSpeed: vitesse à laquelle la jauge de sommeil réduit. Valeur par défaut 0,0012.

tasksTimeAfterError: temps de pause après une erreur sur l’ordinateur. Valeur par défaut 0,5.

startCounterValue: temps initial entre 2 travaux. Valeur par défaut 18.

counterDecreaseStep: temps qui sera soustrait la durée de chaque travail au fil du temps. Valeur par défaut 0,25.

counterClampMin: temps minimum entre 2 travaux. Valeur par défaut 10.

maxTask: nombre maximum de travaux en simultané. Valeur par défaut 4.

sleepSpeed: vitesse à laquelle la barre du jeu dans le lit réduit. Valeur par défaut 0,035.

sleepSpeedDifference: vitesse à laquelle la barre du jeu dans le lit augmente par rapport au paramètre précédent. Valeur par défaut 3.

sleepBarProgressPerSuccess: pourcentage de progrès à ajouter à la jauge de sommeil en cas de réussite du jeu dans le lit. Valeur par défaut 10.

sleepZoneLength: taille de la zone de succès du jeu dans le lit. Valeur par défaut 15.

socialSpeed: vitesse à laquelle la barre du jeu avec les amis réduit. Valeur par défaut 0,09.

socialBarProgressPerSuccess:  pourcentage de progrès à ajouter à la jauge de sociabilité en cas de réussite du jeu avec les amis. Valeur par défaut 5.

socialBarMinTime: temps minimum entre 2 barres dans le jeu avec les amis. Valeur par défaut 0,3.

socialBarMaxTime: temps maximum entre 2 barres dans le jeu avec les amis. Valeur par défaut 1.

socialTimeAfterError: temps de pause après une erreur dans le jeu avec les amis. Valeur par défaut 0,5.

socialZoneLength: taille de la zone de succès du jeu dans le lit. Valeur par défaut 10.
