"""Builds the static "Tips & råd" blog pages for the Rent og effektivt prototype.

Run:  python3 blog-src/build_blog.py   (from the prototype folder)
Writes tips-og-rad/index.html and one HTML page per article.
"""
import json, os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'tips-og-rad')
BASE = 'https://www.rentogeffektivt.no'
DATE = '2026-11-27'
DATE_NO = '27. november 2026'
HOME = '../index.html'

BUSINESS = {
    "@type": "LocalBusiness",
    "@id": BASE + "/#business",
    "name": "R & E Renhold AS",
    "alternateName": "Rent og effektivt",
    "url": BASE + "/",
    "logo": BASE + "/img/logo-dark.png",
    "image": BASE + "/img/hero.webp",
    "telephone": "+47 454 02 012",
    "email": "post@rentogeffektivt.no",
    "address": {"@type": "PostalAddress", "streetAddress": "Stølsmyr 16", "postalCode": "5542",
                "addressLocality": "Karmsund", "addressRegion": "Rogaland", "addressCountry": "NO"},
    "geo": {"@type": "GeoCoordinates", "latitude": 59.3882553, "longitude": 5.3267368},
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                   "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                   "opens": "08:00", "closes": "16:00"}],
    "areaServed": [{"@type": "City", "name": n} for n in ["Haugesund", "Karmøy", "Tysvær", "Bokn", "Sveio"]],
}

ICON_ARROW = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ICON_MENU = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>'

