"""Calculs de 95-mesure.md, version 1.2 (lecture du 2027-01-12, corrigee le 2027-01-13).

Depuis la version 1.1 : le retour suit une seule formule, celle de 50 (chiffrer-rentabilite, formules.md section 4),
appliquee aux termes observes ; un gain net nul ou negatif n'a pas de delai de retour (on ecrit : pas de retour).
Les regimes corriges de la version 1.1 sont retires.

Bibliotheque standard seule. Chaque nombre cite dans 95-mesure.md et dans 90-mise-en-service.md vient d'ici.
Les ENTREES sont les releves simules de mission/sources/ (pieces fictives) : le calcul, lui, est reel et se rejoue :

    python -X utf8 calculs-v1.2.py

Aucune entree n'est lue dans un fichier : elles sont recopiees ci-dessous avec leur piece, pour que la lecture
d'un chiffre de 95 mene a une ligne de ce fichier puis a une ligne d'un releve.
"""
from math import sqrt

# --- Taux horaires charges (entretien finance, repris par 50 section 2) ---
GC, RF, CPT, SUP, AGENT = 31.0, 52.0, 34.0, 38.0, 29.0

# --- Estimation de 50-rentabilite.md section 2, apport de l'option 4, central ---
E50 = dict(V=96, adoption=0.9, min_seance=83, relances_seance=24, reemploi=0.8, erreurs=2,
           cout_erreur=14 * AGENT / 60, fonct=20.0, maint=GC, construction=1348.0, m=0.75, H=18)
E50["min_rel"] = E50["min_seance"] / E50["relances_seance"]

# --- Releves de depart : sources/releves-de-depart-2026-10-27.md, trois lundis (factures, relances, minutes E1+E2+E5+E6)
DEP = [(58, 24, 119), (61, 26, 113), (57, 23, 111)]
# --- Production : sources/releve-mensuel-2027-01-11.md, lundis passes par le flux (relances hors comptes cles, cles, minutes)
FLUX = [("2026-12-14", 29, 5, 62), ("2026-12-21", 29, 4, 55), ("2027-01-04", 32, 6, 58)]
MAIN = ("2026-12-28", 26, 4, 118)  # comptable, plateforme indisponible
COMPTEURS = dict(propositions=[41, 40, 47], supprimees=[7, 7, 9], corrigees=[3, 4, 4])
VALIDATION_CLES_RF_MIN = [11, 9, 8, 12]
LECTURE_COMPTEURS_RF_MIN = 6 * 4
OPS = dict(novembre=957, decembre=1069, janvier_au_10=351, semaines=[352, 351, 21, 346])
MAINT_H = dict(GC=0.7, RF=0.8)
INCIDENTS = [("2026-12-14", dict(RF=0.3), 40 / 60), ("2026-12-28", dict(RF=0.5), 0.0)]  # (date, heures RF, attente GC en h)
RECLAMATIONS = [2, 3, 1, 2]
RECL_DEPART = 13
APPELS_MIN, APPELS_N = 88, 4
CONSTRUCTION_PAYEE = 900.0
HEURES_CONSTRUCTION = dict(GC=8, RF=5.5, CPT=3, SUP=1.5)
ECHANTILLON = dict(hasard=(30, 2), signalees=(8, 1), a_risque=(21, 0), distincts=54)


def moy(xs):
    return sum(xs) / len(xs)


def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h


def titre(t):
    print()
    print("== " + t)


# =============================================================== A. depart et production
titre("A. Duree de la seance et minutes par relance")
dep_rel = sum(r for _, r, _ in DEP)
dep_min = sum(m for _, _, m in DEP)
dep_fact = sum(f for f, _, _ in DEP)
min_rel_dep = dep_min / dep_rel
print(f"depart : {len(DEP)} lundis, {dep_fact} factures, {dep_rel} relances, {dep_min} min ; moyenne {moy([m for _, _, m in DEP]):.2f} min "
      f"(min {min(m for _, _, m in DEP)}, max {max(m for _, _, m in DEP)}) ; {dep_rel / len(DEP):.2f} relances par lundi ; {min_rel_dep:.3f} min par relance")
