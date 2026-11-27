"""Service and area pages, Norwegian and English. Same key = same page in two languages."""

AREA_LINKS = {
    'no': {'haugesund': '../omrader/renhold-haugesund.html', 'karmoy': '../omrader/renhold-karmoy.html'},
    'en': {'haugesund': '../areas/cleaning-haugesund.html', 'karmoy': '../areas/cleaning-karmoy.html'},
}

PAGES = {
# ------------------------------------------------------------------ services
'bedriftsrenhold': {
 'kind': 'service', 'img': 'bedriftsrenhold.webp',
 'no': {
  'path': 'tjenester/bedriftsrenhold.html',
  'seo_title': 'Bedriftsrenhold i Haugesund og på Karmøy | R&E Renhold',
  'desc': 'Fast renhold av kontorer, butikker og fellesarealer på Haugalandet. Dere bestemmer hvor ofte. Godkjent av Arbeidstilsynet. Be om pristilbud.',
  'h1': 'Bedriftsrenhold på Haugalandet', 'crumb': 'Bedriftsrenhold', 'tag': 'Tjeneste',
  'alt': 'Renholder i hansker støvsuger teppegulvet i et moderne kontor med glassvegger',
  'intro': 'Daglig eller regelmessig renhold av kontorer, butikker og fellesarealer. Dere bestemmer hvor ofte og hva som skal gjøres, og vi sørger for at det blir gjort grundig hver gang.',
  'body': '''
<h2>Dette kan inngå</h2>
<ul class="check">
<li>Støvtørking og avtørking av pulter, hyller og flater</li>
<li>Støvsuging og vask av gulv</li>
<li>Toaletter, garderober og dusjer</li>
<li>Kjøkken, kantine og pauserom</li>
<li>Tømming av søppel og kildesortering</li>
<li>Inngangsparti, trapper og fellesarealer</li>
</ul>
<p>Innholdet tilpasses lokalene deres. Det er dere som bestemmer hva som skal med.</p>

<h2>Dere bestemmer hvor ofte</h2>
<p>Noen trenger renhold hver dag, andre klarer seg med én gang i uken eller annenhver uke. Vi lager en løsning ut fra hvor mange som bruker lokalene, hvor mye besøk dere har og hva budsjettet tillater. Behovet kan justeres underveis.</p>

<h2>Slik kommer dere i gang</h2>
<ol>
<li>Be om et uforpliktende pristilbud via skjemaet eller på telefon.</li>
<li>Vi går gjennom lokalene og behovene deres sammen.</li>
<li>Renholdet starter etter avtale.</li>
</ol>

<h2>Hvor vi leverer bedriftsrenhold</h2>
<p>Vi holder til i Karmsund og tar oppdrag i <a href="{haugesund}">Haugesund</a>, på <a href="{karmoy}">Karmøy</a> og i resten av Haugalandet.</p>
<p>Vil du lese mer først? Se <a href="../blogg/tips-til-rent-kontor.html">tipsene våre for et rent kontor</a> eller <a href="../blogg/fordeler-med-profesjonelt-renhold.html">fordelene med profesjonelt renhold</a>.</p>
''',
  'cta': ('Klar for fast renhold?', 'Fortell oss om lokalene, så får dere et uforpliktende pristilbud.'),
  'faq': [
   ('Må vi binde oss for lang tid?', 'Avtalen tilpasses dere. Spør gjerne om oppsigelsestid og fleksibilitet når dere ber om pristilbud.'),
   ('Er dere godkjent av Arbeidstilsynet?', 'Ja. R & E Renhold AS er godkjent av Arbeidstilsynet, slik alle renholdsvirksomheter i Norge skal være.'),
   ('Hvordan får vi vite hva det koster?', 'Prisen avhenger av størrelse, hvor ofte det skal vaskes og hva som skal inngå. Be om et uforpliktende pristilbud, så får dere en pris tilpasset lokalene.'),
  ],
 },
 'en': {
  'path': 'services/office-cleaning.html',
  'seo_title': 'Office and commercial cleaning in Haugesund | R&E Renhold',
  'desc': 'Regular cleaning of offices, shops and shared areas in Haugalandet. You decide how often. Approved by the Labour Inspection Authority. Request a quote.',
  'h1': 'Office and commercial cleaning in Haugalandet', 'crumb': 'Office cleaning', 'tag': 'Service',
  'alt': 'Cleaner in gloves vacuuming the carpet in a modern office with glass walls',
  'intro': 'Daily or regular cleaning of offices, shops and shared areas. You decide how often and what is included, and we make sure it is done thoroughly every time.',
  'body': '''
<h2>What can be included</h2>
<ul class="check">
<li>Dusting and wiping desks, shelves and surfaces</li>
<li>Vacuuming and washing floors</li>
<li>Toilets, changing rooms and showers</li>
<li>Kitchens, canteens and break rooms</li>
<li>Emptying bins and recycling</li>
<li>Entrances, stairs and shared areas</li>
</ul>
<p>The scope is tailored to your premises. You decide what is included.</p>

<h2>You decide how often</h2>
<p>Some need cleaning every day, others manage with once a week or every other week. We put together a solution based on how many people use the premises, how many visitors you have and your budget. It can be adjusted along the way.</p>

<h2>How to get started</h2>
<ol>
<li>Request a no-obligation quote using the form or by phone.</li>
<li>We go through your premises and needs together.</li>
<li>Cleaning starts as agreed.</li>
</ol>

<h2>Where we provide office cleaning</h2>
<p>We are based in Karmsund and take on work in <a href="{haugesund}">Haugesund</a>, on <a href="{karmoy}">Karmøy</a> and across the rest of Haugalandet.</p>
<p>Want to read more first? See <a href="../blog/office-cleaning-tips.html">our tips for a clean office</a> or <a href="../blog/benefits-of-professional-cleaning.html">the benefits of professional cleaning</a>.</p>
''',
  'cta': ('Ready for regular cleaning?', 'Tell us about your premises and we will send you a no-obligation quote.'),
  'faq': [
   ('Do we need to sign up for a long time?', 'The agreement is tailored to you. Feel free to ask about notice periods and flexibility when you request a quote.'),
   ('Are you approved by the Labour Inspection Authority?', 'Yes. R & E Renhold AS is approved by the Labour Inspection Authority, as every cleaning company in Norway must be.'),
   ('How do we find out what it costs?', 'The price depends on size, how often you want cleaning and what is included. Request a no-obligation quote and you will get a price tailored to your premises.'),
  ],
 },
},
'spesialrenhold': {
 'kind': 'service', 'img': 'spesialrenhold.webp',
 'no': {
  'path': 'tjenester/spesialrenhold.html',
  'seo_title': 'Spesialrenhold og hovedrengjøring | Haugesund og Karmøy',
  'desc': 'Spesialrenhold når vanlig renhold ikke strekker til: hovedrengjøring, rengjøring etter oppussing og før overlevering av lokaler på Haugalandet.',
  'h1': 'Spesialrenhold for bedrifter', 'crumb': 'Spesialrenhold', 'tag': 'Tjeneste',
  'alt': 'Hånd i gul hanske tørker av et skrivebord med klut og rengjøringsspray',
  'intro': 'Noen ganger trenger lokalene mer enn det faste renholdet. Spesialrenhold tilpasses oppdraget, enten det er en grundig hovedrengjøring eller lokaler som skal være klare til nye leietakere.',
  'body': '''
<h2>Typiske oppdrag</h2>
<ul class="check">
<li>Hovedrengjøring av kontorer og fellesarealer</li>
<li>Rengjøring etter oppussing eller ombygging</li>
<li>Rengjøring før overlevering av lokaler</li>
<li>Grundig rengjøring av kjøkken og sanitærrom</li>
<li>Høye flater, lamper og ventiler</li>
</ul>

<h2>Tilpasset hvert oppdrag</h2>
<p>Ingen spesialrenhold er helt like. Vi går gjennom hva som skal gjøres, hvilke flater og materialer det gjelder, og når lokalene må være ferdige. Så setter vi opp en plan og et pristilbud ut fra det.</p>

<h2>Kombiner med gulvbehandling</h2>
<p>Ved en grundig rengjøring er det ofte lurt å gi gulvet en ny start samtidig. Les om <a href="boning-og-oppskuring.html">boning og oppskuring av gulv</a>.</p>

<h2>Les mer</h2>
<p>Se <a href="../blogg/hovedrengjoring-bedrift-og-hjem.html">planen vår for hovedrengjøring</a> og <a href="../blogg/sjekkliste-flyttevask.html">sjekklisten for flyttevask</a>. Vi tar oppdrag i <a href="{haugesund}">Haugesund</a>, på <a href="{karmoy}">Karmøy</a> og i resten av Haugalandet.</p>
''',
  'cta': ('Trenger lokalene en grundig runde?', 'Beskriv oppdraget, så får dere et uforpliktende pristilbud.'),
  'faq': [
   ('Hva er forskjellen på spesialrenhold og vanlig renhold?', 'Vanlig renhold holder lokalene rene fra uke til uke. Spesialrenhold er grundigere og tar med det som ikke gjøres i det faste renholdet.'),
   ('Kan spesialrenhold bestilles som et enkeltoppdrag?', 'Ja, spesialrenhold kan bestilles uten fast avtale. Ta kontakt for et uforpliktende pristilbud.'),
  ],
 },
 'en': {
  'path': 'services/specialist-cleaning.html',
  'seo_title': 'Specialist and deep cleaning | Haugesund and Karmøy',
  'desc': 'Specialist cleaning when regular cleaning is not enough: deep cleans, cleaning after renovation and before handing over premises in Haugalandet.',
  'h1': 'Specialist cleaning for businesses', 'crumb': 'Specialist cleaning', 'tag': 'Service',
  'alt': 'Hand in a yellow glove wiping a desk with a cloth and cleaning spray',
  'intro': 'Sometimes premises need more than regular cleaning. Specialist cleaning is tailored to the job, whether it is a thorough deep clean or premises that need to be ready for new tenants.',
  'body': '''
<h2>Typical jobs</h2>
<ul class="check">
<li>Deep cleaning of offices and shared areas</li>
<li>Cleaning after renovation or refurbishment</li>
<li>Cleaning before handing over premises</li>
<li>Thorough cleaning of kitchens and washrooms</li>
<li>High surfaces, lamps and vents</li>
</ul>

<h2>Tailored to every job</h2>
<p>No two specialist cleans are the same. We go through what needs doing, which surfaces and materials are involved, and when the premises need to be ready. We then put together a plan and a quote based on that.</p>

<h2>Combine with floor treatment</h2>
<p>During a thorough clean it often makes sense to give the floor a fresh start at the same time. Read about <a href="floor-stripping-and-polishing.html">floor stripping and polishing</a>.</p>

<h2>Read more</h2>
<p>See <a href="../blog/deep-cleaning-guide.html">our deep cleaning plan</a> and <a href="../blog/move-out-cleaning-checklist.html">the move-out cleaning checklist</a>. We take on work in <a href="{haugesund}">Haugesund</a>, on <a href="{karmoy}">Karmøy</a> and across the rest of Haugalandet.</p>
''',
  'cta': ('Do your premises need a thorough clean?', 'Describe the job and we will send you a no-obligation quote.'),
  'faq': [
   ('What is the difference between specialist and regular cleaning?', 'Regular cleaning keeps premises clean from week to week. Specialist cleaning is more thorough and covers what is not done in the regular cleaning.'),
   ('Can specialist cleaning be booked as a one-off job?', 'Yes, specialist cleaning can be booked without a regular agreement. Get in touch for a no-obligation quote.'),
  ],
 },
},
'boning': {
 'kind': 'service', 'img': 'boning.webp',
 'no': {
  'path': 'tjenester/boning-og-oppskuring.html',
  'seo_title': 'Boning og oppskuring av gulv i Haugesund | R&E Renhold',
  'desc': 'Oppskuring og boning av vinyl- og linoleumsgulv i kontorer, butikker og fellesarealer på Haugalandet. Gi gulvet nytt liv og lengre levetid.',
  'h1': 'Boning og oppskuring av gulv', 'crumb': 'Boning og oppskuring', 'tag': 'Tjeneste',
  'alt': 'Renholder vasker et lyst gulv med mopp i et rom med store vinduer',
  'intro': 'Få gulvet til å se nytt ut igjen. Med oppskuring fjernes gammel, slitt bone, og en ny beskyttende bone gir gulvet glans og tåler hverdagen bedre.',
  'body': '''
<h2>Når trenger gulvet ny bone?</h2>
<p>Et gulv som ser matt og grått ut selv rett etter vask, eller som har tydelige gangveier, er ofte modent for oppskuring og ny bone. Du kan lese mer om tegnene i <a href="../blogg/boning-og-vedlikehold-av-gulv.html">guiden vår om gulvvedlikehold</a>.</p>

<h2>Gulv vi behandler</h2>
<p>Boning passer for vinyl og linoleum, som er vanlig i kontorer, butikker, skoler og fellesarealer. Fliser og tregulv har egne behandlinger og bones ikke.</p>

<h2>Slik foregår jobben</h2>
<ol>
<li>Gulvet ryddes og støvsuges.</li>
<li>Gammel bone skures bort med maskin.</li>
<li>Gulvet skylles og tørker.</li>
<li>Ny bone legges i flere tynne lag.</li>
<li>Gulvet herder før det tas i bruk igjen.</li>
</ol>

<h2>Område</h2>
<p>Vi behandler gulv i <a href="{haugesund}">Haugesund</a>, på <a href="{karmoy}">Karmøy</a> og i resten av Haugalandet. Gulvbehandling kan også kombineres med <a href="spesialrenhold.html">spesialrenhold</a>.</p>
''',
  'cta': ('Ser gulvene slitne ut?', 'Fortell oss om gulvene og lokalene, så får dere et uforpliktende pristilbud.'),
  'faq': [
   ('Kan jobben gjøres utenom åpningstid?', 'Fordi gulvet må tørke mellom lagene, passer det ofte å gjøre jobben på kveldstid eller i helgen. Tidspunkt avtales med dere.'),
   ('Hvor lang tid tar det?', 'Det avhenger av størrelsen på gulvet og hvor mange lag som trengs. Dere får et anslag sammen med pristilbudet.'),
  ],
 },
 'en': {
  'path': 'services/floor-stripping-and-polishing.html',
  'seo_title': 'Floor stripping and polishing in Haugesund | R&E Renhold',
  'desc': 'Stripping and polishing of vinyl and linoleum floors in offices, shops and shared areas in Haugalandet. Give your floor new life and a longer lifespan.',
  'h1': 'Floor stripping and polishing', 'crumb': 'Floor stripping and polishing', 'tag': 'Service',
  'alt': 'Cleaner mopping a bright floor in a room with large windows',
  'intro': 'Make your floor look new again. Stripping removes old, worn polish, and a new protective coat gives the floor shine and helps it stand up to everyday use.',
  'body': '''
<h2>When does a floor need a new coat?</h2>
<p>A floor that looks dull and grey even straight after cleaning, or that has clear walkways, is often ready for stripping and a new coat. You can read more about the signs in <a href="../blog/floor-polishing-and-maintenance.html">our floor maintenance guide</a>.</p>

<h2>Floors we treat</h2>
<p>Polishing suits vinyl and linoleum, which are common in offices, shops, schools and shared areas. Tiles and wooden floors have their own treatments and are not polished.</p>

<h2>How the job is done</h2>
<ol>
<li>The floor is cleared and vacuumed.</li>
<li>Old polish is stripped off with a machine.</li>
<li>The floor is rinsed and left to dry.</li>
<li>New polish is applied in several thin coats.</li>
<li>The floor cures before it is used again.</li>
</ol>

<h2>Area</h2>
<p>We treat floors in <a href="{haugesund}">Haugesund</a>, on <a href="{karmoy}">Karmøy</a> and across the rest of Haugalandet. Floor treatment can also be combined with <a href="specialist-cleaning.html">specialist cleaning</a>.</p>
''',
  'cta': ('Are your floors looking tired?', 'Tell us about your floors and premises and we will send you a no-obligation quote.'),
  'faq': [
   ('Can the work be done outside opening hours?', 'Because the floor has to dry between coats, the work is often best done in the evening or at the weekend. The timing is agreed with you.'),
   ('How long does it take?', 'It depends on the size of the floor and how many coats are needed. You will get an estimate with the quote.'),
  ],
 },
},
# ------------------------------------------------------------------ areas
'haugesund': {
 'kind': 'area', 'img': 'blog/rent-kontor.webp', 'city': 'Haugesund',
 'no': {
  'path': 'omrader/renhold-haugesund.html',
  'seo_title': 'Renhold i Haugesund for bedrifter | R&E Renhold',
  'desc': 'Lokalt renholdsfirma for bedrifter i Haugesund: bedriftsrenhold, spesialrenhold og boning av gulv. Kort vei fra Karmsund. Be om pristilbud.',
  'h1': 'Renhold for bedrifter i Haugesund', 'crumb': 'Haugesund', 'tag': 'Område',
  'alt': 'Lyst og ryddig kontor med glassvegger og grønne planter',
  'intro': 'Vi holder til i Stølsmyr i Karmsund, rett ved Raglamyr, og har kort vei til bedrifter over hele Haugesund, fra kontorer i sentrum til butikker og næringsbygg i handelsområdene.',
  'body': '''
<h2>Tjenester i Haugesund</h2>
<ul>
<li><a href="../tjenester/bedriftsrenhold.html"><strong>Bedriftsrenhold</strong></a>: fast renhold av kontorer, butikker og fellesarealer.</li>
<li><a href="../tjenester/spesialrenhold.html"><strong>Spesialrenhold</strong></a>: hovedrengjøring og grundige engangsoppdrag.</li>
<li><a href="../tjenester/boning-og-oppskuring.html"><strong>Boning og oppskuring</strong></a>: nytt liv til vinyl- og linoleumsgulv.</li>
</ul>

<h2>Bygg vi rengjør i Haugesund</h2>
<p>Kontorer og kontorfellesskap i sentrum, butikker og handelslokaler, borettslag og sameier, skoler og offentlige bygg, samt lager og lettere industri.</p>

<h2>Fordelen med et lokalt renholdsfirma</h2>
<p>Kort vei betyr at det er enkelt å møtes, gå gjennom lokalene og følge opp underveis. Når noe skal justeres, er vi i nærheten.</p>
<p>Vi dekker også <a href="{karmoy}">Karmøy</a>, Tysvær, Bokn og Sveio.</p>
''',
  'cta': ('Trenger bedriften renhold i Haugesund?', 'Be om et uforpliktende pristilbud, så tar vi kontakt.'),
  'faq': [
   ('Dekker dere hele Haugesund?', 'Ja. Fra kontoret vårt i Karmsund har vi kort vei til hele Haugesund.'),
   ('Hvilke typer bedrifter jobber dere for?', 'Vi tilbyr renhold for kontorer, butikker, borettslag, skoler og offentlige bygg, og lager og lettere industri.'),
  ],
 },
 'en': {
  'path': 'areas/cleaning-haugesund.html',
  'seo_title': 'Commercial cleaning in Haugesund | R&E Renhold',
  'desc': 'Local cleaning company for businesses in Haugesund: office cleaning, specialist cleaning and floor polishing. A short trip from Karmsund. Request a quote.',
  'h1': 'Commercial cleaning in Haugesund', 'crumb': 'Haugesund', 'tag': 'Area',
  'alt': 'Bright, tidy office with glass walls and green plants',
  'intro': 'We are based at Stølsmyr in Karmsund, right next to Raglamyr, and are a short trip from businesses across Haugesund, from offices in the town centre to shops and commercial buildings in the retail areas.',
  'body': '''
<h2>Services in Haugesund</h2>
<ul>
<li><a href="../services/office-cleaning.html"><strong>Office cleaning</strong></a>: regular cleaning of offices, shops and shared areas.</li>
<li><a href="../services/specialist-cleaning.html"><strong>Specialist cleaning</strong></a>: deep cleans and thorough one-off jobs.</li>
<li><a href="../services/floor-stripping-and-polishing.html"><strong>Floor stripping and polishing</strong></a>: new life for vinyl and linoleum floors.</li>
</ul>

<h2>Buildings we clean in Haugesund</h2>
<p>Offices and co-working spaces in the town centre, shops and retail premises, housing associations, schools and public buildings, and warehouses and light industry.</p>

<h2>The advantage of a local cleaning company</h2>
<p>Being close by makes it easy to meet, walk through the premises and follow up along the way. When something needs adjusting, we are nearby.</p>
<p>We also cover <a href="{karmoy}">Karmøy</a>, Tysvær, Bokn and Sveio.</p>
''',
  'cta': ('Does your business need cleaning in Haugesund?', 'Request a no-obligation quote and we will get in touch.'),
  'faq': [
   ('Do you cover all of Haugesund?', 'Yes. From our office in Karmsund we are a short trip from all of Haugesund.'),
   ('What kinds of businesses do you work for?', 'We offer cleaning for offices, shops, housing associations, schools and public buildings, and warehouses and light industry.'),
  ],
 },
},
'karmoy': {
 'kind': 'area', 'img': 'om-oss.webp', 'city': 'Karmøy',
 'no': {
  'path': 'omrader/renhold-karmoy.html',
  'seo_title': 'Renhold på Karmøy for bedrifter | R&E Renhold',
  'desc': 'Bedriftsrenhold, spesialrenhold og boning av gulv for bedrifter på Karmøy, fra Kopervik og Åkrehamn til Avaldsnes. Lokalt renholdsfirma fra Karmsund.',
  'h1': 'Renhold for bedrifter på Karmøy', 'crumb': 'Karmøy', 'tag': 'Område',
  'alt': 'Renholder i gule hansker vasker et vindu med nal og spray',
  'intro': 'Karmøy ligger rett over Karmsundet fra oss. Vi tilbyr renhold til bedrifter på øya, enten lokalene ligger i Kopervik, Åkrehamn, Avaldsnes eller et annet sted i kommunen.',
  'body': '''
<h2>Tjenester på Karmøy</h2>
<ul>
<li><a href="../tjenester/bedriftsrenhold.html"><strong>Bedriftsrenhold</strong></a>: fast renhold, så ofte dere ønsker.</li>
<li><a href="../tjenester/spesialrenhold.html"><strong>Spesialrenhold</strong></a>: når lokalene trenger en grundigere runde.</li>
<li><a href="../tjenester/boning-og-oppskuring.html"><strong>Boning og oppskuring</strong></a>: for slitte vinyl- og linoleumsgulv.</li>
</ul>

<h2>Renhold tilpasset ulike typer bygg</h2>
<p>Karmøy har et variert næringsliv, med industri, handel og kontorer. Mange bygg har lager, verksted, garderober eller kantine i tillegg til kontorer. Renholdet tilpasses det som finnes i lokalene, slik at alt får riktig behandling.</p>

<h2>Godkjent og lokalt</h2>
<p>R &amp; E Renhold AS er godkjent av Arbeidstilsynet og har drevet med renhold siden 2016. Vi dekker også <a href="{haugesund}">Haugesund</a>, Tysvær, Bokn og Sveio.</p>
''',
  'cta': ('Trenger bedriften renhold på Karmøy?', 'Be om et uforpliktende pristilbud, så tar vi kontakt.'),
  'faq': [
   ('Tar dere oppdrag over hele Karmøy?', 'Ta kontakt med adressen til lokalene, så avklarer vi oppdraget og gir et uforpliktende pristilbud.'),
   ('Kan renholdet omfatte garderober og kantine?', 'Ja. Bedriftsrenhold kan omfatte kontorer, garderober, kantiner og andre fellesarealer, etter hva dere trenger.'),
  ],
 },
 'en': {
  'path': 'areas/cleaning-karmoy.html',
  'seo_title': 'Commercial cleaning on Karmøy | R&E Renhold',
  'desc': 'Office cleaning, specialist cleaning and floor polishing for businesses on Karmøy, from Kopervik and Åkrehamn to Avaldsnes. Based in Karmsund.',
  'h1': 'Commercial cleaning on Karmøy', 'crumb': 'Karmøy', 'tag': 'Area',
  'alt': 'Cleaner in yellow gloves cleaning a window with a squeegee and spray',
  'intro': 'Karmøy lies just across the Karmsund strait from us. We offer cleaning to businesses on the island, whether your premises are in Kopervik, Åkrehamn, Avaldsnes or elsewhere in the municipality.',
  'body': '''
<h2>Services on Karmøy</h2>
<ul>
<li><a href="../services/office-cleaning.html"><strong>Office cleaning</strong></a>: regular cleaning, as often as you need.</li>
<li><a href="../services/specialist-cleaning.html"><strong>Specialist cleaning</strong></a>: when your premises need a more thorough round.</li>
<li><a href="../services/floor-stripping-and-polishing.html"><strong>Floor stripping and polishing</strong></a>: for worn vinyl and linoleum floors.</li>
</ul>

<h2>Cleaning tailored to different buildings</h2>
<p>Karmøy has a varied business community, with industry, retail and offices. Many buildings have storage, workshops, changing rooms or a canteen as well as offices. Cleaning is tailored to what is in the premises, so everything gets the right treatment.</p>

<h2>Approved and local</h2>
<p>R &amp; E Renhold AS is approved by the Labour Inspection Authority and has been in the cleaning business since 2016. We also cover <a href="{haugesund}">Haugesund</a>, Tysvær, Bokn and Sveio.</p>
''',
  'cta': ('Does your business need cleaning on Karmøy?', 'Request a no-obligation quote and we will get in touch.'),
  'faq': [
   ('Do you take on work across all of Karmøy?', 'Get in touch with the address of your premises and we will confirm the job and send a no-obligation quote.'),
   ('Can the cleaning include changing rooms and the canteen?', 'Yes. Office cleaning can cover offices, changing rooms, canteens and other shared areas, depending on what you need.'),
  ],
 },
},
}
ORDER_SERVICES = ['bedriftsrenhold', 'spesialrenhold', 'boning']
ORDER_AREAS = ['haugesund', 'karmoy']