# --------------------------------------------------------------------------- articles
ARTICLES = [
{
 "slug": "fordeler-med-profesjonelt-renhold",
 "seo_title": "Profesjonelt renhold for bedrifter: 6 fordeler | R&E Renhold",
 "desc": "Hva får bedriften igjen for profesjonelt renhold? Seks fordeler, og hvordan du sjekker at renholdsfirmaet er godkjent av Arbeidstilsynet.",
 "h1": "6 fordeler med profesjonelt renhold for bedriften",
 "tag": "Bedrift",
 "img": "profesjonelt-renhold.webp",
 "alt": "Lyst og rent kontor med resepsjonsdisk, grønne planter og blanke flater",
 "excerpt": "Seks grunner til at stadig flere bedrifter setter bort renholdet, og hva du bør sjekke før du velger firma.",
 "intro": "Mange mindre bedrifter starter med at de ansatte tar renholdet selv. Det fungerer en stund, men etter hvert blir det ofte ujevnt, og noen får mer av jobben enn andre. Her er seks grunner til at stadig flere setter bort renholdet, og hva du bør sjekke før du velger firma.",
 "toc": [("tid", "De ansatte får tiden tilbake"), ("kvalitet", "Jevn kvalitet"), ("inneklima", "Bedre inneklima og trivsel"),
         ("inntrykk", "Et godt førsteinntrykk"), ("utstyr", "Riktig utstyr og metoder"), ("kostnader", "Forutsigbare kostnader"),
         ("godkjent", "Sjekk at firmaet er godkjent"), ("avtale", "Hva bør avtalen inneholde?")],
 "body": """
<h2 id="tid">1. De ansatte kan bruke tiden på jobben sin</h2>
<p>Når de ansatte selv skal vaske toaletter, tømme søppel og vaske gulv, går det tid fra oppgavene de faktisk er ansatt for. Regner du timene sammen over et år, blir det fort mer enn man tror. Med fast renhold slipper dere å fordele vaskelister, og ingen trenger å bli sittende igjen etter arbeidstid.</p>

<h2 id="kvalitet">2. Jevn kvalitet, uke etter uke</h2>
<p>Et profesjonelt renholdsfirma jobber etter en avtalt plan. Det betyr at de samme oppgavene blir gjort hver gang, også de som er lette å glemme, som lister, dørhåndtak og ventiler. Et fast team blir dessuten kjent med bygget og vet hvor det trenger ekstra innsats.</p>

<h2 id="inneklima">3. Bedre inneklima og trivsel</h2>
<p>Støv og smuss på flater og gulv påvirker hvordan lufta oppleves, og hvordan det føles å komme på jobb. Mange opplever at et jevnt og grundig renhold gir færre plager med støv og en arbeidsplass det er hyggeligere å være på. Det er særlig merkbart i åpne landskap der mange deler de samme flatene.</p>

<h2 id="inntrykk">4. Et godt førsteinntrykk for kunder og besøkende</h2>
<p>Inngangsparti, møterom og toaletter er ofte det første kundene ser. Et rent og ryddig lokale sier noe om hvordan bedriften jobber, uten at du trenger å si et ord.</p>

<h2 id="utstyr">5. Riktig utstyr og metoder</h2>
<p>Renholdere bruker utstyr og midler som er laget for jobben, for eksempel mikrofiber som fjerner mer smuss med mindre kjemikalier. Riktige midler beskytter også flatene. Et vinyl- eller linoleumsgulv kan for eksempel ta skade av feil rengjøringsmiddel, mens riktig vedlikehold får det til å vare lenger. Les mer i guiden vår om <a href="boning-og-vedlikehold-av-gulv.html">boning og vedlikehold av gulv</a>.</p>

<h2 id="kostnader">6. Forutsigbare kostnader</h2>
<p>Med en fast avtale vet dere hva renholdet koster hver måned. Dere slipper å kjøpe inn maskiner og midler, og dere slipper å ordne vikar når noen er syke eller på ferie.</p>

<h2 id="godkjent">Sjekk at renholdsfirmaet er godkjent</h2>
<p>I Norge må alle som selger renholdstjenester være godkjent av Arbeidstilsynet og stå i registeret over godkjente renholdsvirksomheter. Ordningen skal sikre ordnede lønns- og arbeidsforhold i bransjen. Det er ikke lov å kjøpe renhold fra firma som ikke er godkjent, og bedrifter som kjøper renhold har plikt til å sjekke dette.</p>
<ul class="check">
<li>Søk opp firmaet i Arbeidstilsynets register over godkjente renholdsvirksomheter.</li>
<li>Be om å se HMS-kortet til renholderne. Alle som jobber med renhold skal ha det.</li>
<li>Spør hvem som er kontaktperson, og hvordan dere melder fra hvis noe ikke er som avtalt.</li>
</ul>
<p>R &amp; E Renhold AS er godkjent av Arbeidstilsynet.</p>

<h2 id="avtale">Hva bør en renholdsavtale inneholde?</h2>
<p>En god avtale gjør det enkelt for begge parter. Sørg for at den beskriver:</p>
<ul>
<li>hvilke oppgaver som skal gjøres, og hvor ofte</li>
<li>når på døgnet renholdet skjer</li>
<li>hvem som er fast kontaktperson</li>
<li>hvordan avvik og ønsker om endringer håndteres</li>
<li>pris, oppsigelsestid og hva som er inkludert</li>
</ul>
<p>Lurer du på hvor ofte lokalene deres bør vaskes? Se <a href="tips-til-rent-kontor.html">tipsene våre for et rent kontor</a>, eller les om <a href="../index.html#tjenester">bedriftsrenhold hos oss</a>.</p>
""",
 "cta": ("Vurderer dere å sette bort renholdet?", "R & E Renhold er godkjent av Arbeidstilsynet og har levert bedriftsrenhold på Haugalandet siden 2016."),
 "faq": [
   ("Hvordan sjekker jeg om et renholdsfirma er godkjent?", "Søk opp firmaet i Arbeidstilsynets register over godkjente renholdsvirksomheter. Renholderne skal også bære HMS-kort når de er på jobb."),
   ("Lønner det seg med profesjonelt renhold for en liten bedrift?", "Ofte ja, særlig når man regner med tiden de ansatte ellers bruker på vasking. Mange små bedrifter starter med renhold én gang i uken."),
   ("Kan vi kombinere eget og profesjonelt renhold?", "Ja. Mange lar de ansatte ta enkle daglige oppgaver, som oppvask og rydding av egen pult, mens renholdsfirmaet tar resten."),
 ],
 "related": ["tips-til-rent-kontor", "boning-og-vedlikehold-av-gulv"],
},
{
 "slug": "tips-til-rent-kontor",
 "seo_title": "Rent kontor hele uka: 8 tips for bedrifter i Haugesund",
 "desc": "Praktiske tips til et renere kontor: rutiner for pulter, kjøkken og toaletter, og hvor ofte kontoret bør vaskes. Råd fra et renholdsfirma på Haugalandet.",
 "h1": "Rent kontor hele uka: 8 tips som faktisk fungerer",
 "tag": "Bedrift",
 "img": "rent-kontor.webp",
 "alt": "Lyst og ryddig kontor med glassvegger, skrivebord og grønne planter",
 "excerpt": "Små vaner avgjør om kontoret føles rent på fredag, ikke bare mandag morgen. Åtte enkle grep for hele arbeidsplassen.",
 "intro": "Et rent kontor handler ikke bare om at renholderen kommer innom. Små vaner i løpet av uka avgjør om lokalene føles ryddige på fredag ettermiddag, eller bare mandag morgen. Her er åtte tips vi gir bedriftskunder i Haugesund og på Karmøy.",
 "toc": [("plan", "Lag en enkel renholdsplan"), ("tips", "8 tips for et renere kontor"), ("frekvens", "Hvor ofte bør kontoret vaskes?")],
 "body": """
<h2 id="plan">Lag en enkel renholdsplan</h2>
<p>En renholdsplan trenger ikke være lang. Én side som viser hva som gjøres daglig, ukentlig og månedlig, og hvem som har ansvaret, er nok. Del gjerne oppgavene i to: det de ansatte gjør selv, som oppvask og rydding av egen pult, og det renholderen tar, som gulv, toaletter og flater.</p>

<h2 id="tips">8 tips for et renere kontor</h2>
<h3>1. Rydd pulten før du går hjem</h3>
<p>En ryddig pult kan tørkes av. Papirbunker, kopper og ledninger gjør at renholderen må hoppe over flatene. Avtal gjerne en «ren pult»-regel for fredager.</p>
<h3>2. Ha faste regler for kjøkkenet</h3>
<p>Kjøkkenet er stedet som oftest blir et problem. Avtal at hver enkelt setter egen kopp i oppvaskmaskinen, og at kjøleskapet tømmes på en fast dag.</p>
<h3>3. Tørk av berøringspunkter oftere</h3>
<p>Dørhåndtak, lysbrytere, kaffemaskin, skrivere og heisknapper tas på av mange hver dag. Det er her smuss og bakterier lettest spres videre, så disse flatene bør få ekstra oppmerksomhet.</p>
<h3>4. Legg ut gode inngangsmatter</h3>
<p>Mye av skitten på gulvet blir båret inn under skoene. Med vått vær og grus om vinteren på Haugalandet gjør en god matte både innenfor og utenfor døra stor forskjell. Det skåner også gulvet.</p>
<h3>5. Gjør det enkelt å kildesortere</h3>
<p>Tydelig merkede beholdere på faste steder gir mindre rot og færre fulle søppelbøtter på pultene.</p>
<h3>6. Hold toalettene påfylt</h3>
<p>Tomt for såpe eller papir er noe av det første ansatte og besøkende legger merke til. Avtal hvem som har ansvar for påfyll mellom hver vask.</p>
<h3>7. Tenk på inneklimaet</h3>
<p>Støv samler seg på høye flater, lamper og ventiler. Sørg for at disse blir tørket jevnlig, og at ventilasjonsanlegget får service etter planen.</p>
<h3>8. Avtal en fast frekvens for renholdet</h3>
<p>Det siste tipset er det viktigste: bestem hvor ofte lokalene skal vaskes, og hold det.</p>

<h2 id="frekvens">Hvor ofte bør kontoret vaskes?</h2>
<p>Det finnes ingen fasit, men antall ansatte, kundebesøk og type lokaler er det som avgjør. Dette er vanlige utgangspunkt:</p>
<ul>
<li><strong>Få ansatte og lite besøk:</strong> ofte én til to ganger i uken.</li>
<li><strong>Mange ansatte eller daglig kundebesøk:</strong> flere ganger i uken eller daglig.</li>
<li><strong>Toaletter og kjøkken:</strong> oftere enn resten av lokalene, uansett størrelse.</li>
</ul>
<div class="tip"><p><strong>Tips:</strong> En gang eller to i året bør dere også ta en grundigere runde. Se <a href="hovedrengjoring-bedrift-og-hjem.html">planen vår for hovedrengjøring</a>.</p></div>
<p>Vurderer dere å sette bort renholdet? Les om <a href="fordeler-med-profesjonelt-renhold.html">fordelene med profesjonelt renhold</a>, eller se hva vi tilbyr innen <a href="../index.html#tjenester">bedriftsrenhold</a>.</p>
""",
 "cta": ("Trenger kontoret fast renhold?", "Vi lager en renholdsplan tilpasset lokalene deres i Haugesund, Karmøy og resten av Haugalandet."),
 "faq": [
   ("Hvor ofte bør et kontor vaskes?", "Det avhenger av hvor mange som jobber der og hvor mye besøk dere har. Mange små kontorer klarer seg med renhold én til to ganger i uken, mens toaletter og kjøkken ofte trenger mer."),
   ("Hva koster kontorrenhold?", "Prisen avhenger av størrelsen på lokalene, hvor ofte det skal vaskes og hva som skal inngå. Den enkleste måten å få et svar på er å be om et pristilbud."),
   ("Må vi være til stede når det vaskes?", "Nei. Renholdet kan ofte legges til tidspunkter som ikke forstyrrer arbeidsdagen."),
 ],
 "related": ["fordeler-med-profesjonelt-renhold", "hovedrengjoring-bedrift-og-hjem"],
},
{
 "slug": "sjekkliste-flyttevask",
 "seo_title": "Flyttevask sjekkliste: rom for rom | Haugesund og Karmøy",
 "desc": "Komplett sjekkliste for flyttevask av bolig og næringslokale: kjøkken, bad, vinduer og overlevering. Det du må huske før nøkkelen leveres.",
 "h1": "Sjekkliste for flyttevask: rom for rom",
 "tag": "Bolig og bedrift",
 "img": "flyttevask.webp",
 "alt": "Mopp, bøtte og rengjøringsmiddel for gulv klare til flyttevask",
 "excerpt": "Alt som skal vaskes før du leverer nøkkelen, rom for rom. Med egen liste for kontor- og næringslokaler.",
 "intro": "Flyttevask er den grundigste vasken de fleste gjør. Enten du flytter ut av en leilighet eller bedriften skal ut av et kontorlokale, forventer neste leietaker eller eier at alt er rent, også de stedene man vanligvis ikke ser. Bruk sjekklisten under som huskeliste.",
 "toc": [("start", "Før du starter"), ("kjokken", "Kjøkken"), ("bad", "Bad og vaskerom"), ("rom", "Stue, soverom og kontorer"),
         ("naering", "Næringslokaler: dette glemmes ofte"), ("overlevering", "Overlevering")],
 "body": """
<h2 id="start">Før du starter</h2>
<p>Flyttevask går raskest når rommene er tomme. Tøm skap og skuffer, og ta bilder av lokalene før du begynner. Bildene er nyttige hvis det oppstår spørsmål ved overleveringen.</p>
<p>Ha dette klart: mikrofiberkluter, allrengjøringsmiddel, avkalkingsmiddel, ovnsrens, bøtte, mopp, støvsuger og en trygg gardintrapp.</p>
<div class="tip"><p><strong>Vask ovenfra og ned.</strong> Da faller støv og smuss på flater du ikke har vasket ennå, og du slipper å ta ting to ganger.</p></div>

<h2 id="kjokken">Kjøkken</h2>
<ul class="check">
<li>Vask alle skap og skuffer, både innvendig og utvendig.</li>
<li>Rengjør stekeovn, ovnsbrett, rister og koketopp.</li>
<li>Trekk ut komfyr og kjøleskap, og vask bak, under og på sidene.</li>
<li>Avfrost og vask kjøleskap og fryser. La dørene stå åpne etterpå.</li>
<li>Rens ventilator og fettfilter.</li>
<li>Avkalk vask og blandebatteri, og tørk av fliser over benken.</li>
</ul>

<h2 id="bad">Bad og vaskerom</h2>
<ul class="check">
<li>Avkalk fliser, dusjvegger og armaturer.</li>
<li>Rens sluk og fjern hår og såperester.</li>
<li>Vask toalettet grundig, også rundt foten og bak.</li>
<li>Tørk av speil, skap, lamper og ventiler.</li>
<li>Vask gulvet og fugene.</li>
</ul>

<h2 id="rom">Stue, soverom og kontorer</h2>
<ul class="check">
<li>Tørk av dører, karmer, lister og stikkontakter.</li>
<li>Vask vinduer innvendig, inkludert karmer og vinduskarm.</li>
<li>Vask innvendig i skap og garderober.</li>
<li>Tørk støv på lamper, ovner og høye flater.</li>
<li>Støvsug og vask gulvet, også i hjørner og langs veggene.</li>
</ul>

<h2 id="naering">Næringslokaler: dette glemmes ofte</h2>
<p>Når en bedrift flytter ut av et kontor eller en butikk, er det noen steder som ofte blir glemt:</p>
<ul class="check">
<li>Pauserom og kjøkkenkrok, inkludert kaffemaskin og oppvaskmaskin.</li>
<li>Lager, boder og arkivrom.</li>
<li>Ventilasjonsventiler og lysarmaturer.</li>
<li>Skilt, oppslag og tape på vegger og dører.</li>
<li>Gulvbelegg i korridorer og inngangsparti.</li>
</ul>
<p>Slitte vinyl- og linoleumsgulv kan ofte få nytt liv med oppskuring og ny bone før overlevering. Les mer i guiden vår om <a href="boning-og-vedlikehold-av-gulv.html">boning og vedlikehold av gulv</a>.</p>

<h2 id="overlevering">Overlevering</h2>
<p>Både husleieloven og de fleste leiekontrakter forutsetter at lokalet leveres ryddet og rengjort. Sjekk derfor hva som står i kontrakten om standard og eventuelle krav til profesjonell vask.</p>
<ul>
<li>Gå gjennom lokalet sammen med utleier eller ny eier.</li>
<li>Ta nye bilder når vasken er ferdig.</li>
<li>Avtal skriftlig hvis noe skal utbedres i etterkant.</li>
</ul>
<p>Vil du heller gjøre en grundig vask uten å flytte? Se <a href="hovedrengjoring-bedrift-og-hjem.html">planen vår for hovedrengjøring</a>.</p>
""",
 "cta": ("Skal bedriften flytte ut av lokalene?", "Vi tar spesialrenhold av kontor og næringslokaler på Haugalandet, så dere kan konsentrere dere om selve flyttingen."),
 "faq": [
   ("Hvor lang tid tar en flyttevask?", "Det varierer med størrelse og hvor skittent det er. Sett av god tid: en vanlig leilighet tar ofte en hel dag for én person, mens større boliger og lokaler tar lengre tid."),
   ("Hvem har ansvar for flyttevasken?", "Normalt den som flytter ut. Sjekk leiekontrakten eller kjøpekontrakten, der står det ofte hvilken standard som forventes."),
   ("Må vinduene vaskes utvendig?", "Innvendig vask er vanlig. Utvendig vask av vinduer som ikke kan nås trygt, avtales ofte særskilt. Sjekk hva kontrakten sier."),
 ],
 "related": ["hovedrengjoring-bedrift-og-hjem", "boning-og-vedlikehold-av-gulv"],
},
{
 "slug": "boning-og-vedlikehold-av-gulv",
 "seo_title": "Boning av gulv: når, hvordan og hvor ofte? | Haugesund",
 "desc": "Slik tar du vare på vinyl-, linoleum-, flis- og tregulv. Lær når gulvet bør skures opp og bones, og hvordan riktig daglig vask forlenger levetiden.",
 "h1": "Boning og vedlikehold av gulv: slik holder gulvet lenger",
 "tag": "Gulv",
 "img": "boning-gulv.webp",
 "alt": "Stort, lyst næringslokale med søyler og et blankt, nyvasket gulv",
 "excerpt": "Hvilke gulv kan bones, når trenger de ny bone, og hvordan riktig daglig vask får belegget til å vare lenger.",
 "intro": "Gulvet er den flaten i et bygg som får mest slitasje. Med riktig daglig vask og ny beskyttende bone når det trengs, kan et belegg holde seg pent i mange år lenger. Her er det du bør vite.",
 "toc": [("hva", "Hva er boning?"), ("typer", "Hvilke gulv kan bones?"), ("tegn", "Tegn på at gulvet trenger ny bone"),
         ("hvor-ofte", "Hvor ofte bør gulvet bones?"), ("daglig", "Daglig vedlikehold"), ("prosess", "Slik foregår oppskuring og boning")],
 "body": """
<h2 id="hva">Hva er boning?</h2>
<p>Boning betyr at gulvet får et tynt, beskyttende lag med polish, kalt bone. Det er bonen som tar imot slitasjen fra sko, stoler og traller, ikke selve gulvbelegget. Etter hvert blir bonelaget skittent og ripete. Da fjernes det gamle laget med <strong>oppskuring</strong>, før gulvet får ny bone.</p>

<h2 id="typer">Hvilke gulv kan bones?</h2>
<h3>Vinyl og linoleum</h3>
<p>Dette er de vanligste gulvene å bone, og de finnes i de fleste kontorer, skoler, butikker og fellesarealer. Linoleum tåler dårlig sterkt alkaliske midler, så bruk pH-nøytrale rengjøringsmidler i det daglige.</p>
<h3>Fliser</h3>
<p>Fliser bones vanligvis ikke. Her handler vedlikeholdet om grundig vask, rene fuger og avkalking i våtrom.</p>
<h3>Tre og parkett</h3>
<p>Tregulv er enten oljet eller lakkert og vedlikeholdes med egne produkter, som såpe eller olje. De skal ikke bones.</p>

<h2 id="tegn">Tegn på at gulvet trenger ny bone</h2>
<ul class="check">
<li>Gulvet er matt og grått, selv rett etter vask.</li>
<li>Du ser tydelige gangveier der folk går mest.</li>
<li>Riper og flekker setter seg og er vanskelige å få bort.</li>
<li>Smuss ser ut til å feste seg raskere enn før.</li>
</ul>

<h2 id="hvor-ofte">Hvor ofte bør gulvet bones?</h2>
<p>Det kommer an på trafikken. Inngangspartier, korridorer og butikker med mange besøkende trenger det oftere enn et lite brukt møterom. Mange gjør det én til to ganger i året i travle områder, og sjeldnere ellers. Et godt daglig renhold gjør at det kan gå lengre tid mellom hver gang.</p>

<h2 id="daglig">Daglig vedlikehold som forlenger levetiden</h2>
<ul>
<li><strong>Gode inngangsmatter</strong> stopper grus og vann før det når gulvet.</li>
<li><strong>Tørrmopp eller støvsug før våtvask</strong>, så du ikke drar grus rundt.</li>
<li><strong>Riktig dosering</strong>. For mye såpe gir et klebrig lag som samler smuss.</li>
<li><strong>Fuktig, ikke våt mopp</strong>. Mye vann kan trenge inn i skjøter og kanter.</li>
<li><strong>Filtknotter under stoler og bordbein</strong> gir færre riper.</li>
<li><strong>Fjern flekker raskt</strong>, før de setter seg.</li>
</ul>

<h2 id="prosess">Slik foregår oppskuring og boning</h2>
<ol>
<li>Møbler flyttes, og gulvet støvsuges.</li>
<li>Gammel bone skures bort med maskin og et egnet middel.</li>
<li>Gulvet skylles og tørker helt.</li>
<li>Ny bone legges i flere tynne lag, med tørketid mellom hvert lag.</li>
<li>Møblene settes tilbake når gulvet er herdet.</li>
</ol>
<p>Fordi gulvet må tørke mellom lagene, gjøres jobben ofte på kveldstid eller i helgen. Se også hvordan gulvet passer inn i <a href="tips-til-rent-kontor.html">det daglige renholdet på kontoret</a>, eller les om <a href="../index.html#tjenester">boning og oppskuring hos oss</a>.</p>
""",
 "cta": ("Ser gulvene slitne ut?", "Vi skurer opp og boner gulv i kontorer, butikker og fellesarealer i Haugesund og omegn."),
 "faq": [
   ("Hvor lang tid tar det før gulvet kan brukes igjen?", "Det avhenger av produktet og antall lag. Gulvet må tørke helt mellom lagene, så mange velger å gjøre jobben på kveldstid eller i helgen."),
   ("Kan man bone parkett?", "Nei. Vanlig bone er laget for belegg som vinyl og linoleum. Parkett og tregulv vedlikeholdes med såpe, olje eller lakk, avhengig av hvordan de er behandlet."),
   ("Hvor ofte bør gulvet bones?", "I områder med mye trafikk er én til to ganger i året vanlig. Rom med lite bruk kan klare seg med sjeldnere behandling."),
 ],
 "related": ["tips-til-rent-kontor", "sjekkliste-flyttevask"],
},
{
 "slug": "hovedrengjoring-bedrift-og-hjem",
 "seo_title": "Hovedrengjøring: enkel plan for kontor og hjem | Tips og råd",
 "desc": "Slik planlegger du hovedrengjøringen på jobb eller hjemme: hva som bør med, hvilke midler som passer til hva, og tips som sparer tid.",
 "h1": "Hovedrengjøring: en enkel plan for bedrift og hjem",
 "tag": "Bedrift og hjem",
 "img": "hovedrengjoring.webp",
 "alt": "Hender i hansker spruter rengjøringsmiddel og tørker av en benkeplate ved vasken",
 "excerpt": "Hva som bør med, hvilke midler som passer til kalk og fett, og en sjekkliste for både arbeidsplassen og hjemmet.",
 "intro": "En eller to ganger i året er det lurt å gå grundigere til verks enn i det vanlige renholdet. Hovedrengjøring tar med alt det som ikke blir gjort hver uke. Her er en plan som fungerer både på arbeidsplassen og hjemme.",
 "toc": [("nar", "Når passer det?"), ("midler", "Riktig middel til riktig smuss"), ("jobb", "På arbeidsplassen"),
         ("hjemme", "Hjemme"), ("tid", "Tips som sparer tid")],
 "body": """
<h2 id="nar">Når passer det med hovedrengjøring?</h2>
<p>Våren er populær, når vinterens grus, salt og støv skal ut. Mange tar også en runde om høsten eller før jul. På arbeidsplassen er rolige perioder som fellesferien eller romjulen ofte de beste tidspunktene, fordi lokalene står mer tomme.</p>

<h2 id="midler">Velg riktig middel til riktig smuss</h2>
<p>Det sparer mye tid å bruke et middel som passer til smusset:</p>
<h3>Kalk og såperester</h3>
<p>Sure midler, som avkalkingsmiddel, løser opp kalk i dusj, vask og på armaturer. Ikke bruk dem på naturstein som marmor og kalkstein.</p>
<h3>Fett og matrester</h3>
<p>Basiske midler løser opp fett på kjøkkenet, for eksempel på ventilator, komfyr og skapdører.</p>
<h3>Vanlig hverdagssmuss</h3>
<p>Et mildt allrengjøringsmiddel og en mikrofiberklut holder til det meste.</p>
<div class="tip"><p><strong>Viktig:</strong> Bland aldri klor med syreholdige midler. Da kan det dannes giftige gasser.</p></div>

<h2 id="jobb">Hovedrengjøring på arbeidsplassen</h2>
<ul class="check">
<li>Tøm og vask kjøkkenskap, kjøleskap og mikrobølgeovn.</li>
<li>Rengjør stoler, sofaer og andre tekstiler.</li>
<li>Tørk støv på høye flater, lamper og ventiler.</li>
<li>Vask vinduer, karmer og glassvegger.</li>
<li>Rengjør tastaturer, telefoner og skjermer med et egnet middel.</li>
<li>Rydd lager, arkiv og boder.</li>
<li>Vurder oppskuring og ny bone på slitte gulv.</li>
</ul>
<p>Gulvet er ofte det som gir størst forskjell. Les mer om <a href="boning-og-vedlikehold-av-gulv.html">boning og vedlikehold av gulv</a>.</p>

<h2 id="hjemme">Hovedrengjøring hjemme</h2>
<ul class="check">
<li>Vask vegger, dører og karmer der det trengs.</li>
<li>Vask kjøkkenskapene innvendig.</li>
<li>Rens stekeovn, ventilator og fettfilter.</li>
<li>Vask gardiner, puter og tepper.</li>
<li>Avkalk badet grundig, også sluk og fuger.</li>
<li>Støvsug og vask under og bak møblene.</li>
</ul>
<p>Skal du flytte? Da trenger du en enda grundigere runde. Bruk <a href="sjekkliste-flyttevask.html">sjekklisten vår for flyttevask</a>.</p>

<h2 id="tid">Tips som sparer tid</h2>
<ul>
<li>Jobb ovenfra og ned, og innerst i rommet og ut.</li>
<li>Ta ett rom av gangen, så du ser fremgangen.</li>
<li>La midlene virke noen minutter før du skrubber.</li>
<li>Bruk mikrofiber, som fjerner mer smuss med mindre middel.</li>
<li>Sett av tid i kalenderen, så det faktisk blir gjort.</li>
</ul>
""",
 "cta": ("Vil dere slippe hovedrengjøringen på jobb?", "Vi tar spesialrenhold og hovedrengjøring av kontorer og næringslokaler på Haugalandet."),
 "faq": [
   ("Hvor ofte bør man ta hovedrengjøring?", "En til to ganger i året passer for de fleste. Mange velger våren og høsten."),
   ("Hva er forskjellen på vanlig renhold og hovedrengjøring?", "Vanlig renhold holder flatene rene fra uke til uke. Hovedrengjøring tar med det som gjøres sjeldnere, som skap innvendig, høye flater, vinduer og ventiler."),
   ("Kan eddik brukes på alt?", "Nei. Eddik er surt og kan skade naturstein som marmor og kalkstein, og enkelte metaller. Sjekk alltid hva flaten tåler."),
 ],
 "related": ["sjekkliste-flyttevask", "fordeler-med-profesjonelt-renhold"],
},
]
BY_SLUG = {a["slug"]: a for a in ARTICLES}