p_rel = sum(r for _, r, _, _ in FLUX)
p_cles = sum(c for _, _, c, _ in FLUX)
p_min = sum(m for _, _, _, m in FLUX)
min_rel_prod = p_min / p_rel
dur = [m for _, _, _, m in FLUX]
print(f"production avec le flux : {len(FLUX)} lundis, {p_rel} relances hors cles, {p_cles} cles, {p_min} min ; moyenne {moy(dur):.2f} min "
      f"(min {min(dur)}, max {max(dur)}) ; {p_rel / len(FLUX):.2f} relances par lundi ; {min_rel_prod:.3f} min par relance")
gain_rel = min_rel_dep - min_rel_prod
print(f"gain par relance = {min_rel_dep:.3f} - {min_rel_prod:.3f} = {gain_rel:.3f} min ; par seance type de 24 relances {gain_rel * 24:.1f} min ; "
      f"au volume reel de {p_rel / len(FLUX):.0f} relances par lundi {gain_rel * p_rel / len(FLUX):.1f} min")
print(f"50 : par relance bas {58 / 24:.3f}, central {E50['min_rel']:.3f}, haut {100 / 24:.3f} min")
m_nom, m_rel_main, m_cles, m_min = MAIN
print(f"temoin : seance a la main du {m_nom} = {m_min} min pour {m_rel_main} relances = {m_min / m_rel_main:.3f} min par relance (depart {min_rel_dep:.3f})")
contrefactuel = (p_rel + m_rel_main) * min_rel_dep
reel = p_min + m_min
print(f"controle croise : 4 lundis reels {reel} min contre {contrefactuel:.1f} min tout a la main au rythme du depart ; ecart {contrefactuel - reel:.1f} min "
      f"(gain du flux seul {p_rel * gain_rel:.1f} min)")
print(f"validation des comptes cles par le RF : {sum(VALIDATION_CLES_RF_MIN)} min en {len(VALIDATION_CLES_RF_MIN)} lundis "
      f"({moy(VALIDATION_CLES_RF_MIN):.1f} min par lundi), depart non chronometre")

# =============================================================== B. volume et adoption
titre("B. Volume et adoption")
occ_tot = p_rel + m_rel_main
adopt_rel = p_rel / occ_tot
print(f"relances hors cles : {p_rel} par le flux + {m_rel_main} a la main = {occ_tot} ; depart pour 4 lundis {dep_rel / len(DEP) * 4:.1f} ; "
      f"variation {100 * (occ_tot / (dep_rel / len(DEP) * 4) - 1):+.0f} %")
print(f"adoption IND-08 (seances) = {len(FLUX)} sur {len(FLUX) + 1} = {100 * len(FLUX) / (len(FLUX) + 1):.0f} % ; en relances = {p_rel} / {occ_tot} = {100 * adopt_rel:.1f} % ; "
      f"sans le lundi de panne 100 %")
envoyees_totales = occ_tot + p_cles + m_cles
print(f"relances envoyees en tout (cles comprises) : {envoyees_totales} ; par le flux {p_rel + p_cles}")

# =============================================================== C. gain brut observe
titre("C. Gain brut observe")
heures_lib = p_rel * gain_rel / 60
valeur_lib = heures_lib * GC
appels_h = APPELS_MIN / 60
reemploi = appels_h / heures_lib
gain_temps = valeur_lib * reemploi
print(f"heures liberees = {p_rel} x {gain_rel:.3f} / 60 = {heures_lib:.3f} h = {heures_lib * 60:.1f} min ; valeur a {GC:.0f} EUR = {valeur_lib:.2f} EUR")
print(f"appels : {APPELS_N} appels, {APPELS_MIN} min ({APPELS_MIN / APPELS_N:.0f} min par appel) ; reemploi = {appels_h:.3f} / {heures_lib:.3f} = {100 * reemploi:.1f} %")
print(f"gain temps reemploye = {valeur_lib:.2f} x {reemploi:.4f} = {gain_temps:.2f} EUR [F] ; temps libere non reemploye {heures_lib - appels_h:.3f} h = {valeur_lib - gain_temps:.2f} EUR de valeur non financiere")
print(f"usage nomme par la direction generale : 12 appels par mois x {APPELS_MIN / APPELS_N:.0f} min = {12 * APPELS_MIN / APPELS_N:.0f} min = {12 * APPELS_MIN / APPELS_N / 60:.2f} h")
evitees_total = RECL_DEPART - sum(RECLAMATIONS)
evitees_apport = max(0, evitees_total - 4)  # 50 section 2 : l'option 0 en retire 4 [H]
gain_err = evitees_apport * E50["cout_erreur"]
print(f"reclamations : depart {RECL_DEPART} par mois, observe {sum(RECLAMATIONS)} sur 4 semaines ; evitees en tout {evitees_total}, dont {evitees_apport} imputee a l'option 4 "
      f"(l'option 0 en retire 4 [H]) ; cout d'une erreur {E50['cout_erreur']:.4f} EUR ; gain {gain_err:.2f} EUR [E]")
