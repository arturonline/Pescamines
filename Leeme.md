# Minesweeper in python by Artur Badenes Puig

## 1. Descripció

En aquest programa desenvoluparem el joc del Pescamines (Buscaminas o Minesweeper). El joc parteix d’un tauler inicialment buit i tot tapat. Sobre aquest tauler es sortegen una serie de mines que es situen de manera aleatòria.

L’usuari ha d’anar destapant caselles. Al fer clic sobre una casella poden passar tres coses:

- Hi ha una mina i el joc acaba
- Hi ha almenys una mina adjacent a la casella marcada. Es destapa la casella i s’informa de quantes mines adjacents hi han.
- No hi ha cap mina adjacent. Es destapen totes les caselles adjacents a la destapada.

Amb aquestes pistes l’usuari decideix com va evolucionant el joc. Si l’usuari vol pot marcar caselles com a possible, sense desmarcar-la. Això el sistema ho pinta com una bandereta.

Quan s’han quedat sols les mines marcades (o no), el joc acaba de manera satisfactòria.
Aquest joc incorpora moltes facetes interessants de cara a la programació, com poden ser: matrius,
sortejos, entrada i validació de dades, conteig i recursió. I la més important, anem a implementar-ho
poc a poc.

## 2. Implementació

El programa en començar crearà el tauler i el minarà. A continuació el mostrarà (amb totes les caselles tapades clar). A continuació preguntarà si volem destapar o marcar una casella, junt a la casella que volem tractar. El programa mostrar de nou el tauler informant del total de caselles marcades i destapades. Si per algun motiu destapem alguna mina, llavors es perd el joc.