# --------------------------------------------------------------------------- helpers
def esc(s):
    return html.escape(s, quote=True)


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace('</', '<\\/') + '</script>'


def read_minutes(a):
    text = a["intro"] + " " + a["body"] + " " + " ".join(q + " " + x for q, x in a["faq"])
    words = len(re.sub(r'<[^>]+>', ' ', text).split())
    return max(2, round(words / 200))


def head(title, desc, path, image, og_type, schemas):
    url = f'{BASE}/{path}'
    return f'''<!doctype html>
<html lang="nb">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/{image}">
<meta property="og:locale" content="nb_NO">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="../assets/blog.css">
{"".join(ld(s) for s in schemas)}
</head>
<body>
'''


def header():
    return f'''<header class="site-h pad">
  <div class="wrap nav">
    <a class="logo" href="{HOME}"><img src="../img/logo-dark.png" alt="R&amp;E Renhold, Rent &amp; Effektivt" width="624" height="176"></a>
    <nav class="links" aria-label="Hovedmeny">
      <a href="{HOME}#tjenester">Tjenester</a><a href="{HOME}#om-oss">Om oss</a><a href="index.html" aria-current="page">Tips &amp; råd</a><a href="{HOME}#kontakt">Kontakt</a>
    </nav>
    <a class="btn btn-quote" href="{HOME}#kontakt">Få pristilbud</a>
    <details class="mnav"><summary aria-label="Meny">{ICON_MENU}</summary>
      <nav aria-label="Mobilmeny"><a href="{HOME}#tjenester">Tjenester</a><a href="{HOME}#om-oss">Om oss</a><a href="index.html">Tips &amp; råd</a><a href="{HOME}#kontakt">Kontakt</a><a class="btn btn-quote" href="{HOME}#kontakt">Få gratis pristilbud</a></nav>
    </details>
  </div>
</header>
'''