print(f"pour 100 relances envoyees : depart {100 * RECL_DEPART / E50['V']:.1f} ({RECL_DEPART} pour {E50['V']}) ; observe {100 * sum(RECLAMATIONS) / envoyees_totales:.1f} ({sum(RECLAMATIONS)} pour {envoyees_totales})")
brut = gain_temps + gain_err
print(f"GAIN BRUT observe = {gain_temps:.2f} + {gain_err:.2f} = {brut:.2f} EUR [E] ; dont [F] {gain_temps:.2f}")
brut_50 = (E50["V"] * E50["min_rel"] / 60 * GC * E50["reemploi"] + E50["erreurs"] * E50["cout_erreur"]) * E50["adoption"]
print(f"50 central (apport) : gain brut {brut_50:.2f} EUR ; temps {E50['V'] * E50['min_rel'] / 60 * GC * E50['reemploi'] * E50['adoption']:.2f} ; erreurs {E50['erreurs'] * E50['cout_erreur'] * E50['adoption']:.2f}")

# =============================================================== D. couts reels
titre("D. Couts reels de la periode")
fonct = 35.0
maint = MAINT_H["GC"] * GC + MAINT_H["RF"] * RF
superv = LECTURE_COMPTEURS_RF_MIN / 60 * RF
inc = sum(sum(h * RF for h in rf.values()) + att * GC for _, rf, att in INCIDENTS)
print(f"fonctionnement (facture de decembre, palier Equipe) {fonct:.2f} ; maintenance {sum(MAINT_H.values()):.1f} h = {MAINT_H['GC']} x {GC:.0f} + {MAINT_H['RF']} x {RF:.0f} = {maint:.2f} ; "
      f"supervision {LECTURE_COMPTEURS_RF_MIN} min x {RF:.0f} / 60 = {superv:.2f} ; incidents {inc:.2f}")
for d, rf, att in INCIDENTS:
    print(f"   incident {d} : RF {sum(rf.values())} h = {sum(h * RF for h in rf.values()):.2f} EUR ; attente GC {att * 60:.0f} min = {att * GC:.2f} EUR")
cout_total = fonct + maint + superv + inc
mob = sum(HEURES_CONSTRUCTION[k] * t for k, t in (("GC", GC), ("RF", RF), ("CPT", CPT), ("SUP", SUP)))
C = CONSTRUCTION_PAYEE + mob
print(f"construction : payee {CONSTRUCTION_PAYEE:.0f} + mobilisee {mob:.0f} ({HEURES_CONSTRUCTION['GC']} h x {GC:.0f} + {HEURES_CONSTRUCTION['RF']} h x {RF:.0f} + "
      f"{HEURES_CONSTRUCTION['CPT']} h x {CPT:.0f} + {HEURES_CONSTRUCTION['SUP']} h x {SUP:.0f}) = {C:.0f} EUR contre {E50['construction']:.0f} estimes ({100 * (C / E50['construction'] - 1):+.0f} %)")
print(f"total des couts de la periode : {cout_total:.2f} EUR ; sans incidents {cout_total - inc:.2f}")

# =============================================================== E. gain net
titre("E. Gain net observe")
net = brut - cout_total
net_hi = brut - (cout_total - inc)
net_sans_err = gain_temps - cout_total
print(f"GAIN NET observe = {brut:.2f} - {cout_total:.2f} = {net:.2f} EUR [E] ; sans les incidents {net_hi:.2f} ; sans compter les erreurs evitees {net_sans_err:.2f} [F]")
net_50 = brut_50 - E50["fonct"] - E50["maint"]
print(f"50 central : gain net {net_50:.2f} ; ecart {net - net_50:+.2f} ; cumul apres 1 periode {net:.2f}")
print(f"seuil de rentabilite mensuelle : gain brut {brut:.2f} contre fonctionnement + maintenance {fonct + maint:.2f} (+ supervision {superv:.2f} = {fonct + maint + superv:.2f}) : "
      f"{'coute plus qu il ne rapporte' if brut < fonct + maint + superv else 'couvre ses couts'}")

