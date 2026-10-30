# stock.py : le stock de novembre, une publication par jour du lundi 2 au lundi 30.
#   Les visuels sortent des 6 modèles (modeles.py) ; le calendrier part en PDF pour la validation de Raph.
#   Photos de l'équipe : les déposer dans PUBLICATIONS/_photos/ sous le nom de la clé `ph` (ex. ganvie.jpg),
#   écrire le nom de l'auteur dans AUTEURS, puis relancer. Sans photo, la zone photo sort transparente (à remplir dans CapCut).
#   Classements « selon vous » : remplir `top` avec les 5 plus cités du dimanche (nom, ligne, texte, clé photo), puis relancer.
#   Portraits : remplir citation, nom et metier quand l'équipe les a recueillis, puis relancer.
# python3 stock.py
import shutil
from bd import *
from modeles import m01_couv, m01_page, m02, m03, m04, m05, m06, COURT
from pilote import NUMERO

PH = H.parent / '_photos'
D = OUT / '3 - Le stock de novembre'
PILOTE = OUT / '2 - Le pilote' / 'Publication de lancement' / f'{N}Lancement du pilote - 1.png'
FIN = PK / '8 - Réseaux sociaux' / 'Gabarits Instagram' / 'Carrousel' / f'{N}Carrousel 3 - fin.png'
JOURS = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
COURT = {**COURT, 7: 'Vidéo'}
NOM_RDV = {**{n: RDV[n][0] for n in RDV}, 7: 'LA VIDÉO'}

AUTEURS = {}            # clé photo → nom de l'auteur, ex. 'ganvie': 'Prénom Nom'
POS = {}                # clé photo → cadrage, ex. 'ganvie': '50% 60%'

PORTRAIT = "Son portrait en hauteur, son prénom, sa phrase et son accord pour la publication. Le nom de la personne qui a pris la photo."