def footer():
    return f'''<footer class="site-f pad">
  <div class="wrap">
    <div class="fgrid">
      <div class="fcol"><a class="flogo" href="{HOME}"><img src="../img/logo-dark.png" alt="R&amp;E Renhold, Rent &amp; Effektivt" width="624" height="176" loading="lazy"></a></div>
      <div class="fcol"><a href="{HOME}#tjenester">Tjenester</a><a href="index.html">Tips &amp; råd</a><a href="{HOME}#kontakt">Få pristilbud</a></div>
      <div class="fcol"><a href="mailto:post@rentogeffektivt.no">post@rentogeffektivt.no</a><a href="https://www.google.com/maps/dir/?api=1&amp;destination=R%20%26%20E%20Renhold%20AS%2C%20St%C3%B8lsmyr%2016%2C%205542%20Karmsund" target="_blank" rel="noopener">Stølsmyr 16, 5542 Karmsund</a></div>
      <div class="fcol"><span>Man til fre 08:00 til 16:00</span><span>Org.nr. 916 712 731</span></div>
    </div>
    <div class="legal"><span>© 2026 R &amp; E Renhold AS</span><span>Prototype laget av Kilowott</span></div>
  </div>
</footer>
</body>
</html>
'''


def card(a, level='h2', feat=False, lazy=True):
    mins = read_minutes(a)
    url = a["slug"] + '.html'
    return f'''<article class="card{' feat' if feat else ''}">
  <a href="{url}" tabindex="-1" aria-hidden="true"><img src="../img/blog/{a["img"]}" alt="{esc(a["alt"])}" width="1200" height="750"{' loading="lazy"' if lazy else ''}></a>
  <div class="cb">
    <div class="meta"><span class="tag">{esc(a["tag"])}</span><span>{mins} min lesetid</span></div>
    <{level}><a href="{url}">{esc(a["h1"])}</a></{level}>
    <p>{esc(a["excerpt"])}</p>
    <a class="more" href="{url}" aria-label="Les mer: {esc(a["h1"])}">Les mer {ICON_ARROW}</a>
  </div>
</article>'''


