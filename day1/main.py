# mit imports kannst du code in dein script importieren. So kannst du code von anderen nutzen
# diese zu importierenden sachen nennt man Bibliotheken/Module
# das kann man z.B. machen, wenn man für etwas zu faul ist code zu schreiben
# unter anderem das generieren von zufallswerten
# dafür ist dieses Modul da. es generiert dir einen Zufallswert

import random

# dieser IF-Block sorgt dafür, das dieser Code nur ausgeführt wird wenn du wirklich exakt diese Datei startest
# Falls du diese Datei via import in einem anderen script aufrufst, wird der code der in diesem IF-Block steht nicht ausgeführt
if __name__ == "__main__":
    # das ist ein neuer Datentyp
    # Man nennt ihn Array. In einem Array kann man mehrere Werte speichern
    # Du greifst auf einen bestimmten Wert im Array zu, indem du arraynname[stelle]
    # also z.B. preise[0]: Das wäre dann "Auto"
    # WICHTIG: Bei arrays fängt man bei null an mit zählen d.h. in dem Fall
    # 0 -> "Auto", 1 -> "Doktortitel", 2 -> "Haus", 3 -> "Pokal"
    preise = ["Auto", "Doktortitel", "Haus", "Pokal"]
    # Das inventar speichert deine Gewonnenen gegenstände
    # Um Items an einen Array anzuhängen benutzt man die Append funktion
    # Man nutzt sie wie folgt: arrayname.append(___DAS WAS DU ANHÄNGEN WILLST___)
    # ___DAS WAS DU ANHÄNGEN WILLST___ kann dabei alles sein. Eine Zahl, Ein string, eine variable
    # z.B. inventar.append(preise[2]) -> Hängt an den Inventar den 2en wert von preise an. Das wäre dann also "Haus"
    # nach dieser Operation würde dein Array nicht mehr so Aussehen: []
    # sondern so: ["Haus"]
    inventar = []
    # Noch eine wichtige info. Um einen Zufallszahl zu generieren benutzt du die Funktion randint im Modul random
    # Du schreibst also: random.randint() dabei ist random der Modulname und randint der name der Funktion
    # die funktion random.randint(startwert, schlusswert) nimmt wie hier zu sehen 2 Argumente
    # D.h. random.randint(0, 10) liefert dir eine Zufallszahl von 0-10
    # Um einen Zufallswert aus einem Array zu nehmen benutzt du die Funktion choice im Modul random
    # Du nutzt sie so: random.choice(arrayname)
    # D.h. random.choice(preise) gibt dir einen Zufallswert aus dem Array. z.B. "Haus" oder "Auto"

    # hier noch ein paar Vorgaben von mir
    startwert = 0
    schlusswert = 10

    
    # Schreibe hier deinen Code für das Spiel. Viel Spaß!

