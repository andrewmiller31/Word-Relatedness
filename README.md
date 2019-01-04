# Word-Relatedness
A program that determines how related two words are based on the contents of their respective Wikipedia pages. The relatedness measure
is on a scale of -1 to 1 where -1 is no relatedness and 1 is exact match. The program works by comparing how many words are in common based of the first n amount of words. Stop words are omitted to avoid noise. The stop words are chosen by mining them from Wikipedia. You may use the ones that I found, or mine your own with sw.py. 

To run wiki-relatedness.py:

python wiki-relatedness.py \<numpy array of stop words\>
  
To run sw.py:

stop-words.py \<array name\>

## Example Dialogue
Input N value: 1000

Input word 1: cat

Input word 2: dog

relatedness: 0.3880

overlaps: asian, controversial, hunting, under, include, large, mammal, subspecies, asia, others, along, study, published, usually, classification, sire, use, remains, more, populations, known, animals, can, male, example, breeds, household, sense, species, interbreed, animal, 1758, ancestor, may, such, types, natural, taxonomy, years, through, rapidly, them, dam, they, lineage, predators, found, referred, female, term, forms, origin, number, another, size, given, dogs, relationship, part, than, population, behaviors, modern, traditionally, isolated, any, mother, anatomy, most, considered, m, typically, taxonomic, only, black, do, his, morphological, despite, common, vision, humans, edition, see, close, various, between, europe, ability, distinguish, group, many, genus, among, color, companionship, capable, due, genetic, senses, former, those, these, behavior, wild, clearly, member, well, english, proposed, being, domestic, human, east, possible, like, often, people, some, gradually, predatory, equally, there, form, mammals, related, partially, made, different, called, irish, bred, certain, domesticated, no, generally, smell, teeth, unspayed, ago, independently, having, once 

Input word 1: World War I

Input word 2: World War II

relatedness: 0.6270

overlaps: caused, global, battle, fronts, paris, concerned, vast, prevent, abbreviated, revolution, invaded, cost, even, established, fatalities, led, following, china, civilians, 100, great, prior, resulting, defeat, military, marked, 1945, devastation, troops, france, 6, more, under, wars, known, capturing, making, history, august, days, states, allowed, united, end, 1, may, halted, september, over, major, japan, possessions, then, primary, front, day, victory, series, globe, changed, out, empires, million, free, conflicts, advance, allies, british, allied, romania, industrial, historian, 2, 1919, western, entente, july, 1917, war, powers, russia, austriahungary, majority, forces, though, most, involving, germany, germans, later, treaty, dissolved, german, agreed, treaties, ottoman, than, only, he, during, imposed, through, bulgaria, declared, nations, opening, 3, cooperation, between, europe, terms, however, league, signed, many, april, roman, became, period, conference, west, political, much, territory, armistice, eastern, influence, these, socialist, while, losses, eventually, defeated, ii, against, alliances, italy, largest, 9, conflict, european, used, upon, i, soviet, generally, human, east, versailles, government, early, background, 30, belgium, world, 50, often, creation, some, pacific, home, empire, colonial, power, balkans, 1939, central, alliance, primarily, attrition, support, long, start, fought, russian, october, up, us, nationalist, deadliest, britain, no, peace, republic, june, began, moved, lasted 

Input word 1: Star Wars

Input word 2: Star Trek

relatedness: 0.4450

overlaps: tv, far, fall, direct, second, further, led, highestgrossing, inspired, followed, would, few, films, rights, i, work, movies, nine, making, control, stated, species, united, travel, may, such, media, over, episodes, own, including, during, spinoff, before, late, production, 2016, might, then, them, they, opera, january, each, referred, studios, another, generation, series, society, out, space, shows, wanted, created, where, american, revenue, story, script, too, park, rejected, released, television, binds, most, episode, later, phenomenon, make, producer, going, hope, his, wrote, set, culture, still, fans, various, we, franchise, many, adventures, games, pop, cancel, throughout, due, pilot, developing, these, value, cast, animated, century, technology, things, began, same, difficult, intended, early, 1974, 1973, just, love, death, role, world, success, become, although, involving, act, civil, aliens, down, additional, there, war, billion, offer, sequel, trying, he, made, up, stories, similar, popularity, together, planets, film, no, setting, you, star, 2008, original 