def crumb_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


# --------------------------------------------------------------------------- pages
def article_page(a):
    path = f'tips-og-rad/{a["slug"]}.html'
    img = f'img/blog/{a["img"]}'
    mins = read_minutes(a)
    schemas = [
        {"@context": "https://schema.org", "@type": "BlogPosting", "mainEntityOfPage": f'{BASE}/{path}',
         "headline": a["h1"], "description": a["desc"], "image": f'{BASE}/{img}', "inLanguage": "nb-NO",
         "datePublished": DATE, "dateModified": DATE,
         "author": {"@type": "Organization", "name": "R & E Renhold AS", "url": BASE + "/"},
         "publisher": {"@type": "Organization", "name": "R & E Renhold AS", "logo": {"@type": "ImageObject", "url": BASE + "/img/logo-dark.png"}},
         "about": {"@id": BASE + "/#business"}},
        dict(BUSINESS, **{"@context": "https://schema.org"}),
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a["faq"]]},
        crumb_ld([("Forside", BASE + "/"), ("Tips og råd", BASE + "/tips-og-rad/"), (a["h1"], f'{BASE}/{path}')]),
    ]
    toc = ''.join(f'<li><a href="#{i}">{esc(t)}</a></li>' for i, t in a["toc"])
    faq = ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(ans)}</p></details>' for q, ans in a["faq"])
    rel = ''.join(card(BY_SLUG[s], level='h3') for s in a["related"])
    cta_h, cta_p = a["cta"]
    out = head(a["seo_title"], a["desc"], path, img, 'article', schemas) + header() + f'''<main>
  <div class="pad">
    <div class="ahead">
      <nav class="crumbs" aria-label="Brødsmuler"><a href="{HOME}">Forside</a><span aria-hidden="true">/</span><a href="index.html">Tips og råd</a><span aria-hidden="true">/</span><span>{esc(a["tag"])}</span></nav>
      <h1>{esc(a["h1"])}</h1>
      <div class="meta"><span class="tag">{esc(a["tag"])}</span><span>Publisert <time datetime="{DATE}">{DATE_NO}</time></span><span>{mins} min lesetid</span></div>
    </div>
    <div class="ahero"><img src="../img/blog/{a["img"]}" alt="{esc(a["alt"])}" width="1200" height="750" fetchpriority="high"></div>
    <article class="article">
      <p class="intro">{esc(a["intro"])}</p>
      <nav class="toc" aria-label="Innhold"><b>Innhold</b><ol>{toc}</ol></nav>
      {a["body"].strip()}
      <aside class="cta"><div><h2>{esc(cta_h)}</h2><p>{esc(cta_p)}</p></div><a class="btn btn-quote" href="{HOME}#kontakt">Få gratis pristilbud {ICON_ARROW}</a></aside>
      <section aria-labelledby="faq-h"><h2 id="faq-h">Ofte stilte spørsmål</h2><div class="faq">{faq}</div></section>
    </article>
  </div>
  <section class="related pad" aria-labelledby="rel-h"><div class="wrap"><h2 id="rel-h">Les også</h2><div class="rgrid">{rel}</div></div></section>
</main>
''' + footer()
    return out