# j : jour de novembre · r : rendez-vous (1 à 6, 7 = la vidéo du samedi) · v : textes du visuel
# leg : légende à publier · faut : ce qu'il faut de l'équipe · verif : une info du visuel à confirmer avant de publier
STOCK = [
    # ---------------------------------------------------------------- semaine 1
    dict(j=2, r=1, pilote=True, sujet='Les 10 meilleurs restaurants de Cotonou',
         detail="Le pilote, en carrousel de 3 : « Offert », « Ce qu'il y a dedans », « Écrivez GUIDE ». Le PDF part à chaque demande, jusqu'au 13.",
         leg=f"Notre classement des 10 meilleurs restaurants de Cotonou est prêt, et il est offert. Du maquis à la terrasse, avec le plan Google Maps de chaque adresse. Pour le recevoir, écrivez GUIDE sur WhatsApp au {NUMERO}.",
         faut="Le numéro WhatsApp qui répond à GUIDE. Une personne qui envoie le PDF et compte les demandes chaque soir."),
    dict(j=3, r=3, sujet='La vendeuse de piment de Dantokpa', ph='piment-dantokpa',
         v=dict(citation='', nom='', metier='Vendeuse de piment à Dantokpa'),
         demander="Qu'est-ce qu'il faut savoir pour bien choisir son piment ?",
         leg="Le visage du pays : [prénom], vendeuse de piment au marché Dantokpa. « [sa phrase] » Vous la connaissez ? Passez-lui le bonjour en commentaire.",
         faut=PORTRAIT),
    dict(j=4, r=4, sujet='Le taux du franc CFA',
         v=dict(chiffre='655,957', legende='francs CFA pour 1 euro', texte="Le taux est fixe : il ne change pas d'un jour à l'autre.",
                astuce='Changez en banque ou en bureau agréé, et gardez de petites coupures pour le zém et le marché.'),
         leg="1 euro = 655,957 francs CFA, tous les jours de l'année. Un bureau qui vous donne moins prend une commission : comparez avant de changer. Enregistrez ce post pour votre prochain séjour.",
         faut='Rien : le visuel est prêt.'),
    dict(j=5, r=2, sujet='Ganvié', ph='ganvie',
         v=dict(nom='GANVIÉ', ville='Sô-Ava · lac Nokoué',
                infos=("En pirogue depuis l'embarcadère d'Abomey-Calavi", 'La pirogue et le guide se règlent au départ', 'Lac Nokoué, au nord de Cotonou')),
         leg="Ganvié, la cité lacustre du lac Nokoué. On y va en pirogue depuis l'embarcadère d'Abomey-Calavi. Vous y êtes déjà allé ? Racontez-nous en commentaire.",
         faut="4 à 6 photos de Ganvié tirées des anciennes publications, avec le nom de leur auteur. Les horaires de l'embarcadère, vérifiés par téléphone."),
    dict(j=6, r=5, sujet='Le Festival SICA', verif=True,
         v=dict(jours='9 – 15', mois='NOVEMBRE', evenement='FESTIVAL SICA', ou='Cotonou',
                savoir='La 20e édition : concerts, défilé et soirée des trophées.'),
         leg="Le Festival SICA fête sa 20e édition à Cotonou, du 9 au 15 novembre : concerts, défilé, soirée des trophées. Vous y allez ? Taguez la personne qui vient avec vous.",
         faut="Confirmer le lieu et le programme auprès des organisateurs, pour la ligne « Où »."),
    dict(j=7, r=7, sujet='Le pilote en 20 secondes',
         detail="Les 10 restaurants en plans rapides, puis l'écran « Écrivez GUIDE ». TikTok, puis Reel.",
         leg='10 adresses en 20 secondes. Le classement complet est offert : écrivez GUIDE sur WhatsApp.',
         faut="Une courte vidéo par restaurant : envoyée par l'établissement, ou filmée en y mangeant."),
    dict(j=8, r=6, sujet='Votre plage préférée',
         v=dict(question='VOTRE PLAGE PRÉFÉRÉE AUTOUR DE COTONOU ?',
                sous='Son nom en commentaire. Les 5 plus citées entrent dans notre classement du lundi 16.'),
         leg='Fidjrossè, Ouidah, Grand-Popo… Quelle est votre plage préférée autour de Cotonou ? Les 5 plus citées feront notre classement du lundi 16 novembre.',
         faut='Le samedi 14, compter les plages citées en commentaire et m’envoyer les 5 premières.'),
    # ---------------------------------------------------------------- semaine 2
    dict(j=9, r=1, sujet='Les 5 lieux à voir à Ouidah',
         v=dict(kicker='Le top 5', titre='LES 5 LIEUX À VOIR À OUIDAH'),
         top=[('La Porte du Non-Retour', 'Ouidah · route des Esclaves', 'Le dernier arrêt de la route des Esclaves, face à la mer.', 'ouidah-porte'),
              ('Le temple des Pythons', 'Ouidah · centre-ville', 'Le temple vodun où vivent les pythons sacrés, en plein centre-ville.', 'ouidah-pythons'),
              ('La forêt sacrée de Kpassè', 'Ouidah', 'La forêt du roi Kpassè, peuplée de statues des divinités vodun.', 'ouidah-kpasse'),
              ("Le musée d'Histoire", 'Ouidah · fort portugais', "L'histoire de la ville et de la traite, dans l'ancien fort portugais.", 'ouidah-musee'),
              ("La basilique de l'Immaculée-Conception", 'Ouidah · centre-ville', 'La basilique du centre-ville, juste en face du temple des Pythons.', 'ouidah-basilique')],
         leg='Les 5 lieux à voir à Ouidah, à une heure de Cotonou. Faites défiler, et dites-nous lequel vous avez déjà vu. Les Vodun Days s’y tiennent du 2 au 9 janvier.',
         faut='Une photo par lieu si vous en avez, avec son auteur. Sans photo, le carrousel sort en version graphique, déjà prête.'),
    dict(j=10, r=3, sujet='Le zémidjan', ph='zemidjan',
         v=dict(citation='', nom='', metier='Zémidjan à Cotonou'),
         demander="Qu'est-ce qu'un passager doit savoir avant de monter ?",
         leg='Le visage du pays : [prénom], zémidjan à Cotonou. « [sa phrase] » Votre meilleur souvenir de zém, en commentaire.',
         faut=PORTRAIT),
    dict(j=11, r=4, sujet='Les numéros à 10 chiffres',
         v=dict(chiffre='01', legende='devant tous les numéros du Bénin',
                texte="Depuis le 30 novembre 2024, les numéros béninois ont 10 chiffres : 01, puis les 8 chiffres d'avant.",
                astuce="Depuis l'étranger, composez +229 01 puis les 8 chiffres. Mettez vos contacts à jour avant d'arriver."),
         leg='Un numéro béninois qui ne passe plus ? Ajoutez 01 devant. Depuis le 30 novembre 2024, tous les numéros du pays ont 10 chiffres. Partagez à ceux qui rentrent pour les fêtes.',
         faut='Rien : le visuel est prêt.'),
    dict(j=12, r=2, sujet='La route des Pêches', ph='route-des-peches', verif=True,
         v=dict(nom='LA ROUTE DES PÊCHES', ville='De Cotonou à Ouidah',
                infos=("Vers l'ouest depuis Fidjrossè, le long de la mer", 'La route est libre ; paillotes et boissons se paient sur place', 'Entre Fidjrossè et Ouidah')),
         leg='La route des Pêches longe la mer de Cotonou à Ouidah : plages, cocotiers, villages de pêcheurs. Votre arrêt préféré sur la route ? En commentaire.',
         faut="4 à 6 photos avec leur auteur. L'état de la route, vérifié avant de publier."),
    dict(j=13, r=5, sujet='Le week-end des 14 et 15',
         v=dict(jours='14 – 15', mois='NOVEMBRE', evenement='', ou='', savoir=''),
         leg='Ce week-end à Cotonou : [l’événement], [le lieu], [l’heure]. Vous y allez ?',
         faut='Un événement du week-end, avec son lieu et son heure : la clôture du SICA si le programme la confirme, un concert, une expo, un match.'),
    dict(j=14, r=7, sujet='Ganvié en 30 secondes',
         detail="Le départ de l'embarcadère, la traversée, les maisons sur pilotis, le marché sur l'eau.",
         leg='Ganvié en 30 secondes, depuis la pirogue. Pour y aller : notre publication du jeudi 5.',
         faut='Les vidéos de Ganvié déjà tournées pour la page, avec leur auteur.'),
    dict(j=15, r=6, sujet='Le premier rendez-vous',
         v=dict(question='UN PREMIER RENDEZ-VOUS À COTONOU, VOUS ALLEZ OÙ ?',
                sous='Le nom et le quartier en commentaire. Le top 5 sort le lundi 23.'),
         leg="Un premier rendez-vous à Cotonou : vous l'emmenez où ? Le nom et le quartier en commentaire. Les 5 plus cités sortent le lundi 23 novembre.",
         faut='Le samedi 21, compter les lieux cités en commentaire et m’envoyer les 5 premiers.'),
    # ---------------------------------------------------------------- semaine 3
    dict(j=16, r=1, sujet='Vos 5 plages préférées', votes='du dimanche 8',
         v=dict(kicker='Selon vous', titre='VOS 5 PLAGES PRÉFÉRÉES AUTOUR DE COTONOU'), top=[],
         aussi='Ce jour-là, ensemble : le bilan du pilote. 1 000 demandes ou plus, on fait le guide.',
         leg='Vous avez voté : voici vos 5 plages préférées autour de Cotonou. Faites défiler pour le trajet depuis le centre.',
         faut='Les 5 plages les plus citées le 8. Une photo par plage avec son auteur, et le trajet depuis le centre.'),
    dict(j=17, r=3, sujet='En cuisine chez un restaurant du classement', ph='cuisine',
         v=dict(citation='', nom='', metier=''),
         demander="Le plat qu'il faut goûter chez vous ?",
         leg='Le visage du pays : [prénom], en cuisine chez [restaurant], dans notre classement des 10 meilleurs de Cotonou. « [sa phrase] »',
         faut="Un restaurant du classement d'accord pour le portrait. " + PORTRAIT),
    dict(j=18, r=4, sujet='La saison sèche',
         v=dict(chiffre='DÉC. – MARS', legende='la grande saison sèche dans le Sud',
                texte='Le meilleur moment pour Cotonou, Ouidah et Ganvié : peu de pluie et des pistes praticables.',
                astuce="De décembre à février, l'harmattan voile le ciel et assèche l'air : prévoyez de l'eau et de quoi protéger vos yeux."),
         leg='Vous préparez votre séjour ? De décembre à mars, c’est la grande saison sèche dans le Sud du Bénin. Enregistrez, et partagez à ceux qui rentrent pour les fêtes.',
         faut='Rien : le visuel est prêt.'),
    dict(j=19, r=2, sujet='Dantokpa', ph='dantokpa',
         v=dict(nom='DANTOKPA', ville='Cotonou · le grand marché',
                infos=('Au bord de la lagune de Cotonou', "Négociez : le premier prix n'est jamais le dernier", 'Marché Dantokpa, Cotonou')),
         leg='Dantokpa, le grand marché de Cotonou, au bord de la lagune : tissus, épices, piment, objets du vodun. Votre astuce pour bien y négocier ?',
         faut="4 à 6 photos prises en passant au marché, avec leur auteur, et l'accord des personnes photographiées de près."),
    dict(j=20, r=5, sujet='Le week-end des 21 et 22',
         v=dict(jours='21 – 22', mois='NOVEMBRE', evenement='', ou='', savoir=''),
         leg='Ce week-end à Cotonou : [l’événement], [le lieu], [l’heure]. Vous y allez ?',
         faut='Un événement du week-end, avec son lieu et son heure : un concert, une expo, un marché, un match.'),
    dict(j=21, r=7, sujet='Dantokpa en 30 secondes',
         detail="Les allées, les couleurs, les voix du marché. Pas de visage en gros plan sans accord.",
         leg='Dantokpa en 30 secondes. Vous y allez pour acheter quoi, vous ?',
         faut="Une vidéo tournée au marché par l'équipe, au téléphone."),
    dict(j=22, r=6, sujet='Les fêtes en famille',
         v=dict(question='VOUS RENTREZ POUR LES FÊTES ?',
                sous='Votre sortie en famille préférée à Cotonou, en commentaire. Les 5 plus citées sortent le lundi 30.'),
         leg='Vous rentrez pour les fêtes ? Dites-nous votre sortie en famille préférée à Cotonou. Les 5 plus citées sortent le lundi 30 novembre.',
         faut='Le samedi 28, compter les sorties citées en commentaire et m’envoyer les 5 premières.'),
    # ---------------------------------------------------------------- semaine 4
    dict(j=23, r=1, sujet='Vos 5 lieux pour un premier rendez-vous', votes='du dimanche 15',
         v=dict(kicker='Selon vous', titre='VOS 5 LIEUX POUR UN PREMIER RENDEZ-VOUS'), top=[],
         leg='Vous avez voté : vos 5 lieux pour un premier rendez-vous à Cotonou. Enregistrez pour la prochaine fois.',
         faut='Les 5 lieux les plus cités le 15. Une photo par lieu avec son auteur.'),
    dict(j=24, r=3, sujet='Un artisan de Cotonou', ph='artisan',
         v=dict(citation='', nom='', metier=''),
         demander='Combien de temps pour faire une pièce comme celle-ci ?',
         leg='Le visage du pays : [prénom], [son métier] à Cotonou. « [sa phrase] »',
         faut=PORTRAIT),
    dict(j=25, r=4, sujet='Cotonou – Ouidah',
         v=dict(chiffre='40 KM', legende='entre Cotonou et Ouidah', texte='Ouidah se visite dans la journée depuis Cotonou.',
                astuce='Pour les Vodun Days, du 2 au 9 janvier, réservez votre chambre et votre transport dès maintenant.'),
         leg='Cotonou – Ouidah : environ 40 km. Ouidah se fait dans la journée, et c’est là que se tiennent les Vodun Days, du 2 au 9 janvier. Taguez ceux avec qui vous y allez.',
         faut='Rien : le visuel est prêt.'),
    dict(j=26, r=2, sujet="L'Amazone", ph='amazone', verif=True,
         v=dict(nom="L'AMAZONE", ville='Cotonou · bord de mer',
                infos=("Sur l'esplanade de l'Amazone, face à la mer", 'Accès libre, de jour comme de soir', "Esplanade de l'Amazone, Cotonou")),
         leg="L'Amazone : 30 mètres de haut, face à la mer, en hommage aux guerrières du royaume du Dahomey. Vous avez déjà votre photo avec elle ?",
         faut="4 à 6 photos avec leur auteur. L'accès et les horaires de l'esplanade, vérifiés."),
    dict(j=27, r=5, sujet='Les Vodun Days',
         v=dict(jours='2 – 9', mois='JANVIER 2027', evenement='VODUN DAYS', ou='Ouidah',
                savoir='Une semaine de fête, à une heure de Cotonou. Réservez tôt.'),
         leg='C’est noté : les Vodun Days 2027 ont lieu à Ouidah, du 2 au 9 janvier. Vous y serez ? Dites-le en commentaire. En décembre, on prépare la série « Vodun Days : le guide ».',
         faut="Rien. Me dire si quelqu'un de l'équipe y sera."),
    dict(j=28, r=7, sujet='Votre coin',
         detail='Les vidéos envoyées par les abonnés, 3 à 5 secondes chacune, avec le nom de chacun à l’écran.',
         leg='Vous nous avez envoyé votre coin : voici les premiers. Envoyez le vôtre en message, avec votre nom.',
         faut="Les vidéos reçues après « Envoyez-nous votre coin », avec le nom et l'accord de chaque auteur."),
    dict(j=29, r=6, sujet='Les Vodun Days, vos souvenirs',
         v=dict(question='VOUS ÊTES DÉJÀ ALLÉ AUX VODUN DAYS ?',
                sous='Votre meilleur souvenir, ou ce que vous voulez voir en janvier, en commentaire.'),
         leg='Vous êtes déjà allé aux Vodun Days à Ouidah ? Racontez-nous votre meilleur souvenir. Vos réponses nourrissent notre série de décembre.',
         faut='Garder les meilleurs commentaires pour la série de décembre.'),
    # ---------------------------------------------------------------- semaine 5
    dict(j=30, r=1, sujet='Vos 5 sorties en famille', votes='du dimanche 22',
         v=dict(kicker='Selon vous', titre='VOS 5 SORTIES EN FAMILLE À COTONOU'), top=[],
         leg='Pour les fêtes, vous avez voté : vos 5 sorties en famille à Cotonou. Enregistrez pour décembre.',
         faut='Les 5 sorties les plus citées le 22. Une photo par lieu avec son auteur.'),
]

