# Projektintroduktion: Space Invaders Spil

Velkommen til Space Invaders! Dette projekt er en genskabelse af det klassiske arkadespil Space Invaders, der blev populært i slutningen af 1970'erne. Målet med dette projekt er at opnå større viden med javascript og biblioteket P5.

## Funktioner

Dette Space Invaders-spil vil indeholde følgende funktioner:

1. **Klassisk Gameplay:**  Genskabelse af en ikonisk gameplay-oplevelse med et rumskib, der skyder på indtrængende rumvæsner, som bevæger sig nedad mod jorden.

2. **Klassisk Grafik:** Genskabelse af den klassiske grafik, der vækker barndomsminder hos mine forældres og bedsteforældres generation, som giver spillet sit klassiske look.

## Udviklingsmetode

I de kommende sektioner vil jeg detaljere min udviklingsmetode for dette Space Invaders-projekt. Jeg vil diskutere værktøjer, teknologier og trin, der anvendes til at skabe spillet, inklusive design, kodning og testning.

1. **Værktøjer og teknologier**
Spillet er udviklet i kode miljøet Visual Studio Code (VS Code), med følgende Extentiosn: 1. Live Server, som fungere som et test miljø for koden. 2. p5.vscode, som kan genere p5js miljøet til udvikling af programmet. 3. GitHub CO-pilot, som er en AI der kommer med forslag til koden, bruges mest til at give dem data så de kan udvikle en bedre AI. 4. ChatGPT, som hjælper med debugging af logiske fejl, der ikke opfanges som en syntaks fejl af VS Code.

2. **Design af grafik**
Alt grafikken er hjemmelavet ud fra gamle billeder af spillet og der kan forekomme afvigelser. Grafikken er lavet i programmet Asesprite.

3. **Koden**
Alt kode er kommenteret, den primære kode findes i filen: sketch.js, men alle klasser der henvises til er i seperate scripts, filnavnet er klassens navn + .js.

4. **Test af spillet**
Programmet er løbende blevet testet i de enkelte trin om det ønskede resultat forkommer, ud fra modellen: Hvad testes, hvad er forventet, hvad er resultatet, Succes/Fiasko?

   Følgende test er foretaget:
   Spaceships liv testes, spaceship har 3 liv og dør efterfølgende, spaceship dør og en restart skærm kommer, spaceship forsvinder spillet viser do kun gameover og din score i et split sekund, det er delvist en succes, men en bug skal fikses.

   Når aliens rammes af spaceships laser, aliens forsvinder når de rammes af et skud fra spaceship, aliens forsvinder når de rammes, dette er en succes.

    Rumskibe kommer en gang i mellem, der skal komme et rumskib hver 300'erne frame, det vil sige hvert 300/60 = 5 sekund, der kommer et rumskib hvert 5 sekund, dette er en succes.
 