def index_page():
    title = "Tips og råd om renhold | R&E Renhold Haugesund"
    desc = "Praktiske råd om kontorrenhold, flyttevask, gulvpleie og hovedrengjøring fra et lokalt renholdsfirma på Haugalandet."
    path = 'tips-og-rad/'
    schemas = [
        {"@context": "https://schema.org", "@type": "Blog", "name": "Tips og råd om renhold", "url": BASE + "/tips-og-rad/",
         "inLanguage": "nb-NO", "publisher": {"@id": BASE + "/#business"},
         "blogPost": [{"@type": "BlogPosting", "headline": a["h1"], "url": f'{BASE}/tips-og-rad/{a["slug"]}.html', "datePublished": DATE} for a in ARTICLES]},
        dict(BUSINESS, **{"@context": "https://schema.org"}),
        crumb_ld([("Forside", BASE + "/"), ("Tips og råd", BASE + "/tips-og-rad/")]),
    ]
    first, rest = ARTICLES[0], ARTICLES[1:]
    cards = card(first, feat=True, lazy=False) + ''.join(card(a) for a in rest)
    return head(title, desc, path, 'img/blog/' + first["img"], 'website', schemas) + header() + f'''<main>
  <section class="bhead pad">
    <div class="wrap">
      <nav class="crumbs" aria-label="Brødsmuler"><a href="{HOME}">Forside</a><span aria-hidden="true">/</span><span>Tips og råd</span></nav>
      <h1>Tips og råd om renhold</h1>
      <p class="lead">Praktiske råd fra hverdagen som renholdsfirma på Haugalandet. For bedrifter som vil ha det rent, og alle som vil gjøre jobben enklere.</p>
    </div>
  </section>
  <div class="pad"><div class="wrap bgrid">{cards}</div></div>
</main>
''' + footer()


def main():
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_page())
    for a in ARTICLES:
        with open(os.path.join(OUT, a["slug"] + '.html'), 'w', encoding='utf-8') as f:
            f.write(article_page(a))
        print(a["slug"], read_minutes(a), 'min', len(a["seo_title"]), 'title chars', len(a["desc"]), 'desc chars')


if __name__ == '__main__':
    main()