Input word 1: lion

Input word 2: tiger

relatedness: 0.6040

overlaps: caused, results, tail, those, large, p, 20th, force, likely, subspecies, scientific, asia, 19th, fossil, asiatic, groups, study, larger, alaska, published, usually, gene, distinct, few, depicted, therefore, films, more, females, populations, occurred, known, work, cat, nine, can, male, india, times, species, animal, 1758, may, neck, naturae, greek, evolutionary, rounded, panthera, years, lb, systema, apex, late, 2017, males, predator, they, lineage, name, each, found, revised, literature, etymology, million, carl, conflicts, earliest, used, unknown, origin, size, little, ancient, indicate, than, sister, distinguished, latter, bengal, relatives, most, kg, especially, flow, typically, based, northern, pleistocene, only, taxonomy, his, morphological, during, areas, evolution, jaguar, countries, preying, where, ears, specialist, national, humans, lion, 1929, skulls, phylogeographic, distinctive, recognisable, between, probably, latin, group, both, last, many, region, became, genus, among, period, forms, described, basis, genetic, recognised, eastern, tiger, these, iucn, characteristics, middle, same, widely, several, centuries, closest, leopard, recent, task, well, analysis, thought, flags, proposed, being, snow, human, world, classification, deposits, gave, around, big, early, possibly, prominent, because, old, often, habitat, some, lineages, extinct, dense, does, glacial, although, about, remains, range, female, linnaeus, there, cats, lions, specimens, head, related, true, absent, captive, ungulates, similar, felis, muscular, diverged, whereas, valid, variation, important, ago, longer 

Input word 1: sun

Input word 2: cave

relatedness: 0.2480

overlaps: layers, include, large, smaller, mi, second, estimated, above, usually, total, type, more, known, word, can, believed, give, process, near, high, hydrogen, influenced, may, such, years, produced, including, hot, they, day, term, square, formation, undergo, south, another, system, collapse, than, toward, 335, though, most, later, km, much, only, over, through, result, between, many, among, basis, due, formed, those, these, will, surface, if, off, nearby, less, shape, human, deposits, source, 5, aspects, around, kilometres, world, become, exposed, some, 50, refer, popular, within, long, form, sometimes, associated, again, no, whereas, out 

Input word 1: schleeb

Input word 2: snake

relatedness: -1.0000

overlaps:  

Input word 1: mars

Input word 2: mars