# =============================================================== F. decomposition de l'ecart
titre("F. Decomposition de l'ecart entre 50 (central) et l'observe, terme apres terme (ordre ecrit)")


def net_modele(V, a, m_rel, r, E_val, f, mt, sv, ic, adoption_sur_erreurs=True):
    temps = V * m_rel / 60 * GC * r
    b = (temps + E_val) * a if adoption_sur_erreurs else temps * a + E_val
    return b - f - mt - sv - ic


c_err = E50["cout_erreur"]
pas = []
V, a, m_rel, r = E50["V"], E50["adoption"], E50["min_rel"], E50["reemploi"]
Ev, f, mt, sv, ic = E50["erreurs"] * c_err, E50["fonct"], E50["maint"], 0.0, 0.0
cur = net_modele(V, a, m_rel, r, Ev, f, mt, sv, ic)
print(f"depart (50 central) : {cur:.2f}")
suite = [
    ("volume 96 -> %d relances hors cles" % occ_tot, dict(V=occ_tot)),
    ("adoption 90 %% -> %.1f %% des relances" % (100 * adopt_rel), dict(a=adopt_rel)),
    ("minutes %.3f -> %.3f par relance" % (E50["min_rel"], gain_rel), dict(m_rel=gain_rel)),
    ("reemploi 80 %% -> %.1f %%" % (100 * reemploi), dict(r=reemploi)),
    ("erreurs evitees 2 -> %d (adoption deja comptee)" % evitees_apport, dict(Ev=gain_err, adoption_sur_erreurs=False)),
    ("fonctionnement 20 -> %.0f" % fonct, dict(f=fonct)),
    ("maintenance %.0f -> %.2f" % (E50["maint"], maint), dict(mt=maint)),
    ("supervision 0 -> %.2f" % superv, dict(sv=superv)),
    ("incidents 0 -> %.2f" % inc, dict(ic=inc)),
]
etat = dict(V=V, a=a, m_rel=m_rel, r=r, E_val=Ev, f=f, mt=mt, sv=sv, ic=ic, adoption_sur_erreurs=True)
for lib, chg in suite:
    chg = {("E_val" if k == "Ev" else k): v for k, v in chg.items()}
    etat.update(chg)
    nouveau = net_modele(**etat)
    print(f"   {lib:62s} {nouveau - cur:+8.2f} -> {nouveau:8.2f}")
    cur = nouveau
print(f"arrivee : {cur:.2f} (observe {net:.2f})")

# =============================================================== G. retour et seuil de rentabilite
titre("G. Retour : une seule formule, celle de 50 section 4, appliquee aux termes observes")
formule = "(construction payee + construction mobilisee + gain brut x m) / gain net mensuel"
for lib, n in (("periode telle que relevee", net), ("sans les incidents", net_hi)):
    if n > 0:
        print(f"   {lib} : gain net {n:.2f} -> retour projete {(C + brut * E50['m']) / n:.1f} mois [E] ({formule})")
    else:
        print(f"   {lib} : gain net {n:.2f} <= 0 -> PAS DE RETOUR (un gain net nul ou negatif n'a pas de delai de retour ; formule de 50 : {formule})")
print(f"   cumul reel apres une periode : {net:.2f} EUR contre une construction de {C:.0f} EUR : non rattrape")
cout_poursuite = fonct + maint + superv
print(f"   cout de poursuite par mois [E], tel que releve (fonctionnement {fonct:.2f} + maintenance {maint:.2f} + supervision {superv:.2f}), hors incidents : {cout_poursuite:.2f}")
manque = cout_poursuite - brut
duree_appel = APPELS_MIN / APPELS_N
valeur_appel = duree_appel / 60 * GC
appels_min = (cout_poursuite - gain_err) / valeur_appel
r_min = (cout_poursuite - gain_err) / valeur_lib
print(f"   seuil de rentabilite mensuelle : gain brut {brut:.2f} contre {cout_poursuite:.2f} ; il manque {manque:.2f} EUR par periode")
print(f"   un appel de {duree_appel:.0f} min reemploie {valeur_appel:.2f} EUR de temps libere ; gain net nul, au volume et a l'adoption observes, a "
      f"{100 * r_min:.1f} % de reemploi du temps libere ({heures_lib:.2f} h, soit {heures_lib * 60 / duree_appel:.1f} appels de {duree_appel:.0f} min), "
      f"c'est-a-dire {appels_min:.1f} appels par periode (observe : {APPELS_N})")