DECEMBRE = ['Les sorties des fêtes et l’agenda, chaque semaine', 'La série « Vodun Days : le guide », avec vos souvenirs du 29 novembre',
            'Le Cotonou Comedy Festival, dates à confirmer', 'Les premiers partenaires, toujours signalés « Partenaire »']

# ---------------------------------------------------------------- outils
def sem(j): return min((j - 2) // 7 + 1, 5)
def jour(j): return JOURS[(j - 2) % 7]

def ph(k):
    """(chemin, cadrage) de la photo d'équipe, ou None si elle n'est pas encore là."""
    if not k: return None
    for ext in ('jpg', 'jpeg', 'png', 'webp'):
        f = PH / f'{k}.{ext}'
        if f.exists(): return (str(f), POS.get(k, '50% 50%'))
    return None

def credit(k, H):
    a = AUTEURS.get(k)
    if not (a and ph(k)): return ''
    return (f'<div class="abs u" style="right:24px;top:{round(H * .2)}px;writing-mode:vertical-rl;transform:rotate(180deg);font-weight:600;font-size:19px;'
            f'letter-spacing:.12em;color:{SAB};opacity:.88;text-shadow:0 1px 6px rgba(45,42,34,.7)">Photo · {a}</div>')

def etat(e):
    """(texte, couleur) de l'état de la publication."""
    r, v = e['r'], e.get('v', {})
    if e.get('pilote'): return ('Numéro GUIDE attendu', BRO) if '•' in NUMERO else ('Prêt', VER)
    if r == 7: return 'Vidéo attendue', BRO
    if r == 1 and 'votes' in e and not e.get('top'): return 'Votes attendus', BRO
    if r == 3 and not v.get('citation'): return 'Portrait attendu', BRO
    if r == 5 and not v.get('evenement'): return 'Infos attendues', BRO
    if r == 2 and not ph(e.get('ph')): return 'Photos attendues', BRO
    if e.get('verif'): return 'À confirmer', BROF
    return 'Prêt', VER

def fichier(e, suite):
    return D / f'Semaine {sem(e["j"])}' / f'{N}{jour(e["j"])} - {COURT[e["r"]]} - {suite}.png'

# ---------------------------------------------------------------- visuels
def visuels(e):
    """Met en file les visuels de la publication ; renvoie celui qui sert de vignette au calendrier."""
    r, v, k, j = e['r'], e.get('v', {}), e.get('ph'), e['j']
    if e.get('pilote'): return PILOTE
    if r == 7: return None
    if r == 1:
        p = ph(k)
        out = page(f's{j}-couv', 1080, 1350, m01_couv(ph=p, typo_fond=not p, **v) + credit(k, 1350), fichier(e, '1 couverture'))
        for n, (nom, ligne, texte, kk) in enumerate(e.get('top', []), 1):
            pp = ph(kk)
            page(f's{j}-p{n}', 1080, 1350, m01_page(n=n, ph=pp, nom=nom.upper(), ligne=ligne, texte=texte, typo_fond=not pp) + credit(kk, 1350),
                 fichier(e, f'{n + 1} {nom}'))
        if e.get('top'):
            f = fichier(e, f'{len(e["top"]) + 2} fin'); f.parent.mkdir(parents=True, exist_ok=True); shutil.copy(FIN, f)
        return out
    if r == 3 and not v.get('citation'): return None
    if r == 5 and not v.get('evenement'): return None
    fn = {2: m02, 3: m03, 4: m04, 5: m05, 6: m06}[r]
    a = dict(v, ph=ph(k)) if r in (2, 3) else v
    t = r in (2, 3) and not a['ph']
    out = page(f's{j}', 1080, 1350, fn(**a) + credit(k, 1350), fichier(e, 'publication'), transparent=t)
    page(f's{j}-story', 1080, 1920, fn(H=1920, **a) + credit(k, 1920), fichier(e, 'story'), transparent=t)
    return out

# ---------------------------------------------------------------- calendrier PDF (A4 paysage)
CSS = BASE + f'''@page{{size:297mm 210mm;margin:0}}html,body{{background:{SAB}}}
.pg{{position:relative;width:297mm;height:210mm;overflow:hidden;break-after:page}}.pg:last-child{{break-after:auto}}
.k{{font:800 6.4pt Urbanist;letter-spacing:.22em;text-transform:uppercase;color:{BROF}}}
.p{{font:500 7.6pt/1.36 Urbanist;color:{ENC}}}
.folio{{position:absolute;left:14mm;right:14mm;bottom:7mm;display:flex;justify-content:space-between;font:600 6.4pt Urbanist;letter-spacing:.14em;text-transform:uppercase;color:{BROF}}}
.grid{{display:grid;grid-template-columns:15mm 29mm 15mm 72mm 75mm 46mm;column-gap:3.4mm}}
.row{{padding:1.7mm 0;border-top:.25mm solid rgba(45,42,34,.16);align-items:start}}
.chip{{display:inline-block;font:800 6pt Urbanist;letter-spacing:.1em;text-transform:uppercase;color:{SAB};border-radius:2mm;padding:.9mm 2mm .8mm;margin-bottom:1.4mm}}
.vig{{width:15mm;height:18.75mm;border-radius:1.2mm;overflow:hidden;background:rgba(45,42,34,.13);display:flex;align-items:center;justify-content:center;text-align:center;font:700 5.6pt/1.25 Urbanist;color:{BROF};padding:1mm}}
.vig img{{width:100%;height:100%;object-fit:cover}}'''

def grain(c):
    g = 'grain-light.png' if c == SAB else 'grain-dark.png'
    return f'<div class="abs" style="inset:0;background:{c}"></div><div class="abs" style="inset:0;background:url({A(g)});background-size:140mm;opacity:.38"></div>'

def arches():
    return (f'<div class="abs" style="left:0;right:0;bottom:0;height:12mm;background:url({A("pat-arches-bs.svg")});background-size:5.45mm 12mm"></div>'
            f'<div class="abs" style="left:0;right:0;bottom:12mm;height:.8mm;background:{BRO}"></div>')

def folio(n):
    return f'<div class="folio"><span>Benin Discovery · Le stock de novembre</span><span>{n:02d}</span></div>'

def pastille(r):
    # la vidéo n'a pas de numéro : un triangle « lecture » à la place
    n = f'{r:02d}' if r < 7 else f'<span style="width:0;height:0;border-left:2.2mm solid {SAB};border-top:1.3mm solid transparent;border-bottom:1.3mm solid transparent;margin-left:.6mm"></span>'
    return (f'<div style="display:flex;align-items:center;gap:1.8mm"><span class="e" style="flex:0 0 6.4mm;height:6.4mm;border-radius:50%;background:{BRO};color:{SAB};'
            f'display:flex;align-items:center;justify-content:center;font-size:8pt;line-height:1;padding-top:{".3mm" if r < 7 else "0"}">{n}</span>'
            f'<span class="e" style="font-size:8.6pt;line-height:1.05;color:{ENC}">{NOM_RDV[r]}</span></div>')

def resume(e):
    """Ce que dit le visuel, en une ou deux lignes."""
    r, v = e['r'], e.get('v', {})
    if e.get('detail'): return e['detail']
    if r == 1:
        if e.get('top'): return ' · '.join(f'{n}. {t[0]}' for n, t in enumerate(e['top'], 1))
        return f'Couverture prête. Les 5 pages se font avec les votes {e["votes"]}.'
    if r == 2: return ' · '.join(v['infos'])
    if r == 3: return f'À lui demander : « {e["demander"]} »' if not v.get('citation') else f'« {v["citation"]} » {v["nom"]}, {v["metier"]}'
    if r == 4: return f'<b>{v["chiffre"]}</b> {v["legende"]}. {v["texte"]} L\'astuce : {v["astuce"]}'
    if r == 5: return f'{v["savoir"]} Où : {v["ou"]}.' if v.get('evenement') else 'Visuel à remplir avec l’événement choisi.'
    if r == 6: return v['sous']
    return ''

def ligne(e, vig):
    t, c = etat(e)
    vg = (f'<div class="vig"><img src="{U(vig)}"></div>' if vig and Path(vig).exists()
          else f'<div class="vig">{ {7: "Vidéo", 3: "Portrait à venir", 5: "Après vos infos"}.get(e["r"], "À venir") }</div>')
    aussi = f'<div class="p" style="margin-top:1.2mm;font-style:italic;color:{BROF}">{e["aussi"]}</div>' if e.get('aussi') else ''
    return (f'<div class="grid row">'
            f'<div><div class="e" style="font-size:19pt;line-height:.9;color:{BRO}">{e["j"]}</div><div class="k" style="margin-top:1mm;letter-spacing:.12em">{jour(e["j"])}</div></div>'
            f'<div style="padding-top:.6mm">{pastille(e["r"])}</div>{vg}'
            f'<div><div class="e" style="font-size:10.4pt;line-height:1;color:{ENC};margin-bottom:1.3mm">{e["sujet"].upper()}</div><div class="p">{resume(e)}</div>{aussi}</div>'
            f'<div class="p">{e["leg"]}</div>'
            f'<div><span class="chip" style="background:{c}">{t}</span><div class="p" style="font-size:7.2pt">{e["faut"]}</div></div></div>')

def entete(titre, dates, n):
    heads = ''.join(f'<div class="k" style="font-size:5.8pt">{h}</div>' for h in ['Jour', 'Rendez-vous', 'Visuel', 'La publication', 'La légende', "Ce qu'il faut de vous"])
    return (f'<div class="abs" style="left:14mm;top:12mm;display:flex;align-items:baseline;gap:5mm">'
            f'<div class="e" style="font-size:26pt;color:{ENC}">{titre}</div><div class="k">{dates}</div></div>'
            f'<img class="abs" src="{logo(1)}" style="right:14mm;top:11mm;width:30mm">'
            f'<div class="abs grid" style="left:14mm;top:27mm">{heads}</div>')

def calendrier(vigs):
    P = []
    # 1 · couverture
    P.append(f'''<section class="pg">{grain(ENC)}
<img class="abs" src="{ILLU("sable")}" style="left:90mm;top:-20mm;width:260mm;opacity:.09">
<img class="abs" src="{logo(2)}" style="left:16mm;top:15mm;width:52mm">
<div class="abs" style="left:16mm;right:120mm;bottom:40mm;color:{SAB}">
<div style="width:18mm;height:1.1mm;background:{BRO};margin-bottom:5mm"></div>
<div class="k" style="color:{SAB};opacity:.9;margin-bottom:3.5mm">Le calendrier</div>
<div class="e" style="font-size:44pt;line-height:.94">LE STOCK DE NOVEMBRE</div>
<div class="u" style="font:500 11pt/1.45 Urbanist;margin-top:5mm;opacity:.9">Une publication par jour, du lundi 2 au lundi 30 novembre. Chaque ligne donne le visuel, la légende à publier et ce qu'il faut de vous.</div></div>
<div class="abs e" style="right:16mm;bottom:30mm;font-size:150pt;line-height:.8;color:{BRO}">29</div>
{arches()}</section>''')
    # 2 · comment ça tourne
    semaine = ''.join(f'<div style="display:flex;align-items:center;gap:4mm;padding:2.6mm 0;border-top:.25mm solid rgba(45,42,34,.16)">'
                      f'<span class="k" style="width:19mm;letter-spacing:.12em">{jr}</span>{pastille(r)}</div>'
                      for jr, r in zip(JOURS, [1, 3, 4, 2, 5, 7, 6]))
    blocs = ''.join(f'<div style="margin-bottom:5mm"><div class="e" style="font-size:12pt;color:{ENC};margin-bottom:1.3mm">{t}</div><div class="p" style="font-size:8.6pt">{x}</div></div>'
                    for t, x in [('LE PILOTE, DU 2 AU 13', "Chaque demande « GUIDE » reçoit le PDF des 10 restaurants. On compte les demandes chaque soir. Lundi 16, le bilan : 1 000 demandes ou plus, le guide de Cotonou sort le 1er décembre."),
                                 ('LES VOTES DU DIMANCHE', 'La question du dimanche donne le classement du lundi, huit jours plus tard. Le samedi, on compte les réponses et on garde les 5 plus citées.'),
                                 ('CHAQUE JOUR', 'Une story : le rappel GUIDE pendant le pilote, les coulisses, les réponses aux commentaires.'),
                                 ('LES RÈGLES', "Un classement ne s'achète pas. Chaque photo porte le nom de son auteur. Les personnes photographiées de près donnent leur accord. Horaires et accès vérifiés par téléphone avant de publier.")])
    etats = ''.join(f'<div style="display:flex;align-items:flex-start;gap:3mm;margin-bottom:2mm"><span class="chip" style="background:{c};margin:0;flex:0 0 auto">{t}</span><span class="p">{x}</span></div>'
                    for t, c, x in [('Prêt', VER, 'Le visuel est fait. On publie.'),
                                    ('À confirmer', BROF, 'Le visuel est fait ; une info est à vérifier avant de publier.'),
                                    ('… attendu(es)', BRO, 'Le visuel se termine dès que vous envoyez ce qui est indiqué.')])
    P.append(f'''<section class="pg">{grain(SAB)}
<div class="abs" style="left:14mm;top:13mm;width:120mm"><div class="k" style="margin-bottom:2.5mm">Mode d'emploi</div>
<div class="e" style="font-size:26pt;color:{ENC};margin-bottom:6mm">COMMENT ÇA TOURNE</div>
<div class="k" style="margin-bottom:1.5mm">La semaine type</div>{semaine}
<div class="k" style="margin:7mm 0 2.5mm">Les états</div>{etats}</div>
<div class="abs" style="left:150mm;right:14mm;top:31mm">{blocs}</div>
{folio(2)}</section>''')
    # 3 à 6 · les semaines
    pg = 3
    for s, dates in [(1, '2 – 8 novembre'), (2, '9 – 15 novembre'), (3, '16 – 22 novembre'), (4, '23 – 29 novembre')]:
        rows = ''.join(ligne(e, vigs.get(e['j'])) for e in STOCK if sem(e['j']) == s)
        P.append(f'<section class="pg">{grain(SAB)}{entete(f"SEMAINE {s}", dates, pg)}<div class="abs" style="left:14mm;right:14mm;top:31mm">{rows}</div>{folio(pg)}</section>')
        pg += 1
    # 7 · lundi 30 et décembre
    rows = ''.join(ligne(e, vigs.get(e['j'])) for e in STOCK if sem(e['j']) == 5)
    dec = ''.join(f'<div class="p" style="font-size:9pt;padding:2.4mm 0;border-top:.25mm solid rgba(242,227,198,.2);color:{SAB}">{x}</div>' for x in DECEMBRE)
    P.append(f'''<section class="pg">{grain(SAB)}{entete("SEMAINE 5", "lundi 30 novembre", pg)}
<div class="abs" style="left:14mm;right:14mm;top:31mm">{rows}</div>
<div class="abs" style="left:14mm;right:14mm;top:84mm;background:{ENC};border-radius:3mm;padding:9mm 10mm 10mm;display:flex;gap:14mm">
<div style="flex:0 0 95mm"><div class="k" style="color:{BRO};margin-bottom:2.5mm">Ensuite</div>
<div class="e" style="font-size:24pt;line-height:.96;color:{SAB}">EN DÉCEMBRE, LA SAISON DE LA DIASPORA</div>
<div class="p" style="font-size:9pt;color:{SAB};opacity:.9;margin-top:4mm">Le calendrier de décembre se valide avant le 25 novembre.</div></div>
<div style="flex:1">{dec}</div></div>
{folio(pg)}</section>''')
    return f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{typo("".join(P))}</body></html>'

def build():
    vigs = {e['j']: visuels(e) for e in STOCK}
    render()
    doc('stock-pdf', calendrier(vigs), D / f'{N}Le stock de novembre.pdf')
    render()
    for e in STOCK:
        t, _ = etat(e)
        if t != 'Prêt': print(f'{e["j"]:>2} {jour(e["j"]):<9} {COURT[e["r"]]:<17} {t}')

if __name__ == '__main__':
    build()