relatedness: 1.0000
overlaps: magnetically, limited, caused, magnetic, asteroids, four, ceased, avalanche, consists, follow, abundant, displaying, localized, polarity, subjected, young, oldest, olivine, suns, stochastic, include, indicating, alternating, brown, global, returned, geology, landforms, olympus, 1794, comparatively, minerals, elevations, entire, differentiated, 5261, 5300, underlain, bright, large, avalanches, greenish, small, 294, overlaid, highcalcium, 190, past, imply, bombardment, sulfide, estimated, even, disk, appear, organisms, sun, crust, thickness, current, poles, consisting, thin, body, layers, alkaline, cryosphere, hundreds, water, reported, kilometers, path, november, appears, reversals, 38, 33, 31, era, 36, 35, suggests, amount, chemical, resulting, published, composed, golden, named, marked, visible, 700metrehigh, total, scarred, eye, would, contains, telescopes, few, soil, more, lander, apparent, basalt, glass, known, rotational, pushed, 1999, cap, mi, theories, oxide, regions, can, following, averages, latitudes, history, protoplanetary, grained, impacts, process, fadedit, involve, surveyor, performed, tan, spanning, terrestrial, varied, tilt, feature, surpassed, 1, fourth, express, ft, may, southern, silicarich, tholeiitic, such, data, highlands, liquid, ones, typical, help, produces, astronomical, years, radar, experiments, including, astrobiology, still, before, 25, 20, sodium, susceptible, 29, late, detected, systems, covered, 2016, planitia, then, perchloratestreaks, material, they, half, easily, february, name, oxygen, rocks, magnitude, noachian, rock, volcano, 8500, referred, heavy, dichotomy, hemispheric, fossae, event, out, god, surrounded, socalled, suggesting, planum, cause, red, shows, theory, possibility, quite, formation, besides, put, hematite, venus, chlorine, enormous, silicate, created, reexamined, grabens, times, silicon, place, south, borealis, phobos, features, primary, reaches, floors, directly, feldspar, rovers, thick, size, mercury, earths, sheet, start, revealed, structured, diameter, system, approximately, deimos, plains, accretion, observations, gives, trapped, shallow, optical, sulphur, than, 11, 15, showed, 19, utopia, future, 2020, magnesium, iron, finely, steep, function, amazonis, marsgeological, seen, ocean, albedo, mountain, depending, 1617, gravity, metallic, plutosized, internal, interior, silicates, 200, normal, troughs, 77, most, seasons, upland, 78, noachis, 2300, average, cover, km, points, intrusions, deeply, typically, planetary, atmosphere, show, discovered, colors, earth, july, impact, reminiscent, giant, coloring, deserts, northern, short, only, rich, hesperia, sulfur, cerberus, plate, get, canyons, between, cannot, 125, lighter, during, aluminum, naked, twice, common, activity, cycles, explanations, sheetlike, devils, up, irregularly, radius, result, outward, surfaces, hesperian, 06, distinctive, dipole, windafter, moons, probably, across, andesitic, secondhighest, craters, dynamo, both, planned, hydrology, missions, many, region, marineris, boulders, roman, mons, otherwise, among, stretches, volcanic, basins, period, lake, 60, pole, 65, runaway, due, tiny, immense, magnetized, much, mars, basin, dry, life, nickel, quantities, sufficient, formed, streaks, pyroxenes, covers, extant, extensive, present, plants, trojan, atmospheric, look, reddish, these, appearance, amazonian, middle, calcium, melted, ongoing, reconnaissance, flooding, taking, characteristics, site, surface, soils, ironii, commonly, if, containing, suggest, make, lava, parts, split, largest, underground, several, events, higher, closest, flows, ironiii, edges, dust, frequently, recent, largely, obstacles, well, roughly, superiormars, eureka, thought, materials, english, position, bodies, seasonal, less, underlying, spread, exomars, october, yet, captured, sampled, except, geological, meteorite, potential, struck, remaining, bands, showing, caps, dark, finding, accepted, necessary, like, aitken, shaped, bulge, nutrients, 50, paleomagnetism, because, often, metres, martian, meters, images, home, butterscotch, orbiter, dense, investigations, ice, moon, 10600, orbited, core, 300, equivalent, pressure, although, found, terra, dormant, about, tharsis, boiling, highsilicon, carries, concentrations, slightly, permafrost, equally, mantle, within, 6600, valleys, primarily, habitability, area, plagioclase, there, valles, detectable, low, forward, slopes, cliff, war, lowest, ago, elsewhere, potassium, basic, volume, hemisphere, solar, groundbased, ph, made, smooth, maximum, planet, record, growth, those, secondsmallest, similar, called, rust, strongly, athabasca, tectonic, likewise, metals, evidence, jupiter, exist, periods, planets, mya, physical, assessing, redorange, no, amounts, whereas, 45, 40, field, 1115, polar, elements, energetic, phoenix, models, occurred, structure, phosphorus, billion, land, prevalent, salt, age, resolving, depth, nasa, mass, 2005, 2008, silica, having 

Input word 1: EXITNOW

Input word 2: 