print(f"   maximum possible, tout le temps libere reemploye : gain net {valeur_lib + gain_err - cout_poursuite:+.2f} EUR (hors incidents)")

# =============================================================== H. point mort
titre("H. Point mort a 18 mois recalcule (formules de chiffrer-rentabilite, section 6)")
H, m = E50["H"], E50["m"]
pm_50 = (E50["construction"] + H * (E50["fonct"] + E50["maint"])) / (H - m)
print(f"50 : ({E50['construction']:.0f} + {H} x {E50['fonct'] + E50['maint']:.0f}) / ({H} - {m}) = {pm_50:.2f} EUR de gain brut")
for lib, F in (("construction reelle, couts de 50 (20 + 31)", 20 + GC), ("construction reelle, couts releves (35 + 63,30 + 20,80)", fonct + maint + superv)):
    pm = (C + H * F) / (H - m)
    min_rel = (pm - gain_err) / (E50["V"] * GC * 0.8 / 60)
    print(f"   {lib:66s} gain brut minimal {pm:7.2f} EUR ; minutes par relance (volume 96, reemploi 80 %) {min_rel:.2f}, soit {min_rel * 24:.1f} min par seance de 24")
print(f"   observe : {gain_rel:.3f} min par relance, soit {gain_rel * 24:.1f} min par seance de 24 ; brut observe {brut:.2f}")

# =============================================================== I. indicateurs
titre("I. Indicateurs de 60 section 14")
prop = COMPTEURS["propositions"]
sup_ = COMPTEURS["supprimees"]
cor = COMPTEURS["corrigees"]
print("IND-05 par lundi : " + ", ".join(f"{100 * (s + c) / p:.1f} %" for p, s, c in zip(prop, sup_, cor)) +
      f" ; agrege ({sum(sup_)} + {sum(cor)}) / {sum(prop)} = {100 * (sum(sup_) + sum(cor)) / sum(prop):.1f} %")
sous15 = 18
sup_pilote = 6 + 9 + 8
print(f"   au pilote (lundis 2 a 4) : {sous15} suppressions sur {sup_pilote} sont des factures sous 15 EUR ({100 * sous15 / sup_pilote:.0f} %) [F] ; "
      f"production avec la meme part [E] : IND-05 passerait de {100 * (sum(sup_) + sum(cor)) / sum(prop):.1f} % a "
      f"{100 * (sum(sup_) + sum(cor) - round(sum(sup_) * sous15 / sup_pilote)) / sum(prop):.1f} % ({round(sum(sup_) * sous15 / sup_pilote)} suppressions de moins)")
print(f"IND-01 : {sum(RECLAMATIONS)} sur 4 semaines (cible 7 par mois, depart {RECL_DEPART})")
print(f"IND-04 : 0 sur {p_rel + p_cles} relances du flux ; IND-02 : 0")
print(f"IND-09 : novembre {OPS['novembre']} operations (20 EUR), decembre {OPS['decembre']} (35 EUR, palier Equipe) ; somme des semaines {sum(OPS['semaines'])} ; "
      f"janvier au 10 : {OPS['janvier_au_10']} ; projection de janvier {OPS['janvier_au_10'] + 3 * OPS['semaines'][3]} [E] (21 jours restants a {OPS['semaines'][3]} par semaine)")
print(f"IND-10 : {sum(MAINT_H.values()):.1f} h sur 4 semaines")
print(f"IND-03 : moyenne des lundis avec le flux {moy(dur):.1f} min (cible 60)")
ops_30 = round((236 - 21) * 52 / 12)
print(f"consommation estimee par la maquette : 10 min = {round(342 * 52 / 12)} par mois ; 30 min sans passage de 17 h = {ops_30} par mois [E]")

# =============================================================== J. echantillon
titre("J. Lecture de cas")
n, k = ECHANTILLON["hasard"]
lo, hi = wilson(k, n)
print(f"tirage au hasard : {k} echecs sur {n} = {100 * k / n:.1f} % ; intervalle de Wilson a 95 % : {100 * lo:.1f} a {100 * hi:.1f} %")
tot_lus = ECHANTILLON["distincts"]
tot_ech = ECHANTILLON["hasard"][1] + ECHANTILLON["signalees"][1] + ECHANTILLON["a_risque"][1]
print(f"cas lus distincts {tot_lus} ; echecs {tot_ech} (alerte 0, lecture {ECHANTILLON['hasard'][1]}, reclamation {ECHANTILLON['signalees'][1]})")
